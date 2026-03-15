def analisar_sentimento_pt(frase):
    # Nosso dicionário de inteligência
    palavras_positivas = ['excelente', 'ajudou', 'muito', 'economizou',
                          'sensacional', 'atencioso', 'técnico', 'bom', 'ótimo']
    palavras_negativas = ['frustrado', 'demora',
                          'erro', 'falha', 'ruim', 'péssimo', 'problema']

    frase = frase.lower()
    score = 0

    # Lógica de contagem
    for palavra in palavras_positivas:
        if palavra in frase:
            score += 0.5

    for palavra in palavras_negativas:
        if palavra in frase:
            score -= 0.5

    return score


def processar_laboratorio(nome_arquivo):
    print(f"\n{'='*50}")
    print(f"   LABORATÓRIO DE IA - ENGENHEIRO VITOR FERNANDES")
    print(f"{'='*50}\n")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

            for i, linha in enumerate(linhas, 1):
                comentario = linha.strip()
                if not comentario:
                    continue

                score = analisar_sentimento_pt(comentario)

                if score > 0:
                    status = "✅ POSITIVO"
                elif score < 0:
                    status = "❌ NEGATIVO"
                else:
                    status = "⚪ NEUTRO"

                print(f"Frase {i}: {comentario}")
                print(f"Resultado: {status} (Score: {score:.2f})")
                print("-" * 30)

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")


# Execução
processar_laboratorio('comentarios.txt')
print("\nProcessamento Concluído com Sucesso!")
