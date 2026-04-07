class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        if(self.disponivel == True):
            self.disponivel = False
            print("Livro emprestado com sucesso")
        else:
            print("O livro já está emprestado")

    def devolver(self):
        if(self.disponivel == False):
            self.disponivel = True
            print("Livro devolvido com sucesso.")

livro = Livro("Dom Casmurro")
livro.emprestar()
livro.emprestar()
livro.devolver()