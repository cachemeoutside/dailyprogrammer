# Challenge #379 [Easy] Progressive taxation

## Reference
[Link to challenge](https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation)

### Solution
* Create a class to keep track of what is in a tax bracket
  * lower income
  * upper income
  * rate for associated bracket
* Allow program to read a CSV file that allows various tax brackets to be imported
* Program reads CSV file to import tax brackets into program
* A list of sample incomes are provided and hardcoded in the program for testing input
* The program iterates through the list of income
  * checks if the income exceeds maxed allowed income
    * if income does not exceed
      * iterate through each tax bracket and calculate taxes owed per bracket
      * Loop ends with a return value when income lies between a bracket range
    * else, exit out of the program
    

### Usage
```
python3 progressive_taxation.py
```
