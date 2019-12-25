#%%
A = [8, 7, 21, 28, 29, 78, 90, 80, 81]

def findLongestSequence_greedy(A):
    i = 0
    max = []
    temp = []

    while i < len(A):
        if i + 1 == len(A):
            temp += [A[i]]
            max = temp

        elif A[i] < A[i + 1]:
            temp += [A[i]]
        else:
            if len(max) < len(temp):
                max = temp
            temp.clear()
            
        i += 1
    
    return max

def findLongestSequence_dp(A, pos=0, max=[]):
    if pos == len(A):
        return max

    for i in range(len(A)):
        pass
    
#%%
seq = findLongestSequence_greedy(A)
seq
#%%
