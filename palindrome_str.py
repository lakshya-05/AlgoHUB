# check if a string palindrome or not

s = "nitin"
left, right = 0, len(s)-1

while left < right:
    if s[left] != s[right]:
        print("NOT Palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome String")
    
