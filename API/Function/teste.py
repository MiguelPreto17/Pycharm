from Function.abc import A


def banana(a):
    if a == "A":
        print("Ola")
    else:
        print("Adeus")


def func1(b):
    if b == "valor1":
        A.nominal_energy = 2
    else:
        A.nominal_energy = 3
    A.p_dc_max_c = A.result * 2
    print(A.p_dc_max_c)
    print(A.nominal_energy)
