alex = {'nome': 'Alex', 'cargo': 'Hacker', 'idade': 28, 'confianca': '***'}
helena = {'nome': 'Helena Voss', 'cargo': 'Diretora da NEXUS', 'idade': 30, 'confianca': 30}
karla = {'nome': 'Dra. Karla', 'cargo': 'Cientista', 'idade': 32, 'confianca': 50}
dante = {'nome': 'Dante Moreau', 'cargo': 'Aliado', 'idade': 29, 'confianca': 40}
oraculo = {'nome': 'Oraculo', 'cargo': 'Inteligencia Artificial', 'idade': 3, 'confianca': 0}

personagens = {'alex': alex, 'helena': helena, 'karla': karla, 'dante': dante, 'oraculo': oraculo}

documento1 = {'id': 1, 'nome': 'Projeto ORÁCULO', 'responsavel': 'Dra. Karla', 'tipo': 'Confidencial', 'ENCONTRADO': False}
documento2 = {'id': 2, 'nome': 'Relatório de Segurança', 'responsavel': 'Helena Voss', 'tipo': 'Relatório', 'ENCONTRADO': False}
documento3 = {'id': 3, 'nome': 'Plano de contingência', 'responsavel': 'Dante Moreau', 'tipo': 'Plano', 'ENCONTRADO': False}
documento4 = {'id': 4, 'nome': 'Documento Secreto', 'responsavel': 'Oraculo', 'tipo': 'Confidencial', 'ENCONTRADO': False}

documentos = [documento1, documento2, documento3, documento4]
inventario = []

def buscar_personagem(nome):
    documento = nome.lower().strip()
    if documento in personagens:
        p = personagens[documento]
        return f"--- Documentação ---\nNome: {p['nome']}\nCargo: {p['cargo']}\nIdade: {p['idade']}\nConfiança: {p['confianca']}"
    return "Personagem não encontrado."

def encontrar_documento_por_id(doc_id):
    for doc in documentos:
        if doc['id'] == doc_id:
            if not doc['ENCONTRADO']:
                doc['ENCONTRADO'] = True
                inventario.append(doc)
                return f"Você encontrou o documento: {doc['nome']}!"
            else:
                return f"Documento já encontrado: {doc['nome']}"
    return "ID de documento inválido."

def exibir_inventario_texto():
    if not inventario:
        return "===== INVENTÁRIO (VAZIO) ====="
    texto = "===== INVENTÁRIO =====\n"
    for numero, doc in enumerate(inventario, start=1):
        if doc['ENCONTRADO']:
            texto += f"{numero} - {doc['nome']}\n"
    return texto.strip()