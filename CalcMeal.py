
from MessDuty import *
import sys
from datetime import date

today = date.today()

'''
*  Please make sure that you install the python3 
*  Change The day Accordingly with Daily Booking link
*  Specify the no. of items for BreakFast,Lunch and Dinner class
*  The Command for running the Mess Dishes  =>  python3 CalcMeal.py <day of week>  > TextFile.txt

'''


isPaapad = True  # Check the boolean with your specific day
isSaalad = True  # Check the boolean with your specific day

print("The Order List of ",today," menu are following")

try:
    day = sys.argv[1]
    print('='*15,' BreakFast ','='*15)   
    breakfast = BreakFast(nBread=10,nEggs=23,nKela=24,nTea=10,nMilk=10,nIndian=43)     
    breakfast.BreakFastSummary(day)

    print('='*15,' Lunch ','='*15)
    lunch = Lunch(day=day,nBaseMeal=61,nRoti=57,nExtraFry=0,nDahi=16,nSplVeg=12,nSplNonVeg=29,isPaapad=isPaapad,isSaalad=isSaalad)
    lunch.LunchSummary(day)
    lunch.ListOfLunch(day)

    print('='*15,' Dinner ','='*15)
    dinner = Dinner(day=day,nBaseMeal=58,nRoti=86,nExtraFry=0,nDahi=0,nSplVeg=9,nSplNonVeg=25)
    dinner.DinnerSummary(day,0)
    dinner.ListOfDinner(day)
except:
    print("Give the argument day such as Monday,Tuesday,Wednesday,Thursday,Saturday,Sunday")


