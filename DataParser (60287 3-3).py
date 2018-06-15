# Import Libraries
import os
import numpy as np
import pandas as pd

dz = 0.01;
NN = 500;
v = np.arange(0, NN + 1)
ρcr = [0.0026, 0.0049]
at = [3.93 * 10 ** -3, 4.03 * 10 ** -3]

### Start Enter Directory and Sheet###
File_Directory = r'C:\\Users\\Cillian.Hayde\\CableCrossing.xlsx'
Sheet = 'IecExample'
###  End  Enter Directory and Sheet###

ImportData = pd.read_excel(File_Directory, Sheet)
DF = pd.DataFrame(ImportData)

Cable = DF.iloc[:, 3:]

Formation = Cable.iloc[7, :]  # Formation
ConductorMaterial = Cable.iloc[3, :]

V = Cable.iloc[1, :];
I = Cable.iloc[11];
R = Cable.iloc[12]  # AC Cable Electrical Parameters
n = Cable.iloc[2, :]
A = Cable.iloc[9, :];  # Area of Conductor
θM = Cable.iloc[10, :];  # Maximum Permissible Temperature
λ1 = Cable.iloc[13, :];
λ2 = Cable.iloc[14, :]  # Loss Factors

T1 = Cable.iloc[15, :];
T2 = Cable.iloc[16, :];
T3 = Cable.iloc[17, :];
T4 = Cable.iloc[18, :]  # Thermal Resistance

Wd = Cable.iloc[20, :];
Wh = Cable.iloc[23, :]  # Heat Loss (Dielectric and cable)
Wh['Cable2'], Wh['Cable1'] = Wh['Cable1'], Wh['Cable2']

N = Cable.iloc[8, :];
S = Cable.iloc[24, :];
L = Cable.iloc[25, :];
B = Cable.iloc[26, :]  # Cable Parameters

ρsoil = Cable.iloc[27, :];
θA = Cable.iloc[28, :]  # Environment

V = V.values.astype(float);
I = I.values.astype(float);
R = R.values.astype(float)  # AC Cable Electrical Parameters
n = n.values.astype(float)
A = A.values.astype(float);  # Area of Conductor
θM = θM.values.astype(float);  # Maximum Permissible Temperature
λ1 = λ1.values.astype(float);
λ2 = λ2.values.astype(float)  # Loss Factors

T1 = T1.values.astype(float);
T2 = T2.values.astype(float);
T3 = T3.values.astype(float);
T4 = T4.values.astype(float)  # Thermal Resistance

# Heat Loss (Dielectric and cable)

Wd = Wd.values.astype(float);
Wh = Wh.values.astype(float)

N = N.values.astype(float);
S = S.values.astype(float);
L = L.values.astype(float);
B = B.values.astype(float)  # Cable Parameters

ρsoil = ρsoil.values.astype(float);
θA = θA.values.astype(float)  # Environment

print(type(V))