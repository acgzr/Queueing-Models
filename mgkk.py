A = float(eval(input('Enter Lambda = ')))
U = float(eval(input('Enter Mu = ')))
k = int(eval(input('Enter k = ')))
Cs = float(eval(input('Enter Cs (0?) = ')))
sum1 = iF = 1
for i in range(1,k+1):
    iF *= i
    sum1 += ((A/U)**i)/iF
P = [1/sum1]
print("P({0:d}) = {1:.4G}%".format(j,P[0]*100))
jF = 1
for j in range(1,k+1):
    jF *= j
    P += [(((A/U)**j)/jF)/sum1]
    print("P({0:d}) = {1:.4G}%".format(j,P[j]*100))
L = (1-P[k])*A/U
print("L = {0:.4G}".format(L))
W = L/A
print("W = {0:.4G}".format(W))
Rho = A/(k*U)
print("Rho (p) = {0:.4G}".format(Rho))
if Cs != 0:
    CT = Cs*k
    print("CT = Cs*k = {0:.2f}".format(Cs*k))
#190928
