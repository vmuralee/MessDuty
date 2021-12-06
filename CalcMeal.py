from MessDuty import *

'''
*  Please make sure that you install the python3 
*  Change The day Accordingly with Daily Booking link
*  Specify the no. of items for BreakFast,Lunch and Dinner class
*  The Command for running the Mess Dishes  =>  python3 CalcMeal.py > TextFile.txt

'''

isPaapad = True  # Check the boolean with your specific day
isSaalad = True  # Check the boolean with your specific day

print('='*15,' BreakFast ','='*15)   
breakfast = BreakFast(nBread=10,nEggs=23,nKela=24,nTea=10,nMilk=10,nIndian=43)     
breakfast.BreakFastSummary('Tuesday')
print('='*15,' Lunch ','='*15)
lunch = Lunch(day='Tuesday',nBaseMeal=61,nRoti=57,nExtraFry=0,nDahi=16,nSplVeg=12,nSplNonVeg=29,isPaapad=isPaapad,isSaalad=isSaalad)
lunch.LunchSummary('Tuesday')
lunch.ListOfLunch('Tuesday')
print('='*15,' Dinner ','='*15)
dinner = Dinner(day='Tuesday',nBaseMeal=58,nRoti=86,nExtraFry=0,nDahi=0,nSplVeg=9,nSplNonVeg=25)
dinner.DinnerSummary('Tuesday',0)
dinner.ListOfDinner('Tuesday')
