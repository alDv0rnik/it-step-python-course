class Material:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    def get_material(self):
        return f'{self.__name};{self.__density}'


class Subject:
    def __init__(self, name, material, volume):
        self.__name = name
        self.__material = material
        self.__volume = volume
        materials = {'steel': 7850.0, 'copper': 8500}
        self.density = materials.get(self.__material)

    def __get_mass(self):
        mass = self.density * self.__volume
        return mass

    def get_subject(self):
        return f'{self.__name};{self.__material};{self.density};{self.__volume};{self.__get_mass()}'


class Runner:
    def __init__(self, steel_wire: Subject):
        self.steel_wire = steel_wire

    def get_subject(self):
        return f"The wire mass is {self.steel_wire.get_subject().split(';')[-1]} kg"


steel = Runner(Subject('wire', 'steel', 0.03))
print(steel.get_subject())
copper = Runner(Subject('wire', 'copper', 0.03))
print(copper.get_subject())
