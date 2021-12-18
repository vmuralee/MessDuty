# MessDuty

## Installation
You have to make sure that your system already have git and python3, please try to install the latest stable version of python3. After that
please add the following commands in your terminal.
```
git clone https://github.com/vmuralee/MessDuty.git
cd MessDuty
```
If you are wanted to change the mess menu for new month, please create a new branch with branch name as current month. For example,
```
git checkout -b January
```
Otherwise, you can skip above step.
## How to run the code
In the Respective ***MessDuty*** folder you have to edit the CalcMeal.py file. Important things you have to check are,
- Check the *isPappad* boolean, it should be __True__ whether the day has pappad.
- Check the *isSaalad* boolean, it should be __True__ whether the day has Salad.
- Edit __BreakFast,Lunch and Dinner__ classes with __day,No of items,.. etc.__ in the respective day. 

Once you updated the file run the following command,
```
python3 CalcMeal.py <day of week>  > "Text file"
```
An example is given below,
```
python3 CalcMeal.py Sunday  > OutFile.txt
```
A new file created with the all the ingrediant an their respective measurement for the specific day. 

## Changing the Menu 
If you are preparing a new menu, you can easily modify the package. Go to the ***.json*** files and change accordingly to your new menu. Please consult the __PMC__ before you make the changes. Once you set the menu, you don't have to worry anymore. The code will take care the rest of calculation. It is strongly advice those who are created new menu should do a manual calculation and cross check with compiled result.  
Once you set the menu please give the pull request to respirotary.