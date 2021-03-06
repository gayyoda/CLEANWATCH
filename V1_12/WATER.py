import Iso, Eff
from math import *
import numpy as np
r = 10026.35e-3
vol = np.pi*pow(r, 3)*2
mass = vol*1e3
defPPM = [0.002, 0.01] #[Rn222 [Bq/kg], RN]
IsoAct = defPPM
revIsoAct = defPPM
IsoList = Iso.WATER
IType = ['PPM', 'Events per day']
IsoDecay = [Iso.Rn222,
            Iso.RN]
IsoEff = [Eff.WATERRn222]
         #[1]]
EffErr = [Eff.WATERRn222Err]
         #[0]]
def Activity(PPM):
    IAct = []
   # for i in range(len(PPM)-1):
   #     IAct.append(PPM[i]*vol)
   #     print('Activity for ' + Iso.WATER[i] + ' = %5e' % IAct[i])
   # IAct.append(defPPM[-1])
   #Rn222
    IAct.append(PPM[0]*vol*mass)
    print('Activity for ' + Iso.WATER[0] + ' = %.5e' % IAct[0])
    IAct.append(PPM[1])
    print('Activity for ' + Iso.WATER[1] + ' = %.5e' % IAct[1])
    return IAct
def revActivity(BG, Eff, NEff):
    rIsoAct = []
    for i in range(len(IsoList)-1):
        maxbg = max(BG[i])
        x = BG[i].index(maxbg)
        if Eff[i][x] != 0:
            rIsoAct.append(maxbg/Eff[i][x]/vol)
        else:
            revIsoAct.append(0)
    #print(rIsoAct)
    return rIsoAct
#defAct = Activity(defPPM)
