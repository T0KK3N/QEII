# QEII - DANIEL MORA

## Project Description
This project is intended to provide a solution for Problem #2. No further information is provided to mantain the secrecy of the project.

## Files Description
The project contains the development of the app, the test cases and the automated script providing the solution for the test case #1 (Negative Numbers):

Backend:
app.py (Developed with the framework Flask for web apps)

Frontend: 
1. Folder "static" - folder "css" - styles.css (CSS)
                - folder "js" - script.js (Javascript)

2. Folder "templates" - index.html (HTML)

Test Cases:
testcases.md (Contains 7 test cases)

Test Script:
test_negative_numbers.py (Selenium)

## Technologies used:
1. Python 3.12.2
2. Selenium 4.18.1
3. Chrome webdriver 122.0.6261.111
4. Flask 3.0.2
5. VsCode 1.87.0

## Installation Process:
1. Make sure you have Python installed on your device. For this, you can download Python from here: https://www.python.org/. In my case I used the 3.12.2 version. Once you downloaded the installation wizard you just have to follow the wizard steps. I highly suggest you check the option for adding the PATH to the windows environment variables. To check if it is installed correctly just open a cmd and type: python --version or py --version. It will show the version if the installation was done correctly.
2. Then you need to install Selenium by typing in the cmd: pip install selenium. In case that does not work try: py -m pip install selenium
3. You need to install the chrome webdriver. In my case I used the 122.0.6261.111 and I downloaded from here: https://googlechromelabs.github.io/chrome-for-testing/ . Be sure to match the platform and the version of your Chrome driver; you can check it at by clicking the 3 dots in the top right corner of your Chrome browser, the Help - About Google Chrome. I suggest you paste the file inside C:\Program Files (x86).
4. In my case I used VsCode as my text editor to develop the app and test my python script. If using VsCode I suggest you add the Python(2024.2.1) and Code Runner(v0.12.1) inside the Extensions tab (I used the latest versions for both of them)

## Running The App:
1. You can open the QEII folder in VsCode. Before running the app, be sure to open a terminal and run pip install Flask to install the Flask framework.
2. Within the terminal inside the folder, run the command "py test_negative_numbers.py", it will load the app.py and test the script. If you just want to run the app then run "py app.py". It will run on http://127.0.0.1:5000


## Contact Information:
If you have any questions feel free to contact me at danielmora414@gmail.com 