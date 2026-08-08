class Placas:
    def __init__(self, n):            
        self.vet = [0] * n 
        self.maxObjs = n  
        self.numObjs = 0  

    def insere(self, chave):        
        if self.numObjs >= self.maxObjs:           
            self.vet += [0] * self.maxObjs
            self.maxObjs *= 2
        self.vet[self.numObjs] = chave
        self.numObjs += 1

    def readFromFile(self, filename):     
        try:
            with open(filename, 'r') as file:
                self.vet = [0] * self.maxObjs  # Reinicializa o vetor
                self.numObjs = 0                
                for line in file:
                    self.insere(line.strip())  # Função insere
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{filename}' não encontrado.")
        except ValueError:
            raise ValueError("Erro ao processar o arquivo. Certifique-se de que o arquivo contém placas válidas.")

    def countingSortByPosition(self, position):
       
        k = 36  # Para tratar caracteres de '0'-'9' e 'A'-'Z'
        C = [0] * k
        B = [0] * self.numObjs

        # Mapeia os caracteres para índices: '0'-'9' -> 0-9, 'A'-'Z' -> 10-35
        def char_to_index(char):
            if '0' <= char <= '9':
                return ord(char) - ord('0')
            else:  # 'A'-'Z'
                return ord(char) - ord('A') + 10

        # Passo 1: Contar ocorrências dos caracteres na posição
        for placa in self.vet[:self.numObjs]:
            index = char_to_index(placa[position])
            C[index] += 1

        # Passo 2: Calcular os prefixos acumulados
        for i in range(1, k):
            C[i] += C[i - 1]

        # Passo 3: Construir o array ordenado com base no dígito/posição atual
        for i in range(self.numObjs - 1, -1, -1):
            index = char_to_index(self.vet[i][position])
            B[C[index] - 1] = self.vet[i]
            C[index] -= 1

        # Atualizar o vetor original com os valores ordenados
        self.vet[:self.numObjs] = B

    def radixSort(self):
        
        if self.numObjs == 0:
            raise ValueError("Arquivo sem placas. Não é possível realizar a ordenação.")

        # Ordenar pelas posições da placa, da direita para a esquerda
        positions = [6, 5, 4, 3, 2, 1, 0] 
        for pos in positions:
            self.countingSortByPosition(pos)

    def overwriteFile(self, filename): # Sobescreve o arquivo com as placas já ordenadas
        with open(filename, 'w') as file:
            for i in range(self.numObjs):
                file.write(self.vet[i] + '\n')
