#Nombre: Javiera Cabezas
#Laboratorio TPA

class Camara:
    
    def __init__(self, id, nom, res):
        self.id = id
        self.nombre = nom
        self.resolucion = res
        
    def transmitir(self):
        nombre = self.nombre
        print("Se está transmitiendo desde la cámara: "+nombre)
        
class Dispositivo(Camara):
    
    def __init__(self, id , nom, res, marca, modelo):
        super().__init__(id, nom, res)
        self.marca = marca
        self.modelo = modelo
        
    def transmitir(self):
        marca = self.marca
        mod = self.modelo
        print("Se está transmitiendo desde: "+marca+mod)
        
class Sesion:
    
    def __init__(self, id, asig, profesor, sala, fecha, hInicio, hFin, cam, listaCam):
        self.id = id
        self.asignatura = asig
        self.profesor = profesor
        self.sala = sala
        self.fecha = fecha
        self.horaInicio = hInicio
        self.horaFinal = hFin
        self.camaraEnUso = cam
        self.listaCamaras = listaCam
        
    def iniciarTransmicion(self):
        id = self.id
        print("sesión ", id, "iniciando")
        self.camaraEnUso.transmitir()
        
    def terminarTransmicion(self):
        id = self.id
        print("Sesión ", id, "terminada")
        
    def cambiarCamara(self):
        x = self.listaCamaras.index(self.camaraEnUso)
        if x == len(self.listaCamaras)-1:
            x = 0
        else:
            x += 1
        self.camaraEnUso = self.listaCamaras[x]
        print("Cambiando a cámara: ", self.camaraEnUso.nombre)
        
class Main:
    def __init__(self):
        self.sesiones = []
        
    def crearSesion(self):
        id = input("Ingresar id: ")
        asig = input("Nombre Asignatura: ")
        profesor = input("Nombre Profesor: ")
        sala = input("Nombre Sala: ")
        fecha = input("Fecha de la sesión: ")
        hInicio = input("Ingrese la hora de inicio: ")
        hFin = input("Ingrese la hora de fin: ")
        
        camaras = []
        numCam = int(input("Numero de cámaras utilizadas en la sesión: "))
        for i in range(numCam):
            i =+1
            i = str(i)
            idCam = input("Ingrese el id de la cámara "+i+": ")
            nom = input("Ingrese el nombre de la cámara "+i+ ": ")
            res = input("Ingrese la resolución de la cámara "+i+": ")
            marca = input("Ingrese la marca de la cámara "+i+": ")
            mod = input("Ingrese el modelo de la cámara "+i+": ")
            dispositivo = Dispositivo(idCam, nom, res, marca, mod)
            camaras.append[dispositivo]
            
        camaraEnUso = camaras[0]  
        sesion = Sesion(id, asig, profesor, sala, fecha, hInicio, hFin, camaraEnUso, camaras)
                    
inicio = Main()            
inicio.crearSesion()        
        
    
        
        
        
        
    