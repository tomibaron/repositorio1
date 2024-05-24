class Tamagotchi:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "Indiferente"
        self.esta_vivo = True
    
    def estado_de_humor(self):
        if 0<= self.nivel_felicidad < 20:
            self.humor = "Enojado"
        elif 20 <= self.nivel_felicidad < 40:
            self.humor = "Triste"
        elif 40 <= self.nivel_felicidad < 60:
            self.humor = "Indiferente"
        elif 60 <= self.nivel_felicidad < 80:
            self.humor = "Feliz"
        elif 80<= self.nivel_felicidad <=100:
            self.humor = "Eufórico"
    
    def verificacion_de_estado(self):
        if self.nivel_energia <= 0:
            self.nivel_energia = 0
            self.esta_vivo = False
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear unx nuevx :(")
        elif self.nivel_energia == 0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear unx nuevx :(")
        else:
            print(f"Tu tamagotchi {self.nombre} está vivx. Puedes continuar jugando con el/ella")
    
    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Energía: {self.nivel_energia}")
        print(f"Hambre: {self.nivel_hambre}")
        print(f"Felicidad: {self.nivel_felicidad}")
        print(f"Humor: {self.humor}")
        
    def alimentar(self):
        if self.esta_vivo:
            print (f"¡Tu tamagotchi {self.nombre} está comiendo! Ñam Ñam")
            self.nivel_hambre -= 10
            self.nivel_energia -= 15
            self.estado_de_humor()
        elif self.nivel_energia == 0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear unx nuevx :(")
        elif self.nivel_energia <=0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear uno nuevo :(")
    
    def jugar(self):
        if self.esta_vivo == True and self.nivel_hambre <20:
            print (f"¡Tu tamagotchi {self.nombre} está jugando! Yuhuuu")
            self.nivel_felicidad += 20
            self.nivel_energia -=18
            self.nivel_hambre +=10
            self.estado_de_humor()
        elif self.esta_vivo == True and self.nivel_hambre >=20:
            print (f"¡Tu tamagotchi {self.nombre} está jugando pero tiene hambre, ten cuidado! Yuhuuu")
            self.nivel_felicidad -= 10
            self.nivel_energia -=20
            self.nivel_hambre +=10
            self.estado_de_humor()
        elif self.nivel_energia == 0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear unx nuevx :(")
        elif self.nivel_energia <=0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear uno nuevo :(")
    
    def dormir(self):
        if self.esta_vivo == True and self.nivel_hambre <20:
            print (f"¡Tu tamagotchi {self.nombre} está durmiendo! Zzz Zzz")
            self.nivel_energia +40
            self.nivel_hambre +=5
            self.estado_de_humor()
        elif self.esta_vivo == True and self.nivel_hambre >=20:
            print (f"¡Tu tamagotchi {self.nombre} está durmiendo pero tiene hambre, ten cuidado! Zzz Zzz")
            self.nivel_energia +=20
            self.nivel_felicidad -=30
            self.nivel_hambre +=5
            self.estado_de_humor()
        elif self.nivel_energia == 0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear unx nuevx :(")
        elif self.nivel_energia <=0:
            print(f"Tu tamagotchi {self.nombre} ha muerto por falta de energía. Deberás crear uno nuevo :(")

Tota = Tamagotchi ("Alicia")
Porota = Tamagotchi ("Rosa")