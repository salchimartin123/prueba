class Personaje:
    def __init__(self, nombre, nivel, raza_id, estado_id, usuario_id, habilidad_id, equip_id, poder_id):
        self.nombre = nombre
        self.nivel = nivel
        self.raza_id = raza_id
        self.estado_id = estado_id
        self.usuario_id = usuario_id
        self.habilidad_id = habilidad_id
        self.equip_id = equip_id
        self.poder_id = poder_id

    def __str__(self):
        return f"Personaje: {self.nombre}, Nivel: {self.nivel}, Raza ID: {self.raza_id}, Estado ID: {self.estado_id}, Jugador ID: {self.jugador_id}, Habilidad ID: {self.habilidad_id}, Equipamiento ID: {self.equip_id}, Poder ID: {self.poder_id}"