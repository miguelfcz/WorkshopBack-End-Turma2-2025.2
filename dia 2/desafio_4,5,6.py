class animal():

    def __init__(self, nome, idade, tipo_animal):
        self.nome = nome
        self.idade = idade
        self.tipo_animal = tipo_animal

    def falar(self):
        return "Animal falando"
    
    def apresentar(self):
        return f"Nome: {self.nome}, idade: {self.idade}"
    
class cachorro(animal):
    def __init__(self, nome, idade, tipo_animal):
        super().__init__(nome, idade, tipo_animal)

    def falar(self):
        return "Latindo"

class gato(animal):
    def __init__(self, nome, idade, tipo_animal):
        super().__init__(nome, idade, tipo_animal)
        
    def falar(self):
        return "Miau"

class pato(animal):
    def __init__(self, nome, idade, tipo_animal):
        super().__init__(nome, idade, tipo_animal)
        
    def falar(self):
        return "Quack"

class macaco(animal):
    def __init__(self, nome, idade, tipo_animal):
        super().__init__(nome, idade,tipo_animal)
        
    def falar(self):
        return "UuUuAaAa"
    
class zoologico(animal):
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)
    
    def listar_animais(self):
        return [animal.nome for animal in self.animais]
    
    def filtrar_por_tipo(self, tipo_animal):
        return [animal.tipo_animal for animal in self.animais if isinstance(animal, tipo_animal)]
    

zoo = zoologico()

zoo.adicionar_animal(cachorro("Cachorro1", 3, "cachorro"))
zoo.adicionar_animal(gato("Gato1", 4, "gato"))
zoo.adicionar_animal(pato("Pato1", 2, "pato"))
zoo.adicionar_animal(macaco("Macaco1", 1, "macaco"))
zoo.adicionar_animal(macaco("Macaco2", 1, "macaco"))

print(zoo.listar_animais())
print(zoo.filtrar_por_tipo(macaco))