#%%
a = 'AbcDE'
b = 'ABDE'

d = 'KXzQ'
e = 'K'

def abbreviation(a, b):
    i = 0
    j = 0
    C = ''
    while i < len(b) and j < len(a):
        if a[j].islower():
            if b[i] == a[j].upper():
                C = C + b[i]
                i = i + 1
        else:
            if b[i] == a[j]:
                C = C + b[i]
                i = i + 1
            else:
                return False

        j = j + 1
            
        
    return C == b

# %%
abbreviation(d, e)

# %%
