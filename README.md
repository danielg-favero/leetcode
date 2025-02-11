# Fundamentos para resolução de LeetCode

Principais conceitos e problemas resolvidos dentro do `LeetCode`

## "Big O" Notation

Mede a complexidade assintomática nos piores casos de resolução de um problema.

Ex1: Percorrer um `array` de `n` elementos tem uma complexidade de `O(n)`

Ex2: Algoritmo de `bubblesort` precisa percorrer um `array` pelo menos 2 vezes por iteração, ou seja, possui uma complexidade de `O(nˆ2)`

## Array

Uma espaço de memória que possui diversos elementos.

Exs: 
- `[0000 1111 0000 1111]` Array de 4 elementos de 4 bits
- `[00001111 00001111]` Array de 2 elementos de 8 bits
- `[0000111100001111]` Array de 1 elementos de 16 bits

> Em JS, um `array` na forma `[]` não corresponde a definição exata de um `array`, ele é um objeto mais complexo. Para trabalhar de forma correta com `arrays` de verdade em JS, é preciso utilizar o objeto `ArrayBuffer` do `node`

## Linked List (Listas encadeadas)

Diferente de um `array`, os elementos da lista não estão em sequência na memória, cada elemento elemento aponta para o endereço de memória do próximo elemento.

Para encontrar o tamanho da lista, é preciso percorrer toda a lista, ou possuir um parâmetro que contenha o tamanho.

Comparação entre `array` e `linked list`:

|             | Leitura                                      | Inserção                                     | Delete                                       |
|-------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| Linked List | pior: O(n) <br> melhor: O(1) - Começo ou fim | pior: O(n) <br> melhor: O(1) - Começo ou fim | pior: O(n) <br> melhor: O(1) - Começo ou fim |
| Array       | O(1)                                         | O(1)                                         | O(1)                                         |

## Queue (Filas)

É uma lista encadeada que segue a lógica de FIFO (*First In First Out*), muito usada para *buffering* de *streaming* de dados.

Exemplo de `queue` em `python`:

```python
import queue import Queue
from collection import deque # Double-Ended Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.get()) # output: 1
print(q.get()) # output: 2
print(q.get()) # output: 3
```

## Stack (Pilha)

É uma lista encadeada que segue a lógica LIFO (*Last In First Out*).

Exemplo de uma implementação de um `stack` em `python`;

```python
import queue import Queue
from collection import deque # Double-Ended Queue

q = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop()) # output: 3
print(stack.pop()) # output: 2
print(stack.pop()) # output: 1
```

É possível implementar uma `stack` usando um pointeiro para manipular os itens da pilha

```python
class Stack:
    def __init__(self, max_len = 1000):
        self.items = [0] * max_len
        self.max_len = max_len
        self.pointer = 0

    def push(self, item):
        self.items[self.pointer] = item
        self.pointer += 1

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty List")

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty List")

        return self.items[-1]

    def size(self):
        return len(self.items)
```

> Um `array` em python tem vários funcionalidades de uma `stack` padrão

Também é possível implementar uma `stack` usando uma lista encadeada

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Empty Stack")

        popped_node = self.top
        self.top = popped_node.next

        self._size -= 1

        return popped_node.value

    def peek(self):
        if self.top is None:
            raise IndexError("Empty Stack")

        return self.top.value

    def size(self):
        return self._size
```

## Binary Tree (Árvore Binária)

Uma lista encadeada que possui um ponteiro para outros dois outros elementos (geralmente chamados de `left` e `right`).

### Como percorrer uma Árvore Binária (Traversals)

1. **Preorder**: Percorre todos os nós a esquerda primeiro e adiciona os resultados a medida que percorre a árvore.

```
    5
   /\
  3  10
 /   /\
1   7  15

[5, 3, 1, 10, 7, 15]
```

2. **Inorder**: Percorre todos os nós até chegar a folha mais a esquerda e vai adicionando ao resultado. Se a árvore estiver balanceada os resultados estaram ordenados

```
    5
   /\
  3  10
 /   /\
1   7  15

[1, 3, 5, 7, 10, 15]
```

3. **Postorder**: Percorre todos os nós para livrar a memória da Call Stack dos métodos recursivos o mais rápido possível. O root será o último elemento a ser adicionado ao resultado.

```
    5
   /\
  3  10
 /   /\
1   7  15

[1, 3, 7, 15, 10, 5]
```

### Buscas em árvore binárias

1. **Busca em profundidade (DFS)**: Percorre, à partir do root, até chegar em um nó folha. Muito usado para percorrer uma árvore inteira e resolver o problema.
2. **Busca em largura (BFS)**: Abre a procura em todos os nós da direita e esqueda, à partir do root, até chegar em todos os nós folhas (é mais fácil implementar esse algoritmo com uma estrutura de dados auxiliar).

## Hashmap (Tabela Hash)

É uma estrutura de dados no formato `chave` e `valor`. Nessa estrutura de dados, a complexidade média de leitura, inserção e remoção é **O(1)**.

Para isso ser possível, é preciso que as chaves do `hashmap` passem para uma `hash function` que retorne o índice em `array`. Alguns exemplos de `hash functions` são `SHA-256` e `MD5`.

### Load Factor

Diferença de tamanho entre a quantidade de dados que temos e a estrutura de dados utilizada

EX: `[_, _, _, _, _, _, _, _, 1, 2] -> Load Factor = 2 / 10 = 0.2 ou 20%` ou seja, 20% de chance de uma colisão dentro do array.

Artigos demonstram que 70% é um valor permitido para segurança e performance no `hashmap`. Quando chega-se em 70% da estrutura de dados, é aumentado o tamanho dele em determinada proporção e as posições dos elementos são recalculadas.

## Grafos

É uma estrutura de dados que representa a ligação entre nós através de vértices. Geralmente um grafo pode ser representado por um **Grafo de Adjacência**.

Ex:

```python
[[0, 0, 1, 0, 0],
 [0, 1, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [1, 0, 0, 1, 1]]
```

## Trie (Prefix tree)

Quando caminhamos nessa árvore, mantém-se um estado do que foi caminhado anteriormente. Um exemplo dessa estrutura de dados é um algoritmo de *autocomplete*.

Exemplo de uma implementação de um `Trie` em `python` para o algoritmo de *autocomplete*;

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children[char]
                return False
            current_node = current_node.childer[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
```

## B-Tree

Uma árvore auto balanceável que seguem as seguintes regras:

- É preciso definir o número de chaves e *childrens* que ela deve ter
- O número de *children* é sempre 1 a mais que o número de chaves
- Todos os últimos *nodes* estão no mesmo nível

# Técnicas de exercícios com Arrays

## Two Pointer

Consiste em inicializar dois ponteiros (geralmente um no início e um no fim), o lado bom disso é que iremos usar esses ponteiros

## Sliding Window

Técnica muito utilizada quando a solução do problema é

- `subarray`
- Tamanho do `subarray`
- `substring`
- Tamanho de `substring`

Um pseudocódigo que resolve muitos problemas de `Sliding Window` é:

```
WHILE
    RIGHT++
    WHILE
        LEFT++
```

> O while de fora expande a janela, enquanto o de dentro contrai a janela. E geralmente durante a contração (LEFT++) é que é feio uma checkagem

## Binary Search (Busca binária)

Método de busca dentro de `arrays` ordenados.

- Complexidade Temporal: `O(logn)`
- Complexidade Espacial: `O(1)`

Exemplo de busca binária em `python` usando a técnica de `two pointer`.

```python
def binary_search(nums: list[int], n: int):
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = int((lo + hi)/2)

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid

    return -1
```

## Exponential Search

Similar em complexidade a busca binária. Os ponteiros `left` e `right` aumentam de forma exponencial até se encontrar o `subarray` que contenha o elemento da busca

Exemplo de busca exponencial em `python` usando a técnica de `two pointer`.

```python
def binary_search(nums: list[int], n: int, lo: int, hi: int):
    while lo < hi:
        mid = int((lo + hi)/2)

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid

    return -1

def exponential_search(nums: list[int], n: int):
    if nums[0] == n:
        return 0

    length = len(nums)
    i = 1

    while i < length and nums[i] < n:
        i *= 2
    
    if nums[i] == target:
        return i

    return binary_search(nums, n, i//2, min(i, length - 1))
```

## Grafos

Uma estrutura de dados que representa a conexão entre diversos nós. Geralmente representado por meio de uma `matriz de adjacência`

### Algoritmo de Dijsktra

Algoritmo utilizado para calcular e construir uma árvore de caminhos mínimos dentro do grafo.

```python
def dijkstra(graph, start):
    min_heap = [(0, start)] # Fila de processamento, inicialmente inicia com [(0, 'A')]
    distances = { node: float('inf') for node in graph }
    distances[start] = 0

    while min_heap:
        # Aqui o heap funciona como uma fila de prioridades
        # Processando os elementos de menor valor antes
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]: continue

        # Acessar todos os vizinhos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances
```
