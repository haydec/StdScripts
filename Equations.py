import numpy as np


def equation1(dThetai, dThetaM, dThetaD):
    df = np.sqrt(1 - (dThetai / (dThetaM - dThetaD)))
    return (df)


def equation2(Wh, ρsoil, γ, dz, v, L1, L2, B, N):
    N = N.reshape(len(N), 1)
    v = v.reshape(len(v), 1)
    B = B.reshape(1, len(B))

    C1 = (np.multiply((Wh * ρsoil), np.exp(γ * dz) - 1) / (4 * np.pi)).reshape(2, 1)

    C3 = np.exp(np.multiply(-v, γ * dz))

    C4 = ((L[0] + L[1]) ** 2 + (np.multiply(v, dz * np.sin(B)) ** 2))
    C5 = ((L[0] - L[1]) ** 2 + (np.multiply(v, dz * np.sin(B)) ** 2))

    C6 = np.log(np.divide(C4, C5))
    C7 = np.multiply(C3, C6)

    C8 = np.sum(C7, axis=0, keepdims=True).reshape(2, 1)

    print('C1=', C1)
    # print('C3=',C3),print('C4=',C4),print('C5=',C5),print('C6=',C6),print('C7=',C7)
    print('C8=', C8)
    print('C1 shape =', C1.shape)
    # print('C3 shape =', C3.shape),print('C4 shape =', C4.shape),print('C5 shape =', C5.shape),print('C6 shape =', C6.shape),#print('C7 shape =', C7.shape)
    print('C8 shape =', C8.shape)
    Δθi = (N * np.multiply(C1, C8)).T

    return (Δθi)


def equation3(dW, T, TL, Tr):
    temp = (1 - dW * T) * (TL / Tr)
    gamma = np.power(temp, 0.5)
    return (gamma)


def equation4(RhoCr, A):
    TL = (RhoCr) / (A * 10 ** -6)
    return (TL)


def equation5(T1, T2, T3, T4, n):
    Tr = T1 + n * (T2 + T3 + T4);  # Equation 5
    return (Tr)


def equation6(T1, T2, T3, T4, n, λ1, λ2):
    T = T1 + n * (((1 + λ1) * T2) + ((1 + λ1 + λ2) * (T3 + T4)))
    return (T)


def equation7(Wd, T1, T2, T3, T4, n):
    ΔθD = Wd * ((T1 / 2) + n * (T2 + T3 + T4))
    return (ΔθD)


def equation8(ΔW0, Δθ0, ΔθM, Δθd):
    ΔW = ΔW0 * (1 - (Δθ0 / (ΔθM - Δθd)))
    return (ΔW)


def equation9(R, at, I, θm):
    dW0 = (R * at * I ** 2) / (1 + at * (θM - 20))
    return (dW0)


def Equation12(ρsoil, L1, L2, B, z, Wh):
    C1 = (ρsoil / (4 * np.pi)) * Wh
    C2 = np.log(((L1 + L2) ** 2 + (z ** 2) * np.sin(B) ** 2) / ((L1 - L2) ** 2 + (z ** 2) * np.sin(B)) ** 2)

    Δθuh = C1 * C2

    return (Δθuh)


def equation13(ρsoil, Wh, N, L1, L2):
    Δθ0 = ((ρsoil * Wh * N) / (4 * np.pi)) * np.log((L1 + L2) ** 2 / (L1 - L2) ** 2)
    return (Δθ0)


def equation14(Δθi, ΔθM, ΔθD):
    DF = np.sqrt(1 - (Δθi / (ΔθM - ΔθD)))
    return (DF)


def equation15(TmhL, TmhC, TmhR, Wh):
    Δθ = TmhL * Wh + TmhC * Wh + TmhR * Wh
    return (Δθ)


def equation17(ρsoil, Wh, L, S):
    C1 = ((ρsoil) / (4 * np.pi))

    C2 = Wh * np.log((L[0] + L[1]) ** 2 / (L[0] - L[1]) ** 2)
    C3 = Wh * np.log(((L[0] + L[1]) ** 2 + S ** 2) / ((L[0] - L[1]) ** 2 + S ** 2))
    C4 = Wh * np.log(((L[0] + L[1]) ** 2 + S ** 2) / ((L[0] - L[1]) ** 2 + S ** 2))

    Δθ0 = C1 * (C2 + C3 + C4)

    return (Δθ0)


def DMaxTemp(θM, θA):
    ΔθM = θM - θA
    return (ΔθM)
