def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    i=0
    while i<len(s):
        if str(s[i]).islower():
            k=k+1
        i=i+1

    return k
print(main('Python 2022'))