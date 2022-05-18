# ----------------------------------------------
# Program by Arthur for study                                         
#                                               
#                                               
# Version         Date         lesson           
#  none           2022       'if else elif on python '   
#                                               
#-----------------------------------------------

all_car=['Acura NSX 2017 Sportscar ',
           'Acura RSX-S 2004 Coupe ',
           'Alfa Romeo',
           'Giulia Quadrofoglio 2016 Performance',
           'Aston Martin DB5 1964 Classic',
           'Aston Martin DB11 2017 Sportscar',
           'Aston Martin Vulcan 2016 Hypercar',
           'audi',
           'Audi R8 V10 Performance Coupe 2019 Supercar',
           'bmw',
           'Audi S5 Sportback 2017 Performance',
           'vw',
           'BMW i8 Roadster 2018 Open-top',
           'BMW Z4 M40i 2020 Open-top',
           'BMW M4 2018 Performance']
german_car=['bmw','vw','audi']

for x in all_car:
    if x in german_car:
        print(x + "is German car")
    else:
        print(x + " isn't German car")