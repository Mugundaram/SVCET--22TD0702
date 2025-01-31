def isPalindrome(s):
    return s == s[::-1]
s = "tamil"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")