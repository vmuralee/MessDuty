#############################################
###  Author of the Code is Vinay Krishnan ###
###  vinaykrishnanmb@gmail.com ##############
#############################################



import json
from typing import DefaultDict

Fastdays = ['Monday','Thursday','Saturday']
days     = ['Monday','Tuesday','Wednesday','Thursday','Saturday','Friday','Sunday']

file0 = open("BreakFast.json")

file1 = open("LunchBaaji.json")
file2 = open("LunchNonVeg.json")
file3 = open("LunchSplVeg.json")

file4 = open("DinnerBaaji.json")
file5 = open("DinnerNonVeg.json")
file6 = open("DinnerSplVeg.json")




BreakFastDish_dict = json.load(file0)

LunchBaaji_dict  = json.load(file1)
LunchNonVeg_dict = json.load(file2)
LunchSplVeg_dict = json.load(file3)

DinnerBaaji_dict  = json.load(file4)
DinnerNonVeg_dict = json.load(file5)
DinnerSplVeg_dict = json.load(file6)


class BreakFast:
    def __init__(self,nBread,nEggs,nKela,nTea,nMilk,nIndian):
        self.totBread = nBread*2 
        self.totTea   = nTea + 4
        self.totMilk  = nMilk
        self.nEggs    = nEggs
        self.nIndian  = nIndian + 4
        self.nKela    = nKela

    def PrintDiary(self):
        Milk_inLiter = (self.totMilk*250+self.totTea*50)/1000
        print('Total Milk:  ',Milk_inLiter,' L')
        print('No. of Bread:  ',self.totBread)
        print('No. of eggs: ',self.nEggs)
        print('No. of Kela: ',self.nKela)

        print(f'{self.totMilk} glass of milks seves 200ml each')
        print(f'{self.totTea - 4} + 4 cups of Tea = {self.totTea} cups')

    def CalcDish(self,day):
        Dish = BreakFastDish_dict[day]['Name']
        if Dish =="Idli-Sambar":
            print('Ingridents for  ',Dish)
            NoIdli = self.nIndian*2
            BatterFor1Idli = 1/17
            BatterInKg = NoIdli*BatterFor1Idli
            Rice=750*BatterInKg/1000
            Biri=250*BatterInKg/1000
            print(f'Non boil rice = {Rice} kg')
            print(f'Biri Daal ={Biri} Kg')
            DishDict = BreakFastDish_dict[day]['Ingrediants']
            for ing,qty in DishDict.items():
                Qty = qty*self.nIndian
                print(f'{ing} : {Qty/1000} Kg')
        elif Dish =="Bada-ghugni":
            print('Ingridents for  ',Dish)
            NoBada = self.nIndian*2
            BatterForBada = 1/17
            BatterInKg = NoBada*BatterForBada
            Rice=400*BatterInKg/1000
            Biri=600*BatterInKg/1000
            print(f'Non boil rice = {Rice} kg')
            print(f'Biri Daal ={Biri} Kg')
            DishDict = BreakFastDish_dict[day]['Ingrediants']
            for ing,qty in DishDict.items():
                Qty = qty*self.nIndian
                print(f'{ing} : {Qty/1000} Kg')
        else:
            DishDict = BreakFastDish_dict[day]['Ingrediants']
            for ing,qty in DishDict.items():
                Qty = qty*self.nIndian
                print(f'{ing} : {Qty/1000} Kg')
        print(BreakFastDish_dict[day]['Name'],f': {self.nIndian - 4} + 4 = {self.nIndian}')

    def BreakFastSummary(self,day):
        self.PrintDiary()
        self.CalcDish(day)


    
class Lunch:
    def __init__(self,day,nBaseMeal,nRoti,nExtraFry,nDahi,nSplVeg,nSplNonVeg,isPaapad,isSaalad):
        self.isPaapad = isPaapad
        self.isSaalad = isSaalad
        self.TotBaseMeal = nBaseMeal + 4 + 2
        self.TotSplVeg = nSplVeg
        self.TotNonVeg = nSplNonVeg + 4
        self.TotRoti   = nRoti + 9
        self.TotDahi   = nDahi
        self.nExtraFry = nExtraFry
        if day in Fastdays:
            self.TotSplVeg = nSplVeg + 4
            self.TotNonVeg = nSplNonVeg

    def CalcRiceAndRoti(self):
        AttaInKg = self.TotRoti/25.0 
        RiceInKg = (self.TotBaseMeal*0.14 - AttaInKg)
        print('Atta : ',AttaInKg,' Kg for ',self.TotRoti,' people')
        print('Rice : ',RiceInKg, ' Kg for ',self.TotBaseMeal,' people')
        

    def CalcDaalAndPapad(self,day):
        DaalDict = LunchBaaji_dict[day]['Daal']
        self.nPapad    = self.TotBaseMeal
        for daal,qty in DaalDict.items():
            Qty = qty*self.TotBaseMeal
            print(f'{daal} : {Qty/1000} Kg')
        

    def CalcBaaji(self,day):
        self.TotBaaji = self.TotBaseMeal + self.nExtraFry
        VegDict = LunchBaaji_dict[day]['Ingridients']
        for veg,qty in VegDict.items():
            Qty = qty*self.TotBaaji
            print(f'{veg} needs {Qty/1000} Kg')

    def CalcSalad(self,day):
        SaaladDict = LunchBaaji_dict[day]['Salaad']
        if self.isSaalad == True:
            for veg,qty in SaaladDict.items():
                print(f'{veg} : {qty}')
        else:
            for veg,qty in SaaladDict.items():
                Qty = qty*self.TotBaseMeal
                print(f'{veg} : {Qty/1000} Kg')
        

    def CalcSplNonVeg(self,day):
        NonVegDict = LunchNonVeg_dict[day]['Ingridients']
        for non,qty in NonVegDict.items():
            Qty = qty*self.TotNonVeg
            if non == 'Fish':
                print(f'{non} needs {Qty/1000} kg and {self.TotNonVeg} pieces')
            else:
                print(f'{non} needs {Qty/1000}')

        

    def CalcSplVeg(self,day):
        SplVegDict = LunchSplVeg_dict[day]['Ingridients']
        for veg,qty in SplVegDict.items():
            Qty = qty*self.TotSplVeg
            print(f'{veg} needs {Qty/1000} Kg')
                

    def LunchSummary(self,day):
        self.CalcRiceAndRoti()
        self.CalcDaalAndPapad(day)
        self.CalcBaaji(day)
        self.CalcSalad(day)
        self.CalcSplNonVeg(day)
        self.CalcSplVeg(day)

    def ListOfLunch(self,day):
        print("*"*15,"Today's Menu","*"*15)
        print(f'Base Meal for Lunch {self.TotBaseMeal-4} + 4 = {self.TotBaseMeal}')
        print(f'No. of Roti for Lunch {self.TotRoti}')
        if(self.isPaapad == True):
            print(f'No. of Paapad is {self.nPapad}')
        baajiName = LunchBaaji_dict[day]['Name']
        print('No. Dahi packets ',self.TotDahi)
        print(f'No. of {baajiName} for Lunch {self.TotBaaji-self.nExtraFry} + {self.nExtraFry} plates ')
        NonVegDishName = LunchNonVeg_dict[day]['Name']
        VegDishName = LunchSplVeg_dict[day]['Name']
        if day in Fastdays:
            print(f'No. of {NonVegDishName} Spl Non-Veg {self.TotNonVeg} plates')
            print(f'No. of {VegDishName} Spl Veg {self.TotSplVeg-4} + 4 = {self.TotSplVeg} plates')
        else:
            print(f'No. of {NonVegDishName} Spl Non-Veg {self.TotNonVeg-4} + 4 = {self.TotNonVeg} plates')
            print(f'No. of {VegDishName} Spl Veg {self.TotSplVeg} plates')





class Dinner:
    def __init__(self,day,nBaseMeal,nRoti,nExtraFry,nDahi,nSplVeg,nSplNonVeg):
        self.TotBaseMeal = nBaseMeal + 4 + 2
        self.nExtraFry = nExtraFry
        self.TotSplVeg = nSplVeg
        self.TotNonVeg = nSplNonVeg + 4
        self.TotRoti   = nRoti + 9
        self.TotDahi   = nDahi
        if day in Fastdays:
            self.TotSplVeg = nSplVeg + 4
            self.TotNonVeg = nSplNonVeg


    def CalcRiceAndRoti(self,day):
        AttaInKg = self.TotRoti/25.0 
        RiceInKg = (self.TotBaseMeal*0.14 - AttaInKg)
        isSplBase = False
        if(DinnerBaaji_dict[day]['Spl_Base'] != "None"):
            isSplBase = True
        if(DinnerBaaji_dict[day]['Spl_Base'] == "Kichadi" and isSplBase == True):
            print('Today is Kichadi, Sorry :(')
            SplBase_dict = DinnerBaaji_dict[day]['SplBaseIngri']
            for item,qty in SplBase_dict.items():
                Qty = qty*self.TotBaseMeal
                print(f'{item} : {Qty/1000} Kg')
            # print(f'Rice :  {80*self.TotBaseMeal/1000} Kg')
            # print(f'Mung Daal : {80*self.TotBaseMeal/1000} Kg')
            # print(f'Cauliflower : {0.010*self.TotBaseMeal} Kg')
            # print(f'Beans : {0.010*self.TotBaseMeal} Kg')
            # print(f'Gajjar : {0.005*self.TotBaseMeal} Kg')
            print('Atta : ',AttaInKg,' Kg for ',self.TotRoti,' people')
            print(f'Base Meal {self.TotBaseMeal-4} + 4 = {self.TotBaseMeal}')
            print(f'No. of Roti {self.TotRoti}')
        elif(DinnerBaaji_dict[day]['Spl_Base'] == "Fried Rice" and isSplBase == True):
            print('Hooray Today is Fried Rice')
            print('Atta : ',AttaInKg,' Kg for ',self.TotRoti,' people')
            print('Jeera Rice : ',RiceInKg*1.2, ' Kg for ',self.TotBaseMeal,' people')
            SplBase_dict = DinnerBaaji_dict[day]['SplBaseIngri']
            for item,qty in SplBase_dict.items():
                Qty = qty*self.TotBaseMeal
                print(f'{item} : {Qty/1000} Kg')
            print(f'Base Meal {self.TotBaseMeal-4} + 4 = {self.TotBaseMeal}')
            print(f'No. of Roti {self.TotRoti}')

            # print('Beans for Fried Rice: ',10*self.TotBaseMeal/1000,' Kg')
            # print('Gobi for Fried Rice: ',10*self.TotBaseMeal/1000,' Kg')
            # print('Gajjar for Fried Rice: ',10*self.TotBaseMeal/1000,' Kg')
            # print('Grean Peas for Fried Rice: ',5*self.TotBaseMeal/1000,' Kg')

        else:
            print('Atta : ',AttaInKg,' Kg for ',self.TotRoti,' people')
            print('Rice : ',RiceInKg, ' Kg for ',self.TotBaseMeal,' people')

    def CalcDaal(self,day):
        if day == 'Saturday':
            print(f'Arhad Daal: {0.75/50 * self.TotRoti} Kg')
        else:
            DaalDict = DinnerBaaji_dict[day]['Daal']
            for daal,qty in DaalDict.items():
                Qty = qty*self.TotBaseMeal
                print(f'{daal} : {Qty/1000} Kg')

    def CalcBaaji(self,day):
        self.TotBaaji = self.TotBaseMeal + self.nExtraFry
        VegDict = DinnerBaaji_dict[day]['Ingridients']
        for veg,qty in VegDict.items():
            Qty = qty*self.TotBaaji
            if veg == "Coconut":
                print(f'{veg} needs 2 nos')
            else:
                print(f'{veg} needs {Qty/1000} Kg')
    def CalcDessert(self,day):
        self.TotDesert = self.TotBaseMeal
        DessertDict = DinnerBaaji_dict[day]['Dessert']
        for ing,qty in DessertDict.items():
            if ing == "Sweets":
                print('No. of Sweets :',self.TotBaseMeal)
            else:
                Qty = qty*self.TotDesert
                print(f'{ing} : {Qty/1000}')

    def CalcSplNonVeg(self,day):
        NonVegDict = DinnerNonVeg_dict[day]['Ingridients']
        dish = DinnerNonVeg_dict[day]['Name']
        if dish == 'Egg Omlet' or dish == 'Egg-Alu-Jhol':
            print(f'No. of Egg :  {2*self.TotNonVeg}')
        else:
            for non,qty in NonVegDict.items():
                Qty = qty*self.TotNonVeg
                if non == 'Fish':
                    print(f'{non} needs {Qty/1000} kg and {self.TotNonVeg} pieces')
                else:
                    print(f'{non} needs {Qty/1000} Kg')
        
    def CalcSplVeg(self,day):
        SplVegDict = DinnerSplVeg_dict[day]['Ingridients']
        for veg,qty in SplVegDict.items():
            Qty = qty*self.TotSplVeg
            print(f'{veg} needs {Qty/1000} Kg')

    def DinnerSummary(self,day,nExtra):
        self.CalcRiceAndRoti(day)
        self.CalcDaal(day)
        self.CalcBaaji(day)
        self.CalcSplNonVeg(day)
        self.CalcSplVeg(day)
        self.CalcDessert(day)

    def ListOfDinner(self,day):
        print("*"*15,"Today's Menu","*"*15)
        print(f'Base Meal for Dinner {self.TotBaseMeal-4} + 4 = {self.TotBaseMeal}')
        print(f'No. of Roti for Dinner {self.TotRoti}')
        baajiName = DinnerBaaji_dict[day]['Name']
        print('No. Dahi packets ',self.TotDahi)
        print(f'No. of {baajiName} for Dinner {self.TotBaaji-self.nExtraFry} + {self.nExtraFry} plates ')
        NonVegDishName = DinnerNonVeg_dict[day]['Name']
        VegDishName = DinnerSplVeg_dict[day]['Name']
        if day in Fastdays:
            print(f'No. of {NonVegDishName} Spl Non-Veg {self.TotNonVeg} plates')
            print(f'No. of {VegDishName} Spl Veg {self.TotSplVeg-4} + 4 = {self.TotSplVeg} plates')
        else:
            print(f'No. of {NonVegDishName} Spl Non-Veg {self.TotNonVeg-4} + 4 = {self.TotNonVeg} plates')
            print(f'No. of {VegDishName} Spl Veg {self.TotSplVeg} plates')
        desert = DinnerBaaji_dict[day]['Desert Name']
        print(f'No. of desert {desert}')



        


    

    
