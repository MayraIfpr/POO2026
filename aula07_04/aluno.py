from aluno_principal import Aluno, Turma

mayra = Aluno("Mayra", 16, "Info")
ana = Aluno("Ana", 17, "Info")
enzo = Aluno("Enzo", 17, "Info")

info2024 = Turma("INFO2024", 2024)
info2024.estudantes.append(mayra)
info2024.estudantes.append(ana)
info2024.estudantes.append(enzo)

# nome = input("Qual seu nome: ")
# idade = int(input("Qual sua idade: "))
# curso = input("Qual o curso que você está cursando: ")

# mayra = Aluno(nome, idade, curso)
# mayra.pedir_notas()
# print("A média é : ", mayra.calcular_media())
  
# # ra = input("Qual seu ra: ")
# alun1 = Aluno(nome, idade, curso)
# alun1.apresentar()
# alun1.ra = ra
# alun1.apresentar()

  