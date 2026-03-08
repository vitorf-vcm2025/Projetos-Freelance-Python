import json

# Função que simula o coração de um Bot para CRM (Bitrix24/WhatsApp)
def processar_notificacao_webhook(dados_em_json):
    # Transformando o texto (JSON) em um dicionário Python
    dados = json.loads(dados_em_json)
    
    nome_cliente = dados.get("cliente", "Visitante")
    assunto = dados.get("interesse", "Informações Gerais")
    
    print("-" * 30)
    print(f"🤖 BOT STATUS: Nova interação detectada!")
    print(f"👤 Cliente: {nome_cliente}")
    print(f"🎯 Interesse: {assunto}")
    print(f"✅ Ação: Criando tarefa automática no painel do consultor.")
    print("-" * 30)
    
    return "Processado com Sucesso"

# Exemplo de dado que o sistema receberia
payload_simulado = '{"cliente": "Miguel Fernandes", "interesse": "Automação de Vendas"}'

# Executando a simulação
processar_notificacao_webhook(payload_simulado)