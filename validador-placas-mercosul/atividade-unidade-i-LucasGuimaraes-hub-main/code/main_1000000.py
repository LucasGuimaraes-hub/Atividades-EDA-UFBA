import ordenacao

n = 1000000 # 1 milhão
placas = ordenacao.Placas(n)
placas.readFromFile("data/PIVs-1000000.piv")
placas.radixSort()
placas.overwriteFile("data/PIVs-1000000-ordenado.piv")

print("A ordenação foi concluída. O arquivo 'PIVs-1000000-ordenado.piv' foi atualizado.")
