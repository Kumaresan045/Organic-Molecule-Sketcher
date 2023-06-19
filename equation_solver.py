import numpy as np
subscript={0:'\u2080',1:'\u2081',2:'\u2082',3:'\u2083',4:'\u2084',5:'\u2085',6:'\u2086',7:'\u2087',8:'\u2088',9:'\u2089'}

def combi(a,b):
    lis=[]
    for i in range(2**a):
        st=str(bin(i))[2:]
        st='0'*(a-len(st))+st
        if st.count('1')==b:    
            lis.append(st)
    return lis
#______________________________#
def coalesce(a,reactants):
    lr=reactants.split('+')
    string=''
    for i in range(len(lr)):
        if a[i]!=1:
            string+=str(a[i])
        for char in lr[i]:
            if char.isnumeric():
                string+=subscript[int(char)]
            else:
                string+=char
        if i<len(lr)-1:
            string+='+'
    return string    
#______________________________#
def hcf(lis):
    gcd=min(lis)
    while True:
        i=0
        for elem in lis:
            if elem%gcd==0:
                i+=1
                continue
            else:
                break
        if i==len(lis):
            for j in range(len(lis)):
                lis[j]=int(lis[j]/gcd)
            return lis
        else:
            gcd-=1
            continue
            
#_________________________________#
def lcm(lis):
    if max(lis)==int(max(lis)):
        no_=max(lis)
    else:
        no_=int(max(lis)+1)
    while True:
        i=0
        while i<len(lis):
            if round(no_*lis[i],1)==int(round(no_*lis[i],1)):
                i+=1
                continue
            else:
                no_+=1
                break
        if i==len(lis):
            break
        else:
            continue
    for j in range(len(lis)):
        lis[j]=round(lis[j]*no_)
    return lis
#_____________________________________#
def checkredund(a,b):
    dc=[]
    for x in range(len(a)):
        if b[x]!=0 and a[x]!=0:
            dq=a[x]/b[x]
            dc.append(dq)
        elif b[x]==0 and a[x]==0:
            pass
        elif b[x]==0 or a[x]==0:
            return False
    de=dc[0]
    co=0
    while co<len(dc):
        if de==dc[co]:
            co+=1
            continue
        else:
            return False
        
    return True
        
#________________________________________#
def checkdupe(rcoeff):
    dupent=[]
    for i in range(len(rcoeff)):
        temp=rcoeff[i]
        for j in range(i+1,len(rcoeff)):
            if checkredund(temp,rcoeff[j]):
                dupent.append(j)
    return dupent    
#___________________________________________#
def eqnsolver(coeff_arr,cons_arr):
    bcoeff=[1]
    if len(coeff_arr)==len(coeff_arr[0]):
        sol=np.linalg.solve(coeff_arr,cons_arr)
    else:
        poss=combi(len(coeff_arr),len(coeff_arr[0]))
        for event in poss:
            coeff_arr_1=[]
            cons_arr_1=[]
            for i in range(len(event)):
                if int(event[i]):
                    coeff_arr_1.append(coeff_arr[i])
                    cons_arr_1.append(cons_arr[i])
            try:
                sol=np.linalg.solve(coeff_arr_1,cons_arr_1)
            except:
                continue
                    
                    
    for i in range(len(sol)):
        sol[i]=round(sol[i],2)
    l=list(sol)
    bcoeff.extend(l)
    return bcoeff
#______________________________________________#

def consolidate(reagents,mf):
    global l_ele
    seq=reagents.split('+')
    l_dict=list()
    l_ele=list()
    l_l_coeff=list()
    for mcl in seq:
        testvariable_bracket=False
        d_atomicity=dict()
        for i in range(len(mcl)):
            if mcl[i]=="(":
                testvariable_bracket=True
                multifac=mcl[mcl.find(')',i)+1]
                if mcl.find(')',i)+2<len(mcl) and mcl[mcl.find(')',i)+2].isnumeric():
                    multifac+= mcl[mcl.find(')',i)+2]
                multifac=int(multifac)
            elif mcl[i]==')':
                testvariable_bracket=False
                multifac=1
            elif i<len(mcl)-1 and mcl[i].isupper() and mcl[i+1].islower():
                end=i+2
            elif mcl[i].isupper():
                end=i+1
            if mcl[i].isupper():
                if mcl[i:end] not in d_atomicity:
                    d_atomicity[mcl[i:end]]=0
                if end<len(mcl) and mcl[end].isnumeric():
                    fac=mcl[end]
                    if end<len(mcl)-1 and mcl[end+1].isnumeric():
                        fac+=mcl[end+1]
                    fac=int(fac)
                else:
                    fac=1
                if testvariable_bracket:
                    fac*=multifac
                d_atomicity[mcl[i:end]]+=fac
        l_dict.append(d_atomicity)
    for d in l_dict:
        for el in d:
            if el not in l_ele:
                l_ele.append(el)
    l_ele.sort()
    for el in l_ele:
        l_coeff=list()
        for d in l_dict:
            if el in d:
                l_coeff.append(d[el]*mf)
            else:
                l_coeff.append(0)
        l_l_coeff.append(l_coeff)
    return l_l_coeff

#______________________________________________________________________________________________________________#

    


