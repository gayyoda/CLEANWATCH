import matplotlib.pyplot as plt
from statistics import mean
PMT = [8127, 8252, 8309, 8260, 8274, 8164, 8382, 8276, 8281, 8246, 8337, 8222, 8211, 8370, 8176, 8385, 8240, 8265, 8246, 8172, 8358, 8312, 8201, 8241, 8217, 8267, 8202, 8234, 8104, 8170, 8233, 8164, 8337, 8303, 8253, 8277, 8128, 8309, 8290, 8234]
VETO = [7087, 7085, 6955, 7072, 7199, 7070, 6992, 7018, 7046, 7072, 7106, 7119, 7135, 6998, 7251, 7045, 7078, 7035, 7151, 7085, 6950, 7151, 7032, 7183, 7177, 7081, 7061, 7124, 7058, 7104, 7047, 7078, 7017, 7161, 7073, 7088, 7108, 7097, 7076, 7065]
TANK = [2584, 2576, 2506, 2624, 2615, 2558, 2630, 2594, 2583, 2716, 2619, 2698, 2577, 2563, 2680, 2575, 2532, 2616, 2560, 2635, 2550, 2508, 2614, 2580, 2661, 2528, 2500, 2555, 2661, 2630, 2635, 2586, 2545, 2516, 2604, 2549, 2643, 2630, 2614, 2741]
CONC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1]
ROCK = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
WATER = [8443, 8410, 8410, 8476, 8527, 8569, 8525, 8480, 8331, 8426, 8561, 8443, 8435, 8579, 8444, 8518, 8508, 8487, 8393, 8424, 8456, 8464, 8615, 8453, 8458, 8523, 8460, 8362, 8357, 8453, 8387, 8400, 8448, 8558, 8438, 8475, 8502, 8459, 8595, 8433] 
PMT_m = mean(PMT)
VETO_m = mean(VETO)
TANK_m = mean(TANK)
CONC_m = mean(CONC)
ROCK_m = mean(ROCK)
WATER_m = mean(WATER)
tot = PMT_m + VETO_m + TANK_m + CONC_m + ROCK_m + WATER_m
#plt.pie([PMT_m, VETO_m, TANK_m, CONC_m, ROCK_m], explode =[0.1, 0.1, 0.1, 0.1, 0.1], labels = ['PMT', 'VETO', 'TANK', 'CONC', 'ROCK'], autopct = '%1.3e%%')
plt.show()
#print(PMT_m + VETO_m + TANK_m + CONC_m + ROCK_m, "events")
print('PMT = %.5e' % (PMT_m/tot))
print('VETO = %.5e' % (VETO_m/tot))
print('TANK = %.5e' % (TANK_m/tot))
print('CONC = %.5e' % (CONC_m/tot))
print('ROCK = %.5e' % (ROCK_m/tot))
print('WATER = %.5e' % (WATER_m/tot))
print('Total events = %.5e' % tot)
