class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo 
        self.autor = autor 

    def exibir_info(self):
        print(f"Título: {self.titulo} | Autor: {self.autor}")

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        if not self.livros:
            print("Não há livros na biblioteca")
        else:
            for livro in self.livros:
                livro.exibir_info()

    def buscar_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                livro.exibir_info()
                return
        print("Livro não encontrado")

# Testando
l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

b = Biblioteca()
b.adicionar_livro(l1)
b.adicionar_livro(l2)

b.listar_livros()
b.buscar_por_titulo("Dom Casmurro")
b.buscar_por_titulo("1984")
