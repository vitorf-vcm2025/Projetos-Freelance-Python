import json
import os
from datetime import datetime

# Simulação de dados recebidos de uma API (como Mercado Livre)


def buscar_dados_vendas():
    print("🤖 Conectando à API e extraindo dados...")
    # Simulando um arquivo XML/JSON de venda
    venda_exemplo = {
        "id_transacao": "MLB789456123",
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "valor": 450.00,
        "status": "Pago"
    }
    return venda_exemplo


def salvar_no_google_drive_simulado(dados):
    print(
        f"📤 Enviando transação {dados['id_transacao']} para o Google Drive...")
    nome_arquivo = f"venda_{dados['id_transacao']}.json"

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"✅ Sucesso! Arquivo '{nome_arquivo}' salvo na pasta de destino.")


# Execução do script
if __name__ == "__main__":
    venda = buscar_dados_vendas()
    salvar_no_google_drive_simulado(venda)
