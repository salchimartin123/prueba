import mysql.connector
import os
import time
from poder import Poder
from raza import Raza
from equipamiento import Equipamiento
from habilidad import Habilidad
from estado import Estado
from usuario import Usuario
from jugador import Jugador
from gamemaster import GameMaster
from personaje import Personaje

# Funciones auxiliares para la gestión del juego
def conectar_bd():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Coloca tu contraseña si es diferente
        database="juegoderol"
    )
    return conexion

def obtener_usuario(nombre, cursor):
    query = "SELECT id, nombre, contrasena, area FROM Usuario WHERE nombre = %s"
    cursor.execute(query, (nombre,))
    result = cursor.fetchone()
    if result:
        return Usuario(result[1], result[2], result[3], result[0])
    else:
        return None

def insertar_usuario(nombre, contrasena, area, conexion, cursor):
    query = "INSERT INTO Usuario (nombre, contrasena, area) VALUES (%s, %s, %s)"
    cursor.execute(query, (nombre, contrasena, area))
    conexion.commit()
    print(f"Usuario '{nombre}' insertado correctamente.")
    time.sleep(2)
    limpiar_pantalla()

def obtener_razas(cursor):
    query = "SELECT id_raza, nombre, tipo FROM Raza"
    cursor.execute(query)
    return cursor.fetchall()

def obtener_habilidades_por_raza(id_raza, cursor):
    query = "SELECT id_habilidad, nombre, descripcion FROM Habilidad WHERE hab_raza_id = %s"
    cursor.execute(query, (id_raza,))
    return cursor.fetchall()

def obtener_equipamientos(cursor):
    query = "SELECT id_equip, nombre, descripcion FROM Equipamiento"
    cursor.execute(query)
    return cursor.fetchall()

def obtener_poderes_por_raza(id_raza, cursor):
    query = "SELECT id_poder, nombre, descripcion FROM Poder WHERE poder_raza_id = %s"
    cursor.execute(query, (id_raza,))
    return cursor.fetchall()

def obtener_estado_muerto(cursor):
    query = "SELECT id_estado FROM Estado WHERE nombre = 'muerto'"
    cursor.execute(query)
    return cursor.fetchone()[0]

def obtener_estado_vivo(cursor):
    query = "SELECT id_estado FROM Estado WHERE nombre = 'vivo'"
    cursor.execute(query)
    return cursor.fetchone()[0]

def crear_personaje(usuario, cursor, conexion):
    limpiar_pantalla()
    print("Creación de personaje")
    nombre_personaje = input("Ingrese el nombre del personaje: ")

    # Mostrar razas disponibles
    razas = obtener_razas(cursor)
    print("Seleccione una raza:")
    for idx, raza in enumerate(razas):
        print(f"{idx + 1}. {raza[1]} ({raza[2]})")

    id_raza = seleccionar_entero("Ingrese el número de la raza elegida: ", len(razas))
    id_raza_seleccionada = razas[id_raza - 1][0]  # Obtener la id_raza correspondiente
    limpiar_pantalla()

    # Mostrar habilidades disponibles para la raza seleccionada
    habilidades = obtener_habilidades_por_raza(id_raza_seleccionada, cursor)
    print("Seleccione hasta 2 habilidades (puede elegir solo una si lo desea):")
    for idx, habilidad in enumerate(habilidades):
        print(f"{idx + 1}. {habilidad[1]}: {habilidad[2]}")

    habilidades_seleccionadas = seleccionar_varios_enteros("Ingrese los números de las habilidades seleccionadas (separadas por comas): ", len(habilidades), 2)

    id_habilidad1 = habilidades[habilidades_seleccionadas[0] - 1][0]
    id_habilidad2 = habilidades[habilidades_seleccionadas[1] - 1][0] if len(habilidades_seleccionadas) > 1 else None
    limpiar_pantalla()

    # Mostrar equipamientos disponibles
    equipamientos = obtener_equipamientos(cursor)
    print("Seleccione 1 equipamiento (o presione Enter para omitir):")
    for idx, equipamiento in enumerate(equipamientos):
        print(f"{idx + 1}. {equipamiento[1]}: {equipamiento[2]}")

    id_equip = seleccionar_entero("Ingrese el número del equipamiento elegido (o presione Enter para omitir): ", len(equipamientos))
    if id_equip is not None:
        id_equip = equipamientos[id_equip - 1][0]

    limpiar_pantalla()
    # Mostrar poderes disponibles para la raza seleccionada
    poderes = obtener_poderes_por_raza(id_raza_seleccionada, cursor)
    if not poderes:
        print("No hay poderes disponibles para la raza seleccionada. Intente con otra raza.")
        time.sleep(2)
        limpiar_pantalla()
        return

    print("Seleccione 1 poder:")
    for idx, poder in enumerate(poderes):
        print(f"{idx + 1}. {poder[1]}: {poder[2]}")

    indice_poder_seleccionado = seleccionar_entero("Ingrese el número del poder elegido: ", len(poderes))
    id_poder = poderes[indice_poder_seleccionado - 1][0]

    limpiar_pantalla()

    # Obtener el estado 'vivo'
    id_estado_vivo = obtener_estado_vivo(cursor)

    try:
        query = """
            INSERT INTO Personaje (nombre, nivel, estado_id, usuario_id, raza_id, habilidad_id1, habilidad_id2, equip_id, poder_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre_personaje, 1, id_estado_vivo, usuario.id_usuario, id_raza_seleccionada, id_habilidad1, id_habilidad2, id_equip, id_poder))
        conexion.commit()

        # Mostrar información del personaje creado
        print(f"\nPersonaje '{nombre_personaje}' creado correctamente con los siguientes detalles:")
        print(f"- Raza: {razas[id_raza - 1][1]}")
        print(f"- Habilidades: {habilidades[habilidades_seleccionadas[0] - 1][1]}{', ' + habilidades[habilidades_seleccionadas[1] - 1][1] if len(habilidades_seleccionadas) > 1 else ''}")
        if id_equip is not None:
            print(f"- Equipamiento: {equipamientos[id_equip - 1][1]}")
        print(f"- Poder: {poderes[indice_poder_seleccionado - 1][1]}")
        print(f"- Estado: Vivo")
        print(f"- Nivel: 1")

        time.sleep(5)
        limpiar_pantalla()

    except mysql.connector.Error as err:
        print(f"Error al insertar el personaje: {err}")

    except Exception as ex:
        print(f"Error desconocido: {ex}")

    finally:
        time.sleep(3)
        limpiar_pantalla()


def cambiar_equipamiento(usuario, cursor, conexion):
    print(f"Opciones de equipamiento para {usuario.nombre}:")

    # Mostrar personajes del usuario
    query_personajes = "SELECT id_personaje, nombre, estado_id FROM Personaje WHERE usuario_id = %s"
    cursor.execute(query_personajes, (usuario.id_usuario,))
    personajes = cursor.fetchall()

    if not personajes:
        print("No tienes personajes creados.")
        time.sleep(2)
        limpiar_pantalla()
        return

    print("Personajes creados:")
    for idx, personaje in enumerate(personajes):
        print(f"{idx + 1}. {personaje[1]}")

    id_personaje_seleccionado = seleccionar_entero("Ingrese el número del personaje elegido: ", len(personajes))
    id_personaje = personajes[id_personaje_seleccionado - 1][0]
    estado_personaje = personajes[id_personaje_seleccionado - 1][2]

    id_estado_muerto = obtener_estado_muerto(cursor)

    # Verificar si el personaje está en estado 'muerto'
    if estado_personaje == id_estado_muerto:
        print("No se puede cambiar el equipamiento porque el personaje está muerto.")
        time.sleep(2)
        return

    print("Opciones:")
    print("1. Cambiar equipamiento")
    print("2. Completar equipamiento actual")
    print("3. Volver")

    opcion = seleccionar_entero("Seleccione una opción: ", 3)

    if opcion == 1:
        # Mostrar equipamientos disponibles
        equipamientos = obtener_equipamientos(cursor)
        print("Seleccione 1 equipamiento nuevo:")
        for idx, equipamiento in enumerate(equipamientos):
            print(f"{idx + 1}. {equipamiento[1]}: {equipamiento[2]}")

        id_equip_nuevo = seleccionar_entero("Ingrese el número del equipamiento nuevo: ", len(equipamientos))
        id_equip_nuevo = equipamientos[id_equip_nuevo - 1][0]

    elif opcion == 2:
        # Mantener el equipamiento actual
        query_equip_actual = "SELECT equip_id FROM Personaje WHERE id_personaje = %s"
        cursor.execute(query_equip_actual, (id_personaje,))
        id_equip_nuevo = cursor.fetchone()[0]

    elif opcion == 3:
        return

    # Actualizar el equipamiento del personaje en la base de datos
    update_query = "UPDATE Personaje SET equip_id = %s WHERE id_personaje = %s"
    try:
        cursor.execute(update_query, (id_equip_nuevo, id_personaje))
        conexion.commit()
        print(f"Equipamiento cambiado correctamente para el personaje '{personajes[id_personaje_seleccionado - 1][1]}'.")

    except mysql.connector.Error as err:
        print(f"Error al actualizar el equipamiento: {err}")

    time.sleep(3)
    limpiar_pantalla()

def ver_personajes_creados(usuario, cursor):
    query = """
        SELECT p.id_personaje, p.nombre, p.nivel, e.nombre AS estado, r.nombre AS raza,
               h1.nombre AS habilidad1, h2.nombre AS habilidad2, eq.nombre AS equipamiento,
               po.nombre AS poder
        FROM Personaje p
        INNER JOIN Estado e ON p.estado_id = e.id_estado
        INNER JOIN Raza r ON p.raza_id = r.id_raza
        LEFT JOIN Habilidad h1 ON p.habilidad_id1 = h1.id_habilidad
        LEFT JOIN Habilidad h2 ON p.habilidad_id2 = h2.id_habilidad
        INNER JOIN Equipamiento eq ON p.equip_id = eq.id_equip
        INNER JOIN Poder po ON p.poder_id = po.id_poder
        WHERE p.usuario_id = %s
    """
    cursor.execute(query, (usuario.id_usuario,))
    personajes = cursor.fetchall()

    if not personajes:
        print("No tienes personajes creados.")
    else:
        print("Tus personajes creados:")
        for idx, personaje in enumerate(personajes):
            print(f"\nPersonaje {idx + 1}:")
            print(f"- Nombre: {personaje[1]}")
            print(f"- Nivel: {personaje[2]}")
            print(f"- Estado: {personaje[3]}")
            print(f"- Raza: {personaje[4]}")
            print(f"- Habilidades: {personaje[5]}{', ' + personaje[6] if personaje[6] else ''}")
            print(f"- Equipamiento: {personaje[7]}")
            print(f"- Poder: {personaje[8]}")

    input("\nPresiona Enter para continuar...")
    time.sleep(2)
    limpiar_pantalla()


def main():
    while True:
        limpiar_pantalla()
        conexion = conectar_bd()
        cursor = conexion.cursor()

        print("Bienvenido al juego de rol.")

        area = input("¿Desea ingresar como Jugador (1) o como GameMaster (2)? (Ingrese 'q' para salir) ").lower()
        limpiar_pantalla()

        if area == '1':
            area = 'jugador'
        elif area == '2':
            area = 'gamemaster'
        elif area == 'q':
            print("Saliendo del programa...\n")
            time.sleep(2)
            limpiar_pantalla()
            break
        else:
            print("Opción no válida. Por favor, ingrese '1' para Jugador o '2' para GameMaster.\n")
            time.sleep(2)
            limpiar_pantalla()
            continue

        while True:
            print(f"Bienvenido {area.capitalize()}.\n")
            print("Seleccione una opción:")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("q. Salir")

            opcion = input("Ingrese su opción: ").lower()
            limpiar_pantalla()

            if opcion == '1':
                nombre = input("Ingrese su nombre de usuario: ")
                usuario = obtener_usuario(nombre, cursor)

                if usuario:
                    if usuario.area == area:
                        usuario.conectar(cursor)
                        if usuario.conectado:
                            if area == 'jugador':
                                while True:
                                    print(f"Opciones para {usuario.nombre}:")
                                    print("1. Crear personaje")
                                    print("2. Ver mis personajes creados")
                                    print("3. Cambiar equipamiento de un personaje")
                                    print("4. Salir")

                                    opcion_jugador = input("Ingrese su opción: ")

                                    if opcion_jugador == '1':
                                        crear_personaje(usuario, cursor, conexion)
                                    elif opcion_jugador == '2':
                                        ver_personajes_creados(usuario, cursor)
                                    elif opcion_jugador == '3':
                                        cambiar_equipamiento(usuario, cursor, conexion)
                                    elif opcion_jugador == '4':
                                        limpiar_pantalla()
                                        break
                                    else:
                                        print("Opción no válida. Intente de nuevo.")
                                    limpiar_pantalla()
                            elif area == 'gamemaster':
                                gamemaster = GameMaster(usuario.nombre)
                                while True:
                                    print("Opciones de GameMaster:")
                                    print("1. Modificar fichas de personajes")
                                    print("2. Ver informe de personajes")
                                    print("3. Agregar raza al sistema")
                                    print("4. Agregar estado al sistema")
                                    print("5. Agregar equipamiento al sistema")
                                    print("6. Agregar habilidad al sistema")
                                    print("7. Agregar poder al sistema")
                                    print("8. Editar descripción de habilidad")
                                    print("9. Editar descripcion de poder")
                                    print("10. Editar nombre de equipamiento")
                                    print("q. Salir")

                                    opcion_gm = input("Seleccione una opción: ")

                                    if opcion_gm == '1':
                                        gamemaster.modificar_fichas(cursor, conexion)
                                    elif opcion_gm == '2':
                                        gamemaster.ver_informe_personajes(cursor)
                                    elif opcion_gm == '3':
                                        gamemaster.agregar_raza(cursor, conexion)
                                    elif opcion_gm == '4':
                                        gamemaster.agregar_estado(cursor, conexion)
                                    elif opcion_gm == '5':
                                        gamemaster.agregar_equipamiento(cursor, conexion)
                                    elif opcion_gm == '6':
                                        gamemaster.agregar_habilidad(cursor, conexion)
                                    elif opcion_gm == '7':
                                        gamemaster.agregar_poder(cursor, conexion)
                                    elif opcion_gm == '8':
                                        gamemaster.editar_descripcion_habilidad(cursor, conexion)
                                    elif opcion_gm == '9':
                                        gamemaster.editar_descripcion_poder(cursor, conexion)
                                    elif opcion_gm == '10':
                                        gamemaster.editar_equipamiento(cursor, conexion)
                                    elif opcion_gm == 'q':
                                        break
                                    else:
                                        print("Opción no válida. Intente de nuevo.")
                                    time.sleep(2)
                                    limpiar_pantalla()
                        else:
                            print("Error al conectar. Intente nuevamente.")
                            time.sleep(2)
                            limpiar_pantalla()
                    else:
                        print(f"Usuario '{nombre}' no es {area.capitalize()}. Intente con otra opción.\n")
                        time.sleep(2)
                        limpiar_pantalla()
                else:
                    print("Usuario no encontrado. Regístrese primero.\n")
                    time.sleep(2)
                    limpiar_pantalla()

            elif opcion == '2':
                nombre = input("Ingrese su nombre de usuario: ")
                contrasena = input("Ingrese su contraseña: ")
                insertar_usuario(nombre, contrasena, area, conexion, cursor)
                time.sleep(2)
                limpiar_pantalla()

            elif opcion == 'q':
                print("Saliendo del programa...\n")
                time.sleep(2)
                limpiar_pantalla()
                break

            else:
                print("Opción no válida. Intente de nuevo.\n")
                time.sleep(2)
                limpiar_pantalla()

        cursor.close()
        conexion.close()

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def seleccionar_hasta_dos_enteros(mensaje, maximo):
    while True:
        entrada = input(mensaje)
        if not entrada:
            limpiar_pantalla()
            return []
        numeros = entrada.split(',')
        if len(numeros) > 2:
            print("Debe ingresar como máximo dos números separados por comas.")
            continue
        try:
            numeros = [int(num.strip()) for num in numeros]
            if all(1 <= num <= maximo for num in numeros):
                limpiar_pantalla()
                return numeros
            else:
                print(f"Números fuera de rango. Deben estar entre 1 y {maximo}.")
        except ValueError:
            print("Entrada inválida. Ingrese números enteros separados por comas.")

def seleccionar_entero(mensaje, max_opciones):
    while True:
        try:
            seleccion = int(input(mensaje))
            if 1 <= seleccion <= max_opciones:
                return seleccion
            else:
                print(f"Por favor, ingrese un número válido entre 1 y {max_opciones}.")
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
                print(f"Por favor, ingrese hasta {max_seleccion} números válidos entre 1 y {max_valor}.")
        except ValueError:
            print("Por favor, ingrese números válidos separados por comas.")


if __name__ == "__main__":
    main()  # seleccionar