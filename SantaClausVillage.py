#SantaClausVillage

#Tworzenie budynków
class Buildings:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.resident_inside = []

  #lista mieszkańców w budynku
  def append_resident(self, resident):
    self.resident_inside.append(resident) 
    
  def describe_buildings(self):
    print(f"It's a {self.name}. {self.description}")

#Mieszkańcy miasteczka
class Resident:
  def __init__(self, name, age, role):
    self.name = name
    self.age = age
    self.role = role  
  def przedstaw_sie(self):
    print(f"I'm {self.name}, I'm {self.age}, I'm {self.role}")
  def age(self):
    self.age += 1


#Budynki
class HouseOfSantaClaus(Buildings):
  def christmas_party(self):
    print("Organizing a Christmas party!")

class ChristmasWorkshop(Buildings):
  def make_gifts(self):
    print("Making gifts for children")
  
class ToysManufactury(Buildings):
  def production(self):
    print("Producing toys for children.")


#Mieszkańcy
class SantaClaus(Resident):
  def przedstaw_sie(self):
    print(f"I'm Santa Claus {self.name}, I'm {self.age} years. I'm {self.role}.")
class Reindeer(Resident):
  def przedstaw_sie(self):
    super().przedstaw_sie()
    print("We are pulling Santa's sleigh. We are in a hurry to deliver \nall gifts to the children on time")

class Elf(Resident):
  def przedstaw_sie(self):
    super().przedstaw_sie()
    print("We help Santa Claus give gifts to children")

class Snowman(Resident):
  def przedstaw_sie(self):
    super().przedstaw_sie()
    print("I'm an attaction")


def main():
  Mikołaj = SantaClaus("Mikołaj", 100, "Swiętym Mikołajem")
  Rudolf = Reindeer("Rudolf", 50, "reindeer")
  Maurycy = Reindeer("Maurycy", 60, "reindeer")
  Błysk = Reindeer("Błysk", 90, "reindeer")
  Pyszałek = Reindeer("Pyszałek", 90, "reindeer")
  Alvin = Elf("Alvin", 70, "elf")
  Elvis = Elf("Elvis", 90, "elf")
  Jurand = Elf("Jurand", 100, "elf")
  Ken = Elf("Ken", 75, "elf")
  Polo = Snowman("Polo", 70, "snowman")  

#Opis budynków
  house = HouseOfSantaClaus("House of Santa Claus", "It's a place \nwhere Santa Claus live in and invite guests.")
  workshop = ChristmasWorkshop("It's a Christmas workshop to guests", "There is a place \nin which children can attend to write own wishes, \nmake some Christmas decorations and make Christmas dainties.")
  manufactury = ToysManufactury("It's a toys manufactury", "Elfs produce toys to childrens") 

  house.describe_buildings()
  workshop.describe_buildings()
  manufactury.describe_buildings()
  
  #Dodawanie mieszkańców do budynków
  house.append_resident(Mikołaj)
  workshop.append_resident(Alvin)
  workshop.append_resident(Elvis)
  manufactury.append_resident(Jurand)
  manufactury.append_resident(Ken)
  
  Mikołaj.przedstaw_sie()
  Rudolf.przedstaw_sie()
  Maurycy.przedstaw_sie()
  Błysk.przedstaw_sie()
  Pyszałek.przedstaw_sie()
  Alvin.przedstaw_sie()
  Elvis.przedstaw_sie()
  Jurand.przedstaw_sie()
  Ken.przedstaw_sie()
  Polo.przedstaw_sie()

if __name__ == "__main__":
  main()

