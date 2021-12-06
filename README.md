# MessDuty

## Installation
You have to make sure that your system already have git and python3, please try to install the latest stable version of python3. After that
please add the following commands in your terminal.
```
git clone https://github.com/vmuralee/MessDuty.git
```
A folder of MessDuty will appear on your current directory.
## How to run the code
In the Respective ***MessDuty*** folder you have to edit the CalcMeal.py file. Important things you have to check are,
- Check the *isPappad* boolean, it should be __True__ whether the day has pappad.
- Check the *isSaalad* boolean, it should be __True__ whether the day has Salad.
- Edit __BreakFast,Lunch and Dinner__ classes with __day,No of items,.. etc.__ in the respective day. 

Once you updated the file run the following command,
```
python3 CalcMeal.py > OutputFile.txt
```
A new file created with the all the ingrediant an their respective measurement for the specific day. 

## Changing the Menu 
One can change the Menu and their respective quantities in the corresponding json file. 
