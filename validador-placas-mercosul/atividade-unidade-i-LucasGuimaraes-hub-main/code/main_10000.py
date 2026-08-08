import ordenacao

n = 10000 # 10 mil
placas = ordenacao.Placas(n)
placas.readFromFile("data/PIVs-10000.piv")
placas.radixSort()
placas.overwriteFile("data/PIVs-10000-ordenado.piv")

print("A ordenação foi concluída. O arquivo 'PIVs-10000-ordenado.piv' foi atualizado.")