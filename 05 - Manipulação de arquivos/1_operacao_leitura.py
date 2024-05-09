# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(
    "/home/romanzini/projetos/python_backend_developer/02_dominando_python_estruturas_dados/trilha-python/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.read())
arquivo.close()

arquivo = open(
    "/home/romanzini/projetos/python_backend_developer/02_dominando_python_estruturas_dados/trilha-python/05 - Manipulação de arquivos//lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

arquivo = open(
    "/home/romanzini/projetos/python_backend_developer/02_dominando_python_estruturas_dados/trilha-python/05 - Manipulação de arquivos//lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()

arquivo = open(
    "/home/romanzini/projetos/python_backend_developer/02_dominando_python_estruturas_dados/trilha-python/05 - Manipulação de arquivos//lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
