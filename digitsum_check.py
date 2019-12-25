#%%
import time
import math
def find(m, s):
    if s < 0:
       return 0
    if m == 1:
        if s == 0 or s > 9:
            return 0
        return s
    
    t = -1
    for i in range(10):
        t = max(t, find(m - 1, s - i) * 10 + i)
    
    return t
    
a = {}

def len_digit(i):
    return len("%i" % i)

def find_dp(m, s):
    global a
    if s < 0:
       return (0, 0)
    if m == 1:
        if s == 0:
            return (0, 0)
        if s > 9:
            return (math.inf, 0)
        return (s, s)
    
    t = math.inf, -math.inf
    for i in range(10):
        if a.get((m - 1, s - i)) == None:
            a[(m - 1, s - i)] = find_dp(m - 1, s - i)

        t = min(t[0], a[(m - 1, s - i)][0] * 10 + i), max(t[1], a[(m - 1, s - i)][1] * 10 + i)
    
    return t

#%%
t0 = time.time()
all_sum = find_dp(3, 15)

# for i in a:
#     print(i, a[i])
print(all_sum)
t1 = time.time()
print('%.3f seconds' % (t1-t0))



# %%
