import os
import numpy as np

delta=30
letters=dict()
letters['A']=0
letters['C']=1
letters['G']=2
letters['T']=3

alpha=np.zeros((4,4))
for i in range(0,4):
    alpha[i][i]=0
alpha[0][1]=alpha[1][0]=110
alpha[0][2]=alpha[2][0]=48
alpha[0][3]=alpha[3][0]=94
alpha[1][2]=alpha[2][1]=118
alpha[1][3]=alpha[3][1]=48
alpha[2][3]=alpha[3][2]=110

def substring(s,i,j):
    substring=""
    for k in range(i,j):
        substring+=s[k]
    return substring

def input_string(base_string,indices):
    input_string=base_string
    for i in range(0,len(indices)):
        indice=indices[i]
        input_string=substring(base_string,0,indice+1)+base_string+substring(base_string,indice+1,len((base_string)))
        base_string=input_string
    return input_string

def read_from_input_file(file):
    with open(file,'r') as f:
        base_string1=f.readline().strip()
        indices1=[]
        indices2=[]
        for line in f:
            line=line.strip()
            if(line.isdigit()):
                indices1.append(int(line))
            else:
                break
        base_string2=line
        for line in f:
            line=line.strip()
            if(line.isdigit()):
                indices2.append(int(line))
            else:
                break
    final_string1=input_string(base_string1,indices1)
    final_string2=input_string(base_string2,indices2)
    return final_string1,final_string2




def seqAlign_basic(s1,s2):

    
    n= len(s1)
    m= len(s2)

    dp=np.zeros((n+1,m+1))


    for index1 in range(0,n+1):
        dp[index1][0]=index1*delta
        
    for index2 in range(0,m+1):
        dp[0][index2]=index2*delta
    


    for index1 in range(1,n+1):
        for index2 in range(1,m+1):
            replace= dp[index1-1][index2-1]+alpha[letters[s1[index1-1]]][letters[s2[index2-1]]]
            remove= dp[index1-1][index2]+delta
            insert= dp[index1][index2-1]+delta

            dp[index1][index2]=min(replace,remove,insert)
        
    return int(dp[n][m])


s1,s2=read_from_input_file('./SampleTestCases/input1.txt')
value=seqAlign_basic(s1,s2)

print(value)


