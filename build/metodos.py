

import datetime
from enum import Enum

class EstadoEnvio(Enum): #los estados de envio que se usaran y visualizaran en la interfaz
    RECIBIDO = "Recibimos tu envío"
    EN_REPARTO_AEREO = "En reparto aéreo"
    VIAJANDO_A_TU_DESTINO = "Viajando a tu destino"
    EN_CENTRO_LOGISTICO = "En centro logístico (bodega)"
    EN_CAMINO_HACIA_TI = "En camino hacia ti"
    ENTREGADO = "Entregado"

class Rol(Enum): #los actores del proceso
    PERSONAL_LOGISTICA = "Personal de logística"
    GERENTE_COMERCIAL = "Gerente Comercial"
    DESTINATARIO = "Destinatario"
    CONDUCTOR = "Conductor"
    CLIENTE = "Cliente"
    QUIMICO = "Químico"

class Usuario: #Se define la clase padre Rol
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

class Cliente(Usuario): #Clase cliente de tipo usuario
    def __init__(self, nombre, identificador):
        super().__init__(nombre, Rol.CLIENTE)
        self.identificador = identificador
        self.envios = []

class Transportista(Usuario): #Clase transportista de tipo usuario
    def __init__(self, nombre):
        super().__init__(nombre, Rol.CONDUCTOR)

class Quimico(Usuario): #Clase quimico de tipo usuario
    def __init__(self, nombre):
        super().__init__(nombre, Rol.QUIMICO)

class GerenteComercial(Usuario): #Clase gerente comercial de tipo usuario
    def __init__(self, nombre):
        super().__init__(nombre, Rol.GERENTE_COMERCIAL)

class CambioEstado: #clase que indica el estado actual del envio
    def __init__(self, estado, fecha, ubicacion):
        self.estado = estado
        self.fecha = fecha
        self.ubicacion = ubicacion

class Envio:
    def __init__(self, id_job, guia_aerea, cliente, tipo_producto, destino, temperatura, hora_entrega, transportista=None,accidente=None):
        self.id_job = id_job
        self.guia_aerea = guia_aerea
        self.cliente = cliente
        self.tipo_producto = tipo_producto
        self.destino = destino
        self.temperatura = temperatura
        self.hora_entrega = hora_entrega
        self.transportista = transportista #NO SE ESTÁ USANDO
        self.estado_actual = EstadoEnvio.RECIBIDO
        self.historial_estados = [CambioEstado(EstadoEnvio.RECIBIDO, datetime.datetime.now(), "Aeropuerto El Dorado")]
        self.ubicacion_actual = "Aeropuerto El Dorado"
        self.accidente=accidente

    def actualizar_estado(self, nuevo_estado, ubicacion):
        self.estado_actual = nuevo_estado
        self.ubicacion_actual = ubicacion
        self.historial_estados.append(CambioEstado(nuevo_estado, datetime.datetime.now(), ubicacion))
    


class SistemaSeguimiento:
    def __init__(self):
        self.envios = {}
        self.usuarios = {}
        self.clientes = {}
        self.transportistas = []
        self.quimicos = []
        self.gerentes_comerciales = []

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.nombre] = usuario
        if isinstance(usuario, Cliente):
            self.clientes[usuario.identificador] = usuario
        elif isinstance(usuario, Transportista):
            self.transportistas.append(usuario)
        elif isinstance(usuario, Quimico):
            self.quimicos.append(usuario)
        elif isinstance(usuario, GerenteComercial):
            self.gerentes_comerciales.append(usuario)

    def crear_envio(self, guia_aerea, cliente, tipo_producto, destino, temperatura, hora_entrega):
        id_job = f"JOB{len(self.envios) + 1:03}"
        nuevo_envio = Envio(id_job, guia_aerea, cliente, tipo_producto, destino, temperatura, hora_entrega)
        self.envios[id_job] = nuevo_envio
        cliente.envios.append(nuevo_envio)
        return id_job

    def actualizar_estado_envio(self, id_job, nuevo_estado, ubicacion):
        if id_job in self.envios:
            self.envios[id_job].actualizar_estado(nuevo_estado, ubicacion)
            if nuevo_estado != EstadoEnvio["EN_RETRASO"]:
                self.envios[id_job].accidente=None
            return True
        return False

    def obtener_info_envio(self, id_job):
        if id_job in self.envios:
            envio = self.envios[id_job]
            if envio.accidente == None:
                return f"JOB: {envio.id_job}, Guía Aérea: {envio.guia_aerea}, Cliente: {envio.cliente.nombre}, " \
                       f"Tipo: {envio.tipo_producto}, Destino: {envio.destino}, Estado: {envio.estado_actual.value}, " \
                       f"Temperatura: {envio.temperatura}, Hora de entrega: {envio.hora_entrega}, " \
                       f"Ubicación actual: {envio.ubicacion_actual}"
            else:
                return f"JOB: {envio.id_job}, Guía Aérea: {envio.guia_aerea}, Cliente: {envio.cliente.nombre}, " \
                       f"Tipo: {envio.tipo_producto}, Destino: {envio.destino}, Estado: {envio.estado_actual.value}, " \
                       f"Temperatura: {envio.temperatura}, Hora de entrega: {envio.hora_entrega}, " \
                       f"Ubicación actual: {envio.ubicacion_actual}, "\
                       f"Accidente:{envio.accidente}"

        return "Envío no encontrado"

    def obtener_historial_envio(self, id_job):
        if id_job in self.envios:
            envio = self.envios[id_job]
            historial = [f"{cambio.fecha} - {cambio.estado.value} en {cambio.ubicacion}" for cambio in envio.historial_estados]
            return "\n".join(historial)
        return "Envío no encontrado"