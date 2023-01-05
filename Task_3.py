
class Material:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    def get_material(self):
        return f"{self.__name};{self.__density}"


class Subject:
    def __init__(self, name, material, volume):
        self.__name = name
        self.__material = material
        self.__volume = volume
        self.density = 7850.0
        self.for_mass = Subject.__get_mass(self, self.density)

    def __get_mass(self, x):
        mass = x * self.__volume
        return mass

    def get_subject(self):
        return f"{self.__name};{self.__material};{self.density};{self.__volume};{self.for_mass}"


class Runner:
    def __init__(self, steel_wire: Subject):
        self.steel_wire = steel_wire

    def get_subject(self):
        r = self.steel_wire.get_subject().split(";")
        res = float(r[2]) * float(r[3])
        return f"{r[1]} wire mass is {res} kg"


r = Runner(Subject("wire", "steel", 0.03))
print(r.get_subject())
