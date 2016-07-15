# file : gazometries


# modification depuis labo 
pH = 7.21
pCO2 = 42
pO2 = 198
bicar_c = 13
SaO2 = 99,8

sodium = 136
potassium = 7.1
chlorures = 111
protides = 60 # g/l
uree = 27.6
glucose = 9.6
lactates = 2.02

def get_trou_anionique():
    return  (sodium + potassium) - (chlorures + bicar_c)

if __name__ == '__main__':
   # print('$%2.2f'.format(get_trou_anionique().format()))
   TA = get_trou_anionique()
   print(str('%2.2f' % TA))
   print(str('%.2f' % TA))
   print(str("trou anionique : {:10.1f} mmol/l (N : 12 +/- 4)  ".format(TA))) # format sur 10 caractères dont 1 décimales
