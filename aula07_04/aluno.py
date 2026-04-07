class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ""
        self.notas = [0]*3
        
 
 # RA = constantes, Ra = Classe, ra = variavel
 
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        while(self.ra == ""):
            print("Esse aluno não tem RA.")
            ra = input("Informe o RA: ")

        print(f"O RA é: {self.ra}")
     
    def pedir_notas(self):
        for i in range(0, len(self.notas)):
            self.notas[i] = int(input(f"Digite a nota {i+1}:"))

    def calcular_media(self):
        soma = 0.0
        for i in range(0, len(self.notas)):
            soma+=self.notas[i]
        media = soma/len(self.notas)
        return media    
            
nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
curso = input("Qual o curso que você está cursando: ")

mayra = Aluno(nome, idade, curso)
mayra.pedir_notas()
print("A média é : ", mayra.calcular_media())

   
    
# ra = input("Qual seu ra: ")
# alun1 = Aluno(nome, idade, curso)
# alun1.apresentar()
# alun1.ra = ra
# alun1.apresentar()

  