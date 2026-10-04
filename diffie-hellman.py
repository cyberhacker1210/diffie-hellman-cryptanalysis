from time import *
import matplotlib.pyplot as plt
import math

def DH(g, p):
    secret_a = p-2
    secret_b = p-2
    A = pow(g,secret_a,p)
    B = pow(g,secret_b,p)
    Ka = pow(B,secret_a,p)
    Kb = pow(A,secret_b,p)
    assert Ka == Kb, "Must have a problem here"
    return (A,B,Ka)
def brute_force(g,p,A):
    start = perf_counter()
    count = 0
    for a in range(0, p):
        Atest = pow(g,a,p)
        count += 1
        if Atest == A:
            end = perf_counter()
            return a, end - start, count
def benchmark():
    Dataset = [
        (11, 1009),
        (5, 10007),
        (2, 100003),
        (2, 1000003),
    ]
    taille_p = []
    temps_exec = []
    nb_iterations = []
    for g , p in Dataset:
        A, _, _ = DH(g, p)
        _, time, nb = brute_force(g, p, A)
        taille_p.append(len(str(p))-1)
        temps_exec.append(time)
        nb_iterations.append(nb)
    return taille_p, temps_exec, nb_iterations
def graph():
    x, y, _ = benchmark()

    plt.plot(x, y, marker='o', color='red', label='Mesurement Force Brute O(p)')
    plt.xlabel("Order of magnitude of modulo p (10^k)")
    plt.ylabel("Execution time (seconds)")
    plt.title("Complexity of brute force on Diffie-Hellman algorithm")
    plt.grid(True)
    plt.savefig("Complexity_brute_force_Diffie-Hellman.png", dpi=300)
    plt.show()
def bsgs(g,p,A):
    start = perf_counter()
    ops = 0
    m = math.isqrt(p) + 1 
    ops += 1
    Bs = {}
    for j in range(m):
        res = (A * pow(g,j,p)) % p
        Bs[res] = j
        ops += 1
    for i in range(1, m+1):
        res = pow(g,i*m,p)
        ops += 1
        if res in Bs:
            couple = (i, Bs[res])
            break
    i, j = couple
    x = i*m-j
    ops += 1
    end = perf_counter()
    time = end - start
    return x, time, ops
A, _, _ = DH(11, 1009)
print(brute_force(11, 1009, A))
print(bsgs(11, 1009, A))


