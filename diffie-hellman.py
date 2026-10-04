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

def benchmark():
    Dataset = [
        (11, 1009),
        (5, 10007),
        (2, 100003),
        (2, 1000003),
    ]
    taille_p = []
    temps_exec_bf = []
    temps_exec_bg = []
    nb_iterations_bf = []
    nb_iterations_bg = []
    for g , p in Dataset:
        A, _, _ = DH(g, p)
        _, time_bf, nb_bf = brute_force(g, p, A)
        _, time_bg, nb_bg = bsgs(g, p, A)

        taille_p.append(len(str(p))-1)
        temps_exec_bf.append(time_bf)
        temps_exec_bg.append(time_bg)
        nb_iterations_bf.append(nb_bf)
        nb_iterations_bg.append(nb_bg)
    return taille_p, temps_exec_bf,temps_exec_bg, nb_iterations_bf, nb_iterations_bg

def graph():
    x, ybf, ybg, _, _ = benchmark()

    plt.plot(x, ybf, marker='o', color='red', label='Mesurement Force Brute O(p)')
    plt.plot(x, ybg, marker='o', color='blue', label='Mesurment BSGS O(sqrt(p))')
    plt.xlabel("Order of magnitude of modulo p (10^k)")
    plt.ylabel("Execution time (seconds)")
    plt.title("Complexity of brute force VS BSGS on Diffie-Hellman algorithm")
    plt.grid(True)
    plt.legend()
    plt.savefig("Complexity_brute_force_vs_BSGS.png", dpi=300)
    plt.show()
graph()
