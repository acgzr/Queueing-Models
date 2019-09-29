A = float(eval(input('Enter Lambda = ')))
U = float(eval(input('Enter Mu = ')))
k = int(eval(input('Enter k = ')))
Cs = float(eval(input('Enter Cs (0?) = ')))
F = []; F = [1]+[F[-1] for n in range(1, k+1) if not F.append(F[-1]*n if F else 1)]
sum1 = []; sum1 = [sum1[-1] for n in range(k+1) if not sum1.append(sum1[-1]+(A/U)**n/F[n] if sum1 else 1)]
P = []
for j in range(k+1):
    P += [(A/U)**j/(F[j]*sum1[-1])]
    print("P({0:d}) = {1:.4G}%".format(j, P[j]*100))
L = (1-P[k])*A/U
print("L = {0:.4G}".format(L))
W = L/A
print("W = {0:.4G}".format(W))
Rho = A/(k*U)
print("Rho (p) = {0:.4G}".format(Rho))
if Cs != 0:
    CT = Cs*k
    print("CT = Cs*k = {0:.2f}".format(Cs*k))
#190929