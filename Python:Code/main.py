import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
from matplotlib import pyplot as plt
import csv
import pywt
import tools

V = np.zeros([3, 80001])
volt = np.zeros([3, 1334])
I = np.zeros([3, 80001]) #
corr = np.zeros([3, 1334]) #
delayFalla = 9000 + (1333 * 4)
i = 0
fs = 80000
with open('Fallas/V60_AG_t1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        V[:, i] = row
        i = i+1
i = 0
with open('I60_AB_R1t1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        I[:, i] = row
        i = i+1
Tc1 = [1, -1/2, -1/2]
Tc2 = [0, np.sqrt(3)/2, -np.sqrt(3)/2]
Tc3 = [1/2, 1/2, 1/2]
Tclarke = (2/3) * np.array([Tc1, Tc2, Tc3])

vuelta = 0
pico_max1 = 0
pico_max2 = 0
pico_max3 = 0
terminar = 0

plt.figure()
plt.plot(V.T)

while terminar != 1:
    for i in range(0, 1334):
        volt[:, i] = V[:, i + delayFalla*2 + (vuelta * 1334)]
        corr[:, i] = I[:, i + delayFalla * 2 + (vuelta * 1334)]
    # print(vuelta)

    VT = volt.T
    IT = corr.T
    (cA1C, cD1C) = pywt.dwt(VT[:, 0], 'db4')
    (cA2C, cD2C) = pywt.dwt(VT[:, 1], 'db4')
    (cA3C, cD3C) = pywt.dwt(VT[:, 2], 'db4')
    pico_max1 = np.max(cD1C)
    pico_max2 = np.max(cD2C)
    pico_max3 = np.max(cD3C)
    vuelta = vuelta + 1
    if pico_max1 > 0.005:
        terminar = 1
    if pico_max2 > 0.005:
        terminar = 1
    if pico_max3 > 0.005:
        terminar = 1

plt.figure()
plt.plot(VT)
plt.xlabel('Samples(n)', fontsize=25)
plt.ylabel('Volts', fontsize=25)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.figure()
plt.xlabel('Samples(n)', fontsize=25)
plt.ylabel('cD1(volts)', fontsize=25)
plt.plot(cD1C)
plt.plot(cD2C)
plt.plot(cD3C)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
# Añado leyenda, tamaño de letra 10, en esquina superior derecha
#plt.legend(('cD1 A', 'cD1 B', 'cD1 C'),prop = {'size': 15}, loc='upper right')

nV = np.dot(VT, Tclarke.T)
nI = np.dot(IT, Tclarke.T)
plt.figure()
plt.plot(nV)
(cA1, cD1) = pywt.dwt(nV[:, 0], 'db4')
(cA2, cD2) = pywt.dwt(nV[:, 1], 'db4')
(cA3, cD3) = pywt.dwt(nV[:, 2], 'db4')

(IcA1, IcD1) = pywt.dwt(nI[:, 0], 'db4')
(IcA2, IcD2) = pywt.dwt(nI[:, 1], 'db4')
(IcA3, IcD3) = pywt.dwt(nI[:, 2], 'db4')

plt.figure()
plt.plot(cD1)
plt.plot(cD2)
plt.plot(cD3)

ener = classi.calculo_energia(cD1C, cD2C, cD3C, cD1, cD2, cD3)
print(ener*10)
# resul = classi.clase(ener)
# clase = resul[0]
clase = 1
texto = classi.clase_texto(clase)
print(texto)
if clase == 1 or clase == 2 or clase == 4 or clase == 8 or clase == 10 or clase == 11:
    loc_max = np.argmax(cD1)
    sen = cD2
    sen2 = IcD2
if clase == 3 or clase == 5 or clase == 6 or clase == 9 or clase == 7:
    loc_max = np.argmax(cD2)
    sen = cD2
    sen2 = IcD1

es = np.copy(cD2C)
es[range(20, 40)] = es[range(20, 40)] *5
plt.figure()
plt.plot(es,'k')
plt.plot(sen)
plt.plot(loc_max,sen[loc_max])
plt.xlabel('Muestras(n)', fontsize=18)
plt.ylabel('cD1AM1(volts)', fontsize=18)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.show()



