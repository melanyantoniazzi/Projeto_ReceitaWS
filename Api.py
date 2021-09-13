import requests
import json

def buscar_dados(vcnpj):

    request = requests.get("https://www.receitaws.com.br/v1/cnpj/" + vcnpj)
    objeto = json.loads(request.content)

    return objeto

#    resultado1 = (objeto['cnpj'])
#    resultado2 = (objeto['nome'])
#    resultado3 = (objeto['email'])

#if __name__ == '__main__':
    #buscar_dados('22066975000155')

#     vcnpj = '22066975000155'
#     result = buscar_dados(vcnpj)

#resultado1 = (result['cnpj'])
#resultado2 = (result['nome'])
#resultado3 = (result['email'])

#print(resultado3)
