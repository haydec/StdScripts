# Import Libraries
import numpy as np
import pandas as pd

dz = 0.01
NN = 500
v = np.arange(0, NN + 1)

# Start Enter Directory and Sheet#
File_Directory = r'C:\\Users\\Cillian.Hayde\\CableCrossing.xlsx'
Sheet = 'IecExample'
#  End  Enter Directory and Sheet#

ImportData = pd.read_excel(File_Directory, Sheet)
DF = pd.DataFrame(ImportData)

Cable = DF.iloc[:, 3:]
Cable = Cable.values

Chaining, V, n, Material, Rho, RhoCr, alpha, Formation, N, A, ThetaM, I, R, Lambda1, Lambda2, T1, T2, T3, T4,\
    Wc, Wd, Ws, Wa, Wh, S, L, B, RhoSoil, ThetaA = Cable[0:len(Cable), 0:len(Cable)]
