class Estado:
    def __init__(self, id_estado, nombre, descripcion):
        self.id_estado = id_estado
        self.nombre = nombre
        self.descripcion = descripcion

def obtener_estado_vivo(cursor):
    query = "SELECT id_estado, nombre, descripcion FROM Estado WHERE nombre = 'vivo'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return Estado(result[0], result[1], result[2])
    else:
        return None