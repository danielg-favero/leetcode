class MinStack:
    """
    Design a `stack` that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

    Implement the `MinStack` class:

    `MinStack()` initializes the `stack` object.
    `void push(int val)` pushes the element val onto the `stack`.
    `void pop()` removes the element on the top of the `stack`.
    `int top()` gets the top element of the `stack`.
    `int getMin()` retrieves the minimum element in the `stack`.

    You must implement a solution with `O(1)` time complexity for each function.

    Solução: Sempre que um problema tiver o enunciado pedindo para "retornar valor em tempo constante"
    é preciso pré calcular esse valor, nesse caso, cria-se um array `min_stack` para ter calculado o
    valor mínimo na `stack` durante a execucao
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            val = min(self.min_stack[-1], val)
        self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            raise IndexError("Empty Stack")

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]