#%%
import random

A = [-2, 1, 3, -4, 5]
B = [2, 1, 5, 8, 4]
C = [3, 5, -7, 8, 10, 50, 100]
D = [random.random() for _ in range(30)]


def maxSubsetSum(A):
    dp = []
    dp.append(A[0])
    dp.append(max(dp[0], A[1]))

    for i in range(2, len(A)):
        dp.append(max(dp[i - 2] + A[i], dp[i - 1], A[i]))
    
    return dp.pop()


# %%
import time

time1 = time.time()

print(maxSubsetSum(A))
print(maxSubsetSum(B))
print(maxSubsetSum(C))
print(maxSubsetSum(D))
time2 = time.time()

print('%.3f secs' % (time2-time1))


# %%
# time1 = time.time()

# print(maxSubsetSum_copied(A))

# time2 = time.time()

# print('%.3f secs' % (time2-time1))


# %%
