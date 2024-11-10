class Perro:

    def __init__(self, raza, nombre, color):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.energia = 100

    def ladrar(self):
        print(self.nombre, "dice guau")
        self.energia -= 5
        
    def moverse(self):
        print(self.nombre, "camina hacia delante")
        self.energia -= 10

    def dormir(self):
        print(self.nombre, "Esta durmiendo")
    
    def Info(self):
        print(self.nombre, self.raza, self.color, self.energia)
    
    #GETTERS

    def get_nombre(self):
        return self.nombre


perro1 = Perro("Chiguagua", "Bob", "Blanco")
perro1.Info()
perro1.ladrar()
perro1.dormir()

class PerroGuia(Perro):
    
    def __init__(self, raza, nombre, color, dueño):
        super().__init__(raza, nombre, color)
        self.dueño = dueño

    def ladrar(self, dueño):
        print(self.nombre, "ladra y avisa a", dueño)

    def get_dueño(self):
        return self.dueño
    
perro2 = PerroGuia("Yorkshire", "Juan", "Marron", "Paco")
perro2.ladrar(perro2.get_dueño())

perro3 = PerroGuia("Pitbull", "MrWorldWide", "Blanco", "Pitbull")

perro4 = PerroGuia("A", "B", "C", "D")

perro5 = PerroGuia()