def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    i=0
    while i<len(s):
       
        if str(s[i]).isdigit():
              k+=int(s[i])
        i+=1
    return k  
print(main('4444'))      