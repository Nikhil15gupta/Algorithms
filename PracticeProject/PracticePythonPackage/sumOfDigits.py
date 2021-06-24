def dec2base(n, k):
    if n == 0:
        return 0
    ans = ""
    while n > 0:
        ans = str(n%k) + ans
        n = n//k
    return int(ans)

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n%10
        n//=10
    return sum

n = 34
k = 6

conv = dec2base(n, k)
print(sumOfDigits(conv))