from osztaly import Alkalmazottak
        

class Work():
    def __init__(self):
        self.alk_lista = []

    def betolt_alkalmazottak(self):
        file = open("alkalmazottak.txt", "r", encoding="utf-8")
        row =  file.readline()


        while(row):
            row = file.readline()
            rowSp = row.split(";")  
            if len(rowSp) > 1:
                alkalmazott = Alkalmazottak(rowSp[0],rowSp[1],rowSp[2],rowSp[3])
                self.alk_lista.append(alkalmazott)     
        return self.alk_lista



    def ment_alkalmazottakat(self):
        for alk in self.alk_lista:
            file = open("alkalmazottak_veg", "a", encoding="utf-8")
            file.write(alk[0])
            file.write(alk[1])
            file.write(alk[2])
            file.write(alk[3])
        return "A fájlba írás megtörtént"

    def controller(self):
        readSuccess = self.betolt_alkalmazottak()
        self.ment_alkalmazottakat()

work = Work()
work.controller()               