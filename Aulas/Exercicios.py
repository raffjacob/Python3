import requests

def main():
    cep_entrada = input("Insira o CEP a ser consultado: ")

    if len(cep_entrada)!=8:
        print("Quantidade de digistos invalida")
        exit()

    request_CEP = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_entrada))

    result_CEP = request_CEP.json()

    if 'erro' not in result_CEP:
        #print(result_CEP)
        print(" - Resultado - ")
        print("CEP: {}".format(result_CEP['cep']))
        print("Rua: {}".format(result_CEP['logradouro']))
        print("Bairro: {}".format(result_CEP['bairro']))
        print("Cidade: {}".format(result_CEP['localidade']))
        print("UF: {}".format(result_CEP['uf']))
    else:
        print("{}: CEP inválido".format(cep_entrada))

    opcao = input("Deseja realizar uma nova consulta?\n1.Sim\n2.Sair\n")
    if opcao == "1" or opcao == "Sim":
        main()
    else:
        exit()
if __name__ == '__main__':
    main()