# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 03:09:34 2020

@author: moulu
"""
from copy import deepcopy
import numpy as np
#sudoku = [[9,5,7,6,1,3,2,8,4],[4,8,3,2,5,7,1,9,6],[6,1,2,8,4,9,5,3,7],[1,7,8,3,6,4,9,5,2],[5,2,4,9,7,1,3,6,8],[3,6,9,5,2,8,7,4,1],[8,4,5,7,9,2,6,1,3],[2,9,1,4,3,6,8,7,5],[7,3,6,1,8,5,4,2,9]]
#s = [[0,0,0,0,0,0,2,0,0],[0,8,0,0,0,7,0,9,0],[6,0,2,0,0,0,5,0,0],[0,7,0,0,6,0,0,0,0],[0,0,0,9,0,1,0,0,0],[0,0,0,0,2,0,0,4,0],[0,0,5,0,0,0,6,0,3],[0,9,0,4,0,0,0,7,0],[0,0,6,0,0,0,0,0,0]]
#s = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]
#s = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
s = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]
n = [1,2,3,4,5,6,7,8,9]
def checkrow(r,i):
    if r.count(i) == 0:
        return True
    return False    
m = []
for i in range(0,9):
    for j in range(0,9):
        if s[i][j] == 0:
            m.append([i,j])
c = deepcopy(s)
for i in range(0,9):
    for j in range(0,9):
        c[i][j] = s[j][i]
box = []
for i in range(0,9,3):
    for j in range(0,9,3):
        a = []
        a.append(s[i][j])
        a.append(s[i][j+1])
        a.append(s[i][j+2])
        a.append(s[i+1][j])
        a.append(s[i+1][j+1])
        a.append(s[i+1][j+2])
        a.append(s[i+2][j])
        a.append(s[i+2][j+1])
        a.append(s[i+2][j+2])
        box.append(a)
print('s = ',np.array(s))
print('c = ',np.array(c))
print('box =',box)
print('m =',m)

sol = []
count = 0
i = 0
b = 0
while i < len(m):
    count += 1
    if i < b:
        if sol[-1] == 9:
            b = 0
            sol.pop()
            s[m[i][0]][m[i][1]] = 0
            c[m[i][1]][m[i][0]] = 0
            i -= 1
            continue
        else :
            v = sol[-1] + 1
        sol.pop()
        s[m[i][0]][m[i][1]] = 0
        c[m[i][1]][m[i][0]] = 0
    else :
        v = 1
    b = 0
    print('i = ',i)
    g = checkrow(s[m[i][0]],v)
    if g == True :
        g = checkrow(c[m[i][1]],v)
        if g == True :
            if m[i][0] < 3 and m[i][1] < 3 :
                    g = checkrow(box[0],v)
            elif m[i][0] < 3 and m[i][1] >= 3 and m[i][1] < 6 :
                    g = checkrow(box[1],v)
            elif m[i][0] < 3 and m[i][1] >= 6 and m[i][1] < 9 :
                    g = checkrow(box[2],v)
            elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 3 :    
                    g = checkrow(box[3],v)
            elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 6 and m[i][1] >= 3 :
                    g = checkrow(box[4],v)
            elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 9 and m[i][1] >= 6 :
                    g = checkrow(box[5],v)
            elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 3 :
                    g = checkrow(box[6],v)
            elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 6 and m[i][1] >= 3 :
                    g = checkrow(box[7],v)
            elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 9 and m[i][1] >= 6 :
                    g = checkrow(box[8],v)
    print('g = ',g)
    while g != True:
        if v == 9:
            b = i
            i = i-1
            break
        else :
            v +=1
        g = checkrow(s[m[i][0]],v)
        print('row check',g,v)
        if g == True :
            g = checkrow(c[m[i][1]],v)
            print('column check',g,v)
            if g == True :
                if m[i][0] < 3 and m[i][1] < 3 :
                    g = checkrow(box[0],v)
                elif m[i][0] < 3 and m[i][1] >= 3 and m[i][1] < 6 :
                    g = checkrow(box[1],v)
                elif m[i][0] < 3 and m[i][1] >= 6 and m[i][1] < 9 :
                    g = checkrow(box[2],v)
                elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 3 :    
                    g = checkrow(box[3],v)
                elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 6 and m[i][1] >= 3 :
                    g = checkrow(box[4],v)
                elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 9 and m[i][1] >= 6 :
                    g = checkrow(box[5],v)
                elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 3 :
                    g = checkrow(box[6],v)
                elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 6 and m[i][1] >= 3 :
                    g = checkrow(box[7],v)
                elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 9 and m[i][1] >= 6 :
                    g = checkrow(box[8],v)
                print('box check',g,v)

    if g == True :
        sol.append(v)
        s[m[i][0]][m[i][1]] = v
        c[m[i][1]][m[i][0]] = v
    if i<b :
        continue
    i+=1
    print(sol)
    print('.................count = ',count)
    if count >= 161 :
        break
"""
    print("ee value assign chestunnaa",v)
    g = checkrow(c[m[i][1]],v)
    print("kindaki eltondi")
    print(g)
    while g != True :
        if v == 9:
            b = i
            i = i-1
            break
        else :
            v +=1
        g = checkrow(c[m[i][1]],v)
        print('2nd while',v)
    if i < b:
        continue
    print("ee value assign chestunnaa",v)
    if m[i][0] < 3 and m[i][1] < 3 :
        g = checkrow(box[0],v)
    elif m[i][0] < 3 and m[i][1] >= 3 and m[i][1] < 6 :
        g = checkrow(box[1],v)
    elif m[i][0] < 3 and m[i][1] >= 6 and m[i][1] < 9 :
        g = checkrow(box[2],v)
    elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 3 :    
        g = checkrow(box[3],v)
    elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 6 and m[i][1] >= 3 :
        g = checkrow(box[4],v)
    elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 9 and m[i][1] >= 6 :
        g = checkrow(box[5],v)
    elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 3 :
         g = checkrow(box[6],v)
    elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 6 and m[i][1] >= 3 :
        g = checkrow(box[7],v)
    elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 9 and m[i][1] >= 6 :
        g = checkrow(box[8],v)
    print(g)
    while g != True :
        if v == 9 :
            b = i
            i = i-1
            break
        else :
            v += 1
        if m[i][0] < 3 and m[i][1] < 3 :
            g = checkrow(box[0],v)
        elif m[i][0] < 3 and m[i][1] >= 3 and m[i][1] < 6 :
            g = checkrow(box[1],v)
        elif m[i][0] < 3 and m[i][1] >= 6 and m[i][1] < 9 :
            g = checkrow(box[2],v)
        elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 3 :    
            g = checkrow(box[3],v)
        elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 6 and m[i][1] >= 3 :
            g = checkrow(box[4],v)
        elif m[i][0] < 6 and m[i][0] >= 3 and m[i][1] < 9 and m[i][1] >= 6 :
            g = checkrow(box[5],v)
        elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 3 :
            g = checkrow(box[6],v)
        elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 6 and m[i][1] >= 3 :
            g = checkrow(box[7],v)
        elif m[i][0] < 9 and m[i][0] >= 6 and m[i][1] < 9 and m[i][1] >= 6 :
            g = checkrow(box[8],v)
        print('3rd while',v)
    if i < b :
        continue
    s[m[i][0]][m[i][1]] = v
    sol.append(v)
    i += 1
    print('end of the loop')
"""
print(np.array(s))
#print(s == sudoku)    

            





















