#%%
# s = a8, t = h1 
import math

def move(s):
    possible_movements = {}
    if s[0] - 1 >= 1:
        possible_movements['L'] = (s[0]- 1, s[1])

    if s[0] - 1 >= 1 and s[1] + 1 <= 8:
        possible_movements['LU'] = (s[0] - 1, s[1] + 1)
    
    if s[1] + 1 <= 8:
        possible_movements['U'] = (s[0], s[1] + 1)
    
    if s[1] + 1 <= 8 and s[0] + 1 <= 8:
        possible_movements['RU'] = (s[0] + 1, s[1] + 1)
    
    if s[0] + 1 <= 8:
        possible_movements['R'] = (s[0] + 1, s[1])

    if s[0] + 1 <= 8 and s[1] - 1 >= 1:
        possible_movements['RD'] = (s[0] + 1, s[1] - 1)

    if s[1] - 1 >= 1:
        possible_movements['D'] = (s[0], s[1] - 1)

    if s[1] - 1 >= 1 and s[0] - 1 >= 1:
        possible_movements['LD'] = (s[0] - 1, s[1] - 1)
    
    return possible_movements


def chess_min_dist(s, t, min_move=[]):
    temp_s = (ord(s[0]) - 96, int(s[1]))
    temp_t = (ord(t[0]) - 96, int(t[1]))

    # print(temp_s, temp_t)

    while(temp_s != temp_t):
        possible_movements = move(temp_s)

        # find min dist 
        min = ('', 10)
        for k, v in possible_movements.items():
            calc = k, math.sqrt((v[0] - temp_t[0]) ** 2 + (v[1] - temp_t[1]) ** 2)
            
            if calc[1] < min[1]:
                min = calc
        
        print(min[0])

        temp_s = possible_movements[min[0]] 
        

        



#%%
chess_min_dist('h6', 'a8')

# %%
