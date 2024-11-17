def Ternary(pxl):

    """ Input : Decimal Value ; Output : Ternary string """

    tern = [0]*6
    value = [3**(5 - i) for i in range(6)]

    for i in range(6):

        if pxl >= value[i]:
            tern[i] = pxl // value[i]
            pxl = pxl % value[i]

    tern = [str(i) for i in tern]
    tern = "".join(tern)

    return tern
