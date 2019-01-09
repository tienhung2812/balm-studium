import pandas as pd
from math import isclose

RND_NBR = 10

def evalALM(individual):
    

    data = pd.read_excel("data.xlsx", None)  # Load all sheets
    # print(data)
    NBR_BUCKETS = 8
    # For the purpose of readibility, I rewrite individual elements
    # which are our variables in another way   
    
    # print(len(individual))
    # print()
    # print(individual)
    # print(type(individual))
    # print()
    # ABCB = individual[0:8]
    # ABOB = individual[8:16]
    # AGS  = individual[16:24]
    # ADB  = individual[24:32]
    # AA   = individual[32:40]
    # LB   = individual[40:48]
    
    ABCB = [None]*8
    ABOB = [None]*8
    AGS  = [None]*8
    ADB = [None]*8
    AA  = [None]*8
    LB  = [None]*8

    #ABCB[0], ABOB[0], AGS[0], ADB[0], AA[0], LB[0] = individual[0:6]
    
    start = 0 
    for i in range(NBR_BUCKETS):        
        ABCB[i], ABOB[i], AGS[i], ADB[i], AA[i], LB[i] = individual[start+0:start+6]
        start += 6

    # print(individual)
    # ABCB = individual[0]
    # ABOB = individual[1]
    # AGS  = individual[2]
    # ADB  = individual[3]
    # AA   = individual[4]
    # LB   = individual[5]
    
    # print("ABCB: ")
    # print(ABCB)
    # print("ABOB")
    # print(ABOB)
    # print("AGS")
    # print(AGS)
    # print("ADB")
    # print(ADB)
    # print("AA")
    # print(AA)
    # print("LB")
    # print(LB)

    objective = 0
    # Objective Function
    for i in range(0, 8):
        # print(type(data['Return'].iloc[i]['RABCB']))
        # print(type(ABCB[i]))
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
        # print(i)
        # print('return')
        # print(data['Return'].iloc[i]['RABCB']*ABCB[i] + \
        #     data['Return'].iloc[i]['RABOB']*ABOB[i] + \
        #     data['Return'].iloc[i]['RAGS']*AGS[i] + \
        #     data['Return'].iloc[i]['RADB']*ADB[i] + \
        #     data['Return'].iloc[i]['RAA']*AA[i])
        # # print('cost')
        # print(data['Liquidity'].iloc[i]['LDD']*data['Cost'].iloc[i]['CLDD'] - \
        #     data['Liquidity'].iloc[i]['LSD']*data['Cost'].iloc[i]['CLSD'] - \
        #     data['Liquidity'].iloc[i]['LTD']*data['Cost'].iloc[i]['CLTD'] - \
        #     data['Cost'].iloc[i]['CLB']*LB[i])
        # print()
    # print(objective)
    
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
#        isclose(LHS_constraint_1[i], 0)
        if not (round(LHS_constraint_1[i],RND_NBR) >= 0):
            constraint_1 = False
            exit
    # print("LHS constraint_1")
    # print(LHS_constraint_1)
    # print(constraint_1)
    # print("End LHS contraint 1")
    # print()
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
            # print(AA[i])
            # print(0.05*TotalTermAdvances)
            constraint_2 = False
            exit
    # print('contraint 2: ' +str(constraint_2))
    
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
    # print('contraint 8: '+str(constraint_8))
    # -------------
    # Constraint 9
    # Borrowings in bucket 1 should exceed 80% of total borrowings in all buckets.
    total_borrowings = 0
    for i in range(NBR_BUCKETS):
        total_borrowings += LB[i]
    constraint_9 = False
    if round(LB[0] - 0.8 * total_borrowings, RND_NBR)>= 0:
        constraint_9 = True
    
    # print('contraint 9: '+str(constraint_9))
    # -------------
    # Contraint 10
    constraint_10 = True
    
    # print(0.05 * total_borrowings)
    for i in range(5,8):
        # print("LB["+str(i)+"]"+str(LB[i]))
        if not (round(LB[i] - 0.05 * total_borrowings, RND_NBR)>= 0):
            constraint_10 = False
    # print('contraint 10: '+str(constraint_10))
    # -------------
    
    # Test only!!
    # if constraint_1:
    #    return objective,
    # else:
    #     return -100000,

    # Original

    cond = [constraint_1, constraint_2, constraint_3, constraint_4,
            constraint_5, constraint_6, constraint_7, constraint_8,
            constraint_9]
    count = 0
    for c in cond:
        if c:
            count = count+1
    
    print(cond)
    print(objective)
    print(count)
    if constraint_1 and constraint_2 and constraint_3 and constraint_4 \
       and constraint_5 and constraint_6 and constraint_7 and constraint_8 \
       and constraint_9 and constraint_10:                     
       return objective, count,
    elif count >= 7:
        return objective, count, 
    else:
        return objective, count,

#%%

# individual = [
#     [25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052
#     ],
#     [0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0],
#     [43.8421052631575,
#     0,
#     0.368421052631654,
#     0,
#     0,
#     5.26315789473685,
#     5.26315789473687,
#     5.26315789473701],
#     [0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0],
#     [159.078947368421,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631
# ],
#     [
#     206.315789473683,
#     4.63157894736848,
#     0,
#     0.631578947368373,
#     7.63157894736835,
#     12.8947368421052,
#     12.8947368421052,
#     12.8947368421052
#     ]

# ]

# List of variables

# individual = [
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     25.3947368421052,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     43.8421052631575,
#     0,
#     0.368421052631654,
#     0,
#     0,
#     5.26315789473685,
#     5.26315789473687,
#     5.26315789473701,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     159.078947368421,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     12.2368421052631,
#     206.315789473683,
#     4.63157894736848,
#     0,
#     0.631578947368373,
#     7.63157894736835,
#     12.8947368421052,
#     12.8947368421052,
#     12.8947368421052
# ]

# List of variables
# individual = [
#     25.3947368421052,	0,	43.8421052631575,	0,	159.078947368421, 206.315789473683,
#     25.3947368421052,	0,	0,	0,	12.2368421052631, 4.63157894736848,
#     25.3947368421052,	0,	0.368421052631654,	0,	12.2368421052631,0,
#     25.3947368421052,	0,	0,	0,	12.2368421052631, 0.631578947368373,
#     25.3947368421052,	0,	0,	0,	12.2368421052631, 7.63157894736835,
#     25.3947368421052,	0,	5.26315789473685,	0,	12.2368421052631, 12.8947368421052,
#     25.3947368421052,	0,	5.26315789473685,	0,	12.2368421052631, 12.8947368421052,
#     25.3947368421052,	0,	5.26315789473685,	0,	12.2368421052631, 12.8947368421052
#     ]

# print(evalALM(individual))
 

            
