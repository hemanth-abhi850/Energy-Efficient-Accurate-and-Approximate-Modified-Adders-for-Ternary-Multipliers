def TER_CONC3(a,b,c):
    Y=str(a)+str(b)+str(c)
    V=decimal(Y)
    return V

 # Proposed Approximate Design-1

def AFA1(a,b,c): # MFA_1
##         C=0                       C=1               C=2 not exits
    S=[0,1,2, 2,2,0, 2,0,0,  2,2,0, 2,0,0, 0,1,2,  0,0,0, 0,0,0, 0,0,0] 
    C=[0,0,0, 0,0,1, 0,1,1,  0,0,1, 0,1,1, 1,1,1,  0,0,0, 0,0,0, 0,0,0] # B and C are same values because set of C combinations doesnt exits.
    V=TER_CONC3(a,b,c)

    SUM  = S[V]
    CARRY= C[V]

    return [CARRY,SUM]
