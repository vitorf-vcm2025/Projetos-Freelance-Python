from textblob import TextBlob


def analisar_comentario(texto):
    # Transformamos tudo em minúsculo para facilitar a busca
    t = texto.lower()

    # Listas de palavras-chave (O coração da sua lógica)
    positivas = ["excelente", "rápido", "salvou", "incrível", "bom", "ajudou"]
    negativas = ["problemas", "erro", "falha", "ruim", "difícil", "lento"]

    # Lógica de decisão
    if any(word in t for word in positivas):
        return "😊 show"
    elif any(word in t for word in negativas):
        return "😡 Negativo"
    else:
        return "😐 Neutro"


# --- Seus comentários de teste ---
feedbacks = [
    "O sistema de integração com o Mercado Livre está excelente e muito rápido!",
    "Estou tendo problemas com o carregamento dos XMLs no Google Drive.",
    "O atendimento da clínica foi normal, nada de especial.",
    "A automação do Bitrix24 salvou o dia da nossa equipe!"
    "O código do Vitor ficou show!"
]

print("--- 🤖 IA de Lógica Direta do Engenheiro Vitor ---")
for f in feedbacks:
    print(f"Comentário: {f}")
    print(f"IA diz: {analisar_comentario(f)}\n")
