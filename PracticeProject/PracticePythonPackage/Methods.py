
# To find if a string is Palindrome
#input: string
# output: boolean


def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

# To convert a decimal to a base k number
# input: n=number to be converted(int), k = base to convert to(int)

def dec2base(n, k):
    if n == 0:
        return 0
    ans = ""
    while n > 0:
        ans = str(n%k) + ans
        n = n//k
    return int(ans)

# To convert a number into base3
# input: n=int, num = "" (blank string)
# output: string

def base3(n, num):
            if not n: 
                return num
            n, r = divmod(n, 3)
            return base3(n, str(r) + num)
        
