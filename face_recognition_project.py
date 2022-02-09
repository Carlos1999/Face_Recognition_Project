from modo_cadastro_rostos import modo_cadastro_rostos
from modo_vigia import modo_vigia
import sys
import pickle
#Menu 
while True:
    print("-"*100)
    opcao = input("Bem vindo ao menu de reconhecimento facial, digite um número dentre as opções para iniciar: \n1 - Cadastrar novo rosto \n2 - Iniciar modo vigia\n3 - Listar cadastrados\n4 - remover cadastrados\n5 - Sair do Programa\n")
    if(opcao == "1"):      
        modo_cadastro_rostos()
    elif(opcao == "2"):
        modo_vigia()
    elif(opcao == "3"):
        data_leitura = pickle.loads(open("encodings.pickle", "rb").read())
        contador = 0
        if(len(data_leitura["names"])!=0):
            print("Rostos cadastrados:")
            for nomes in data_leitura["names"]:
                contador += 1
                print(contador,"-",nomes)
        else:
            print("Nenhum cadastro.")
    elif(opcao == "4"):
        data_leitura = pickle.loads(open("encodings.pickle", "rb").read())
        nome = input("Digite o nome de quem será removido:")
        if(nome in data_leitura["names"]):
            index = data_leitura["names"].index(nome)
            data_leitura["names"].pop(index)
            data_leitura["encodings"].pop(index)
            f = open("encodings.pickle", "wb")
            f.write(pickle.dumps(data_leitura))
            f.close()
            
            print("Nome",nome,"removido.")
        else:
            print("Nome não cadastrado.")
    elif(opcao == "5"):
        sys.exit()
    else:
        print("Opção inválida, tente novamente!")