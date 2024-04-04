# In this file I have outlined the test cases for this specific project:

## Test Case ID 1: 
QEII001

### Test Case Name: 
Negative Numbers

### Test Description: 
Ensure that the application restricts the input of invalid values such as negative numbers inside the field for quantity of products A,B,C and D.

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Enter negative numbers for each quantity of product field.
3. Click the "Calculate" button.
4. Verify that a message pops for the first negative number in place disallowing the calculus.

### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
Negative numbers between -99999 and -1.

### Expected Result:
Once the negative numbers are placed and the Calculate button is pressed, the application should pop a message claiming that the value must be above or equal to 0.

### Actual Result:
As expected.

### Test Status:
Pass.


## Test Case ID 2: 
QEII002

### Test Case Name: 
Valid Inputs and Correct Calculations

### Test Description: 
Ensure that the application functions properly for the input of valid values inside the field for quantity of products A,B,C and D and makes the correct calculation based on the table.

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Enter whole numbers for each quantity of product field.
3. Click the "Calculate" button.
4. Verify that the order summary message has the correct calculations based on the table.

### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
Whole numbers between 0 and 99999.

### Expected Result:
Once the valid inputs are placed and the Calculate button is pressed, the application should show the order summary with the correct calculations.

### Actual Result:
As expected.

### Test Status:
Pass.


## Test Case ID 3: 
QEII003

### Test Case Name: 
Decimal Numbers

### Test Description: 
Ensure that the application restricts the input of invalid values such as decimal numbers inside the field for quantity of products A,B,C and D.

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Enter decimal numbers for each quantity of product field.
3. Click the "Calculate" button.
4. Verify that a message pops for the first decimal number in place disallowing the calculus.

### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
Decimal numbers separated by a dot or a comma (eg. 12,5 or 12.5). 

### Expected Result:
Once the decimal numbers are placed and the Calculate button is pressed, the application should pop a message claiming that you need to input a correct value and would give you the 2 whole numbers closer to that decimal number.

### Actual Result:
As expected.

### Test Status:
Pass.


## Test Case ID 4: 
QEII004

### Test Case Name: 
Letters and symbols.

### Test Description: 
Ensure that the application restricts the input of invalid values such as letters and symbols inside the field for quantity of products A,B,C and D.

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Enter letters and symbols for each quantity of product field.
3. Click the "Calculate" button.
4. Verify that a message pops for the first letter or symbol in place disallowing the calculus.

### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
Letter "e" and symbol "-". Other letters or symbols cant even be placed.

### Expected Result:
Once the letter or symbol are placed and the Calculate button is pressed, the application should pop a message claiming that you need to enter a number.

### Actual Result:
As expected.

### Test Status:
Pass.


## Test Case ID 5: 
QEII005

### Test Case Name: 
Check stock

### Test Description: 
Ensure that the application rejects the order if any quantity of any product exceeds the available stock.

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Enter a 10 digit whole number for each quantity of product field.
3. Click the "Calculate" button.
4. Verify that a message pops indicating that stock isn't available for the quantity entered.

### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
10 digit whole numbers.

### Expected Result:
Once the 10 digit whole numbers are placed and the Calculate button is pressed, the application should pop a message claiming that stock isn't available for the quantity entered.

### Actual Result:
The application proceeds with the calculus of large numbers and gives you the order summary with those values.

### Test Status:
Failed.


## Test Case ID 6: 
QEII006

### Test Case Name: 
Empty Values

### Test Description: 
Ensure that the application pops a message in case any of the quantity fields are empty disallowing the calculus. 

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Click the "Calculate" button.
3. Verify that a message pops indicating that any field can't be empty.

### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
N/A

### Expected Result:
Once the Calculate button is pressed, the application should pop a message indicating that any field can't be empty.

### Actual Result:
The application doesn't show any message and does nothing after pressing the "Calculate" button.

### Test Status:
Failed.


## Test Case ID 7: 
QEII007

### Test Case Name: 
Displays in Chrome, Firefox and Microsoft Edge

### Test Description: 
Ensure that the application displays properly inside Chrome, Firefox and Microsoft Edge.

### Test Steps:
1. Navigate to http://127.0.0.1:5000/ inside a Chrome Browser.
2. Verify if the page application properly displays.
3. Navigate to http://127.0.0.1:5000/ inside a Firefox Browser.
4. Verify if the page application properly displays.
5. Navigate to http://127.0.0.1:5000/ inside a Microsoft Edge Browser.
6. Verify if the page application properly displays.


### Test Prerequisites:
-Have Google Chrome version 110 or above.
-Have Firefox version 115.9.1 or above.
-Have Microsoft Edge version 96 or above.
-Windows 10 or above.
-app.py is running

### Test Data: 
N/A

### Expected Result:
The application properly displays in each browser listed.

### Actual Result:
As expected.

### Test Status:
Pass.