import pandas as pd
from math import isclose


RND_NBR = 10


def evalALM(data,individual):    
    NBR_BUCKETS = 8        
    ABCB = [None]*8
    ABOB = [None]*8
    AGS  = [None]*8
    ADB = [None]*8
    AA  = [None]*8
    LB  = [None]*8
    
    start = 0 
    for i in range(NBR_BUCKETS):        
        ABCB[i], ABOB[i], AGS[i], ADB[i], AA[i], LB[i] = individual[start+0:start+6]
        start += 6

    objective = 0     # Objective Function's return value

    for i in range(0, 8):
        objective += \
            data['Return'].iloc[i]['RABCB']*ABCB[i] + \
            data['Return'].iloc[i]['RABOB']*ABOB[i] + \
            data['Return'].iloc[i]['RAGS']*AGS[i] + \
            data['Return'].iloc[i]['RADB']*ADB[i] + \
            data['Return'].iloc[i]['RAA']*AA[i] - \
            data['Liquidity'].iloc[i]['LDD']*data['Cost'].iloc[i]['CLDD'] - \
            data['Liquidity'].iloc[i]['LSD']*data['Cost'].iloc[i]['CLSD'] - \
            data['Liquidity'].iloc[i]['LTD']*data['Cost'].iloc[i]['CLTD'] - \
            data['Cost'].iloc[i]['CLB']*LB[i]

    
    # -------------
    # Constraint 1
    # The total revenues must equal the total costs for bucket 1 to maintain
    # liquidity of funds. This is modelled by the following constraint
    # The total revenues must equal the total cost for buckets 1 and 2
    # to maintain liquidity of funds
    # Similiarly, we have liquidity requirements for buckets 1-3, 1-4,..
    # and 1-8
    LHS_constraint_1 = []
    temp =0
    for k in range(NBR_BUCKETS):
        for i in range(k):
            temp = \
                ABCB[i] + ABOB[i] + AGS[i] + ADB[i] + AA[i] - \
                data['Liquidity'].iloc[i]['LDD'] - \
                data['Liquidity'].iloc[i]['LSD'] - \
                data['Liquidity'].iloc[i]['LTD'] - \
                LB[i]      
        LHS_constraint_1.append(temp)

    constraint_1 = True
    for i in range(NBR_BUCKETS):
        if not (round(LHS_constraint_1[i],RND_NBR) >= 0):
            constraint_1 = False
            exit
    # -------------
    
    # -------------
    # Constraint 2
    # Advances in each bucket should exceed 5% of total term advances 
    # in 8 all eight buckets.
    #
    TotalTermAdvances = 0     
    for i in range(NBR_BUCKETS):
        TotalTermAdvances += AA[i]    
    constraint_2 = True
    for i in range(NBR_BUCKETS):
        if not (round(AA[i],3) >= 0.05 * round(TotalTermAdvances, RND_NBR)):
            constraint_2 = False
            exit
            
    
    # -------------
    
    # -------------
    # Constraint 3
    # Balance with central bank in each bucket should exceed 5% of total 
    # assets in all eight buckets.
    totalAssets = 0
    for i in range(NBR_BUCKETS):
        totalAssets += ABCB[i] + ABOB[i] + AGS[i] + ADB[i] + AA[i]
    
    constraint_3 = True
    # print()
    for i in range(NBR_BUCKETS):
        # print()
        # print(ABCB[i] - 0.05 * totalAssets)

        if not (round(ABCB[i] - 0.05 * totalAssets, RND_NBR) >= 0):
            constraint_3 = False
            exit    
    # print('contraint 3: ' +str(constraint_3))
    # print()
    # print()
    # -------------
    
    # -------------
    # Constraint 4
    #  Balance with central bank in bucket 8 should exceed 5% of total 
    #  balances with central bank in all eight buckets
    totalBalanceWithCentralBank = 0
    for i in range(NBR_BUCKETS):
        totalBalanceWithCentralBank += 0.05 * ABCB[i]
    
    constraint_4 = True
    # print()
    # print(ABCB[7])
    # print(0.05 * totalBalanceWithCentralBank)
    # print()
    if not (round(ABCB[7] - 0.05 * totalBalanceWithCentralBank, RND_NBR) >= 0):
        constraint_4 = False
        exit
    # print('contraint 4: '+str(constraint_4))
    
    # -------------


    # -------------
    # Constraint 5
    # Investment in government securities in bucket 8 should exceed 5% 
    # of total investment in government securities in all eight buckets.    
    total_AGS = 0
    for i in range(NBR_BUCKETS):
        total_AGS += AGS[i]
    constraint_5 = True
    if not (round(AGS[7] -0.05 * total_AGS, RND_NBR) >= 0):
        constraint_5 = False
        exit
    # print('contraint 5: '+str(constraint_5))
    # -------------

    # -------------
    # Constraint 6
    # Investment in debentures and bonds in bucket 8 should exceed 5% 
    # of total investment in debentures and bonds in all eight buckets.
    total_ADB = 0
    for i in range(NBR_BUCKETS):
        total_ADB += ADB[i]
    constraint_6 = True
    if not (round(ADB[7] - 0.05 * total_ADB, RND_NBR)>= 0):
        constraint_6 = False
        exit
    # print('contraint 6: '+str(constraint_6))
    # -------------

    # -------------
    # Constraint 7
    # The total investment in government securities in all buckets should 
    # exceed 24% of the total demand deposits, savings deposits, and 
    # term deposits in all buckets.
    # -------------
    total_AGS = 0
    total_deposits = 0
    for i in range(NBR_BUCKETS):
        total_AGS += AGS[i]
        total_deposits += data['Liquidity'].iloc[i]['LDD'] + \
                          data['Liquidity'].iloc[i]['LSD'] + \
                          data['Liquidity'].iloc[i]['LTD']
    
    if round(total_AGS - 0.24 * total_deposits, RND_NBR)>= 0:
        constraint_7 = True
    else:
        constraint_7 = False
    # print('contraint 7: '+str(constraint_7))
    # -------------
    # Constraint 8
    # The total investment in assets in each bucket should be less than 
    # the total demand deposits, savings deposits, and term deposits 
    # in all buckets
    # -------------
    constraint_8 = True
    for i in range(NBR_BUCKETS):
        temp = ABCB[i] + ABOB[i] + AGS[i] + ADB[i] + AA[i] - total_deposits
        if not (round(temp, RND_NBR) <= 0):
            constraint_8 = False
            exit    
    # -------------
    # Constraint 9
    # Borrowings in bucket 1 should exceed 80% of total borrowings in all buckets.
    total_borrowings = 0
    for i in range(NBR_BUCKETS):
        total_borrowings += LB[i]
    constraint_9 = False
    if round(LB[0] - 0.8 * total_borrowings, RND_NBR)>= 0:
        constraint_9 = True
    
    # Contraint 10
    # Borrowings in each of the buckets 6, 7, and 8 should exceed 5% of 8
    # total borrowings in all bucket
    constraint_10 = True
    
    for i in range(5,8):
        # print("LB["+str(i)+"]"+str(LB[i]))
        if not (round(LB[i] - 0.05 * total_borrowings, RND_NBR)>= 0):
            constraint_10 = False

    
    # cond = [constraint_1, constraint_2, constraint_3, constraint_4,
    #         constraint_5, constraint_6, constraint_7, constraint_8,
    #         constraint_9,constraint_10]
    cond = [constraint_1, constraint_2, constraint_4,
            constraint_5, constraint_6, constraint_7, constraint_8,constraint_10]
    count = 0
    for c in cond:
        if c:
            count = count+1
    '''
    conddata = []
    for con in cond:
        if con:
            conddata.append(1)
        else:
            conddata.append(0)
    file = open("cond.dat","r") 
    readData = file.read() 
    file.close()
    # print(len(oldData))
    newData = []
    if(len(readData)==0):
        newData = conddata
    else:
        oldData = []
        for letter in readData.split(','):
            letter = int(letter)
            oldData.append(letter)
        for i in range(0,len(conddata)):
            newData.append(oldData[i]+conddata[i])
    for i in range(0,len(newData)):
        newData[i]= str(newData[i])
    # print(newData)
    file = open("cond.dat","w") 
    stringtowrite= ','.join(newData)
    print(stringtowrite)
    file.write(stringtowrite)
    file.close()
    '''

    return objective, count,


 

            
