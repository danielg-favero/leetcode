def firstUniqChar(s: str) -> int:
    """
    Given a string `s`, find the first non-repeating character in it and return its index. If it does not exists, return `-1`
    """

    counter = {}

    for i, c in enumerate(s):
        if c not in counter:
            counter[c] = [i, 1]
        else: 
            counter[c][1] += 1
    
    for _, val in counter.items():
        if val[1] == 1:
            return val[0]

    return -1