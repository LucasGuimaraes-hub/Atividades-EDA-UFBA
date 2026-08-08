import ordenacao

n = 100000 # 100 mil
placas = ordenacao.Placas(n)
placas.readFromFile("data/PIVs-100000.piv")
placas.radixSort()
placas.overwriteFile("data/PIVs-100000-ordenado.piv")

print("A ordenação foi concluída. O arquivo 'PIVs-100000-ordenado.piv' foi atualizado.")
