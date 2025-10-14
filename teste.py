def verificar_qualidade(medida, tol_inferior, tol_superior):

    if medida >= tol_inferior and medida <= tol_superior:
        return "Aprovado"
    else:
        return "Reprovado"

def calcular_media(medidas):
    return sum(medidas) / len(medidas)


# ------- FUNÇÕES ---------

print("\n")
medidas_lote = [20.1, 20.0, 20.2, 19.9, 20.0, 21.5, 19.8, 20.1]
print(f"Dados brutos coletados: {medidas_lote}")


especificacoes = {
    "produto_id": "EIXO-XT100",
    "diametro_nominal": 20.0,
    "tolerancia_superior": 20.2,
    "tolerancia_inferior": 19.8
}

relatorio_lote = {
    "total_pecas": 0,
    "pecas_aprovadas": 0,
    "pecas_reprovadas": 0,
    "media_do_lote_mm": 0,
    "medidas_reprovadas": []
}


for medida_atual in medidas_lote:           # para cada medida na lista de medidas do lote

    status_peca = verificar_qualidade(
        medida_atual,
        especificacoes["tolerancia_inferior"],
        especificacoes["tolerancia_superior"]
    )
    
    relatorio_lote["total_pecas"] += 1
    
    if status_peca == "Aprovado":
        relatorio_lote["pecas_aprovadas"] += 1
    else:
        relatorio_lote["pecas_reprovadas"] += 1
        relatorio_lote["medidas_reprovadas"].append(medida_atual)

relatorio_lote["media_do_lote_mm"] = calcular_media(medidas_lote)

print("\n--- Relatório de Qualidade do Lote ---")
print(f"Produto: {especificacoes['produto_id']}")


for chave, valor in relatorio_lote.items():                             # chave e valor pois é um dicionário
    valor = [round(num, 2) for num in valor]                            # arredonda os valores da lista
    print(f"{chave.replace('_', ' ').title()}: {valor}")
