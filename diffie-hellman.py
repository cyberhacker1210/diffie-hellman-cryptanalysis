from random import randint
def DH(g, p):
    secret_a = randint(2,p-2)
    secret_b = randint(2,p-2)
    A = pow(g,secret_a,p)
    B = pow(g,secret_b,p)
    Ka = pow(B,secret_a,p)
    Kb = pow(A,secret_b,p)
    assert Ka == Kb, "Hell nah what's wrong with this shi"
    return (A,B,Ka)
