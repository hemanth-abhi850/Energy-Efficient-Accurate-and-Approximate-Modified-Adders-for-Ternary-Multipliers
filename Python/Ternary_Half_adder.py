
def TER_CONC2(a,b):
    Y=str(a)+str(b)
    V=decimal(Y)
    return V

def HA(a,b):
    S=[0,1,2,1,2,0,2,0,1]
    C=[0,0,0,0,0,1,0,1,1]
    V=TER_CONC2(a,b)

    SUM = S[V]
    CARRY= C[V]

    return [CARRY,SUM]
