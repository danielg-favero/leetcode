# Binários

## Operadores binários em python

### AND(&)

```python
5 & 3  # 101 & 011 = 001, resultado é 1
```

### OR(|)

```python
5 | 3  # 101 | 011 = 111, resultado é 7
```

### NOT(˜)

```python
~5  # Inverte 101 para 010, resultado é -6
```

### XOR(^)

```python
5 ^ 3  # 101 ^ 011 = 110, resultado é 6
```

### Left Shift (<<)

"Multiplica" o número por 2

```python
5 << 1  # 101 << 1 = 1010, resultado é 10
```

> Dependendo da linguagem, o tamanho do inteiro muda, chegará um ponto que ao fazer `left shift` os bits irão se perder

### Right Shift (>>)

"Divide" o número por 2

```
5 >> 1  # 101 >> 1 = 10, resultado é 2
```