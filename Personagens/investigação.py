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
    'nome': 'Dr. karla',
    'cargo': 'Cientista',
    'idade': 32,
    'confianca': 50
}

dante = {
    'nome': 'Dante moreau',
    'cargo': 'Alido',
    'idade': 29,
    'confianca': 40
}

oraculo = {
    'nome': 'Oraculo',
    'cargo': 'Inteligencia Artificial',
    'idade': 3,
    'confianca': 0
}

def exibir_personagem(personagem):

    print("-----Documentação do Personagem-----")

    print('Nome:', personagem['nome'])
    print('Cargo: ', personagem['cargo'])
    print('Idade:', personagem['idade'])
    print('confianca', personagem['confianca'])

exibir_personagem(alex)
exibir_personagem(helena)
exibir_personagem(karla)
exibir_personagem(dante)
exibir_personagem(oraculo)

documento = input('Digite o nome do Personagem que deseja ver a documentação: ') .lower()

if documento =='alex':
    exibir_personagem(alex)

elif documento =='helena':
    exibir_personagem(helena)

elif documento =='karla':
    exibir_personagem(karla)

elif documento =='dante':
    exibir_personagem(dante)

elif documento =='oraculo':
    exibir_personagem(oraculo)

else:
    print('Personagem Não encontrado')