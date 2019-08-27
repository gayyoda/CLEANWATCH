from statistics import mean
Ac228 = [0, 0.000141824, 0.000144383, 0, 0, 0.000144300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000143781, 0, 0, 0, 0.000141064, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000141965, 0, 0, 0]
Bi212 = [0.000481290, 0.000122956, 0, 0.000122369, 0.000496833, 0.000365988, 0.000241546, 0.000365052, 0.000122624, 0.000244858, 0.000120207, 0.000484379, 0.000243043, 0.000241488, 0.000239837, 0.000361533, 0.000859107, 0.000239521, 0.000122354, 0.000241313, 0.000240703, 0.000488460, 0.000366659, 0.000123031, 0.000365097, 0.000361620, 0.000369640, 0.000363857, 0.000243279, 0.000493340, 0.000241838, 0.000484555, 0.000244499, 0.000365943, 0.000239006, 0.000243487, 0.000244021, 0.000485732, 0.000243665, 0.000241371]
Pb212 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Tl208 = [0.0367468, 0.0382367, 0.0386462, 0.0436678, 0.0386488, 0.0349500, 0.0367290, 0.0406173, 0.0355759, 0.0389400, 0.0395933, 0.0400184, 0.0375406, 0.0394818, 0.0416635, 0.0366654, 0.0410296, 0.0352222, 0.0374249, 0.0381721, 0.0386146, 0.0413191, 0.0392217, 0.0418779, 0.0375319, 0.0389921, 0.0384796, 0.0352467, 0.0394818, 0.0387974, 0.0365863, 0.0400903, 0.0390183, 0.0412228, 0.0389959, 0.0424219, 0.0390806, 0.0390996, 0.0407895, 0.0375379]
print("Prompt n9 cut of PMT for Th232 decay chain")
print("Ac228 = %.5e" % mean(Ac228))
print("Bi212 = %.5e" % mean(Bi212))
print("Pb212 = %.5e" % mean(Pb212))
print("Tl208 = %.5e" % mean(Tl208))