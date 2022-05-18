# ----------------------------------------------
# Program by Arthur for study                                         
#                                               
#                                               
# Version         Date         lesson           
#  none           2022       'Masive on python part2'   
#                                               
#-----------------------------------------------
model_car=['Acura NSX 2017 Sportscar ',
           'Acura RSX-S 2004 Coupe ',
           'Alfa Romeo',
           'Giulia Quadrofoglio 2016 Performance',
           'Aston Martin DB5 1964 Classic',
           'Aston Martin DB11 2017 Sportscar',
           'Aston Martin Vulcan 2016 Hypercar',
           'Audi R8 V10 Performance Coupe 2019 Supercar',
           'Audi S5 Sportback 2017 Performance',
           'BMW i8 Roadster 2018 Open-top',
           'BMW Z4 M40i 2020 Open-top',
           'BMW M4 2018 Performance']
for x in model_car:
    print(x.lower())
    
mynumb_list= list(range(0,50))
print(mynumb_list)
for x in mynumb_list:
    x=x*2
    print("Список чисел которие умножаються на 2:" + str(x))