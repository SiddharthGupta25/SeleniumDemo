# Test Automation Framework Using Selenium 4

Proof of concept of a test automation framework with selenium over python 3 (v3.10) as language binding. The following codebase is built upon the popular page object model design pattern to keep the test cases and pages decoupled from each other and comprises of the following directories:
Configurations: The config.json file comprises of initial configurations such as the base URL of the application under test, i.e. the entry point of the test cases to be executed. 
Logs: Placeholder directory for all the logs that will be generated during the test run. Frameworklog.log file will be generated inside this directory during the test run
Page-Objects: This directory represents the programmatic model of the pages of the application under test. Use this folder for placing all the elements and corresponding functionalities of the pages such as clicking on a button, entering text in a textbox, etc. 
Test-Cases: This directory represents the actual test cases that have been automated. Place all the testcases leveraging the elements from the page object.     
Reports: Create this directory if reports are required. Allure reporting framework has been used due to its legible and easy to understand user interface. 
Utils: This directory contains all the other common elements that can be used in the test cases like logger, a class representing logging functionality, and wrapper functions built over selenium to interact with the elements on the pages. 
Following are the instructions to get this framework up and running: 
<ul>
   <li>	Ensure that you have python 3 installed. Clone this repository and it will create a folder named “SeleniumDemo”</li>
    <li>Change directory to this folder and run the following command which will create a virtual environment </li>
    python -m venv VENV
    <li>3.	Install the required dependencies using the following commands </li>
    a.	Pip install selenium
    b.	Pip install pytest 
   <li> Download allure reports from the following url and add its bin folder to SYSTEM PATH: 
    https://docs.qameta.io/allure/  </li>
</ul>
