import os
import time

def seleccionar_entero(mensaje, max_opciones):
    while True:
        try:
            seleccion = int(input(mensaje))
            if 1 <= seleccion <= max_opciones:
                return seleccion
            else:
                print(f"Por favor, ingrese un número entre 1 y {max_opciones}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def seleccionar_varios_enteros(mensaje, max_valor, max_seleccion):
    while True:
        try:
            opciones = input(mensaje)
            opciones = [int(opcion.strip()) for opcion in opciones.split(",")]
            if all(1 <= opcion <= max_valor for opcion in opciones) and len(opciones) <= max_seleccion:
                return opciones
            else:
                print(f"Por favor, ingrese hasta {max_seleccion} números entre 1 y {max_valor}.")
        except ValueError:
            print("Por favor, ingrese números válidos separados por comas.")

class GameMaster:
    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_raza(self, cursor, conexion):
        print("Agregar nueva raza al sistema")

        nombre_raza = input("Ingrese el nombre de la nueva raza: ")
        tipo_raza = input("Ingrese el tipo de la nueva raza: ")

        # Insertar nueva raza en la tabla Raza
        insert_query = "INSERT INTO Raza (nombre, tipo) VALUES (%s, %s)"
        try:
            cursor.execute(insert_query, (nombre_raza, tipo_raza))
            conexion.commit()  # Confirmar la transacción
            print("Raza agregada correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al agregar raza: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def agregar_habilidad(self, cursor, conexion):
        print("Agregar nueva habilidad al sistema")

        nombre_habilidad = input("Ingrese el nombre de la nueva habilidad: ")
        descripcion_habilidad = input("Ingrese la descripción de la nueva habilidad: ")

        # Obtener y mostrar razas disponibles
        cursor.execute("SELECT id_raza, nombre FROM Raza")
        razas = cursor.fetchall()

        if not razas:
            print("No hay razas disponibles. Primero agregue razas.")
            return

        print("Seleccione la raza a la que pertenece la habilidad:")
        for idx, raza in enumerate(razas):
            print(f"{idx + 1}. {raza[1]}")

        raza_seleccionada = seleccionar_entero("Ingrese el número de la raza seleccionada: ", len(razas))
        id_raza = razas[raza_seleccionada - 1][0]

        # Insertar nueva habilidad en la tabla Habilidad
        insert_query = "INSERT INTO Habilidad (nombre, descripcion, hab_raza_id) VALUES (%s, %s, %s)"
        try:
            cursor.execute(insert_query, (nombre_habilidad, descripcion_habilidad, id_raza))
            conexion.commit()  # Confirmar la transacción
            print("Habilidad agregada correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al agregar habilidad: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def agregar_poder(self, cursor, conexion):
        print("Agregar nuevo poder al sistema")

        nombre_poder = input("Ingrese el nombre del nuevo poder: ")
        descripcion_poder = input("Ingrese la descripción del nuevo poder: ")

        # Obtener y mostrar razas disponibles
        cursor.execute("SELECT id_raza, nombre FROM Raza")
        razas = cursor.fetchall()

        if not razas:
            print("No hay razas disponibles. Primero agregue razas.")
            return

        print("Seleccione la raza a la que pertenece el poder:")
        for idx, raza in enumerate(razas):
            print(f"{idx + 1}. {raza[1]}")

        raza_seleccionada = seleccionar_entero("Ingrese el número de la raza seleccionada: ", len(razas))
        id_raza = razas[raza_seleccionada - 1][0]

        # Insertar nuevo poder en la tabla Poder
        insert_query = "INSERT INTO Poder (nombre, descripcion, poder_raza_id) VALUES (%s, %s, %s)"
        try:
            cursor.execute(insert_query, (nombre_poder, descripcion_poder, id_raza))
            conexion.commit()  # Confirmar la transacción
            print("Poder agregado correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al agregar poder: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def agregar_equipamiento(self, cursor, conexion):
        print("Agregar nuevo equipamiento al sistema")

        nombre_equipamiento = input("Ingrese el nombre del nuevo equipamiento: ")
        descripcion_equipamiento = input("Ingrese la descripción del nuevo equipamiento: ")

        # Insertar nuevo equipamiento en la tabla Equipamiento
        insert_query = "INSERT INTO Equipamiento (nombre, descripcion) VALUES (%s, %s)"
        try:
            cursor.execute(insert_query, (nombre_equipamiento, descripcion_equipamiento))
            conexion.commit()  # Confirmar la transacción
            print("Equipamiento agregado correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al agregar equipamiento: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def agregar_estado(self, cursor, conexion):
        print("Agregar nuevo estado al sistema")

        nombre_estado = input("Ingrese el nombre del nuevo estado: ")
        descripcion_estado = input("Ingrese la descripción del nuevo estado: ")

        # Insertar nuevo estado en la tabla Estado
        insert_query = "INSERT INTO Estado (nombre, descripcion) VALUES (%s, %s)"
        try:
            cursor.execute(insert_query, (nombre_estado, descripcion_estado))
            conexion.commit()  # Confirmar la transacción
            print("Estado agregado correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al agregar estado: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def editar_descripcion_habilidad(self, cursor, conexion):
        print("Editar descripción de una habilidad")

        # Obtener y mostrar habilidades disponibles
        cursor.execute("SELECT id_habilidad, nombre, descripcion FROM Habilidad")
        habilidades = cursor.fetchall()

        if not habilidades:
            print("No hay habilidades disponibles.")
            return

        print("Seleccione la habilidad que desea editar:")
        for idx, habilidad in enumerate(habilidades):
            print(f"{idx + 1}. {habilidad[1]}: {habilidad[2]}")

        habilidad_seleccionada = seleccionar_entero("Ingrese el número de la habilidad seleccionada: ", len(habilidades))
        id_habilidad = habilidades[habilidad_seleccionada - 1][0]

        nueva_descripcion = input("Ingrese la nueva descripción: ")

        # Actualizar la descripción de la habilidad en la base de datos
        update_query = "UPDATE Habilidad SET descripcion = %s WHERE id_habilidad = %s"
        try:
            cursor.execute(update_query, (nueva_descripcion, id_habilidad))
            conexion.commit()  # Confirmar la transacción
            print("Descripción de la habilidad actualizada correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al actualizar la descripción de la habilidad: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def editar_descripcion_poder(self, cursor, conexion):
        print("Editar descripción de un poder")

        # Obtener y mostrar poderes disponibles
        cursor.execute("SELECT id_poder, nombre, descripcion FROM Poder")
        poderes = cursor.fetchall()

        if not poderes:
            print("No hay poderes disponibles.")
            return

        print("Seleccione el poder que desea editar:")
        for idx, poder in enumerate(poderes):
            print(f"{idx + 1}. {poder[1]}: {poder[2]}")

        poder_seleccionado = seleccionar_entero("Ingrese el número del poder seleccionado: ", len(poderes))
        id_poder = poderes[poder_seleccionado - 1][0]

        nueva_descripcion = input("Ingrese la nueva descripción: ")

        # Actualizar la descripción del poder en la base de datos
        update_query = "UPDATE Poder SET descripcion = %s WHERE id_poder = %s"
        try:
            cursor.execute(update_query, (nueva_descripcion, id_poder))
            conexion.commit()  # Confirmar la transacción
            print("Descripción del poder actualizada correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al actualizar la descripción del poder: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def editar_equipamiento(self, cursor, conexion):
        print("Editar equipamiento existente")

        # Mostrar equipamientos disponibles
        equipamientos = self.obtener_equipamientos(cursor)
        if not equipamientos:
            print("No hay equipamientos disponibles para editar.")
            return

        print("Seleccione el equipamiento que desea editar:")
        for idx, equipamiento in enumerate(equipamientos):
            print(f"{idx + 1}. {equipamiento[1]}: {equipamiento[2]}")

        equipamiento_seleccionado = seleccionar_entero("Ingrese el número del equipamiento seleccionado: ", len(equipamientos))
        id_equipamiento = equipamientos[equipamiento_seleccionado - 1][0]

        # Verificar si algún personaje está usando este equipamiento
        cursor.execute("SELECT COUNT(*) FROM Personaje WHERE equip_id = %s", (id_equipamiento,))
        cantidad_personajes = cursor.fetchone()[0]

        if cantidad_personajes > 0:
            print("No se puede modificar el equipamiento porque está siendo utilizado por uno o más personajes.")
            time.sleep(2)
            self.limpiar_pantalla()
            return

        nuevo_nombre = input("Ingrese el nuevo nombre del equipamiento: ")
        nueva_descripcion = input("Ingrese la nueva descripción del equipamiento: ")

        # Actualizar equipamiento en la tabla Equipamiento
        update_query = "UPDATE Equipamiento SET nombre = %s, descripcion = %s WHERE id_equip = %s"
        try:
            cursor.execute(update_query, (nuevo_nombre, nueva_descripcion, id_equipamiento))
            conexion.commit()  # Confirmar la transacción
            print("Equipamiento actualizado correctamente.")
        except Exception as e:
            conexion.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al actualizar equipamiento: {str(e)}")

        time.sleep(2)
        self.limpiar_pantalla()

    def modificar_fichas(self, cursor, conexion):
        print("Modificar fichas de personajes")

        # Obtener lista de personajes
        cursor.execute("SELECT id_personaje, nombre FROM Personaje")
        personajes = cursor.fetchall()

        if not personajes:
            print("No hay personajes disponibles para modificar.")
            return

        print("Seleccione el personaje que desea modificar:")
        for idx, personaje in enumerate(personajes):
            print(f"{idx + 1}. {personaje[1]}")

        personaje_seleccionado = seleccionar_entero("Ingrese el número del personaje seleccionado: ", len(personajes))

        id_personaje = personajes[personaje_seleccionado - 1][0]

        # Obtener raza del personaje seleccionado
        cursor.execute("SELECT raza_id FROM Personaje WHERE id_personaje = %s", (id_personaje,))
        id_raza_personaje = cursor.fetchone()[0]

        print("1. Editar habilidades")
        print("2. Editar poder")
        print("3. Cambiar estado")
        print("4. Agregar o editar el equipamiento")
        opcion = seleccionar_entero("Seleccione la opción que desea realizar: ", 4)

        if opcion == 1:
            self.editar_habilidades(cursor, id_raza_personaje, id_personaje)
        elif opcion == 2:
            self.editar_poder(cursor, id_raza_personaje, id_personaje)
        elif opcion == 3:
            self.cambiar_estado(cursor, id_personaje, conexion)
        elif opcion == 4:
            self.completar_equipamiento(cursor, id_personaje, conexion)
    def editar_poder(self, cursor, id_raza_personaje, id_personaje):
        print("Editar poder de un personaje")

        # Obtener poderes disponibles para la raza del personaje seleccionado
        query = """
            SELECT p.id_poder, p.nombre, p.descripcion
            FROM Poder p
            WHERE p.poder_raza_id = %s
        """
        cursor.execute(query, (id_raza_personaje,))
        poderes = cursor.fetchall()

        if not poderes:
            print("No hay poderes disponibles para esta raza.")
            return

        print("Seleccione un nuevo poder para el personaje:")
        for idx, poder in enumerate(poderes):
            print(f"{idx + 1}. {poder[1]}: {poder[2]}")

        poder_seleccionado = seleccionar_entero("Ingrese el número del poder seleccionado: ", len(poderes))

        id_poder = poderes[poder_seleccionado - 1][0]

        # Actualizar poder del personaje en la base de datos
        update_query = "UPDATE Personaje SET poder_id = %s WHERE id_personaje = %s"
        print(f"Query SQL: {update_query} (id_poder={id_poder}, id_personaje={id_personaje})")  # Imprimir consulta SQL generada
        try:
            cursor.execute(update_query, (id_poder, id_personaje))
            cursor._connection.commit()  # Confirmar la transacción
            print("Poder actualizado correctamente.")
            time.sleep(2)
        except Exception as e:
            cursor._connection.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al actualizar poder: {str(e)}")
        self.limpiar_pantalla()

    def editar_habilidades(self, cursor, id_raza_personaje, id_personaje):
        print("Editar habilidades de un personaje")

        # Obtener habilidades disponibles para la raza del personaje seleccionado
        query = """
            SELECT h.id_habilidad, h.nombre, h.descripcion
            FROM Habilidad h
            WHERE h.hab_raza_id = %s
        """
        cursor.execute(query, (id_raza_personaje,))
        habilidades = cursor.fetchall()

        if not habilidades:
            print("No hay habilidades disponibles para esta raza.")
            return

        print("Seleccione hasta 2 habilidades adicionales para el personaje:")
        for idx, habilidad in enumerate(habilidades):
            print(f"{idx + 1}. {habilidad[1]}: {habilidad[2]}")

        habilidades_seleccionadas = seleccionar_varios_enteros("Ingrese los números de las habilidades seleccionadas (separadas por comas): ", len(habilidades), 2)

        id_habilidad1 = habilidades[habilidades_seleccionadas[0] - 1][0]
        id_habilidad2 = habilidades[habilidades_seleccionadas[1] - 1][0] if len(habilidades_seleccionadas) > 1 else None

        # Actualizar habilidades del personaje en la base de datos
        update_query = "UPDATE Personaje SET habilidad_id1 = %s, habilidad_id2 = %s WHERE id_personaje = %s"
        print(f"Query SQL: {update_query} (id_habilidad1={id_habilidad1}, id_habilidad2={id_habilidad2}, id_personaje={id_personaje})")  # Imprimir consulta SQL generada
        try:
            cursor.execute(update_query, (id_habilidad1, id_habilidad2, id_personaje))
            cursor._connection.commit()  # Confirmar la transacción
            print("Habilidades actualizadas correctamente.")
            time.sleep(2)
        except Exception as e:
            cursor._connection.rollback()  # Deshacer la transacción en caso de error
            print(f"Error al actualizar habilidades: {str(e)}")
        self.limpiar_pantalla()

    def completar_equipamiento(self, cursor, id_personaje, conexion):
        print("Completar equipamiento de un personaje")
        equipamientos = self.obtener_equipamientos(cursor)
        print("Seleccione 1 equipamiento para el personaje:")
        for idx, equipamiento in enumerate(equipamientos):
            print(f"{idx + 1}. {equipamiento[1]}: {equipamiento[2]}")

        id_equipamiento = seleccionar_entero("Ingrese el número del equipamiento elegido: ", len(equipamientos))
        id_equipamiento = equipamientos[id_equipamiento - 1][0]

        # Actualizar equipamiento del personaje en la base de datos
        update_query = "UPDATE Personaje SET equip_id = %s WHERE id_personaje = %s"
        try:
            cursor.execute(update_query, (id_equipamiento, id_personaje))
            print("Equipamiento actualizado correctamente.")
            conexion.commit()  # Commit después de la actualización
            time.sleep(2)
            self.limpiar_pantalla()
        except Exception as e:
            print(f"Error al actualizar equipamiento: {str(e)}")

    def reemplazar_poderes(self, cursor, id_personaje):
        print("Reemplazar poderes de un personaje")
        # Implementación de reemplazar_poderes aquí
        time.sleep(1)
        self.limpiar_pantalla()

    def subir_nivel(self, cursor, id_personaje, conexion):
        print("Subir nivel de personaje")

        # Obtener el nivel actual del personaje
        query = "SELECT nivel FROM Personaje WHERE id_personaje = %s"
        cursor.execute(query, (id_personaje,))
        nivel_actual = cursor.fetchone()[0]

        # Mostrar el nivel actual y solicitar la cantidad a sumar
        print(f"Nivel actual: {nivel_actual}")
        cantidad_a_sumar = input("Ingrese la cantidad que desea sumar al nivel actual: ")

        try:
            cantidad_a_sumar = int(cantidad_a_sumar)
            if cantidad_a_sumar > 0:
                nuevo_nivel = nivel_actual + cantidad_a_sumar

                # Actualizar el nivel del personaje en la base de datos
                update_query = "UPDATE Personaje SET nivel = %s WHERE id_personaje = %s"
                print(f"Query SQL: {update_query} (nuevo_nivel={nuevo_nivel}, id_personaje={id_personaje})")  # Imprimir consulta SQL generada
                cursor.execute(update_query, (nuevo_nivel, id_personaje))
                print(f"Nivel actualizado a: {nuevo_nivel}")
                conexion.commit()  # Commit después de la actualización
            else:
                print("La cantidad a sumar debe ser mayor que cero.")
        except ValueError:
            print("Ingrese un número válido para la cantidad a sumar.")

        time.sleep(1)
        self.limpiar_pantalla()

    def cambiar_estado(self, cursor, id_personaje, conexion):
        print("Cambiar estado del personaje")

        # Obtener todos los estados disponibles en la base de datos
        cursor.execute("SELECT id_estado, nombre FROM Estado")
        estados = cursor.fetchall()

        if not estados:
            print("No hay estados disponibles para seleccionar.")
            return

        # Mostrar los estados disponibles para elegir
        print("Estados disponibles:")
        for idx, estado in enumerate(estados):
            print(f"{idx + 1}. {estado[1]}")

        opcion_estado = seleccionar_entero("Ingrese el número del estado al que desea cambiar: ", len(estados))
        id_nuevo_estado = estados[opcion_estado - 1][0]

        # Actualizar el estado del personaje en la base de datos
        update_query = "UPDATE Personaje SET estado_id = %s WHERE id_personaje = %s"
        print(f"Query SQL: {update_query} (id_nuevo_estado={id_nuevo_estado}, id_personaje={id_personaje})")  # Imprimir consulta SQL generada
        try:
            cursor.execute(update_query, (id_nuevo_estado, id_personaje))
            print(f"Estado actualizado correctamente.")
            conexion.commit()  # Commit después de la actualización
        except Exception as e:
            print(f"Error al cambiar estado: {str(e)}")

        time.sleep(1)
        self.limpiar_pantalla()

    def ver_informe_personajes(self, cursor):
        print("Informe de personajes:")
        query = """
            SELECT p.nombre, r.nombre AS raza, h1.nombre AS habilidad1, h2.nombre AS habilidad2,
                   eq.nombre AS equipamiento, po.nombre AS poder, e.nombre AS estado, p.nivel
            FROM Personaje p
            INNER JOIN Raza r ON p.raza_id = r.id_raza
            LEFT JOIN Habilidad h1 ON p.habilidad_id1 = h1.id_habilidad
            LEFT JOIN Habilidad h2 ON p.habilidad_id2 = h2.id_habilidad
            LEFT JOIN Equipamiento eq ON p.equip_id = eq.id_equip
            LEFT JOIN Poder po ON p.poder_id = po.id_poder
            INNER JOIN Estado e ON p.estado_id = e.id_estado
        """
        cursor.execute(query)
        personajes = cursor.fetchall()

        for personaje in personajes:
            habilidades = ", ".join(filter(None, [personaje[2], personaje[3]]))
            print(f"\nDetalles del personaje '{personaje[0]}'")
            print(f"- Raza: {personaje[1]}")
            print(f"- Habilidades: {habilidades}")
            print(f"- Equipamiento: {personaje[4] if personaje[4] else 'Ninguno'}")
            print(f"- Poder: {personaje[5] if personaje[5] else 'Ninguno'}")
            print(f"- Estado: {personaje[6]}")
            print(f"- Nivel: {personaje[7]}")
            print("=======================")

        input("Presione Enter para continuar...")
        time.sleep(1)
        self.limpiar_pantalla()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def obtener_habilidades(self, cursor):
        query = "SELECT id_habilidad, nombre, descripcion FROM Habilidad"
        cursor.execute(query)
        return cursor.fetchall()

    def obtener_equipamientos(self, cursor):
        query = "SELECT id_equip, nombre, descripcion FROM Equipamiento"
        cursor.execute(query)
        return cursor.fetchall()