def reverseWords(s: str) -> str:
    """
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
    LeetCode URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
    """

    # Resultado, a resposta será concatenada aqui
    res = ''

    # Two Pointers: Left e Right
    left, right = 0, 0

    # EM PYTHON AS STRINGS SÃO IMUTÁVEIS POR ISSO É PRECISO CONCATENAR
    # RECADO: FAZ EM C OU JS QUE FICA MELHOR

    # Enquanto o Right não chegar no fim da string
    while right < len(s):
        # Percorrer a string até encontrar um espaço
        if s[right] != ' ':
            right += 1
        else:
            # Adicionar na resposta o que estiver entre o Left e o Right
            # [::-1] inverte o resultado
            res += s[left:right + 1][::-1]

            # Passa o right para a próxima palavra
            right += 1

            # Traz o left junto do right
            left = right

    # Inverter e concatenar a última palavra
    res += ' '
    res += s[left:right + 2][::-1]

    # Remover o primeiro espaço em branco
    return res[1:]