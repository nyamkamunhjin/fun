#%%
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def check_prime(num):
    if num <= 1 or num == 4:
        return False
    if num <= 3:
        return True

    for i in range(2, num - 2):
        if gcd(num, i) == 1:
            if (i ** (num - 1)) % num == 1:
                return True
            else:
                return False
    
    return False



# %%
for i in range(200):
    print(i, check_prime(i))
# %%
