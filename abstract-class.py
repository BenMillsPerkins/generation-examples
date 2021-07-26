class ObjectList():
    name = ""
    listOfObjects = []

    def saveToFile(self):
        with open(self.name, 'w') as file:
            file.write()


    def addElement(self, element):
        self.listOfObjects.append(element)



products = ObjectList()
couriers = ObjectList()

products.saveToFile()