import re 
class schedule_Lmax:
    
    def __init__(self) -> None:
        self.pj = []
        self.dj = []
        self.solution = {}
        
        
    def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != "," and lignes[indice][compteur2] != ","):
              while(lignes[indice][compteur2] != ","):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    
        
    def parse_data(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        print(lines)
        self.pj = self.checknumber(lines,1)
        self.dj = self.checknumber(lines,3)
        print("dj", self.dj)
        print("pj", self.pj)
        
    def solve_Lmax(self):
        self.solution = {str(i): self.dj[i] for i in range(len(self.dj))}
        sorted(self.solution.items(), key=lambda k:k[1])
        print(self.solution)
    
        
        