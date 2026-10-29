import os
import sys
import time

VERDE = "\033[92m"
CIANO = "\033[96m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

ESTADO_JOGO = {
    "velocidade_texto": 0.02,
    "tempo_restante": 72,
    "confianca_dante": 50,
    "pistas": {
        "Mensagem 03h17": (
            "Aviso anônimo recebido no terminal: 'O ORÁCULO não falhou.'"
        ),
        "Ficheiro Incompleto": (
            "Contém 3 nomes e coordenadas do antigo centro de dados."
        ),
        "Dante Moreau": (
            "Investigador independente. Informações úteis, intenções incertas."
        ),
    },
}


def limpar_tela():
  os.system("cls" if os.name == "nt" else "clear")


def digitar_texto(texto, cor=RESET, velocidade=None):
  if velocidade is None:
    velocidade = ESTADO_JOGO["velocidade_texto"]

  sys.stdout.write(cor)
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(velocidade)
  sys.stdout.write(RESET + "\n")


def exibir_cabecalho(titulo):
  limpar_tela()
  print(f"{CIANO}{'=' * 60}")
  print(f"{NEGRITO} SISTEMA OPERACIONAL NEXUS v2.0 // {titulo}{RESET}{CIANO}")
  print(f"{'=' * 60}{RESET}")
  exibir_status()


def exibir_status():
  horas = ESTADO_JOGO["tempo_restante"]
  dante = ESTADO_JOGO["confianca_dante"]
  print(
      f"{AMARELO}[STATUS] Tempo Restante: {horas}h | Confiança em Dante:"
      f" {dante}%{RESET}"
  )
  print(f"{CIANO}{'-' * 60}{RESET}\n")


def menu_pistas():
  exibir_cabecalho("BANCO DE DADOS DE PISTAS (MOCK)")

  pistas = ESTADO_JOGO["pistas"]
  if not pistas:
    print(f"{VERMELHO}Nenhuma pista encontrada no banco de dados.{RESET}")
  else:
    for titulo, descricao in pistas.items():
      print(f"{VERDE}[*] {NEGRITO}{titulo}{RESET}{VERDE}: {descricao}{RESET}")
      time.sleep(0.1)
  print(f"\n{CIANO}{'-' * 60}{RESET}")
  input(f"\n{AMARELO}Pressione ENTER para retornar ao menu...{RESET}")


def menu_configuracoes():
  while True:
    exibir_cabecalho("CONFIGURAÇÕES DE INTERFACE")
    print("1. Velocidade do Texto: Rápida")
    print("2. Velocidade do Texto: Normal")
    print("3. Velocidade do Texto: Instantânea")
    print("4. Voltar")

    opcao = input(f"\n{NEGRITO}Selecione uma opção (1-4): {RESET}").strip()

    if opcao == "1":
      ESTADO_JOGO["velocidade_texto"] = 0.005
      digitar_texto("[CONFIG] Velocidade alterada para RÁPIDA.", VERDE)
    elif opcao == "2":
      ESTADO_JOGO["velocidade_texto"] = 0.03
      digitar_texto("[CONFIG] Velocidade alterada para NORMAL.", VERDE)
    elif opcao == "3":
      ESTADO_JOGO["velocidade_texto"] = 0.0
      digitar_texto("[CONFIG] Velocidade alterada para INSTANTÂNEA.", VERDE)
    elif opcao == "4":
      break
    else:
      print(f"{VERMELHO}[ERRO] Opção inválida!{RESET}")
      time.sleep(1)


def menu_investigacao():
  while True:
    exibir_cabecalho("TERMINAL DE INVESTIGAÇÃO - CAPÍTULO 1")
    print("1. Acessar Logs do Antigo Centro de Dados")
    print("2. Interceptar Mensagem Criptografada (03h17)")
    print("3. Analisar Perfil: Dante Moreau")
    print("4. Voltar ao Menu Principal")

    opcao = input(f"\n{NEGRITO}Selecione um nó de dados (1-4): {RESET}").strip()

    if opcao == "1":
      limpar_tela()
      exibir_cabecalho("LOGS // CENTRO DE DADOS")
      digitar_texto(
          "Acessando servidores antigos da NEXUS...", VERDE, velocidade=0.01
      )
      digitar_texto(
          "Alerta: Arquivos da ordem de desligamento do ORÁCULO foram"
          " apagados.",
          VERMELHO,
      )
      digitar_texto(
          "Registros indicam intervenção direta da diretoria antes do"
          " incidente público.",
          CIANO,
      )
      input(f"\n{AMARELO}Pressione ENTER para continuar...{RESET}")
    elif opcao == "2":
      limpar_tela()
      exibir_cabecalho("MENSAGEM CRIPTOGRAFADA")
      digitar_texto(
          "'PHANTOM, eles apagaram os arquivos, mas esqueceram da verdade...'",
          VERDE,
      )
      digitar_texto(
          "'O ORÁCULO não falhou. Ele fez exatamente para o que foi criado.'",
          AMARELO,
      )
      input(f"\n{AMARELO}Pressione ENTER para continuar...{RESET}")
    elif opcao == "3":
      limpar_tela()
      exibir_cabecalho("PERFIL // DANTE MOREAU")
      digitar_texto("Status: Investigador Independente / Hacker", CIANO)
      digitar_texto(
          "Nota: Possui acessos de nível corporativo não explicados.", AMARELO
      )
      input(f"\n{AMARELO}Pressione ENTER para continuar...{RESET}")
    elif opcao == "4":
      break
    else:
      print(f"{VERMELHO}[ERRO] Opção inválida!{RESET}")
      time.sleep(1)


def menu_principal():
  while True:
    exibir_cabecalho("MENU PRINCIPAL")
    print("1. Iniciar Investigação (Terminal Nexus)")
    print("2. Banco de Pistas Coletadas")
    print("3. Opções de Acessibilidade")
    print("4. Desconectar (Sair)")

    opcao = input(f"\n{NEGRITO}Escolha uma opção (1-4): {RESET}").strip()

    if opcao == "1":
      menu_investigacao()
    elif opcao == "2":
      menu_pistas()
    elif opcao == "3":
      menu_configuracoes()
    elif opcao == "4":
      limpar_tela()
      digitar_texto(
          "\nDesconectando do Protocolo ORÁCULO... Até logo, PHANTOM.",
          VERDE,
          0.02,
      )
      break
    else:
      print(f"{VERMELHO}\n[ERRO] Opção inválida! Digite entre 1 e 4.{RESET}")
      time.sleep(1)


if __name__ == "__main__":
  menu_principal()