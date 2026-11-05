#codigo feito com ajuda do Gemini e Chat GPT- Primeira versao da historia com escolhas(teste)

# Dicionário contendo os capítulos, textos descritivos e opções de escolha
"""CyberQuest: O Protocolo ORÁCULO

Versão de desenvolvimento para a Sprint 2.
Mantém a estrutura simples do protótipo da Sprint 1 e acrescenta:
- caminhos diferentes para algumas escolhas;
- registro de decisões;
- desbloqueio de pistas narrativas;
- indicadores numéricos de confiança;
- início do Capítulo 2.

Observação: os identificadores de pistas e a estrutura de estado devem ser
combinados com os integrantes responsáveis por investigacao.py e main.py.
"""

CAPITULOS = {
    1: {
        "titulo": "Capítulo 1 — O Chamado",
        "texto": (
            "Às 03h17, seu terminal emite um alerta silencioso.\n"
            "Uma mensagem desconhecida aparece na tela:\n\n"
            '"PHANTOM, eles apagaram os arquivos, mas esqueceram de apagar a verdade. '
            'O ORÁCULO não falhou. Ele fez exatamente aquilo para o qual foi criado. '
            'Você tem 72 horas. Não confie na NEXUS."\n\n'
            "A mensagem contém um arquivo incompleto, três nomes e as coordenadas de um antigo centro de dados.\n\n"
            "O que você deseja fazer primeiro?"
        ),
        "opcoes": {
            1: "Analisar o arquivo incompleto antes de sair.",
            2: "Tentar rastrear a origem da mensagem criptografada."
        },
        "proximo": {1: 2, 2: 3},
        "efeitos": {
            1: {
                "decisoes": {"investigacao_inicial": "analisar_arquivo"},
                "pistas_desbloqueadas": ["arquivo_incompleto", "lista_tres_nomes"]
            },
            2: {
                "decisoes": {"investigacao_inicial": "rastrear_mensagem"},
                "pistas_desbloqueadas": ["tentativa_rastreio_mensagem"]
            }
        }
    },
    2: {
        "titulo": "Capítulo 1 — Análise do Arquivo",
        "texto": (
            "PHANTOM analisa o arquivo recebido. Parte dos dados foi apagada, mas ainda é possível "
            "identificar fragmentos de registros e uma lista com três nomes.\n\n"
            "As coordenadas do antigo centro de dados continuam sendo a pista mais concreta. "
            "Você decide seguir até o local."
        ),
        "opcoes": {1: "Seguir para o antigo centro de dados."},
        "proximo": {1: 4},
        "efeitos": {1: {"decisoes": {"arquivo_analisado": True}}}
    },
    3: {
        "titulo": "Capítulo 1 — Rastreamento da Mensagem",
        "texto": (
            "PHANTOM tenta rastrear a origem da mensagem. O sinal passa por diferentes rotas e "
            "não revela uma origem confiável. A tentativa, porém, confirma que a mensagem foi "
            "enviada por alguém que conhece os sistemas da NEXUS.\n\n"
            "Sem uma origem identificada, você decide seguir as coordenadas recebidas."
        ),
        "opcoes": {1: "Seguir para o antigo centro de dados."},
        "proximo": {1: 4},
        "efeitos": {1: {"decisoes": {"rastreio_concluido": True}}}
    },
    4: {
        "titulo": "Capítulo 1 — O Centro de Dados",
        "texto": (
            "Você chega ao antigo centro de dados. As portas estão abertas e há sinais de atividade recente.\n"
            "Junto aos servidores centrais, você encontra Dante Moreau, um investigador independente, "
            "vasculhando os terminais de acesso. Ele reconhece o pseudônimo PHANTOM.\n\n"
            "Como você reage?"
        ),
        "opcoes": {
            1: "Confrontar Dante diretamente e exigir explicações.",
            2: "Observar Dante escondido para descobrir o que ele procura."
        },
        "proximo": {1: 5, 2: 6},
        "efeitos": {
            1: {"decisoes": {"reacao_encontro_dante": "confrontou"}},
            2: {
                "decisoes": {"reacao_encontro_dante": "observou"},
                "pistas_desbloqueadas": ["atividade_recente_terminal"]
            }
        }
    },
    5: {
        "titulo": "Capítulo 1 — Confronto",
        "texto": (
            "PHANTOM exige saber por que Dante está no local. Dante não parece surpreso.\n\n"
            'DANTE: "Eu reconheço esse pseudônimo. Estou investigando a NEXUS há semanas. '
            'Se você veio atrás da verdade sobre o ORÁCULO, talvez possamos trocar informações."\n\n'
            "Dante explica que possui contatos e informações, mas não revela todos os seus objetivos."
        ),
        "opcoes": {1: "Ouvir a proposta de Dante."},
        "proximo": {1: 7},
        "efeitos": {1: {"decisoes": {"dante_confrontado": True}}}
    },
    6: {
        "titulo": "Capítulo 1 — Observando Dante",
        "texto": (
            "PHANTOM observa Dante antes de se aproximar. Ele tenta acessar arquivos protegidos "
            "nos terminais e parece procurar registros relacionados à NEXUS.\n\n"
            "Ao perceber que não está sozinho, Dante se vira e reconhece PHANTOM. Ele afirma que "
            "está investigando a empresa há semanas e propõe uma troca de informações."
        ),
        "opcoes": {1: "Aproximar-se e ouvir a proposta de Dante."},
        "proximo": {1: 7},
        "efeitos": {1: {"decisoes": {"dante_observado": True}}}
    },
    7: {
        "titulo": "Capítulo 1 — A Proposta de Dante",
        "texto": (
            "Dante oferece contatos e informações em troca da ajuda de PHANTOM para acessar e "
            "compreender os dados protegidos. Ele diz que os dois querem descobrir o que aconteceu, "
            "mas não explica completamente suas motivações.\n\n"
            "Você ainda não sabe se pode confiar nele. O que decide?"
        ),
        "opcoes": {
            1: "Aceitar a ajuda de Dante e trabalhar com ele.",
            2: "Manter distância e exigir provas antes de confiar nele."
        },
        "proximo": {1: 8, 2: 8},
        "efeitos": {
            1: {
                "decisoes": {"aceitou_ajuda_dante": True},
                "confianca": {"dante": 10}
            },
            2: {
                "decisoes": {"aceitou_ajuda_dante": False},
                "confianca": {"dante": -5}
            }
        }
    },
    8: {
        "titulo": "Capítulo 1 — A Ordem de Desligamento",
        "texto": (
            "Com as informações disponíveis, PHANTOM encontra registros de uma ordem para "
            "desligar o ORÁCULO. A data do documento é anterior ao momento em que a NEXUS "
            "admitiu publicamente que havia um problema.\n\n"
            "A descoberta indica que a empresa sabia mais sobre o incidente do que revelou."
        ),
        "opcoes": {1: "Continuar investigando os registros da NEXUS."},
        "proximo": {1: 9},
        "efeitos": {
            1: {
                "decisoes": {"encontrou_ordem_desligamento": True},
                "pistas_desbloqueadas": ["ordem_desligamento_oraculo"]
            }
        }
    },
    9: {
        "titulo": "Capítulo 2 — A Empresa que Mentiu",
        "texto": (
            "PHANTOM volta sua atenção para a NEXUS. Os registros encontrados levantam novas "
            "perguntas sobre as decisões da liderança e sobre sua própria demissão.\n\n"
            "Você precisa escolher qual informação investigar primeiro."
        ),
        "opcoes": {
            1: "Investigar os registros de expansão das capacidades do ORÁCULO.",
            2: "Investigar os registros relacionados à demissão de PHANTOM."
        },
        "proximo": {1: 10, 2: 11},
        "efeitos": {
            1: {"decisoes": {"investigou_expansao_oraculo": True}},
            2: {"decisoes": {"investigou_demissao_phantom": True}}
        }
    },
    10: {
        "titulo": "Capítulo 2 — A Expansão do Projeto",
        "texto": (
            "Os registros indicam que a NEXUS autorizou a expansão das capacidades do ORÁCULO, "
            "apesar dos alertas sobre os riscos. A decisão aumenta as suspeitas sobre a participação "
            "da liderança no incidente.\n\n"
            "A investigação continua na próxima etapa do projeto."
        ),
        "opcoes": {},
        "proximo": {},
        "efeitos": {}
    },
    11: {
        "titulo": "Capítulo 2 — A Demissão de PHANTOM",
        "texto": (
            "Ao consultar os registros de sua saída, PHANTOM encontra indícios de que sua demissão "
            "foi conveniente para a expansão do projeto. Seus alertas sobre os limites e o mecanismo "
            "de desligamento haviam se tornado um obstáculo para a liderança.\n\n"
            "A investigação continua na próxima etapa do projeto."
        ),
        "opcoes": {},
        "proximo": {},
        "efeitos": {}
    }
}


def criar_estado_inicial():
    """Cria o estado compartilhado da narrativa e das escolhas do jogador."""
    return {
        "capitulo": 1,
        "cena_atual": 1,
        "decisoes": {},
        "pistas_desbloqueadas": [],
        "pistas": [],
        "confianca": {
            "dante": 40,
            "helena_voss": 30,
            "dr_karla": 50,
            "oraculo": 0
        },
        "final": None
    }


def exibir_capitulo(numero_capitulo, estado=None):
    """Exibe uma cena e devolve as opções disponíveis para a interface."""
    cap = CAPITULOS.get(numero_capitulo)
    if cap is None:
        print("\n[Fim desta versão] Não há mais cenas disponíveis nesta etapa.")
        return None

    print("\n" + "=" * 60)
    print(cap["titulo"])
    print("=" * 60)
    print(cap["texto"])

    if not cap["opcoes"]:
        print("\n[Fim da demonstração da Sprint 2]")
        return None

    print("\nEscolhas disponíveis:")
    for chave, descricao in cap["opcoes"].items():
        print(f"[{chave}] {descricao}")

    return cap["opcoes"]


def _aplicar_efeitos(estado, efeitos):
    """Atualiza decisões, pistas desbloqueadas e confiança."""
    if estado is None:
        return

    for chave, valor in efeitos.get("decisoes", {}).items():
        estado.setdefault("decisoes", {})[chave] = valor

    for pista in efeitos.get("pistas_desbloqueadas", []):
        pistas = estado.setdefault("pistas_desbloqueadas", [])
        if pista not in pistas:
            pistas.append(pista)

    for personagem, alteracao in efeitos.get("confianca", {}).items():
        confiancas = estado.setdefault("confianca", {})
        atual = confiancas.get(personagem, 0)
        confiancas[personagem] = max(0, min(100, atual + alteracao))


def processar_escolha(numero_capitulo, escolha, estado=None):
    """Valida uma escolha, registra seus efeitos e devolve a próxima cena.

    Em caso de opção inválida, devolve a cena atual sem alterar o estado.
    """
    cap = CAPITULOS.get(numero_capitulo)
    if cap is None or escolha not in cap["opcoes"]:
        print("\n[Erro] Escolha inválida para esta cena. Tente novamente.")
        return numero_capitulo

    efeitos = cap.get("efeitos", {}).get(escolha, {})
    _aplicar_efeitos(estado, efeitos)

    proxima_cena = cap["proximo"].get(escolha, numero_capitulo)
    if estado is not None:
        estado["cena_atual"] = proxima_cena
        if proxima_cena in CAPITULOS:
            estado["capitulo"] = 1 if proxima_cena <= 8 else 2

    return proxima_cena


def main():
    """Executa a narrativa no terminal para testes isolados."""
    estado = criar_estado_inicial()
    cena_atual = estado["cena_atual"]

    while cena_atual in CAPITULOS:
        opcoes = exibir_capitulo(cena_atual, estado)
        if opcoes is None:
            break

        try:
            escolha = int(input("\nDigite o número da sua escolha: "))
        except ValueError:
            print("\n[Erro] Digite somente o número de uma das opções.")
            continue

        proxima_cena = processar_escolha(cena_atual, escolha, estado)
        if proxima_cena == cena_atual and escolha not in CAPITULOS[cena_atual]["opcoes"]:
            continue
        cena_atual = proxima_cena

    print("\n--- Resumo das decisões desta partida ---")
    print("Decisões:", estado["decisoes"])
    print("Pistas desbloqueadas:", estado["pistas_desbloqueadas"])
    print("Confiança:", estado["confianca"])


if __name__ == "__main__":
    main()
