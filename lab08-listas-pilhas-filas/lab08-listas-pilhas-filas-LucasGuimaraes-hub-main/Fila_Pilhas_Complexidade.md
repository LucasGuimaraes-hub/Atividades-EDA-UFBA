[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-uO6JNlB)
# Complexidade da Fila e Pilha

## Análise de Complexidade

### *3* Mostre como é possível implementar uma **fila** eficientemente utilizando duas **pilhas**

1. enqueue: O elemento é simplesmente adicionado ao topo de _pilhaEntrada, resultando em complexidade O(1).

2. dequeue: Caso _pilhaSaida esteja vazia, todos os elementos de _pilhaEntrada são transferidos para _pilhaSaida. Isso tem complexidade O(n) no pior caso.

No entanto, cada elemento é transferido no máximo uma vez entre as pilhas. Portanto, a complexidade amortizada de dequeue é O(1).

Complexidade Geral: O(n)

### *4* Mostre como é possível implementar uma **fila** eficientemente utilizando duas **pilhas** 

1. push: Inserir em _fila2 é O(1).Mover elementos de _fila1 para _fila2 é O(n) no pior caso.
2. pop: O elemento é simplesmente removido da frente de _fila1, resultando em complexidade O(1).

Portanto, o custo do método push é O(n), enquanto o método pop tem custo O(1).
Complexidade Geral: O(n)