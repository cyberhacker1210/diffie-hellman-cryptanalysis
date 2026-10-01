from time import *
import matplotlib.pyplot as plt

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
    
    plt.plot(x, y, marker='o', color='red', label='Mesures Force Brute O(p)')
    plt.xlabel("Taille du modulo p")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.title("Complexity of brute force on Diffie-Hellman algorithm")
    plt.grid(True)
    plt.savefig("Complexity_brute force_Diffie-Hellman.png", dpi=300)
    plt.show()
graph()


