def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    k=0
    i=0
    while i<len(s):
        if str(s[i]).isalpha():
            if str(s[i])=='a' or str(s[i])=='e' or str(s[i])=='i' or str(s[i])=='o' or str(s[i])=='u' or str(s[i])=='A' or str(s[i])=='E' or str(s[i])=='I' or str(s[i])=='O' or str(s[i])=='U':
                k=k+0
            else:
                k=k+1
        i=i+1
    return k
print(main('CodeschoolUz'))