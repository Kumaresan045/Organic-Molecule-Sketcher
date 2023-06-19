from tkinter import *
from math import cos
from turtle import *
from PIL import ImageTk,Image
import tkinter.messagebox as tm
import tkinter.font as font
import pickle
import importlib
import numpy as np
import mysql.connector as mc
import math
import random

testvariable_err_page=False

#Data For Instructions:

tinsoms='''Having a doubt in the structure of organic compounds?
You'll get the structure of the compound by giving the IUPAC or common name of it by following these instructions:

1. Give the IUPAC name properly with each word (if substituents) seperated by '-' and only lower case letters.

2. In case of N-substituted compounds, capital N can be used. Eg: N-methylamine

3. List the substituents and its positions properly.

4. Click 'Go' after typing the name amd click 'Try again?' if you want the structure of another compound.

5. Some of the valid names are as follows:
       • ethyl propanoate (here no hyphen)
       • o-chloro-phenol (same can be used for m and p)
       • butoxy-cyclopentane
       • propanoic butanoic anhydride (here no hyphen)
       • bicyclo[2.3.1]octane
       • spiro[5.2]octane
       • 2-hydroxy-pent-3-en-al
       • 3-amino-hexanoic acid

6. Some of the invalid names are as follows:
       • Propane
       • 2 hydroxy Ethane
       • 3,ethyl 2-chloro pentanal
       • n-ethyl amine
       • bicyclo (2,3,5) heptane
       • ethanoyl CHLoride'''

tinseqn='''Equation Balancing - A Herculean task right?
Here, you can get the balanced equation by following these instructions:

1. Give the reactants in the Reactants block and the products in the Products block.

2. The chemical formulas of compounds must be given in the proper cases. Eg: Sodium chloride should be given as NaCl.

3. The compounds shd be seperated by '+' only.

4. Ions are not to be given as input.

5. Once the reactants and products are given, press 'Go' to get the balanced equation.

6. If you want to balance another equation press 'Try again'.

7. Examples
      • in reactants block: Fe+O2
        in products block: Fe2O3

      • in reactants block: C+H2SO4
        in products block: CO2+H2O+SO2

      • in reactants block: CH3COOH+CH3CH2CH2OH
        in products block: CH3COOCH2CH2CH3+H2O'''

tinogg='''Ready to test your grasp on Common names of Organic compounds?
You'll face 5 questions each having the structure of well known a organic compound. You have to answer the question by giving the common name of it while following these instructions:

1. Give the common name in the answer block in lower case only. Eg: ethyl alcohol.

2. In case of compounds with names as abbreviations like NBS, CDT it can be as it is.

3. After giving the answer click 'Save & Next' to go for the next question.

4. Each correct answer carries 1 mark and wrong or unanswered questions will not fetch any.

5. Your score will be given after the answering of all 5 questions. 

6. Press the 'Result' button to get the analysis of the questions. A table will be displayed having your answer, the correct answer and the marks scored in that question.
'''


def insoms():
    tm.showinfo(title='Instructions for Name Input',message=tinsoms)
def inseqn():
    tm.showinfo(title='Welcome To Equation Balancer',message=tinseqn)

def Drawnew():
    DrawMol(entry.get(),mode='draw')
def DrawMol(Name,mode):
    global T
    global canvas
    global s1
    canvas=ScrolledCanvas(root)
    canvas.place(relx=0.25,y=200,relheight=0.5,relwidth=0.5)
    s1=TurtleScreen(canvas)
    T=RawTurtle(s1)
    T.ht()
    T.pensize(2)
    global entry
    global N_subs
    global a
    global alkoxysubs
    global alkylsubs
    global b
    global benzenoid_
    global c
    global c_type_subs
    global coohderv_pref
    global coohderv_suff
    global cursor
    global cyclic_oxo_fun
    global cycloalkoxysubs
    global cycloalkylsubs
    global d_subst
    global data
    global dbsubs
    global dfun
    global dfun1
    global dsubalkyl
    global dsubs
    global hetero_acyclic
    global heteroloc
    global i
    global i1
    global i2
    global j
    global k
    global l
    global length
    global list_of_locants
    global list_of_substituents
    global loc
    global locmethsub
    global locmethsub_triv
    global locsub
    global locsubal
    global lsubs
    global lsuff
    global mycon
    global n_alkylsubs
    global name
    global name1
    global othersuff
    global othersuff_ref
    global pchain
    global possiblenames
    global possiblenames1
    global pref
    global revname
    global revrootwords
    global rootwords
    global special_names
    global subalkyl
    global subs
    global suff
    global testname
    global testvariable_1_one_1
    global testvariable_N_subst
    global testvariable_alkyl_othersuff
    global testvariable_amine
    global testvariable_anhy
    global testvariable_benz
    global testvariable_bicyc_spiro_
    global testvariable_bridgehead
    global testvariable_commname
    global testvariable_db_cum_coohderv
    global testvariable_epoxy_used
    global testvariable_ester
    global testvariable_ether
    global testvariable_ether_1
    global testvariable_fused
    global testvariable_hetero
    global testvariable_iso
    global testvariable_ketone
    global testvariable_long
    global testvariable_methderv
    global testvariable_pres_subs
    global testvariable_special_
    global testvariable_spl_ketone
    global testvariable_subalkyl
    global testvariable_subalkyl_0
    global testvariable_subst_phenyl
    global testvariable_sulpho
    global testvariable_sulpho_1
    global testvariable_sulpho_2
    global tobeusedloc
    global trivialsubs
    global usedloc
    global usedloc1




    possiblenames1=[]
    subalkyl=''
    pchain=''
    testvariable_special_=0
    testvariable_fused=0
    testvariable_long=0
    testvariable_subst_phenyl=0
    testvariable_epoxy_used=0
    testvariable_N_subst=0
    testvariable_sulpho_2=0
    testvariable_sulpho_1=0
    testvariable_sulpho=0
    testvariable_pres_subs=0
    testvariable_hetero=0
    testvariable_spl_ketone=0
    testvariable_ether_1=0
    testvariable_1_one_1=0
    testvariable_commname=0
    testvariable_bridgehead=0
    testvariable_methderv=0
    testvariable_ketone=0
    testvariable_ether=0
    testvariable_anhy=0
    testvariable_ester=0
    testvariable_amine=0
    testvariable_bicyc_spiro_=0
    testvariable_alkyl_othersuff=0
    testvariable_benz=0
    testvariable_subalkyl=0
    testvariable_subalkyl_0=0
    testvariable_db_cum_coohderv=0
    testvariable_iso=0
    d_subst=dict()
    heteroloc=dict()
    locmethsub_triv=dict()
    locmethsub=dict()
    locsubal=dict()
    locsub=dict()
    loc=dict()
    dbsubs=dict()
    dsubs={}
    dfun1={}
    dfun={}
    dsubalkyl={}
    list_of_locants=list()
    N_subs=[]
    c_type_subs=[]
    usedloc=[]
    usedloc1=[]
    revrootwords=[]
    cycloalkylsubs=[]
    alkylsubs=[]
    alkoxysubs=[]
    tobeusedloc=[]
    n_alkylsubs=[]
    list_of_substituents=[]
    rootwords=['meth','eth','prop','but','pent','hex','hept','oct','non','dec']
    for k in rootwords:
        revrootwords.append(k[::-1])
    for k in rootwords:
        alkylsubs.append(k+'yl')
        c_type_subs.append(k+'yl')
    for k in rootwords:
        alkoxysubs.append(k+'oxy')
        c_type_subs.append(k+'oxy')
    alkoxysubs.append('phenoxy')
    c_type_subs.append('phenoxy')
    for k in rootwords:
        cycloalkylsubs.append('cyclo'+k+'yl')
        c_type_subs.append('cyclo'+k+'yl')
    for k in rootwords:
        n_alkylsubs.append('n-'+k+'yl')
        c_type_subs.append('n-'+k+'yl')

    possiblenames=[]
    a=0#pchain index
    b=[]#List for storing position of double bond
    c=[]#List for storing position of triple bond
    cyclic_oxo_fun={'carboxylic acid':'COOH','carbaldehyde':'CHO','carbonyl chloride':'COCl','carbonyl fluoride':'COF','carbonyl bromide':'COBr','carbonyl iodide':'COI','carbonitrile':'CN'}
    cycloalkoxysubs={'methoxy':'OCH\u2083','ethoxy':'OC\u2082H\u2085','propoxy':'OC\u2083H\u2087','butoxy':'OC\u2084H\u2089','pentoxy':'OC\u2085H\u2081\u2081','hexoxy':'OC\u2086H\u2081\u2083','heptoxy':'OC\u2087H\u2081\u2085','octoxy':'OC\u2088H\u2081\u2087','nonoxy':'OC\u2089H\u2081\u2089','decoxy':'OC\u2081\u2090H\u2082\u2081','phenoxy':'OC\u2086H\u2085'}
    pref={'hydro':'H','sulpho':'SO\u2083H','mercapto':'SH','amido':'CONH\u2082','hydroxy':'OH','carbonylchloride':'COCl','carbonylfluoride':'COF','carbonylbromide':'COBr','carbonyliodide':'COI','nitro':'NO\u2082','nitroso':'NO','chloro':'Cl','bromo':'Br','fluoro':'F','iodo':'I','amino':'NH\u2082','cyano':'CN','azido':'N\u2083','isocyano':'NC','carboxy':'COOH','formyl':'CHO','acetoxy':'OCOCH\u2083','acetyl':'COCH\u2083'}
    suff={'thiol':'SH','ol':'OH','amine':'NH\u2082','nitrile':'CN','isonitrile':'NC','sulphonicacid':'SO\u2083H'}
    coohderv_suff=['oic acid','oyl chloride','oyl fluoride','oyl bromide','oyl iodide','al','one','amide']
    coohderv_pref=['keto','oxo','aldo']
    othersuff_ref={'alcohol':'hydroxy','chloride':'chloro','fluoride':'fluoro','bromide':'bromo','iodide':'iodo','carboxylic acid':'carboxy','carbaldehyde':'formyl','cyanide':'cyano','isocyanide':'isocyano'}
    othersuff={'alcohol':'OH','chloride':'Cl','fluoride':'F','bromide':'Br','iodide':'I','carboxylic acid':'COOH','carbaldehyde':'CHO','cyanide':'CN','isocyanide':'NC'}
    trivialsubs=['phenyl','isobutyl','isopropyl','isopentyl','neopentyl','sec-butyl','acetyl','tert-butyl','t-butyl']
    benzenoid_={'benzene':{},'subtolyl':{'methyl':[2],'attach':[1]},'subphenyl':{'attach':[1]},'benzoylchloride':{'carbonylchloride':[1]},'benzoylfluoride':{'carbonylfluoride':[1]},'benzoylbromide':{'carbonylbromide':[1]},'benzoyliodide':{'carbonyliodide':[1]},'toluene':{'methyl':[1]},'benzamide':{'amido':[1]},'anisole':{'methoxy':[1]},'phenol':{'hydroxy':[1]},'aniline':{'amino':[1]},'benzoic acid':{'carboxy':[1]},'benzaldehyde':{'formyl':[1]},'benzonitrile':{'cyano':[1]},'xylene':{'methyl':[1,2]},'anisic acid':{'methoxy':[1],'carboxy':[2]},'cymene':{'isopropyl':[1],'methyl':[2]},'cresol':{'methyl':[1],'hydroxy':[2]},'toluidine':{'methyl':[1],'amino':[2]},'anisidine':{'methoxy':[1],'amino':[2]},'toluic acid':{'methyl':[1],'carboxy':[2]}}
    hetero_acyclic=['heteroNN','heteroSS','heteroOO']
    special_names=['cubane']

    for k in pref:
        list_of_substituents.append(k)
    for k in cycloalkoxysubs:
        list_of_substituents.append(k)
        c_type_subs.append('cyclo'+k)
    for k in coohderv_pref:
        list_of_substituents.append(k)
    for k in trivialsubs:
        c_type_subs.append(k)
    for k in hetero_acyclic:
         list_of_substituents.append(k)

        
    #________________________________FUNCTION DEFINIIONS_(soul of the program)______________________________#

    def Err():
        T.speed(0)
        T.pu()
        T.home()
        T.goto(T.xcor()-150,T.ycor()+150)
        T.write('Invalid Name',font=('Arial',32,"normal"))
        T.goto(T.xcor()+150,T.ycor()-350)
        T.pd()
        T.circle(150)
        T.pu()
        T.goto(T.xcor()-80,T.ycor()+170)
        T.pd()
        T.circle(20)
        T.pu()
        T.goto(T.xcor()+160,T.ycor())
        T.pd()
        T.circle(20)
        T.pu()
        T.home()
        T.goto(T.xcor()+50,T.ycor()-150)
        T.pd()
        T.seth(90)
        T.circle(50,180)

        
    #________________________________________________#
    def mvp(letter,coordinates):
        T.fillcolor('white')
        T.pu()
        T.goto(coordinates)
        T.goto(T.xcor(),T.ycor()-10)
        T.seth(0)
        T.begin_fill()
        T.circle(15)
        T.end_fill()
        T.pu()
        T.goto(T.xcor()-7,T.ycor()-2)
        T.write(letter,font=('Arial',18,"normal"))
    #____________________________________________________#
    def drawspecial(name):
        if name=='cubane':
            los=[]
            T.pu()
            T.goto(-100,100)
            T.pd()
            for i in range(4):
                los.append(T.pos())
                T.fd(120)
                T.rt(90)
            T.seth(-45)
            T.pu()
            T.fd(50)
            T.seth(0)
            T.pd()
            for i in range(4):
                T.fd(120)
                T.rt(90)
            for j in los:
                T.pu()
                T.goto(j)
                T.seth(-45)
                T.pd()
                T.fd(50)




    def drawfused(tupl):
        global ring_no
        if name=='fused_ring_((6,[1,3,5],{},{},0),(5,[],{"hydroxy":[3,3],"oxo":[2,4]},{},2))':
            tobeusedloc.extend([3,3])
        for ring_no in range(len(tupl)):
            sides,dbp,Sub,het,attach_loc=tupl[ring_no]
            if ring_no!=0:
                T.pu()
                T.goto(list_of_locants[ring_no-1][attach_loc])
                if attach_loc+1 in list_of_locants[ring_no-1]:
                    T.seth(T.towards(list_of_locants[ring_no-1][attach_loc+1])+180)
                else:
                    T.seth(T.towards(list_of_locants[ring_no-1][1])+180)             
                T.pd()
                cyc(sides,dbp,[],Sub,{},mov=False,hetero_=het)
            else:
                cyc(sides,dbp,[],Sub,{},mov=True,hetero_=het)
                
                    
    #__________________________________________________#
    def drawepoxy(list99):
        global testvariable_epoxy_used
        if not testvariable_epoxy_used:
            loc007,loc008=list99[0],list99[1]
            T.pu()
            T.goto(loc[loc007])
            T.seth(T.towards(loc[loc008]))
            T.lt(60)
            T.pd()
            T.fd(65)
            T.rt(120)
            T.fd(65)
            T.pu()
            T.bk(65)
            mvp('O',T.pos())
        testvariable_epoxy_used=1

    #________________________________________________________#
    def draw_N_subs(list__,type_,orient):
        print(list__)
        refdict={'amideleft':[90,210],'amideright':[0,330],'aminetop':[150,30],'aminebottom':[210,330],'amineleft':[120,240],'amineright':[60,300]}
        no=len(list__)
        q1=alkylsubs.index(list__[0])+1
        T.write('N',font=('Arial',18,'normal'))
        T.pu()
        T.goto(T.xcor()+8,T.ycor()+15)
        centr=T.pos()
        T.seth(refdict[type_+orient][0])
        T.fd(20)
        T.pd()
        for i in range(q1):
            T.fd(40)
            if i%2==0:
                T.rt(60)
            else:
                T.lt(60)
        T.pu()
        T.goto(centr)
        T.seth(refdict[type_+orient][1])
        T.fd(20)
        T.pd()
        if no==2:
            q2=alkylsubs.index(list__[1])+1
            for i in range(q2):
                T.fd(40)
                if i%2==0:
                    T.rt(60)
                else:
                    T.lt(60)
        else:
            T.fd(20)
            curdraw('H')
        T.pu()
                
    def drawsulphonic(x):
        if x==1:
            if not testvariable_sulpho_2:
                T.pd()
                T.fd(30)
            homing=T.pos()
            ketocyclic(0,4)
            ketocyclic(180,4)
            T.goto(homing)
            T.seth(90)
            T.fd(30)
            
        elif x==-1:
            T.pd()
            T.fd(10)
            homing=T.pos()
            ketocyclic(0,4)
            ketocyclic(180,4)
            T.goto(homing)
            T.seth(-90)
            T.fd(30)
            T.pu()
            T.fd(5)
        
        elif x==0:
            homing=T.pos()
            ketocyclic(90,4)
            ketocyclic(270,4)
            T.goto(homing)
            T.seth(180)
            T.fd(30)
        curdraw('OH')    
        T.pu()
        T.goto(homing)
        T.pd()
        mvp('S',T.pos())

    def writepref_special(x,theta_):#Already align it with correct T.heading
        for k in x:
            if k in alkylsubs:
                for j in x[k]:
                    T.seth(theta_)
                    angl=T.heading()
                    a1=alkylsubs.index(k)
                    T.pd()
                    if angl<270 and angl>90:
                        for i in range(a1):
                            if i%2==0:
                                T.lt(60)
                            else:
                                T.rt(60)
                            T.fd(50)
                    elif angl<90 or angl>270:
                        for i in range(a1):
                            if i%2==0:
                                T.rt(60)
                            else:
                                T.lt(60)
                            T.fd(50)
            elif k in cycloalkylsubs:
                for j in x[k]:
                    T.seth(theta_)
                    a1=cycloalkylsubs.index(k)
                    ang=180*((a1-1)/(a1+1))
                    T.lt(ang/2)
                    for i in range(a1+1):
                        T.fd(50)
                        T.rt(180-ang)
            elif k in trivialsubs:
                if testvariable_ether_1 or testvariable_amine:
                    T.pu()
                    T.bk(40)
                    T.pd()
                for j in x[k]:
                    T.seth(theta_)
                    if k=='phenyl':
                        T.fd(40)
                        cyc(6,[1,3,5],[],mov=False)
                    elif k=='isopropyl':
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    elif k=='isobutyl':
                        T.lt(40)
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    elif k=='tert-butyl' or k=='t-butyl':
                        T.lt(90)
                        T.fd(40)
                        T.pu()
                        T.bk(80)
                        T.pd()
                        T.fd(40)
                        T.rt(90)
                        T.fd(40)
                    elif k=='neopentyl':
                        T.lt(40)
                        T.fd(40)
                        T.lt(90)
                        T.fd(40)
                        T.pu()
                        T.bk(80)
                        T.pd()
                        T.fd(40)
                        T.rt(90)
                        T.fd(40)
                    elif k=='isopentyl':
                        T.lt(40)
                        T.fd(40)
                        T.rt(40)
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                        
    #___________________________________________________#
    def drawanhydride(a,b):
        T.goto(0,0)
        T.write('O',font=('Arial',18,'normal'))
        T.pu()
        T.goto(T.xcor()+20,T.ycor()+15)
        T.pd()
        T.lt(30)
        T.fd(50)
        T.goto(T.xcor(),T.ycor()+50)
        T.pu()
        T.goto(T.xcor()-5,T.ycor())
        T.pd()
        T.write('O',font=('Arial',18,'normal'))
        T.pu()
        T.goto(T.xcor()+12,T.ycor())
        T.pd()
        T.goto(T.xcor(),T.ycor()-50)
        if a!='benzoic':
            for i in range(a-1):
                if i%2==0:
                    T.seth(330)
                    T.fd(50)
                else:
                    T.seth(30)
                    T.fd(50)
        else:
            T.seth(330)
            T.fd(50)
            cyc(6,[1,3,5],[],mov=False)
        T.pu()        
        T.goto(-5,15)
        T.seth(150)
        T.pd()
        T.fd(50)
        T.goto(T.xcor(),T.ycor()+50)
        T.pu()
        T.goto(T.xcor()-10,T.ycor())
        T.pd()
        T.write('O',font=('Arial',18,'normal'))
        T.pu()
        T.goto(T.xcor()+3,T.ycor())
        T.pd()
        T.goto(T.xcor(),T.ycor()-50)
        if b!='benzoic':
            for j in range(b-1):
                if j%2==0:
                    T.seth(210)
                    T.fd(50)
                else:
                    T.seth(150)
                    T.fd(50)
        else:
            T.seth(210)
            T.fd(50)
            cyc(6,[1,3,5],[],mov=False)
    #______________________________________________________________#
    def drawester(b,a,typ):
        global dfun1
        if a!='benzoate':
            dfun1={'oic acid':[a]}
            strch(a,[],[])
            T.seth(0)
        else:
            a=2
            loc[2]=T.pos()
            T.seth(225)
            T.fd(40)
            cyc(6,[1,3,5],[],mov=False)
            dfun1={'oic acid':[2]}
            writesuff1(dfun1)
            T.seth(0)
            
        if a%2!=0:
            T.seth(-50)
            T.goto(T.xcor()+20,T.ycor()+10)
            T.pd()
            T.fd(40)
            if typ=='alkyl':
                T.seth(50)
        else:
            T.seth(50)
            T.fd(30)
            T.pd()
            T.fd(40)
            if typ=='alkyl':
                T.seth(-50)
        if typ=='alkyl':    
            for i in range(b-1):
                T.fd(55)
                if i%2==0:
                    T.rt(100)
                else:
                    T.lt(100)
        elif typ=='tri/cyclo':
            loc['O']=T.pos()
            writepref({b:['O']})
    #______________________________________________________________#
    def drawbicyclo(x,y,z): #Make sure to take the arguments in descending order 
        T.pu()
        T.goto(-50,-50)
        T.seth(-90)
        T.pd()
        #For drawing 1st cycle
        for i in range(x+1):
            T.rt(180-180*x/(x+2))
            #T.write(i+1)
            loc[i+1]=T.pos()
            T.fd(70)
        T.seth(180*y/(y+2)-90)
        #For drawing 2nd cycle
        for i in range(y+1):
            #T.write(x+i+2)
            loc[x+i+2]=T.pos()
            T.fd(70)
            T.rt(180-180*y/(y+2))
        T.seth(90+180*z/(z+2))
        #For drawing 3rd cycle
        for i in range(z+1):
            T.fd(70)
            if i!=z:
                #T.write(x+y+i+3)
                loc[x+y+i+3]=T.pos()
                T.rt(180-180*z/(z+2))
        

    #______________________________________________________________#        
    def drawamine(a,b=0,c=0):#if substituents are present in compound we will alter this function
        #a,b,c are integers and they take the values of alkyl groups attached to nitrogen. if 1 degree give b=c=0
        T.pu()
        T.goto(-50,0)
        T.write('N',font=('Arial',18,'normal'))
        T.goto(T.xcor()+8,T.ycor()-5)
        T.goto(-42,15)
        T.seth(30)
        T.fd(20)
        T.pd()
        if c not in trivialsubs and c not in cycloalkylsubs:
            for i in range(c):
                T.fd(50)
                if i%2==0:
                    T.rt(60)
                else:
                    T.lt(60)
        else:
            T.fd(50)
            loc['N1']=T.pos()
            writepref_special({c:['N1']},T.heading())
        if c==0:
            T.fd(20)
            curdraw('H')
        T.pu()
        T.goto(-42,15)
        T.seth(150)
        T.fd(20)
        T.pd()
        if b not in trivialsubs and b not in cycloalkylsubs:
            for i in range(b):
                T.fd(50)
                if i%2==0:
                    T.lt(60)
                else:
                    T.rt(60)
        else:
            T.fd(50)
            loc['N2']=T.pos()
            writepref_special({b:['N2']},T.heading())   
        if b==0:
            T.fd(20)
            curdraw('H')
        T.pu()
        T.goto(-42,15)
        T.seth(270)
        T.fd(20)
        T.pd()
        if a not in trivialsubs and a not in cycloalkylsubs:
            for i in range(a):
                T.fd(50)
                if i%2==0:
                    T.lt(60)
                else:
                    T.rt(60)
        else:
            T.fd(50)
            loc['N1']=T.pos()
            writepref_special({a:['N1']},T.heading())   
            
    #______________________________________________________________#    
    def drawspiro(x,y):
        T.pu()
        T.ht()
        T.goto(0,0)
        k=(x-1)*180/(x+1)
        l=(y-1)*180/(y+1)
        T.seth(-k/2)
        T.pd()
        for i in range(x+1):
            T.rt(180-k)
            loc[i+1]=T.pos()
            #T.write(i+1)
            T.fd(70)
        T.seth(l/2)
        for j in range(y+1):
            if j:
                loc[x+j+1]=T.pos()
                #T.write(x+j+1)
            T.fd(70)
            T.rt(180-l)
    #______________________________________________________________#
    def fbenz(bsubs,benzchain):#Returns the substituent part
        localdict={}
        lbsubs=bsubs.split('-')
        for k in ['o','m','p','ortho','meta','para']:
            if k in lbsubs:
                n1=lbsubs.index(k)
                lbsubs1=lbsubs[:n1]
                lbsubs=lbsubs[n1:]
                for el in lbsubs1:
                    if el.isalpha() and el not in ['o','m','p','ortho','meta','para']:
                        localdict[el]=[int(lbsubs1[lbsubs1.index(el)-1])]
            
        if benzchain=='benzene' and not bsubs or benzchain=='benzene' and len(lbsubs)==1 or benzchain=='benzene' and lbsubs[0] not in ['ortho','meta','para','o','m','p']:
            return bsubs
        elif benzchain in ['benzamide','toluene','anisole','phenol','aniline','subphenyl','benzoic acid','benzaldehyde','benzonitrile','benzoylchloride','benzoylfluoride','benzoylbromide','benzoyliodide'] and not bsubs:
            localdict.update(benzenoid_[benzchain])
            return localdict   
        elif benzchain=='benzene' and len(lbsubs)>1 and lbsubs[1][:2]!='di':
            return bsubs
        elif benzchain=='benzene' and lbsubs[1][:2]=='di':
            lbsubs[1]=lbsubs[1][2:]
            localdict.update(benzenoid_[benzchain])
            if lbsubs[0]=='o' or lbsubs[0]=='ortho':
                    localdict[lbsubs[1]]=[1,2]
            elif lbsubs[0]=='m' or lbsubs[0]=='meta':
                    localdict[lbsubs[1]]=[1,3]
            elif lbsubs[0]=='p' or lbsubs[0]=='para':
                    localdict[lbsubs[1]]=[1,4]
        elif lbsubs[0] in ['o','m','p','ortho','meta','para']:#Whenever Ortho-Meta-Para Encountered
            if benzchain in ['xylene','subtolyl','cresol','toluidine','anisidine','toluic acid','anisic acid','cymene']:#Type:-Both functional grps included in the parentchain
                if lbsubs[0]=='o' or lbsubs[0]=='ortho':
                    localdict.update(benzenoid_[benzchain])
                elif lbsubs[0]=='m' or lbsubs[0]=='meta':
                    localdict.update(benzenoid_[benzchain])
                    for k in localdict:
                        if localdict[k]==[2]:
                            localdict[k]=[3]
                        elif localdict[k]==[1,2]:
                            localdict[k]=[1,3]
                elif lbsubs[0]=='p' or lbsubs[0]=='para':
                    localdict.update(benzenoid_[benzchain])
                    for k in localdict:
                        if localdict[k]==[2]:
                            localdict[k]=[4]
                        elif localdict[k]==[1,2]:
                            localdict[k]=[1,4]
            if benzchain in ['benzamide','toluene','subphenyl','anisole','phenol','aniline','benzoic acid','benzaldehyde','benzonitrile','benzoylchloride','benzoylfluoride','benzoylbromide','benzoyliodide']:
                localdict.update(benzenoid_[benzchain])
                if lbsubs[0]=='o' or lbsubs[0]=='ortho':
                    localdict[lbsubs[1]]=[2]
                elif lbsubs[0]=='m' or lbsubs[0]=='meta':
                    localdict[lbsubs[1]]=[3]
                elif lbsubs[0]=='p' or lbsubs[0]=='para':
                    localdict[lbsubs[1]]=[4]
        elif benzchain in ['benzamide','toluene','subphenyl','anisole','phenol','aniline','benzoic acid','benzaldehyde','benzonitrile','benzoylchloride','benzoylfluoride','benzoylbromide','benzoyliodide'] and lbsubs[0][0].isnumeric():
            for k in benzenoid_[benzchain]:
                bsubs+='-'+str(benzenoid_[benzchain][k][0])+'-'+str(k)
            return bsubs
                    
        return localdict
    #______________________________________________________________#
    def subalkylfun(x):#For substituted alkyl grps
        global testvariable_subalkyl
        global p
        T.pu()
        p=dsubs[x][0]
        T.goto(loc[p])
        if p%2==0:
            T.seth(90)
            T.pd()
            T.fd(55)
            T.seth(140)
        else:
            T.seth(-90)
            T.pd()
            T.fd(55)
            T.seth(-50)
            
        
        x=x[1:len(x)-1]
        lsubalkyl=x.split('-')
        for k in rootwords:
            if k in x:
                i=x.find(k)
                possiblenames1.append(x[i::])
                a2=rootwords.index(k)+1
        length=[]        
        for k in possiblenames1:
            length.append(len(k))
        mchain=possiblenames1[length.index(min(length))]
        schain=x[:len(x)-len(mchain)]
        #---------Block for finding the substitutions----#
        if schain[-1]==' ' or schain[-1]=='-':
                schain=schain[:-1:]
        lsubs1=schain.split('-')
        for i in range(0,len(lsubs1)):
                if lsubs1[i].isalpha() and i==0:
                    dsubalkyl[lsubs1[i]]=[1]
                elif lsubs1[i].isalpha() and len(lsubs1[i-1])==1:
                    dsubalkyl[lsubs1[i]]=[int(lsubs1[i-1])]
                elif lsubs1[i].isalpha() and ',' in lsubs1[i-1]:
                    if 'di' in lsubs1[i]:
                        lsubs1[i]=lsubs1[i][2::]
                    elif 'tri' in lsubs1[i]:
                        lsubs1[i]=lsubs1[i][3::]
                    var=lsubs1[i-1].split(',')
                    var1=[]
                    for k in var:
                        var1.append(int(k))
                    dsubalkyl[lsubs1[i]]=var1
                elif lsubs1[i].isalpha() and lsubs1[i-1].isalpha():
                    dsubalkyl[lsubs[i]]=[1]
        testvariable_subalkyl=1
        strch(a2,[],[])
    #______________________________________________________________#

    def cyclowritesuff1(x):
        for k in x:
            if not usedloc and not testvariable_bicyc_spiro_:
                angle1=angle
            if k in cyclic_oxo_fun:
                for j in dfun1[k]:
                    T.pu()
                    T.goto(loc[j])
                    if j+1 in loc:
                        T.seth(T.towards(loc[j+1])-180-angle1/2)
                    else:
                        T.seth(T.towards(loc[1])-180-angle1/2)
                    T.pd()
                    if dfun1[k].count(j)==2 and j not in usedloc:
                        T.lt(40)
                    elif dfun1[k].count(j)==2 and j in usedloc:
                        T.rt(40)
                    T.fd(30)
                    T.pu()
                    T.goto(T.xcor()-5,T.ycor())
                    curdraw(cyclic_oxo_fun[k])
                    usedloc.append(j)
    #______________________________________________________________#
    def cyclowritesuff(x):
        for k in x:
            if not testvariable_bicyc_spiro_:
                angle1=angle
            if k in suff:
                for j in dfun[k]:
                    T.pu()
                    T.goto(loc[j])
                    if j+1 in loc:
                        T.seth(T.towards(loc[j+1])-180-angle1/2)
                    else:
                        T.seth(T.towards(loc[1])-180-angle1/2)
                    T.pd()
                    if dfun[k].count(j)==2 and j not in usedloc:
                        T.lt(40)
                    elif dfun[k].count(j)==2 and j in usedloc:
                        T.rt(40)
                    T.fd(30)
                    T.pu()
                    T.goto(T.xcor()-5,T.ycor())
                    curdraw(suff[k])
                    usedloc.append(j)
            elif k=='one':
                for j in x[k]:
                    T.pu()
                    T.goto(loc[j])
                    if j+1 in loc:
                        subangle=T.towards(loc[j+1])-180-angle1/2
                    else:
                        subangle=T.towards(loc[1])-180-angle1/2
                    ketocyclic(subangle,a)
    #______________________________________________________________#
    def cyclowritepref(x,locant=loc):
        global angle1
        for k in x:
            if not usedloc and not testvariable_bicyc_spiro_:
                angle1=angle
            elif testvariable_subst_phenyl:
                 angle1=angle
            if k in pref:
                for j in x[k]:
                    testvariable_bridgehead=0
                    T.pu()
                    T.goto(locant[j])
                    if testvariable_bicyc_spiro_ and 'bicyclo' in name:
                        b1,b2,b3=(int(list_[0]),int(list_[1]),int(list_[2]))
                        t1=(b1*180/(b1+2))
                        t2=(b2*180/(b2+2))
                        t3=(b3*180/(b3+2))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+3,b1+b2+3):
                            angle1=t2
                        elif j in range(b1+b2+3,b1+b2+b3+3):
                            angle1=t3
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=270+(t1-t2)/2
                        elif j==b1+2:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t2-t1)/2
                    elif testvariable_bicyc_spiro_ and 'spiro' in name:
                        b1,b2=(int(list_[0]),int(list_[1]))
                        t1=((b1-1)*180/(b1+1))
                        t2=((b2-1)*180/(b2+1))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+2,b1+b2+2):
                            angle2=t2
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t1-t2)/2   
                    if j+1 in locant and not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            T.seth(T.towards(locant[b1+2])-180-angle1/2)
                        elif 'spiro' in name and j==b1+1:
                            T.seth(T.towards(locant[1])-180-angle1/2)
                        else:   
                            T.seth(T.towards(locant[j+1])-180-angle1/2)
                    elif not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            T.seth(T.towards(locant[b1+2])-180-angle1/2)
                        else:   
                            T.seth(T.towards(locant[1])-180-angle1/2)
                    elif testvariable_bridgehead:
                        T.seth(angle1)
                    T.pd()
                    if tobeusedloc.count(j)==2 and j not in usedloc and locant!=locsub or tobeusedloc.count(j)==2 and j not in usedloc and testvariable_fused:
                        T.lt(40)
                    elif tobeusedloc.count(j)==2 and j in usedloc and locant!=locsub or tobeusedloc.count(j)==2 and j in usedloc and testvariable_fused:
                        T.rt(40)
                    T.fd(30)
                    curdraw(pref[k])
                    if locant!=locsub:
                        usedloc.append(j)
                    elif testvariable_fused:
                        usedloc.append(j)
            elif k=='oxo' or k=='keto':
                for j in x[k]:
                    T.pu()
                    T.goto(locant[j])
                    if j+1 in locant:
                        subangle=T.towards(locant[j+1])-180-angle1/2
                    else:
                        subangle=T.towards(locant[1])-180-angle1/2
                    ketocyclic(subangle,a)
            elif k in alkylsubs or k in alkoxysubs:
                for j in x[k]:
                    testvariable_bridgehead=0
                    T.pu()
                    T.goto(locant[j])
                    if testvariable_bicyc_spiro_ and 'bicyclo' in name:
                        b1,b2,b3=(int(list_[0]),int(list_[1]),int(list_[2]))
                        t1=(b1*180/(b1+2))
                        t2=(b2*180/(b2+2))
                        t3=(b3*180/(b3+2))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+3,b1+b2+3):
                            angle1=t2
                        elif j in range(b1+b2+3,b1+b2+b3+3):
                            angle1=t3
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=270+(t1-t2)/2
                        elif j==b1+2:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t2-t1)/2
                    elif testvariable_bicyc_spiro_ and 'spiro' in name:
                        b1,b2=(int(list_[0]),int(list_[1]))
                        t1=((b1-1)*180/(b1+1))
                        t2=((b2-1)*180/(b2+1))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+2,b1+b2+2):
                            angle2=t2
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t1-t2)/2   
                    if j+1 in locant and not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            subangle=T.towards(locant[b1+2])-180-angle1/2
                        elif 'spiro' in name and j==b1+1:
                            T.seth(T.towards(locant[1])-180-angle1/2)
                        else:
                            subangle=T.towards(locant[j+1])-180-angle1/2
                        T.seth(subangle)
                    elif not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            subangle=T.towards(locant[b1+2])-180-angle1/2
                        else:
                            subangle=T.towards(locant[1])-180-angle1/2
                        T.seth(subangle)
                    elif testvariable_bridgehead:
                        T.seth(angle1)
                        subangle=angle1
                    
                    T.pd()
                    if tobeusedloc.count(j)==2 and j not in usedloc and locant!=locsub:
                        T.lt(40)
                    elif tobeusedloc.count(j)==2 and j in usedloc and locant!=locsub:
                        T.rt(40)
                    T.fd(40)
                    if k in alkoxysubs:
                        curdraw(cycloalkoxysubs[k])
                    else:
                        a1=alkylsubs.index(k)+1
                        for i in range(a1-1):
                            if i%2==0:
                                T.rt(50)
                            elif i%2!=0:
                                T.lt(50)
                            T.fd(30)
                        if abs(subangle)<=90:
                            curdraw('CH\u2083')
                        else:
                            curdraw('H\u2083C')
                    if locant!=loc:
                        usedloc.append(j)
            elif k in cycloalkylsubs:
                for j in dsubs[k]:
                    testvariable_bridgehead=0
                    T.pu()
                    T.goto(locant[j])
                    if testvariable_bicyc_spiro_ and 'bicyclo' in name:
                        b1,b2,b3=(int(list_[0]),int(list_[1]),int(list_[2]))
                        t1=(b1*180/(b1+2))
                        t2=(b2*180/(b2+2))
                        t3=(b3*180/(b3+2))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+3,b1+b2+3):
                            angle1=t2
                        elif j in range(b1+b2+3,b1+b2+b3+3):
                            angle1=t3
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=270+(t1-t2)/2
                        elif j==b1+2:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t2-t1)/2
                    elif testvariable_bicyc_spiro_ and 'spiro' in name:
                        b1,b2=(int(list_[0]),int(list_[1]))
                        t1=((b1-1)*180/(b1+1))
                        t2=((b2-1)*180/(b2+1))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+2,b1+b2+2):
                            angle2=t2
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t1-t2)/2   
                    if j+1 in locant and not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            subangle=T.towards(locant[b1+2])-180-angle1/2
                        elif 'spiro' in name and j==b1+1:
                            T.seth(T.towards(locant[1])-180-angle1/2)
                        else:
                            subangle=T.towards(locant[j+1])-180-angle1/2
                        T.seth(subangle)
                    elif not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            subangle=T.towards(locant[b1+2])-180-angle1/2
                        else:
                            subangle=T.towards(locant[1])-180-angle1/2
                        T.seth(subangle)
                    elif testvariable_bridgehead:
                        T.seth(angle1)
                        subangle=angle1
                    T.pd()
                    if tobeusedloc.count(j)==2 and j not in usedloc and locant!=loc:
                        T.lt(40)
                    elif tobeusedloc.count(j)==2 and j in usedloc and locant!=loc:
                        T.rt(40)
                    T.fd(40)
                    a1=cycloalkylsubs.index(k)
                    ang=180*((a1-1)/(a1+1))
                    T.lt(ang/2)
                    for i in range(a1+1):
                        T.fd(50)
                        T.rt(180-ang)
                    usedloc.append(j)
            elif k in trivialsubs:
                for j in dsubs[k]:
                    testvariable_bridgehead=0
                    T.pu()
                    T.goto(locant[j])
                    if testvariable_bicyc_spiro_ and 'bicyclo' in name:
                        b1,b2,b3=(int(list_[0]),int(list_[1]),int(list_[2]))
                        t1=(b1*180/(b1+2))
                        t2=(b2*180/(b2+2))
                        t3=(b3*180/(b3+2))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+3,b1+b2+3):
                            angle1=t2
                        elif j in range(b1+b2+3,b1+b2+b3+3):
                            angle1=t3
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=270+(t1-t2)/2
                        elif j==b1+2:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t2-t1)/2
                    elif testvariable_bicyc_spiro_ and 'spiro' in name:
                        b1,b2=(int(list_[0]),int(list_[1]))
                        t1=((b1-1)*180/(b1+1))
                        t2=((b2-1)*180/(b2+1))
                        if j in range(2,b1+2):
                            angle1=t1
                        elif j in range(b1+2,b1+b2+2):
                            angle2=t2
                        elif j==1:#bridge head
                            testvariable_bridgehead=1
                            angle1=90+(t1-t2)/2   
                    if j+1 in locant and not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            subangle=T.towards(locant[b1+2])-180-angle1/2
                        elif 'spiro' in name and j==b1+1:
                            T.seth(T.towards(locant[1])-180-angle1/2)
                        else:
                            subangle=T.towards(locant[j+1])-180-angle1/2
                        T.seth(subangle)
                    elif not testvariable_bridgehead:
                        if testvariable_bicyc_spiro_ and j==b1+b2+3:
                            subangle=T.towards(locant[b1+2])-180-angle1/2
                        else:
                            subangle=T.towards(locant[1])-180-angle1/2
                        T.seth(subangle)
                    elif testvariable_bridgehead:
                        T.seth(angle1)
                        subangle=angle1
                    T.pd()
                    if tobeusedloc.count(j)==2 and j not in usedloc and locant!=loc:
                        T.lt(40)
                    elif tobeusedloc.count(j)==2 and j in usedloc and locant!=loc:
                        T.rt(40)
                        T.fd(40)
                    T.fd(40)
                    if k=='phenyl':
                        cyc(6,[1,3,5],[],mov=False,dummy=j)
                    elif k=='isopropyl':
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    elif k=='isobutyl':
                        T.lt(40)
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    elif k=='tert-butyl':
                        T.lt(90)
                        T.fd(40)
                        T.pu()
                        T.bk(80)
                        T.pd()
                        T.fd(40)
                        T.rt(90)
                        T.fd(40)
                    elif k=='sec-butyl':
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.rt(80)
                        T.pd()
                        T.fd(40)
                        T.rt(100)
                        T.fd(40)
                    elif k=='acetyl':
                        ####Wait For Sai#####
                        pass
                    elif k=='isopentyl':
                        T.lt(40)
                        T.fd(40)
                        T.rt(40)
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    if locant!=loc:
                        usedloc.append(j)
            elif k=='epoxy':
                drawepoxy(dsubs['epoxy'])
                
    #______________________________________________________________#                        
    def writesuff1(x):
        for k in x:
            for j in x[k]:
                if k in coohderv_suff:
                    T.pu()
                    T.goto(loc[j])
                    if j%2==0:
                        keto(1)
                    else:
                        keto(-1)
                    if k=='one' and len(x[k])==1:
                        break
                    else:
                        T.pu()
                        T.goto(loc[j])
                        if j==1:
                            T.seth(130)
                        elif j%2==0:
                            T.seth(-50)
                        else:
                            T.seth(50)
                        T.pd()
                        if not testvariable_ester:
                            T.fd(30)
                        else:
                            T.fd(40)
                        if k=='oic acid' and j==1:
                            T.pu()
                            T.goto(T.xcor()-50,T.ycor())
                            curdraw('HO')
                        elif k=='oic acid' and j==a and not testvariable_ester:
                            curdraw('OH')
                        elif k=='oic acid' and j==a and testvariable_ester:
                            curdraw('O')
                        elif k=='oic acid' and testvariable_ester and a=='benzoate':
                            curdraw('O')
                        elif k=='oyl chloride':
                            curdraw1('Cl')
                        elif k=='oyl fluoride':
                            curdraw1('F')
                        elif k=='oyl bromide':
                            curdraw1('Br')
                        elif k=='oyl iodide':
                            curdraw1('I')
                        elif k=='al':
                            if j==1:
                                T.pu()
                                T.goto(T.xcor()-35,T.ycor())
                            curdraw('H')
                        elif k=='amide' and j==1:
                            T.pu()
                            if not N_subs:
                                T.goto(T.xcor()-65,T.ycor()+5)
                                curdraw('H\u2082N')
                            else:
                                T.goto(T.xcor()-20,T.ycor())
                                draw_N_subs(N_subs,'amide','left')      
                        elif k=='amide' and j==a:
                            if not N_subs:
                                curdraw('NH\u2082')
                            else:
                                draw_N_subs(N_subs,'amide','right')   
                        if a==1 and not testvariable_ester and not testvariable_ketone:
                            T.goto(loc[1])
                            T.seth(50)
                            T.pd()
                            T.fd(30)
                            T.pu()
                            T.goto(T.xcor()+5,T.ycor()-6)
                            curdraw('H')


    #______________________________________________________________#                    
    def writesuff(x):
        for k in x:
            if k in suff:
                for j in dfun[k]:
                    T.pu()
                    T.goto(loc[j])
                    T.pd()
                    if testvariable_sulpho_1:
                        drawsulphonic(1)
                    else:
                        if k not in ['nitrile','isonitrile'] and j%2==0 and j not in usedloc or k not in ['nitrile','isonitrile'] and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                            T.seth(90)
                            T.fd(30)
                            if k=='sulphonicacid':
                                drawsulphonic(1)
                        elif k not in ['nitrile','isonitrile'] and j%2!= 0 and j not in usedloc or k not in ['nitrile','isonitrile'] and j%2==0 and j in usedloc and usedloc.count(j)<2:
                            T.seth(-90)
                            T.fd(30)
                            if k=='sulphonicacid':
                                drawsulphonic(-1)
                            else:
                                T.pu()
                                T.fd(30)
                            
                        elif j==1 and usedloc.count(j)==2:
                            T.seth(180)
                            T.fd(30)
                            T.pu()
                            T.fd(20)
                            T.goto(T.xcor(),T.ycor()-10)
                            if k=='sulphonicacid':
                                drawsulphonic(0)
                        T.pu()
                        if k not in ['nitrile','isonitrile','sulphonicacid']:
                            T.goto(T.xcor()-5,T.ycor())
                            if not N_subs:
                                T.write(suff[k],font=('Arial',18,"normal"))
                            else:
                                if T.heading()==90:
                                    draw_N_subs(N_subs,'amine','top')
                                elif T.heading()==180:
                                    draw_N_subs(N_subs,'amine','left')
                                elif T.heading()==0:
                                    draw_N_subs(N_subs,'amine','right')
                                elif T.heading()==270:
                                    draw_N_subs(N_subs,'amine','bottom')
                        elif j==1 and k!='sulphonicacid':
                            if not N_subs:
                                T.goto(T.xcor()-30,T.ycor()-20)
                                T.write(suff[k][::-1],font=('Arial',18,"normal"))
                            else:
                                if T.heading()==90:
                                    draw_N_subs(N_subs,'amine','top')
                                elif T.heading()==180:
                                    draw_N_subs(N_subs,'amine','left')
                                elif T.heading()==0:
                                    draw_N_subs(N_subs,'amine','right')
                                elif T.heading()==270:
                                    draw_N_subs(N_subs,'amine','bottom')    
                        elif j%2!=0 and k!='sulphonicacid':
                            T.goto(T.xcor()+3,T.ycor()-22)
                            if not N_subs:
                                T.write(suff[k],font=('Arial',18,"normal"))
                            else:
                                if T.heading()==90:
                                    draw_N_subs(N_subs,'amine','top')
                                elif T.heading()==180:
                                    draw_N_subs(N_subs,'amine','left')
                                elif T.heading()==0:
                                    draw_N_subs(N_subs,'amine','right')
                                elif T.heading()==270:
                                    draw_N_subs(N_subs,'amine','bottom')
                        elif j%2==0 and k!='sulphonicacid':
                            T.goto(T.xcor(),T.ycor()-5)
                            if not N_subs:
                                T.write(suff[k],font=('Arial',18,"normal"))
                            else:
                                if T.heading()==90:
                                    draw_N_subs(N_subs,'amine','top')
                                elif T.heading()==180:
                                    draw_N_subs(N_subs,'amine','left')
                                elif T.heading()==0:
                                    draw_N_subs(N_subs,'amine','right')
                                elif T.heading()==270:
                                    draw_N_subs(N_subs,'amine','bottom')
                    usedloc.append(j)
    #______________________________________________________________#
    def curdraw1(x):#Call this function to draw oxo substitution in a cyclic ring
        h=T.heading()
        T.pu()
        if h==0:
            T.goto(T.xcor()+10,T.ycor()-20)
        elif h>0 and h<30:
            T.goto(T.xcor(),T.ycor()-10)
        elif h==30:
            T.goto(T.xcor()+2,T.ycor()-13)
        elif h<60 and h>30:
            T.goto(T.xcor(),T.ycor()-10)
        elif h==60:
            T.goto(T.xcor(),T.ycor()-10)
        elif h>60 and h<90:
            T.goto(T.xcor(),T.ycor()-7)
        elif h==90:
            T.goto(T.xcor()-5,T.ycor()-5)
        elif h>90 and h<120:
            T.goto(T.xcor()-8,T.ycor()-5)
        elif h==120:
            T.goto(T.xcor()-7,T.ycor()-5)
        elif h>120 and h<150:
            T.goto(T.xcor()-10,T.ycor()-8)
        elif h==150:
            T.goto(T.xcor()-14,T.ycor()-6)
        elif h<180 and h>150:
            T.goto(T.xcor(),T.ycor())
        elif h<210 and h>180:
            T.goto(T.xcor()-15,T.ycor()-10)
        elif h==210:
            T.goto(T.xcor()-20,T.ycor()-15)
        elif h>210 and h<240:
            T.goto(T.xcor()-10,T.ycor()-10)
        elif h==240:
            T.goto(T.xcor()-15,T.ycor()-20)
        elif h>240 and h<270:
           T.goto(T.xcor()-13,T.ycor()-20) 
        elif h==270:
            T.goto(T.xcor()-12,T.ycor()-25)
        elif h<300 and h>270:
            T.goto(T.xcor()-10,T.ycor()-25)
        elif h==300:
            T.goto(T.xcor()-8,T.ycor()-25)
        elif h>300 and h<330:
            T.goto(T.xcor()-8,T.ycor()-23)
        elif h==330:
            T.goto(T.xcor()-6,T.ycor()-22)
        elif h>330 and h<360:
            T.goto(T.xcor()-4,T.ycor()-22) 
        elif h==180:
            T.goto(T.xcor()-18,T.ycor()-12)
        T.write(x,font=('Arial',18,"normal"))

    #_____________________________________________________________#    
    def ketocyclic(h,n):
        T.seth(h)
        x=T.xcor()
        y=T.ycor()
        T.lt(90+180/n)
        T.pu()
        T.fd(4)
        T.rt(90+180/n)
        T.pd()
        T.fd(50)
        curdraw1('O')
        T.pu()
        T.goto(x,y)
        T.rt(90+180/n)
        T.fd(4)
        T.lt(90+180/n)
        T.pd()
        T.fd(50)
        T.pu()
        T.goto(x,y)
        T.pd()
    #_______________________________________________________________________#
    def curdraw(x):#Call this function to draw a substitution in a cyclic ring
        h=T.heading()
        T.pu()
        if h==0:
            T.goto(T.xcor()+10,T.ycor()-10)
        elif h>0 and h<30:
            T.goto(T.xcor()+3,T.ycor()-7)
        elif h==30:
            T.goto(T.xcor()+5,T.ycor()-8)
        elif h<60 and h>30:
            T.goto(T.xcor()+3,T.ycor()-7)
        elif h==60:
            T.goto(T.xcor()+3,T.ycor()-7)
        elif h>60 and h<90:
            T.goto(T.xcor(),T.ycor()-7)
        elif h==90:
            T.goto(T.xcor()-10,T.ycor())
        elif h>90 and h<120:
            T.goto(T.xcor()--11,T.ycor()+3)
        elif h==120:
            T.goto(T.xcor()-10,T.ycor()-2)
        elif h>120 and h<150:
            T.goto(T.xcor()--13,T.ycor()-9)
        elif h==150:
            T.goto(T.xcor()-17,T.ycor()-9)
        elif h<180 and h>150:
            T.goto(T.xcor()-3,T.ycor()-3)
        elif h<210 and h>180:
            T.goto(T.xcor()-18,T.ycor()-13)
        elif h==210:
            T.goto(T.xcor()-23,T.ycor()-18)
        elif h>210 and h<240:
            T.goto(T.xcor()-13,T.ycor()-13)
        elif h==240:
            T.goto(T.xcor()-18,T.ycor()-23)
        elif h>240 and h<270:
           T.goto(T.xcor()-16,T.ycor()-23) 
        elif h==270:
            T.goto(T.xcor()-5,T.ycor()-25)
        elif h<300 and h>270:
            T.goto(T.xcor()-7,T.ycor()-28)
        elif h==300:
            T.goto(T.xcor()-5,T.ycor()-28)
        elif h>300 and h<330:
            T.goto(T.xcor()-5,T.ycor()-26)
        elif h==330:
            T.goto(T.xcor()-3,T.ycor()-25)
        elif h>330 and h<360:
            T.goto(T.xcor()+4,T.ycor()-25) 
        elif h==180:
            T.goto(T.xcor()-20,T.ycor()-10)
        T.write(x,font=('Arial',18,"normal"))    

    #______________________________________________________________#    

    def writepref(x):
        global testvariable_subalkyl
        for k in x:
            if k in pref:
                for j in x[k]:
                    T.pu()
                    T.goto(loc[j])
                    T.pd()
                    if not testvariable_1_one_1 and (j%2==0 and j not in usedloc) or not testvariable_1_one_1 and (j%2!=0 and j in usedloc and usedloc.count(j)<2) :
                        T.seth(90)
                        T.fd(30)
                        if k=='sulpho':
                            drawsulphonic(1)
                    elif not testvariable_1_one_1 and (j%2!= 0 and j not in usedloc) or not testvariable_1_one_1 and (j%2==0 and j in usedloc and usedloc.count(j)<2):
                        T.seth(-90)
                        T.fd(30)
                        if k=='sulpho':
                            drawsulphonic(1)
                        else:
                            T.pu()
                            T.fd(30)
                    elif not testvariable_1_one_1 and j==1 and usedloc.count(j)==2:
                        T.seth(180)
                        T.fd(30)
                        T.pu()
                        T.fd(20)
                        T.goto(T.xcor()-10,T.ycor()-10)
                    elif not testvariable_1_one_1 and j==a and usedloc.count(j)==2:
                        T.seth(0)
                        T.fd(30)
                        T.pu()
                        T.goto(T.xcor()+10,T.ycor()-15)
                    if testvariable_1_one_1 and usedloc.count(j)==0 and j==1:
                        T.seth(130)
                        T.fd(40)
                        curdraw1(pref[k])
                    elif testvariable_1_one_1 and usedloc.count(j)==1 and j==1:
                        T.seth(50)
                        T.fd(40)
                        curdraw(pref[k])
                    elif testvariable_1_one_1 and not testvariable_ester and j%2==0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                        T.seth(90)
                        T.fd(40)
                        curdraw(pref[k])
                    elif (testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j not in usedloc) or (testvariable_1_one_1 and not testvariable_ester and j%2==0 and j in usedloc and usedloc.count(j)<2):
                        T.seth(-90)
                        T.fd(40)
                        curdraw(pref[k])
                    T.pu()
                    T.goto(T.xcor()-5,T.ycor())
                    if not testvariable_1_one_1 and usedloc.count(j)==2 and j==1 and pref[k][-1].isupper() and k!='sulpho':
                        T.write(pref[k][::-1],font=('Arial',18,"normal"))
                    elif not testvariable_1_one_1 and k!='sulpho':
                        T.write(pref[k],font=('Arial',18,"normal"))
                        
                    usedloc.append(j)
            elif k in coohderv_pref:
                for j in dsubs[k]:
                    T.pu()
                    T.goto(loc[j])
                    if j%2==0:
                        keto(1)
                    else:
                        keto(-1)
                    if k=='aldo' and j==1:
                        T.pu()
                        T.goto(loc[j])
                        T.seth(130)
                        T.pd()
                        T.fd(30)
                        curdraw('H')
                        usedloc.append(j)
                    elif k=='aldo' and j==a:
                        T.pu()
                        T.goto(loc[j])
                        if a%2==0:
                            T.seth(-50)
                        else:
                            T.seth(50)
                        T.pd()
                        T.fd(30)
                        curdraw('H')
            elif k in alkylsubs or k in alkoxysubs:
                testvariable_oxy=0
                for j in x[k]:
                    T.pu()
                    if not testvariable_subalkyl:
                        T.goto(loc[j])
                    else:
                        T.goto(locsubal[j])

                    T.pd()
                    if j==1 and 1 not in usedloc and not testvariable_oxy and k in alkoxysubs:
                        testvariable_oxy=1
                        T.seth(130)
                        T.fd(65)
                        T.pu()
                        T.goto(T.xcor()-17,T.ycor()-10)
                        T.write('O',font=('Arial',18,"normal"))
                        T.goto(T.xcor()-2,T.ycor()+10)
                        T.lt(100)
                        T.pd()
                        T.fd(65)
                    elif j==a and a not in usedloc and not testvariable_oxy and k in alkoxysubs:
                        testvariable_oxy=1
                        if a%2==0:
                            T.seth(-50)
                            T.fd(65)
                            T.pu()
                            T.goto(T.xcor()+2,T.ycor()-20)
                        elif a%2!=0:
                            T.seth(50)
                            T.fd(65)
                            T.pu()
                            T.goto(T.xcor()+2,T.ycor()-10)
                        T.write('O',font=('Arial',18,"normal"))
                        if a%2!=0:
                            T.goto(T.xcor()+18,T.ycor()+10)
                        elif a%2==0:
                            T.goto(T.xcor()+22,T.ycor()+15)
                        T.pd()
                        if a%2==0:
                            T.lt(100)
                        elif a%2!=0:
                            T.rt(100)
                        T.fd(65)
                             
                             
                    elif not testvariable_1_one_1 and j%2==0 and j not in usedloc and not testvariable_subalkyl or not testvariable_1_one_1 and j%2!=0 and j in usedloc and not testvariable_subalkyl:                        
                        T.seth(90)
                        T.fd(55)
                        testvariable_oxy=0
                    elif not testvariable_1_one_1 and j%2==0 and j not in usedloc1 and testvariable_subalkyl or not testvariable_1_one_1 and j%2!=0 and j in usedloc1 and testvariable_subalkyl:
                        if p%2!=0:
                            T.seth(0)
                            T.fd(55)
                        else:                        
                            T.seth(180)
                            T.fd(55)
                    elif not testvariable_1_one_1 and j%2!= 0 and j not in usedloc and not testvariable_subalkyl or not testvariable_1_one_1 and j%2==0 and j in usedloc and not testvariable_subalkyl:
                        T.seth(-90)
                        T.fd(55)
                        testvariable_oxy=0
                    elif not testvariable_1_one_1 and j%2!= 0 and j not in usedloc1 and testvariable_subalkyl or not testvariable_1_one_1 and j%2==0 and j in usedloc1 and testvariable_subalkyl:
                        if p%2!=0:
                            T.seth(180)
                            T.fd(55)
                        else:                        
                            T.seth(0)
                            T.fd(55)

                    if k in alkoxysubs and T.heading()==90:
                        T.pu()
                        T.bk(5)
                        T.goto(T.xcor()-8,T.ycor())
                        T.write('O',font=('Arial',18,"normal"))
                        T.fd(25)
                        T.goto(T.xcor()+15,T.ycor()-2)
                        T.rt(40)
                        T.pd()
                        T.fd(55)
                    elif k in alkoxysubs and T.heading()==270:
                        T.pu()
                        T.fd(25)
                        T.goto(T.xcor()-8,T.ycor())
                        T.write('O',font=('Arial',18,"normal"))
                        T.goto(T.xcor(),T.ycor()+5)
                        T.rt(40)
                        T.pd()
                        T.fd(55)
                    elif k in alkoxysubs and T.heading()==180:
                        T.pu()
                        T.fd(20)
                        T.goto(T.xcor(),T.ycor()-15)
                        T.write('O',font=('Arial',18,"normal"))
                        T.goto(T.xcor(),T.ycor()+15)
                        T.rt(40)
                        T.pd()
                        T.fd(55)
                    if k in alkoxysubs and k!='phenoxy':         
                        a1=alkoxysubs.index(k)
                    elif k in alkylsubs:
                        a1=alkylsubs.index(k)
                    if testvariable_1_one_1 and usedloc.count(j)==0 and j==1:
                        T.seth(130)
                        T.fd(45)
                    elif testvariable_1_one_1 and usedloc.count(j)==1 and j==1:
                        T.seth(50)
                        T.fd(45)
                    elif testvariable_1_one_1 and not testvariable_ester and j%2==0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                        T.seth(90)
                        T.fd(45)
                    elif testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2==0 and j in usedloc and usedloc.count(j)<2 :
                        T.seth(-90)
                        T.fd(45)
                    if not testvariable_1_one_1 and k!='phenoxy' and not testvariable_oxy:
                        for i in range(a1):
                            if i%2==0:
                                T.rt(50)
                            elif i%2!=0:
                                T.lt(50)
                            T.fd(45)
                    elif testvariable_oxy and k!='phenoxy':
                        for i in range(a1):
                            if i%2==0:
                                T.rt(100)
                            elif i%2!=0:
                                T.lt(100)
                            T.fd(65)
                        
                    elif k=='phenoxy':
                        cyc(6,[1,3,5],[],mov=False,dummy=j)
                    elif testvariable_1_one_1 and usedloc.count(j)==0:
                        for i in range(a1):
                            if i%2==0:
                                T.lt(100)
                            elif i%2!=0:
                                T.rt(100)
                            T.fd(45)
                    elif testvariable_1_one_1 and usedloc.count(j)==1:
                        for i in range(a1):
                            if i%2==0:
                                T.rt(100)
                            elif i%2!=0:
                                T.lt(100)
                            T.fd(45)
                        
                    if j%2==0 and not testvariable_subalkyl and not testvariable_1_one_1 and k!='phenoxy' and not testvariable_oxy:
                        curdraw('CH\u2083')
                    elif not testvariable_subalkyl and not testvariable_1_one_1 and k!='phenoxy' and not testvariable_oxy:
                        curdraw('H\u2083C')
                    if not testvariable_oxy and not testvariable_subalkyl :
                        usedloc.append(j)
                    elif testvariable_subalkyl:
                        usedloc1.append(j)
            elif k in cycloalkylsubs:
                for j in x[k]:
                    T.pu()
                    T.goto(loc[j])
                    T.pd()
                    if not testvariable_1_one_1 and not testvariable_ester and j%2==0 and j not in usedloc or not testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                        T.seth(90)
                        T.fd(30)   
                    elif not testvariable_1_one_1 and not testvariable_ester and j%2!= 0 and j not in usedloc or not testvariable_1_one_1 and not testvariable_ester and j%2==0 and j in usedloc and usedloc.count(j)<2:
                        T.seth(-90)
                        T.fd(30)
                    elif not testvariable_1_one_1 and not testvariable_ester and j==1 and usedloc.count(j)==2:
                        T.seth(180)
                        T.fd(30)
                    if testvariable_1_one_1 and usedloc.count(j)==0 and j==1:
                        T.seth(130)
                        T.fd(40)
                    elif testvariable_1_one_1 and usedloc.count(j)==1 and j==1:
                        T.seth(50)
                        T.fd(40)
                    elif testvariable_1_one_1 and not testvariable_ester and j%2==0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                        T.seth(90)
                        T.fd(40)
                    elif testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2==0 and j in usedloc and usedloc.count(j)<2 :
                        T.seth(-90)
                        T.fd(40)
                    a1=cycloalkylsubs.index(k)
                    ang=180*((a1-1)/(a1+1))
                    T.lt(ang/2)
                    for i in range(a1+1):
                        T.fd(50)
                        T.rt(180-ang)
                    usedloc.append(j)
            elif k in trivialsubs:
                for j in x[k]:
                    T.pu()
                    try:
                        T.goto(loc[j])
                        if testvariable_ester:
                            T.bk(40)
                        T.pd()
                        if not testvariable_1_one_1 and not testvariable_ester and j%2==0 and j not in usedloc or not testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                            T.seth(90)   
                        elif not testvariable_1_one_1 and not testvariable_ester and j%2!= 0 and j not in usedloc or not testvariable_1_one_1 and not testvariable_ester and j%2==0 and j in usedloc and usedloc.count(j)<2:
                            T.seth(-90)
                        if testvariable_1_one_1 and usedloc.count(j)==0 and j==1:
                            T.seth(130)
                        elif testvariable_1_one_1 and usedloc.count(j)==1 and j==1:
                            T.seth(50)
                        elif testvariable_1_one_1 and not testvariable_ester and j%2==0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j in usedloc and usedloc.count(j)<2 :
                            T.seth(90)
                        elif testvariable_1_one_1 and not testvariable_ester and j%2!=0 and j not in usedloc or testvariable_1_one_1 and not testvariable_ester and j%2==0 and j in usedloc and usedloc.count(j)<2 :
                            T.seth(-90)
                    except:
                        T.goto(0,0)
                        T.seth(180)
                        T.pd()
                    if k=='phenyl':
                        T.fd(40)
                        cyc(6,[1,3,5],[],mov=False,dummy=j)
                    elif k=='isopropyl':
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    elif k=='isobutyl':
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    elif k=='tert-butyl' or k=='t-butyl':
                        T.fd(40)
                        T.lt(90)
                        T.fd(40)
                        T.pu()
                        T.bk(80)
                        T.pd()
                        T.fd(40)
                        T.rt(90)
                        T.fd(40)
                    elif k=='neopentyl':
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.lt(90)
                        T.fd(40)
                        T.pu()
                        T.bk(80)
                        T.pd()
                        T.fd(40)
                        T.rt(90)
                        T.fd(40)
                    elif k=='isopentyl':
                        T.lt(40)
                        T.fd(40)
                        T.rt(40)
                        T.fd(40)
                        T.lt(40)
                        T.fd(40)
                        T.pu()
                        T.bk(40)
                        T.pd()
                        T.rt(80)
                        T.fd(40)
                    usedloc.append(j)
            elif '(' in k and ')' in k:
                subalkylfun(k)
            elif k=='epoxy':
                drawepoxy(dsubs['epoxy'])
            elif k in hetero_acyclic:
                T.pu()
                T.goto(loc[dsubs[k][0]])
                if k=='heteroNN':
                    mvp('N',T.pos())
                elif k=='heteroOO':
                    mvp('O',T.pos())
                elif k=='heteroSS':
                    mvp('S',T.pos())
                
                
    #______________________________________________________________#                                
    def keto(a=1):#give 1 for odd locant -1 for even locant. Caution!:draws c=o wherever the posn of turtle is,in up down orientation
        if a==1:
            T.seth(90)
            T.pu()
            T.fd(50)
            T.pu()
            T.goto(T.xcor()-8,T.ycor()-3)
            T.bk(5)
            T.write('O',font=('Arial',18,"normal"))
            T.fd(5)
            T.goto(T.xcor()+13,T.ycor())
            T.pd()
            T.fd(-50)
            T.pu()
            T.goto(T.xcor()-10,T.ycor())
            T.pd()
            T.fd(50)
        elif a==-1:
            T.seth(-90)
            T.pu()
            T.fd(70)
            T.goto(T.xcor()-8,T.ycor())
            T.write('O',font=('Arial',18,"normal"))
            T.goto(T.xcor()+3,T.ycor()+25)
            T.pd()
            T.bk(50)
            T.pu()
            T.goto(T.xcor()+10,T.ycor())
            T.pd()
            T.fd(50)

    #______________________________________________________________#    

    def tbc(z,mov):#Triple Bond for cyclic compounds
        for k in z:
            T.seth(0)
            T.pu()
            if mov:
                T.goto(loc[k])
                theta=T.towards(loc[k+1])
            else:
                T.goto(locsub[k])
                theta=T.towards(locsub[k+1])
            T.seth(theta)
            T.rt(angle/2)
            T.fd(5)
            T.seth(theta)
            T.pd()
            if not mov:
                T.fd(35-5*cos(((math.pi)/180)*angle/2))
            else:
                T.fd(60-5*cos(((math.pi)/180)*angle/2))
            T.pu()
            if mov:
                T.goto(loc[k])
            else:
                T.goto(locsub[k])
            T.seth(theta)
            T.lt(angle/2)
            T.fd(5)
            T.seth(theta)
            T.pd()
            if not mov:
                T.fd(45-5*cos(((math.pi)/180)*angle/2))
            else:
                T.fd(60-5*cos(((math.pi)/180)*angle/2))
    #______________________________________________________________#

    def dbc(y,mov):#Double Bond for cyclic compounds
        for k in y:
            T.seth(0)
            T.pu()
            if mov and not testvariable_fused:
                T.goto(loc[k])
                if k+1 in loc :
                    theta=T.towards(loc[k+1])
                else:
                    theta=T.towards(loc[1])
                    
            elif not testvariable_fused:
                T.goto(locsub[k])
                if k+1 in locsub:
                    theta=T.towards(locsub[k+1])
                else:
                    theta=T.towards(locsub[1])
            elif testvariable_fused:
                T.goto(list_of_locants[ring_no][k])
                if k+1 in list_of_locants[ring_no]:
                    theta=T.towards(list_of_locants[ring_no][k+1])
                else:
                    theta=T.towards(list_of_locants[ring_no][1])
            T.seth(theta)
            T.rt(angle/2)
            T.fd(5)
            T.seth(theta)
            T.pd()
            if not mov and pchain!='cyclohex-1,3,5-ene' and not testvariable_fused:
                T.fd(45-5*cos(((math.pi)/180)*angle/2))
            else:
                T.fd(60-5*cos(((math.pi)/180)*angle/2))
    #______________________________________________________________#

    def dbs(y):#Double Bond for straight chain
        for k in y:
            T.pu()
            T.goto(loc[k])
            if k%2!=0:           
                T.seth(140)
                T.fd(5)
                T.seth(50)
            else:
                T.seth(50)
                T.fd(5)
                T.rt(100)
            T.pd()
            T.fd(65)
    #______________________________________________________________#        

    def tbs(z):#Triple Bond for straight chain
        for k in z:
            T.pu()
            T.goto(loc[k])
            if k%2!=0:
                T.seth(140)
                T.fd(5)
                T.seth(50)
                T.pd()
                T.fd(65)
                T.pu()
                T.goto(loc[k])
                T.seth(140-180)
                T.fd(5)
                T.seth(50)
            else:
                T.seth(50)
                T.fd(5)
                T.rt(100)
                T.pd()
                T.fd(65)
                T.pu()
                T.goto(loc[k])
                T.seth(230)
                T.fd(5)
                T.seth(-50)
            T.pd()
            T.fd(60)
    #______________________________________________________________#

    def strch(x,y,z):#To draw the parent chain(acyclic)
        global testvariable_subalkyl
        if not testvariable_subalkyl:
            T.seth(50)
        for i in range(x):
            if not testvariable_subalkyl:
                loc[i+1]=T.pos()
            else:
                locsubal[i+1]=T.pos()
            if i<x-1:
                if testvariable_long:
                    T.fd(105)
                else:
                    T.fd(65)
                if i%2==0:
                    T.rt(100)
                else:
                    T.lt(100)
        dbs(y)
        tbs(z)
        if testvariable_subalkyl:
            writepref(dsubalkyl)    
        else:
            writepref(dsubs)
            writesuff(dfun)
            writesuff1(dfun1)
    #_________________________________________________________________________#        

    def cyc(x,y,z,dsubs={},dfun={},mov=True,hetero_={},dummy=0):#To draw the parent chain(cyclic)
        global angle
        global a
        global list_of_locants
        temp_dict=dict()
        angle=(x-2)/x*180
        if mov:
            T.pu()
            T.goto(-50,50)
            T.pd()
            T.seth(-1*(90-angle/2))
        elif not testvariable_fused:
            T.lt(angle/2)
        elif testvariable_fused:
            T.rt(180-(x-2)/x*180)
            a=x
        for i in range(x):
            if mov and not testvariable_fused:
                loc[i+1]=T.pos()     
            elif not testvariable_fused:
                locsub[i+1]=T.pos()
            elif testvariable_fused:
                temp_dict[i+1]=T.pos()             
            if not mov and pchain!='cyclohex-1,3,5-ene' and not testvariable_fused:
                T.fd(50)
            else:
                T.fd(65)
            T.rt(180-(x-2)/x*180)
        if testvariable_fused:
            list_of_locants.append(temp_dict)
        dbc(y,mov)
        tbc(z,mov)
        if not testvariable_fused:
            cyclowritepref(dsubs)
        else:
            cyclowritepref(dsubs,list_of_locants[ring_no])
        cyclowritesuff(dfun)
        cyclowritesuff1(dfun1)
        for atom in hetero_:
            for posn in hetero_[atom]:
                T.pu()
                if not testvariable_fused:
                    T.goto(loc[posn])
                else:
                    T.goto(list_of_locants[ring_no][posn])
                mvp(atom,T.pos())
        if d_subst and mov==False:
            for card in d_subst:
                if card==dummy:
                    sphen=d_subst[card]
                    if 'phenyl' in sphen:
                        subst001=fbenz(sphen[1:-7],'subphenyl')
                    elif 'phenoxyl' in sphen:
                        subst001=fbenz(sphen[1:-9],'subphenyl')
                    elif 'tolyl' in sphen:
                        subst001=fbenz(sphen[1:-6],'subtolyl')
                    if isinstance(subst001,dict):
                        cyclowritepref(subst001,locsub)
    #_______________________________________________________________________________Analysis of compound name_______________________________________________________________________#


    #______________Altering of name________________#
    name=Name
    name=name.strip()
    if name in ['DDT']:
        testvariable_long=1

    #_________________________SQL Connexions_________________________#
    if mode=='draw':
        mycon=mc.connect(host='localhost',user='root',password='AXAdb1700Dilbeek',database='pythonproject')
        cursor=mycon.cursor()
        cursor.execute("select iupac from ref_table where common='{}'".format(name))

        data=cursor.fetchall()
        if data:
            name=data[0][0]
            testvariable_commname=1
    ##_________________Test for special names_________________________##
    for k in special_names:
        if k==name:
            testvariable_special_=1
            drawspecial(name)
    ##__________________Tinkering for Benzoyl Halides____________________##
    if 'benzoyl ' in name:
        name=name[:name.find('benzoyl')+7]+name[name.find('benzoyl')+8:]

    ##_____Alterations for vic-dihalides and gem halides(common notations)______##
    if 'idene chloride' in name or 'idene fluoride' in name or 'idene bromide' in name or 'idene iodide' in name:
        sub99=name[name.find('idene ')+6:]
        sub99=othersuff_ref[sub99]
        name='1,1-di'+sub99+'-'+name[:name.find('idene ')-2]+'ane'
    elif 'ene dichloride' in name or 'ene difluoride' in name or 'ene dibromide' in name or 'ene diiodide' in name:
        sub99=name[name.find('ene di')+6:]
        sub99=othersuff_ref[sub99]
        name='1,2-di'+sub99+'-'+name[:name.find('ene ')-1]+'ane'       
    ##___________________Test for presence of substituents________________##
    for k in list_of_substituents:
        if k in name:
            testvariable_pres_subs=1
    ##__________________Test for sulphonic acid____________________##
    if 'sulphonic acid' in name:
        testvariable_sulpho=1
        name=name.replace('sulphonic acid','sulphonicacid')

    ##_________________Test for fused rings________________________##
    if 'fused_ring' in name:
        testvariable_fused=1
        name1=name[11:]
        t=eval(name1)
        drawfused(t)
        
    ##___________________Test for heteroatoms______________________________##
    if 'heteroatom' in name:
        testvariable_hetero=1
        name1=name[11:]
        t=eval(name1)
        a,b,c,heteroloc,dsubs=t
        cyc(a,b,c,hetero_=heteroloc,dsubs=dsubs)


    ##____________________Test for ketones(non-iupac)______________________##
    if 'ketone' in name:
        testvariable_ketone=1
        lk=name.split()
        lk.remove('ketone')
        try:#will be error free for dialkyl ketone and alkyl alkyl ketone
            if lk[0].startswith('di'):
                c1=rootwords.index(lk[0][2:len(lk[0])-2])+1
                c2=c1
            elif len(lk)==2:
                c1=rootwords.index(lk[0][:-2])+1
                c2=rootwords.index(lk[1][:-2])+1 
            a=c1+c2+1
            dsubs={'keto':[c1+1]}
            strch(a,[],[])
        except:#for cycloalkyl trivialsubs type ketone
            a=1
            if lk[0].startswith('di'):
                lk[0]=lk[0][2:]
                lk.append(lk[0])
                dsubs={lk[0]:[1,1]}
            else:
                dsubs={lk[0]:[1],lk[1]:[1]}
            dfun1={'one':[1]}
            testvariable_spl_ketone=1
            testvariable_1_one_1=1
            strch(a,[],[])        
    ##____________________Test for ethers(non-iupac)______________________##
    if 'ether' in name:
        testvariable_ether=1
        le=name.split()
        le.remove('ether')
        if le[0] in alkylsubs and le[1] in alkylsubs:
            if le[0].startswith('di'):
                le[0]=le[0][2:len(le[0])-2]+'oxy'
                a=rootwords.index(le[0][:-3])+1
            elif len(le)==2:
                le[0]=le[0][:-2]+'oxy'
                a=rootwords.index(le[1][:-2])+1
            dsubs={le[0]:[1]}
            strch(a,[],[])
        else:
            if le[0].startswith('di'):
                le[0]=le[0][2:]
                le.append(le[0])
            testvariable_ether_1=1
            T.goto(0,0)
            T.write('O',font=('Arial',18,'normal'))
            T.pu()
            T.goto(T.xcor()+20,T.ycor()+15)
            T.pd()
            T.lt(30)
            T.fd(50)
            loc['O1']=T.pos()
            writepref_special({le[0]:['O1']},T.heading())
            T.pu()
            T.goto(-5,15)
            T.seth(150)
            T.pd()
            T.fd(50)
            loc['O2']=T.pos()
            writepref_special({le[1]:['O2']},T.heading())
            
    ##____________________Test for anhydrides______________________##
    if 'anhydride' in name:
        testvariable_anhy=1
        la=name.split()
        if la[0]!='benzoic':
            la[0]=la[0][:len(la[0])-5]
            a=rootwords.index(la[0])+1
            if len(la)==2:
                b=rootwords.index(la[0])+1
            elif la[1]!='benzoic':
                la[1]=la[1][:len(la[1])-5]
                b=rootwords.index(la[1])+1
            else:
                b='benzoic'
        else:
            a='benzoic'
            if len(la)==2:
                b='benzoic'
            else:
                la[1]=la[1][:len(la[1])-5]
                b=rootwords.index(la[1])+1
            
        drawanhydride(a,b)
    ##____________________Test for esters_________________________##
    if 'oate' in name:
        testvariable_ester=1
        le=name.split()
        if le[1]!='benzoate':
            le[1]=le[1][:len(le[1])-6]
            a=rootwords.index(le[1])+1
        else:
            a='benzoate'
        if le[0] in trivialsubs or le[0] in cycloalkylsubs :
            drawester(le[0],a,'tri/cyclo')
        elif le[0] in alkylsubs:
            b=alkylsubs.index(le[0])+1
            drawester(b,a,'alkyl')
                
    ##___________Test for 2nd and 3rd degree amines_____________##
    if ('N' in name or 'amine' in name) and not testvariable_pres_subs and 'amide' not in name  and '-amine' not in name and '-diamine' not in name and '-triamine' not in name:
        testvariable_amine=1
        la1=[]
        la2=[]
        la3=[]
        la=name.split('yl')
        for k in la:
            k=k[k.find('-')+1:]
            if '-' in k:
                k=k[k.find('-')+1:]
            elif ' ' in k:
                k=k[k.find(' ')+1:]
            la1.append(k)
        if 'amine' in la1[-1]:
            la1[-1]=la1[-1][:len(la1[-1])-7]
        for k in la1:
            if k.startswith('di'):
                la2.append(k[2:])
                la2.append(k[2:])
            elif k.startswith('tri'):
                la2.append(k[3:])
                la2.append(k[3:])
                la2.append(k[3:])
            elif k in rootwords:
                la2.append(k)
            elif k+'yl' in cycloalkylsubs:
                la2.append(k)
            elif k+'yl' in trivialsubs:
                la2.append(k)
        for k in la2:
            if k in rootwords:
                la3.append(rootwords.index(k)+1)
            elif k+'yl' in trivialsubs or k+'yl' in cycloalkylsubs:
                la3.append(k+'yl')
        if len(la3)==1:
            drawamine(la3[0])
        elif len(la3)==2:
            drawamine(la3[0],la3[1])
        elif len(la3)==3:
            drawamine(la3[0],la3[1],la3[2])
    ##__________Test for N-Substituted amino groups______________##
    if 'N' in name and testvariable_pres_subs and ('amine' in name or 'amide' in name):
        testvariable_N_subst=1    
    ##__________Test for Bicyclo and Spiro compunds_______________##
    if 'bicyclo' in name or 'spiro' in name:
        if 'bicyclo' in name:
            subs=name[:name.find('bicyclo')]
        elif 'spiro' in name:
            subs=name[:name.find('spiro')]
        testvariable_bicyc_spiro_=1
        f=name.find('[')
        g=name.find(']')
        substr=name[f+1:g]
        list_=substr.split('.')
        if 'bicyclo' in name:
            drawbicyclo(int(list_[0]),int(list_[1]),int(list_[2]))
        elif 'spiro' in name:
            drawspiro(int(list_[0]),int(list_[1]))
            
    ##_________Compounds of type:isopropyl alcohol and alkyl halide______##
    for k in othersuff:
        if k in name and 'oyl' not in name and 'cyclo' not in name:
            f=name.find(k)
            fungrp=name[f::]
            subs1=name[:len(name)-len(fungrp):]
            subs1=subs1[:-1:]
            if subs1 in alkylsubs or subs1 in n_alkylsubs:
                testvariable_alkyl_othersuff=1
                if k in othersuff_ref:
                    dsubs[othersuff_ref[k]]=[1]
                else:
                    dsubs[k]=[1]
                if subs1 in alkylsubs:    
                    a=alkylsubs.index(subs1)+1
                else:
                    a=n_alkylsubs.index(subs1)+1
                strch(a,b,c)
                break
                
            writepref({subs1:[1]})
            T.pu()
            T.home()
            T.goto(T.xcor()+3,T.ycor()-15)
            T.write(othersuff[k],font=('Arial',18,"normal"))
            testvariable_iso=1
    #______________Test For Benzenoid Compounds________________#
    for k in benzenoid_:
        if k in name:
            i=name.find(k)
            benzchain=name[i::]
            bsubs=name[:len(name)-len(benzchain)]
            testvariable_benz=1
            subs=fbenz(bsubs,benzchain)
    #___________Compounds not of type:iso propyl halide or benzenoid_or bicylo-spiro or alkyl halide or amine or ester______#
    if not testvariable_iso and not testvariable_alkyl_othersuff  and not testvariable_amine and not testvariable_ester and not testvariable_special_ and not testvariable_anhy and not testvariable_ether and not testvariable_ketone and not testvariable_spl_ketone and not testvariable_hetero and not testvariable_fused:
        revname=name[::-1]
        testname=revname
        if not testvariable_benz and not testvariable_bicyc_spiro_:
            for k in revrootwords:
                if k in testname:
                    i=testname.find(k)
                    possiblenames.append(testname[:i+len(k):][::-1])
                    a=revrootwords.index(k)+1
            length=[]
            for k in possiblenames:
                length.append(len(k))
            try:
                pchain=possiblenames[length.index(min(length))]
            except:
                if not possiblenames and testvariable_sulpho:
                    pchain=name[name.find('sulphonicacid'):]
                    testvariable_sulpho_2=1
                else:
                    Err()
            if 'm'+pchain in possiblenames:
                pchain='m'+pchain
            if a==9 and pchain=='none':
                possiblenames.remove('none')
                length.remove(4)
                pchain=possiblenames[length.index(min(length))]
                for k in rootwords:
                    if k in pchain:
                        a=rootwords.index(k)+1
                        break
        elif not testvariable_bicyc_spiro_ and not testvariable_sulpho:
            pchain='cyclohex-1,3,5-ene'
            a=6
        if not testvariable_bicyc_spiro_:
            i=name.find(pchain)
            name1=pchain[len(rootwords[a-1]):-1:]
            if name[i-5:i]=='cyclo':
                pchain='cyclo'+pchain
            if not testvariable_benz:
                subs=name[:len(name)-len(pchain)]
            for k in rootwords:#for compounds having more c-atoms in substituents than in pchain
                if k in pchain and pchain[pchain.find(k):]!='none':
                    if k=='eth' and pchain[pchain.find('eth')-1]=='m':
                        break
                    a=rootwords.index(k)+1
            if possiblenames and testvariable_sulpho:
                for al in c_type_subs:
                    if al in pchain:
                        testvariable_sulpho_1=1
                        subs+=pchain[:pchain.find(al)+len(al)]
                        pchain=pchain[pchain.find(al)+len(al):]
                        a=1
        #____Block for finding position of double bond and triple bond____#
            i1=name1.find('en')
            l=name1.split('-')
            if 'dien' not in name1 and 'trien' not in name1 and 'tetraen' not in name1 and i1!=-1 and name1[i1-1]!='-': #This codition is to give by default db posn as 1 when nothing is mentioned
                b.append(1)
            elif i1!=-1:
                for o in ['en','dien','trien','tetraen']:
                    if o in l:
                        i1=name1.find(o)
                        f=l[l.index(o)-1]
                        g=f.split(',')
                        for x in g:
                            b.append(int(x))
            i2=name1.find('yn')
            if 'diyn' not in name1 and 'triyn' not in name1 and 'tetrayn' not in name1 and  i2!=-1 and name1[i2-1]!='-' :#This codition is to give by default tb posn as 1 when nothing is mentioned
                c.append(1)
            elif i2!=-1:
                for o in ['yn','diyn','triyn','tetrayn']:
                    if o in l:
                        i2=name1.find(o)
                        f1=l[l.index(o)-1]
                        g1=f1.split(',')
                        for x in g1:
                            c.append(int(x))
        if testvariable_benz and isinstance(subs,str) or not testvariable_benz:
            #_________Block for finding functional grps in the substituent chain(prefixes)_______#
            if subs:
                if subs[-1]==' ' or subs[-1]=='-':
                    subs=subs[:-1:]
                lsubs=subs.split('-')
                if len(lsubs)==1 and ('di' in subs or 'tri' in subs or 'tetra' in subs):
                    if subs.startswith('di'):
                        dsubs[subs[2:]]=[1,1]
                    elif subs.startswith('tri'):
                        dsubs[subs[3:]]=[1,1,1]
                    elif subs.startswith('tetra'):
                        dsubs[subs[5:]]=[1,1,1,1]
                    lsubs=[]
                elif len(lsubs)==1:
                    lsubs=subs.split()
                if 'sec' in lsubs:
                    s=lsubs.index('sec')
                    if lsubs[s+1]=='butyl':
                        lsubs[s]='sec-butyl'
                        del lsubs[s+1:s+2]
                elif 'tert' in lsubs:
                    s=lsubs.index('tert')
                    if lsubs[s+1]=='butyl':
                        lsubs[s]='tert-butyl'
                        del lsubs[s+1:s+2]
                elif 't' in lsubs:
                    s=lsubs.index('t')
                    if lsubs[s+1]=='butyl':
                        lsubs[s]='tert-butyl'
                        del lsubs[s+1:s+2]
                for k in lsubs:
                    if '(' in k and 'phenyl' not in subs[subs.find('('):] and 'phenoxyl' not in subs[subs.find('('):] and 'tolyl' not in subs[subs.find('('):]:#Case of Substituted Alkyl group
                        testvariable_subalkyl_0=1
                        b1=lsubs.index(k)
                    elif '(' in k and ('phenyl' in subs[subs.find('('):] or 'phenoxyl' in subs[subs.find('('):] or 'tolyl' in subs[subs.find('('):]):
                        testvariable_subst_phenyl=1
                    if ')' in k and 'phenyl' not in subs[subs.find('('):] and 'phenoxyl' not in subs[subs.find('('):] and 'tolyl' not in subs[subs.find('('):]:
                        b2=lsubs.index(k)
                    
                if testvariable_subalkyl_0:        
                    for i in range(b1,b2+1):
                        subalkyl+=lsubs[i]+'-'
                    lsubs[b1]=subalkyl[:-1:]
                    del lsubs[b1+1:b2+1]
                for i in range(0,len(lsubs)):
                    if (lsubs[i].isalpha() or lsubs[i] in ['sec-butyl','tert-butyl','t-butyl'] or '(' in lsubs[i] and ')' in lsubs[i]) and i==0:
                        dsubs[lsubs[i]]=[1]
                    elif (lsubs[i].isalpha() or lsubs[i] in ['sec-butyl','tert-butyl','t-butyl'] or '(' in lsubs[i] and ')' in lsubs[i]) and len(lsubs[i-1])==1:
                        if lsubs[i-1]!='N':
                            dsubs[lsubs[i]]=[int(lsubs[i-1])]
                        else:
                            N_subs.append(lsubs[i])
                    elif (lsubs[i].isalpha() or lsubs[i] in ['sec-butyl','tert-butyl','t-butyl'] or '(' in lsubs[i]and ')' in lsubs[i] ) and ',' in lsubs[i-1]:
                        if 'di' in lsubs[i]:
                            lsubs[i]=lsubs[i][2::]
                        elif 'tri' in lsubs[i]:
                            lsubs[i]=lsubs[i][3::]
                        var=lsubs[i-1].split(',')
                        var1=[]
                        for k in var:
                            if k!='N':
                                var1.append(int(k))
                            else:
                                N_subs.append(lsubs[i])
                        dsubs[lsubs[i]]=var1
                    elif lsubs[i].isalpha() and lsubs[i-1].isalpha():
                        dsubs[lsubs[i]]=[1]
                if testvariable_bicyc_spiro_:
                    cyclowritepref(dsubs)
                if testvariable_subst_phenyl:
                    subs_dum=subs
                    while subs_dum.find('(')!=-1:
                        b01=subs_dum.find('(')
                        b02=subs_dum.find(')')
                        point=int(subs_dum[b01-2])
                        d_subst[point]=subs_dum[b01:b02+1]
                        if 'phenyl' in subs_dum[b01:b02+1] or 'tolyl' in subs_dum[b01:b02+1]:
                            if 'phenyl' not in dsubs:
                                dsubs['phenyl']=[point]
                            elif 'phenyl' in dsubs:
                                dsubs['phenyl'].append(point)
                        if 'phenoxyl' in subs_dum[b01:b02+1]:
                            if 'phenoxyl' not in dsubs:
                                dsubs['phenoxy']=[point]
                            elif 'phenoxyl' in dsubs:
                                dsubs['phenoxy'].append(point)
                        subs_dum=subs_dum[subs_dum.find(')')+1:]
        elif isinstance(subs,dict):
            dsubs=subs
        #_______Block for finding functional grps within parent chain(suffixes)_______________________________#
        lsuff=pchain.split('-')
        for k in suff:
            if len(lsuff)!=1:
                if k in lsuff[-1] and lsuff[-2].isalpha():
                    dfun[k]=[1]
                elif k in lsuff[-1] and lsuff[-2].isnumeric():
                    dfun[k]=[int(lsuff[-2])]
                elif k in lsuff[-1] and ',' in lsuff[-2]:
                    if 'di' in lsuff[-1]:
                        lsuff[-1]=lsuff[-1][2::]
                    elif 'tri' in lsuff[-1]:
                        lsuff[-1]=lsuff[-1][3::]
                    elif 'tetra' in lsuff[-1]:
                        lsuff[-1]=lsuff[-1][4::]
                    var=lsuff[-2].split(',')
                    var1=[]
                    for o in var:
                        var1.append(int(o))
                    dfun[k]=var1
            else:
                if k in lsuff[0]:
                    dfun[k]=[1]
        if 'isonitrile' in dfun:
            dfun.pop('nitrile')
        if 'thiol' in dfun:
            dfun.pop('ol')
        #________________Special Block for carbonyls________________#            
        if not dfun and not testvariable_sulpho:   
            if len(lsuff)>1:
                for k in coohderv_suff:
                    if k==lsuff[-1]:
                        testvariable_db_cum_coohderv=1
            if len(lsuff)==1 or testvariable_db_cum_coohderv and not lsuff[-2].isnumeric():
                for k in coohderv_suff:
                    if k in lsuff[-1] and k!='one':
                        dfun1[k]=[1]
                    elif k in lsuff[0] and k=='one':
                        if i!=1:
                            dfun1[k]=[2]
                        else:
                            dfun1[k]=[1]
            for k in coohderv_suff:
                if  not dfun1 and k in lsuff[-1] and ',' in lsuff[-2]:
                    if 'di' in lsuff[-1]:
                        lsuff[-1]=lsuff[-1][2::]
                    elif 'tri' in lsuff[-1]:
                        lsuff[-1]=lsuff[-1][3::]
                    elif 'tetra' in lsuff[-1]:
                        lsuff[-1]=lsuff[-1][4::]
                    var=lsuff[-2].split(',')
                    var1=[]
                    for o in var:
                        var1.append(int(o))
                    dfun1[k]=var1
            for k in coohderv_suff:
                if not dfun1 and k in lsuff[-1] and lsuff[-2].isnumeric():
                    dfun1[k]=[int(lsuff[-2])]
            for k in cyclic_oxo_fun:
                if k in pchain and 'cyclo' in pchain:
                    lc=[]
                    substr=pchain[pchain.find('ane')+3:]
                    substr=substr.strip()
                    subsubstr=substr[:substr.find(k)]
                    if subsubstr:
                        for ele in subsubstr:
                            if ele.isnumeric():
                                lc.append(int(ele))
                        dfun1[k]=lc
                    subsubstr=subsubstr.strip()
                    if not subsubstr:
                        dfun1[k]=[1]
            if 'cyclo' in pchain and 'one' in dfun1 and dfun1['one']==[2]:
                dfun1['one']=[1]

        #__________Sub Block for compounds for type:2-butanol,2-butene_______#
        
        if not testvariable_benz and subs and subs[-1].isnumeric():
            if b:
                b.remove(1)
                b.append(int(subs[-1]))
            elif c:
                c.remove(1)
                c.append(int(subs[-1]))
            elif dfun:
                for k in dfun:
                    dfun[k]=[int(subs[-1])]
            elif dfun1:
                for k in dfun:
                    dfun1[k]=[int(subs[-1])]
        #__________Sub Block for creating a list for the locants to be used___#
        for k in dsubs:
            for j in dsubs[k]:
                tobeusedloc.append(j)
        for k in dfun:
            for j in dfun[k]:
                tobeusedloc.append(j)
        #Pending(type:2,4-butanediol)....
        #_________________Methane and its non-oxo derivatives__________#
        if a==1 and not dfun1 and not testvariable_sulpho_1 and 'oxo' not in dsubs:
            testvariable_methderv=1
            T.write('C',font=('Arial',18,"normal"))
            T.pu()
            T.goto(23,15)
            T.pd()
            T.fd(30)
            locmethsub_triv[1]=T.pos()
            T.pu()
            T.goto(T.xcor()+15,T.ycor()+10)
            locmethsub[1]=T.pos()
            T.goto(8,30)
            T.seth(90)
            T.pd()
            T.fd(30)
            locmethsub_triv[2]=T.pos()
            T.pu()
            T.goto(T.xcor()-3,T.ycor()+25)
            locmethsub[2]=T.pos()
            T.goto(-7,15)
            T.seth(180)
            T.pd()
            T.fd(30)
            locmethsub_triv[3]=T.pos()
            T.pu()
            T.goto(T.xcor()-15,T.ycor()+10)
            locmethsub[3]=T.pos()
            T.goto(8,0)   
            T.seth(270)
            T.pd()
            T.fd(30)
            locmethsub_triv[4]=T.pos()
            T.pu()
            T.goto(T.xcor()-2,T.ycor()-5)
            locmethsub[4]=T.pos()
            for k in dsubs:
                    if k in pref:
                        for j in dsubs[k]:
                            T.pu()
                            T.goto(locmethsub[len(usedloc)+1])
                            curdraw(pref[k])
                            usedloc.append(1)
                    elif k in alkoxysubs:
                        for j in dsubs[k]:
                            T.pu()
                            T.goto(locmethsub[len(usedloc)+1])
                            curdraw(cycloalkoxysubs[k])
                            usedloc.append(1)
                    elif k in cycloalkylsubs:
                        for j in dsubs[k]:
                            T.pu()
                            T.goto(locmethsub_triv[len(usedloc)+1])
                            T.pd()
                            T.seth(len(usedloc)*90)
                            a1=cycloalkylsubs.index(k)
                            ang=180*((a1-1)/(a1+1))
                            T.lt(ang/2)
                            for i in range(a1+1):
                                T.fd(50)
                                T.rt(180-ang)
                            T.pu()
                            T.seth(270)
                            usedloc.append(1)
                    elif k =='phenyl':
                        for j in dsubs[k]:
                            T.pu()
                            T.goto(locmethsub_triv[len(usedloc)+1])
                            T.pd()
                            T.seth(len(usedloc)*90)
                            cyc(6,[1,3,5],[],mov=False)
                            T.pu()
                            T.seth(270)
                            usedloc.append(1)
            for k in dfun:
                if k in suff:
                    for j in dfun[k]:
                            T.pu()
                            T.goto(locmethsub[len(usedloc)+1])
                            curdraw(suff[k])
                            usedloc.append(1)
            for i in range(4-len(tobeusedloc)):
                T.goto(locmethsub[4-i])
                curdraw('H')

    #__________________________________Type-alkan-1-one______________________________#
        if 'one' in dfun1 and 1 in dfun1['one']:
            testvariable_1_one_1=1   
                
    #__________Final call of draw function___________________________________________#  
        if 'cyclo' in pchain:
            dfun.update(dfun1)
            cyc(a,b,c,dsubs,dfun)
        elif not testvariable_methderv and not testvariable_bicyc_spiro_:
            if testvariable_sulpho and not loc:
                loc={1:(0,0)}
            strch(a,b,c)
    if mode=='draw':
        ba=Button(text='Try Again?',command=tryag,bg="#c7eafb",font=myfont,relief=RAISED)
        ba.place(relx=.45,y=700)
    


def Tryage():
    
    global entryp
    global entryr
    global lbl1
    global b5
    global testvariable_err_page
    if testvariable_err_page:
        global lbl07
        lbl07.destroy()
    else:
        lbl1.destroy()
    b5.destroy()
    entryp.delete(0,len(entryp.get()))
    entryr.delete(0,len(entryr.get()))

#__________________________________________#    
def Balance():
    
    
    global entryp
    global entryr
    global lbl1
    global b5
    global testvariable_err_page
    global lbl07
    import equation_solver as eqs
    testvariable_err_page=False
    try:
        lbl1.destroy()
    except:
        pass
    reactants=entryp.get()
    products=entryr.get()
    n=len(reactants.split('+'))
    l_const=[]
    rcoeff=eqs.consolidate(reactants,1)
    pcoeff=eqs.consolidate(products,-1)
    for i in range(len(rcoeff)):
        rcoeff[i].extend(pcoeff[i])
        l_const.append(rcoeff[i][0]*-1)
        rcoeff[i]=rcoeff[i][1:]
    l_dupe=eqs.checkdupe(rcoeff)    
    for ele in l_dupe:
        rcoeff.pop(ele)
        l_const.pop(ele)
    try:
        fbcoeff=eqs.hcf(eqs.lcm(eqs.eqnsolver(rcoeff,l_const)))
        fbreac=fbcoeff[:n]
        fbpro=fbcoeff[n:]
        message='The Balanced Equation is:            '+eqs.coalesce(fbreac,reactants)+' → '+eqs.coalesce(fbpro,products)
        lbl1=Label(text=message,font="Cambria 15",relief=RAISED,padx=10,pady=10)
        lbl1.place(relx=0.3,y=500)
    except:
        testvariable_err_page=True
        lbl07=Label(text='OOPS!\nLooks like something is wrong with the reactants or products or there are infinite ways to balance! Press Try Again',font="Cambria 15",relief=RAISED)
        lbl07.place(relx=0.1,y=500)
    b5=Button(text='Try Again?',command=Tryage,bg="#c7eafb",font=myfont,relief=RAISED)
    b5.place(relx=.45,y=600)

#__________________________________________# 
def tryag():
    global entry
    global T
    entry.delete(0,len(entry.get()))
    T.clear()

#__________________________________________#     
def destruct():
    b1.destroy()
    b2.destroy()
    b3.destroy()
#__________________________________________#     
def runoms():
    global entry
    destruct()
    bg.configure(image=img1)
    bg.place(x=0,y=0,relwidth=1,relheight=1)
    entry=Entry(borderwidth=5,relief=SUNKEN,font="Cambria 15")
    be=Button(text='Go!',command=Drawnew,bg="#c7eafb",font=myfont,relief=RAISED,pady=5,padx=5)
    bf=Button(text='Instructions',command=insoms,bg="#c7eafb",font=myfont,relief=RAISED,padx=20,pady=10)
    entry.place(relx=.45,y=145)
    be.place(relx=.63,y=145)
    bf.place(relx=.885,y=145)
#__________________________________________#
    
def runogg():
    global list_of_random_qs
    global list_of_random_ans
    global bttn
    global instbx
    destruct()
    bg.configure(image=img)
    mycon=mc.connect(host='localhost',user='root',password='AXAdb1700Dilbeek',database='pythonproject')
    cursor=mycon.cursor()
    cursor.execute("select count(iupac) from ref_table;")
    data=cursor.fetchall()
    length=data[0][0]
    cursor.execute("select common from ref_table;")
    list_of_potential_questions=cursor.fetchall()
    cursor.execute("select iupac from ref_table;")
    list_of_potential_answers=cursor.fetchall()
    list_of_random_qs=[]
    list_of_random_ans=[]
    for i in range(5):
        rn=random.randint(0,length-1)
        list_of_random_qs.append(list_of_potential_questions[rn][0])
        list_of_random_ans.append(list_of_potential_answers[rn][0])
    
    instbx=Message(text=tinogg,font="Cambria 15",relief=RAISED)
    bttn=Button(text='Start Quiz!',command=gamestart,bg="#c7eafb",font=myfont,relief=RAISED,padx=5,pady=5)
    instbx.place(relx=0.25,y=150)
    bttn.place(relx=0.46,y=700)
#__________________________________________#
def gamestart():
    global qno
    global lqno
    global responses
    global resp
    global bttn2
    global inst
    responses=[]
    qno=1
    instbx.destroy()
    bttn.destroy()
    inst=Label(text='Enter The Common Name : ',font="Cambria 15",relief=RAISED)
    resp=Entry(borderwidth=5,relief=SUNKEN,font="Cambria 15")
    bttn2=Button(text='Save And Next',command=gamecontd,bg="#c7eafb",font=myfont,relief=RAISED)
    lqno=Label(text='Q1',font="Cambria 15",relief=RAISED)
    inst.place(relx=.25,y=700)
    resp.place(relx=.45,y=695)
    lqno.place(relx=.175,y=200)
    DrawMol(list_of_random_ans[qno-1],mode='quiz')
    bttn2.place(relx=.65,y=695)
#____________________________________________#
def gamecontd():
    global qno
    global lqno
    global responses
    global resp
    global canvas
    global s1
    responses.append(resp.get())
    resp.delete(0,len(resp.get()))
    qno+=1
    lqno.destroy()
    if qno<=5:
        lqno=Label(text='Q{}'.format(qno),font="Cambria 15",relief=RAISED)
        lqno.place(relx=.175,y=200)
        canvas.destroy()
        del canvas
        DrawMol(list_of_random_ans[qno-1],mode='quiz')
    else:
        respsubpage()
    
#__________________________________________#
def respsubpage():
    global lbl1
    global bresult
    bg1=Label(root,image=img)
    bg1.place(x=0,y=0,relwidth=1,relheight=1)
    lbl1=Label(text='Your Responses Are Succesfully Submitted!',font="Cambria 15",relief=RAISED)
    bresult=Button(text='Click Here To Check Your Score!',command=resultpage,bg="#c7eafb",font=myfont,relief=RAISED)
    lbl1.place(relx=.375,y=200)
    bresult.place(relx=.4,y=350)
#__________________________________________#
def resultpage():
    global rep
    global lbl1
    global bresult
    global btn
    rep={'acetic acid':0,'vinegar':0,'lindane':1, 'BHC':1,'COT':2, 'cyclooctatetraene':2,'trinitrophenol':3,'picric acid':3}
    lbl1.destroy()
    bresult.destroy()
    score=0
    for i in range(len(responses)):
        if responses[i]==list_of_random_qs[i]:
            score+=1
        elif responses[i] in rep and list_of_random_qs[i] in rep and rep[responses[i]]==rep[list_of_random_qs[i]]:
            score+=1
    sc=Label(text='Your Score: {}/5'.format(score),font="Cambria 15",relief=RAISED,pady=10)
    btn=Button(text='Question Wise Analysis',command=qanalysis,bg="#c7eafb",font=myfont,relief=RAISED)
    sc.place(relx=0.4,y=150)
    btn.place(relx=0.5,y=150)
#__________________________________________#
def qanalysis():
    global btn
    global rep
    btn.destroy()
    hdng='Q.No      Your Answer              Correct Answer           Mark    '
    l_txt1=[]
    l_txt2=[]
    l_txt3=[]
    for i in range(5):
        txt=str(i+1)+' '*14+responses[i]+'                                         '
        l_txt1.append(Label(text=txt,font="Cambria"))
        txt=list_of_random_qs[i]+'  '*(25-len(list_of_random_qs[i]))
        l_txt2.append(Label(text=txt,font="Cambria"))
        if list_of_random_qs[i]==responses[i]:
            txt='1        '
        elif responses[i] in rep and list_of_random_qs[i] in rep and rep[responses[i]]==rep[list_of_random_qs[i]]:
            score+=1
        else:
            txt='0        '
        l_txt3.append(Label(text=txt,font="Cambria"))
    Label(text=hdng,font="Cambria",bg="#c7eafb").place(relx=0.35,y=250)
    for i in range(len(l_txt1)):
        l_txt1[i].place(relx=0.35,y=280+30*i)
    for i in range(len(l_txt2)):
        l_txt2[i].place(relx=0.49,y=280+30*i)
    for i in range(len(l_txt2)):
        l_txt3[i].place(relx=0.606,y=280+30*i,width=70)

    bq2=Button(root,text="Quit",command=root.destroy,bg="#c7eafb",padx=20,pady=10,font=myfont)
    bq2.place(relx=.9,y=20)
          

    
#__________________________________________#
def runeqn():
    global entryp
    global entryr
    destruct()
    bg.configure(image=img2)
    bg.place(x=0,y=0,relwidth=1,relheight=1)
    entryr=Entry(borderwidth=5,relief=SUNKEN,font="Cambria 15")
    entryp=Entry(borderwidth=5,relief=SUNKEN,font="Cambria 15")
    be=Button(text='Go!',command=Balance,bg="#c7eafb",font=myfont,relief=RAISED)
    bf=Button(text='Instructions',command=inseqn,bg="#c7eafb",font=myfont,relief=RAISED,padx=20,pady=10)
    entryp.place(relx=.45,y=200)
    entryr.place(relx=.45,y=300)
    be.place(relx=.45,y=400)
    bf.place(relx=.885,y=95)

    
#______________________MAIN_____________________________________#

    
root=Tk()
root.geometry('1600x900')
root.title("Budding Chemists: A Virtual Workshop")
img=ImageTk.PhotoImage(Image.open("bgpic2.gif","r"))
img1=ImageTk.PhotoImage(Image.open("bgpic3.gif","r"))
img2=ImageTk.PhotoImage(Image.open("bgpic1.gif","r"))
img3=ImageTk.PhotoImage(Image.open("bgpic4.gif","r"))
bg=Label(root,image=img3)
bg.place(x=0,y=0,relwidth=1,relheight=1)
myfont=font.Font(family="Arial")  
b1=Button(root,text="The Organic Molecule Sketcher",command=runoms,bg="#c7eafb",padx=10,pady=20,font=myfont,relief=SUNKEN,activeforeground='pink',activebackground='black')
b2=Button(root,text="The Organic Chemistry GeNiUS ",command=runogg,bg="#c7eafb",padx=10,pady=20,font=myfont,relief=SUNKEN,activeforeground='pink',activebackground='black')
b3=Button(root,text="The Chemical Equation Balancer",command=runeqn,bg="#c7eafb",padx=10,pady=20,font=myfont,relief=SUNKEN,activeforeground='pink',activebackground='black')
bq=Button(root,text="Quit",command=root.destroy,bg="#c7eafb",padx=20,pady=10,font=myfont)
b1.place(relx=.4,y=200)
b2.place(relx=.4,y=400)
b3.place(relx=.4,y=600)
bq.place(relx=.93,y=20)
root.mainloop()


