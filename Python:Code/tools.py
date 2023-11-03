import numpy as np
from neupy import algorithms
import pandas as pd
import pywt
from matplotlib import pyplot as plt

def clase(ytrain):
    x_train = pd.read_csv('x_train.csv', sep=',', header=None)
    y_train = pd.read_csv('y_train.csv', sep=',', header=None)

    pnn = algorithms.PNN(std=0.008, verbose=False)
    pnn.train(x_train, y_train)

    y_pred = pnn.predict(ytrain)
    return [y_pred]


def clase_texto(numero):
    if numero == 1:
        textoc = "Falla entre AB"
    if numero == 2:
        textoc = "Falla entre AC"
    if numero == 3:
        textoc = "Falla entre BC"
    if numero == 4:
        textoc = "Falla entre AG"
    if numero == 5:
        textoc = "Falla entre BG"
    if numero == 6:
        textoc = "Falla entre CG"
    if numero == 7:
        textoc = "Falla entre ABG"
    if numero == 8:
        textoc = "Falla entre ACG"
    if numero == 9:
        textoc = "Falla entre BCG"
    if numero == 10:
        textoc = "Falla entre ABC"
    if numero == 11:
        textoc = "Falla entre ABCG"
    return [textoc]


def calculo_energia(s1, s2, s3, s4, s5, s6):
    cD1 = s1
    cD2 = s2
    cD3 = s3
    cD1C = s4
    cD2C = s5
    cD3C = s6
    ener1 = np.sum(cD1 * cD1)
    ener2 = np.sum(cD2 * cD2)
    ener3 = np.sum(cD3 * cD3)
    ener4 = np.sum(cD1C * cD1C)
    ener5 = np.sum(cD2C * cD2C)
    ener6 = np.sum(cD3C * cD3C)
    e = [ener1, ener2, ener3, ener4, ener5, ener6]
    energia = e/np.sum(e)
    return energia
