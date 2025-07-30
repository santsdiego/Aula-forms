import pandas as pd
from itertools import combinations

# Carregar a planilha
df = pd.read_excel("visao_contas_a_pagar (46).xls")

# Filtrar valores não conciliados
valores_df = df[df["Valor total da parcela em aberto (R$)"] > 0][["Nome do fornecedor", "Valor original da parcela (R$)"]]
valores = valores_df["Valor original da parcela (R$)"].values

# Valor alvo
alvo = 6154.51

# Buscar combinação
def encontrar_comb(valores, alvo, tolerancia=0.01, max_itens=6):
    for r in range(2, max_itens + 1):
        for combo in combinations(enumerate(valores), r):
            soma = sum(v[1] for v in combo)
            if abs(soma - alvo) <= tolerancia:
                return [valores_df.iloc[v[0]] for v in combo]
    return None

resultado = encontrar_comb(valores, alvo)

# Mostrar resultado
for linha in resultado:
    print(linha)
