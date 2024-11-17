def TER_CONC3(a,b,c):
    Y=str(a)+str(b)+str(c)
    V=decimal(Y)
    return V


def FA(a,b,c):
    S=[0,1,2,1,2,0,2,0,1,1,2,0,2,0,1,0,1,2,2,0,1,0,1,2,1,2,0]
    C=[0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,2]
    V=TER_CONC3(a,b,c)

    SUM = S[V]
    CARRY= C[V]

    return [CARRY,SUM]
