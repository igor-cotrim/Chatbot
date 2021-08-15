from chatterbot import ChatBot
from difflib import SequenceMatcher

ACEITACAO = 0.70

def comparar_mensagens(mensagem, mensagem_candidata):
    confianca = 0.0

    if mensagem.text and mensagem_candidata.text:
        texto_mensagem = mensagem.text
        texto_mensagem_candidata = mensagem_candidata.text

        confianca = SequenceMatcher(
            None,
            texto_mensagem,
            texto_mensagem_candidata
        )
        confianca = round(confianca.ratio(), 2)
        if confianca < ACEITACAO:
            confianca = 0.0
        else:
            print("mensagem do usuario:", texto_mensagem, ", mensagem candidata:", mensagem_candidata, ", nível de confiança:", confianca)

    return confianca

def selecionar_resposta(mensagem, lista_respostas, storage=None):
    resposta = lista_respostas[0]
    print("resposta escolhida:", resposta)

    return resposta


def executar_robo():
    robo = ChatBot("Robô de Atendimento do Alex",
        read_only=True, 
        statement_comparison_function= comparar_mensagens,
        response_selection_method= selecionar_resposta,
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
            }
        ])

    while True:
        entrada = input("digite alguma coisa...\n", )
        resposta = robo.get_response(entrada)
        if resposta.confidence > 0.0:
            print(resposta.text)
        else:
            print("ainda nao sei como responder essa pergunta")
            print("pergunte outra coisa...")

if __name__ == "__main__":
    executar_robo()
