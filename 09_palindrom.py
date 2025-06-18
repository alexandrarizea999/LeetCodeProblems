def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    l = list(map(int, str(x)))
    if l == l[::-1]:
        return True
    else: return False

x = 909
print(isPalindrome(x))