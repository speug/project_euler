def is_palindrome(x):
    x_s = str(x)
    n = len(x_s)
    for i in range(0,n/2):
        n_i = n - i
        if(x_s[i] != x_s[n_i - 1]):
            return False
    return True

#print(is_palindrome(11021))

stop = False
max_pal = 0
for j in range(1,999):
    for k in range(1,999):
        prod = j*k
        if(is_palindrome(prod) and prod > max_pal):
            max_pal = prod
print(max_pal)
