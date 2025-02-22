def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
    """
    You are given `n` rectangles represented by a `0-indexed` 2D integer array rectangles, 
    where `rectangles[i] = [widthi, heighti]` denotes the width and height of the `ith` rectangle.

    Two rectangles `i` and `j (`i < j`) are considered interchangeable if they have the same 
    width-to-height ratio. More formally, two rectangles are interchangeable if 
    `widthi/heighti == widthj/heightj` (using decimal division, not integer division).

    Return the number of pairs of interchangeable rectangles in `rectangles`.

    Solução: Solução: Contar quantas vezes cada `ratio` aparece. Se um `ratio` aparece `n` vezes,
    é possível fazer `n * (n - 1) // 2` pares
    """
    ratio_count = {}
    pairs = 0

    for rectangle in rectangles:
        ratio = rectangle[0]/rectangle[1]

        if ratio_count.get(ratio) is None:
            ratio_count[ratio] = 1
        else:
            ratio_count[ratio] += 1
        
    for [_, value] in ratio_count.items():
        pairs += value * (value - 1) // 2

    return pairs