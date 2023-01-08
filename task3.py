class Material:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_density(self):
        return self.__density

    def get_material(self):
        return self.__name + ';' + str(self.__density)


class Subject:
    def __init__(self, name, material, volume):
        self.__name = name
        self.__material = material
        self.__volume = volume

    def __get_mass(self):
        mass = self.__material.get_density() * self.__volume
        return mass

    def get_subject(self):
        return self.__name + ';' + self.__material.get_name() + ';' + str(self.__volume) + ';' + str(self.__get_mass())


cooper_material = Material('cooper', 8500)
print(cooper_material.get_material())

steel_material = Material('steel', 7850.0)
print(steel_material.get_material())


class Runner:
    def __init__(self, element):
        self.__element = element

    def subject(self):
        print(self.__element.get_subject())

    def change_material(self):
        self.__element = Subject('wire', cooper_material, 0.03)
        print('Масса проволки составляет: ' + str(self.__element.get_subject().split(";")[-1]) + "кг")


steel_wire = Subject("wire", steel_material, 0.03)

run = Runner(steel_wire)

run.subject()
run.change_material()








