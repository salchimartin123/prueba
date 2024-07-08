class Usuario:
    def __init__(self, nombre, contrasena, area, id_usuario=None):
        self.nombre = nombre
        self.contrasena = contrasena
        self.area = area
        self.id_usuario = id_usuario
        self.conectado = False
        self.intentos = 3

    def conectar(self, cursor):
        while self.intentos > 0:
            my_contrasena = input("Ingrese su contraseña: ")
            if my_contrasena == self.contrasena:
                print("¡Se ha conectado exitosamente!")
                self.conectado = True
                break
            else:
                self.intentos -= 1
                print("Contraseña incorrecta, inténtelo nuevamente.")
                print(f"Intentos restantes: {self.intentos}")

        if self.intentos == 0:
            print("Se ha agotado el número de intentos. Usuario bloqueado temporalmente.")

    def desconectar(self):
        if self.conectado:
            print("Se cerró la sesión con éxito.")
            self.conectado = False
        else:
            print("No se ha iniciado sesión.")

    def __str__(self):
        estado = "conectado" if self.conectado else "desconectado"
        return f"Usuario: {self.nombre}, Área: {self.area}, Estado: {estado}"