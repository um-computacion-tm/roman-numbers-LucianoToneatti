
class Persona:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0  

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia += 1 

class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)
    def cursado(self, materia):
        self.materias_cursando.append(materia)

    
# Creamos tres objetos a partir de la clase Profesor
profesor_reichu = Profesor("Reichu", "reichu123@gmail.com", "ID:7777")
print(id(profesor_reichu))
print(profesor_reichu.nombre)
print(profesor_reichu.email)
profesor_luz = Profesor("Luz", "luz321@gmail.com", "ID:1313")
print(id(profesor_luz))
print(profesor_luz.nombre)
print(profesor_luz.email)
profesor_max = Profesor("Max", "maximiliano78@gmail.com", "ID:5555")
print(id(profesor_max))
print(profesor_max.nombre)
print(profesor_max.email)

print("  ")

profesor_reichu.cambiar_nombre("REY")
print(profesor_reichu)
profesor_luz.cambiar_nombre("LUCESITA")
print(profesor_luz)
profesor_max.cambiar_nombre("MAXTIL")
print(profesor_max)

print("  ")

profesor_reichu.asistencia_clase()
print("La asistencia es ")
print(profesor_reichu.asistencia)