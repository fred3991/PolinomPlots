import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle
import time

import os.path
import datetime






###############
##P_out_HMC943APM5E = [8, 9, 10, 11, 12, 13 ,14 ,15 ,16 , 17, 18, 19, 20, 21 ,22, 23 , 24 , 25 , 26 ,26.9 , 27.9 ,28.9 , 29.8, 30.7, 31.5,  32.3, 32.9, 33.5,  33.9, 34.3, 34.5]
#G = 16.59565144
#OP1dB = 11.29;
#IP1dB = OP1dB-(G-1);
#a0 = 0.00013184*IP1dB**4+0.00052302*IP1dB**3-0.047484*IP1dB**2+0.40415*IP1dB+G-1;
#a1 = -0.00052738*IP1dB**3-0.001569*IP1dB**2+0.094968*IP1dB-0.40415
#a2 = 0.00079107*IP1dB**2+0.001569*IP1dB-0.047484
#a3 = -0.00052738*IP1dB-0.00052302
#a4 = 0.00013184
#G_Pin = [];
#P_IN  = [];
#P_Out = [];
#for Pin in np.arange(-25,7,0.1):
#    P_IN.append(Pin);
#    if Pin<(IP1dB-6.3):
#        G_Pin.append(G);
#    if (IP1dB-6.3)<Pin and Pin<(IP1dB+9.2):
#        G_Pin.append(a0+a1*Pin+a2*Pin**2+a3*Pin**3+a4*Pin**4);
#    if Pin>(IP1dB+9.2):
#        G_Pin.append((-Pin+OP1dB)+2);

#for Pout in range(len(G_Pin)):
#    P_Out.append(P_IN[Pout]+G_Pin[Pout]);
#x= P_IN;
#y= G_Pin;
#y2 = P_Out;
##ADSimRF  HMC943APM5E
##y3 = P_out_HMC943APM5E;
#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22
#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#csfont = {'fontname':'Times New Roman'}
#plt.ylabel('Выходная мощность (дБм), Усиление (дБ)',**csfont);  # Подписи у
#plt.xlabel('Входная мощность (дБм)',**csfont);  # Подписи х

#plt.xlim(-25,               7);  
#plt.ylim(-10,              20);  

##1324УВ13У АО НПП Пульсар Широкополосный усилитель с линейной выходной мощность до 15 мВт @3 ГГц
#plt.title(' 1324УВ13У')
#plt.plot(x,y, 'b*-', markersize = 4, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Коэффициент передачи (полином)', markevery=10);
#plt.plot(x,y2, 'k*-', markersize = 4, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w',label ='Выходная мощность - (полином)',markevery=10);


#PinREAL = [-23.1488173, -21.53047477, -19.92198301, -18.31467114, -16.71484918, -15.13643712, -13.55783975, -11.98883605, -10.43132038, -8.8809, -7.336257976, -5.818838432, -4.306269236, -2.804790236, -1.324067465, 0.179671392, 1.668037926, 3.17494868, 4.686421007, 6.212461096]

#PoutREAL = [-6.553165861,-4.955789799, -3.377812938,-1.812720499,-0.254439771,1.274124926,2.795597983,4.311591883,5.807997127,7.285339504,8.716366322,10.04796616,11.23043451,12.19179375,12.86227594,13.27504292,13.58337298,13.80609474,13.88464696,13.83067575]

#GReal = [16.59565144,16.57468497,16.54417007,16.50195065,16.46040941,16.41056205,16.35343773,16.30042793,16.23931751,16.1662395,16.0526243,15.86680459,15.53670374,14.99658398,14.18634341,13.09537153,11.91533506,10.63114606,9.198225956,7.618214649]

#plt.plot(PinREAL,GReal, 'rP-',markersize=6, label ='Коэффициент передачи (измер.)')
#plt.plot(PinREAL,PoutREAL, 'gP-',markersize=6 , label ='Выходная мощность (измер.)')


##plt.plot(x,y3, 'bh-.', markersize = 6, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k',label ='Выходная мощность - ADSimRF',markevery=1);
#plt.grid(color='k', linestyle='--', linewidth=0.3)
#plt.legend(loc=0);
#plt.show()
##############################################################


############МШУ 1324УВ12У_данные!.xlsm 3 ГГц

#P_out_HMC753 = [-3.5, -2.5 , -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5 , 10.5 , 11.5, 12.4 , 13.4, 14.3, 15.2, 16.1, 16.9, 17.6, 18.2, 18.7, 19.1]

#1324УВ12У_данные



G = 15.57632643;
OP1dB = 19.67;
IP1dB = OP1dB-(G-1);


a0 = 0.00013184*IP1dB**4+0.00052302*IP1dB**3-0.047484*IP1dB**2+0.40415*IP1dB+G-1;
a1 = -0.00052738*IP1dB**3-0.001569*IP1dB**2+0.094968*IP1dB-0.40415
a2 = 0.00079107*IP1dB**2+0.001569*IP1dB-0.047484
a3 = -0.00052738*IP1dB-0.00052302
a4 = 0.00013184
G_Pin = [];
P_IN  = [];
P_Out = [];

for Pin in np.arange(-25,10,0.1):
    P_IN.append(Pin);
    if Pin<(IP1dB-6.3):
        G_Pin.append(G);
    if (IP1dB-6.3)<Pin and Pin<(IP1dB+9.2):
        G_Pin.append(a0+a1*Pin+a2*Pin**2+a3*Pin**3+a4*Pin**4);
    if Pin>(IP1dB+9.2):
        G_Pin.append((-Pin+OP1dB)+2);

for Pout in range(len(G_Pin)):
    P_Out.append(P_IN[Pout]+G_Pin[Pout]);
x= P_IN;


y= G_Pin;


y2 = P_Out;
#ADSimRF  
#y3 = P_out_HMC753;



SMALL_SIZE = 15
MEDIUM_SIZE = 18
BIGGER_SIZE = 22
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
csfont = {'fontname':'Times New Roman'}

plt.ylabel('Выходная мощность (дБм), Усиление (дБ)',**csfont);  # Подписи у
plt.xlabel('Входная мощность (дБм)',**csfont);  # Подписи х



plt.title('1324УВ12У_данные') 



#plt.plot(x,y, 'b*-', markersize = 4, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Коэффициент передачи (полином)', markevery=10);
#plt.plot(x,y2, 'k*-', markersize = 4, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w',label ='Выходная мощность - (полином)',markevery=10);

plt.plot(x,y, 'b*-', markersize = 4, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Коэффициент передачи (полином)', markevery=10);
plt.plot(x,y2, 'rP-', markersize = 12, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w',label ='Выходная мощность - (полином)',markevery=10);




PinREAL = [-23.20116393,-21.38806961,-19.57051962,-17.75757899,-15.96169937,-14.17157185,-12.39734132,-10.63459652,-8.871349594,-7.12600476,-5.397973084,-3.678116341,-1.971698995,-0.259813111,1.434029724,3.131737819,4.822334079,6.520340976,8.241727194,10.03869136];
PoutREAL = [-7.624837533,-5.798686801,-3.993916819,-2.181100958,-0.390179717,1.392442441,3.159081112,4.919649262,6.674358694,8.408477989,10.12534908,11.82432003,13.50155937,15.16858249,16.790119,18.3574901,19.73617337,20.65653533,21.09644473,21.23762259]
GainRAL = [15.5763264,15.58938281,15.5766028,15.57647803,15.57151965,15.56401429,15.55642243,15.55424578,15.54570829,15.53448275,15.52332216,15.50243637,15.47325836,15.4283956,15.35608927,15.22575228,14.91383929,14.13619435,12.85471754,11.19893123]



plt.plot(PinREAL,GainRAL, 'rP-',markersize=5, label ='Коэффициент передачи (измер.)')
plt.plot(PinREAL,PoutREAL, 'gP-',markersize=5 , label ='Коэффициент передачи (измер.)')



plt.xlim(-25,               10);  
plt.ylim(-10,              25);  


plt.grid(color='k', linestyle='--', linewidth=0.3)
plt.legend(loc=0);
plt.show()
#############################################################

