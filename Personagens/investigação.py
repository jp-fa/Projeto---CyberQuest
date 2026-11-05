alex = {
    'nome': 'Alex',
    'cargo':'Hacker',
    'idade': 28,
    'confianca': '***'
}

helena = {
    'nome': 'Helena Voss',
    'cargo': 'Diretora da NEXUS',
    'idade': 30,
    'confianca': 30
}

karla = {
    'nome': 'Dra. karla',
    'cargo': 'Cientista',
    'idade': 32,
    'confianca': 50
}

dante = {
    'nome': 'Dante Moreau',
    'cargo': 'Aliado',
    'idade': 29,
    'confianca': 40
}

oraculo = {
    'nome': 'Oraculo',
    'cargo': 'Inteligencia Artificial',
    'idade': 3,
    'confianca': 0

}

personagens = {
    'alex': alex,
    'helena': helena,
    'karla': karla,
    'dante': dante,
    'oraculo': oraculo
}

def exibir_personagem(personagem):

    print("-----Documentação do Personagem-----")

    print('Nome: ', personagem['nome'])
    print('Cargo: ', personagem['cargo'])
    print('Idade: ', personagem['idade'])
    print('confianca: ', personagem['confianca'])


documento = input('Digite o nome do Personagem que deseja ver a documentação: ') .lower()

if documento in personagens:
    exibir_personagem(personagens[documento])
else:
    print('personagem não encontrado:')

documento1 = {
    'nome': 'Projeto ORÁCULO',
    'responsavel': 'Dra. Karla',
    'tipo': 'Confidencial',
    'ENCONTRADO': False
}

documento2 = {
    'nome': 'Relatório de Segurança',
    'responsavel': 'Helena Voss',
    'tipo': 'Relatório',
    'ENCONTRADO': False
}

documento3 = {
    'nome': 'Plano de contingência',
    'responsavel': 'Dante Moreau',
    'tipo': 'Plano',
    'ENCONTRADO': False
}

documento4 = {
    'nome': 'Documento Secreto',
    'responsavel': 'Oraculo',
    'tipo': 'Confidencial',
    'ENCONTRADO': False
}

documentos = [
    documento1,
    documento2,
    documento3,
    documento4
]

inventario = []

def encontrar_documento(documento):
    if documento['ENCONTRADO'] == False:
        documento['ENCONTRADO'] = True
        inventario.append(documento)
    else:
        print('Documento já encontrado: ', documento['nome'])

# encontrar_documento(documento1)
# encontrar_documento(documento2)
# encontrar_documento(documento3)
# encontrar_documento(documento4)

# print(inventario)

print('===== LABORATÓRIO DA DRA. KARLA =====')
print('1 - Investigar a mesa')
print('2 - Sair do laboratório')

escolha = input('O que deseja fazer? ')

if escolha == '1':
    encontrar_documento(documento1)
elif escolha == '2':
    print('Você decidiu sair do laboratório.')
else:
    print('Opção inválida!')

print('===== SALA DE SEGURANÇA =====')
print('1 - Investigar a mesa')
print('2 - Sair da sala de segurança')

escolha = input('O que deseja fazer? ')

if escolha == '1':
    print('Você encontrou um documento!')
    encontrar_documento(documento2)
elif escolha == '2':
    print('Você decidiu sair da sala de segurança.')
else:
    print('Opção inválida!')

print('===== SALA DE PLANEJAMENTO =====')
print('1 - Investigar a mesa')
print('2 - Sair da sala de planejamento')

escolha = input('O que deseja fazer? ')

if escolha == '1':
    print('Você encontou um documento!')
    encontrar_documento(documento4)
elif escolha == '2':
    print('Você decidiu sair da sala de planejamento.')
else:
    print('Opção inválida!')


print('===== ESCRITÓRIO DE DANTE MOREAU =====')
print('1 - Investigar a mesa')
print('2 - Investigar o computador')
print('3 - Sair do escritório')

escolha = input('O que deseja fazer? ')

if escolha == '1':
    encontrar_documento(documento3)

elif escolha == '2':
    print('Computador bloqueado por senha')
elif escolha == '3':
    print('Você saiu do escritório.')
else:
    print('Opção inválida!')


def exibir_inventario():
    print('===== iNVENTARIO =====')
    for numero, documento in enumerate(inventario, start=1):
        if documento['ENCONTRADO']:
            print(numero, '-', documento['nome'])

exibir_inventario()

while True:
    print('===== CENTRAL DE INVESTIGAÇÂO =====')
    ambientes = input('Digite o nome do ambiente que deseja investigar') .lower()

    if ambientes =='laboratorio':
        print('Você está no laboratório da Dra. Karla.')

    elif ambientes =='sala de segurança':
        print('Você está na sala de segurança.')

    elif ambientes == 'sala de planejamento':
        print('você está na sala de planejamento>')

    elif ambientes =='dante moreau':
        print('Você está no escritório de Dante Moreau.')

    elif ambientes == '0':
        break
    else:
        print('Ambiente não encontrado. Por favor, digite um ambiente válido ou 0 para sair.')