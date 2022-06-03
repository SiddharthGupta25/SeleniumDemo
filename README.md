# Test Automation Framework Using Selenium 4

Proof of concept of a test automation framework with selenium over python 3 (v3.10) as language binding. The following codebase is built upon the popular page object model design pattern to keep the test cases and pages decoupled from each other and comprises of the following directories:
Configurations: The config.json file comprises of initial configurations such as the base URL of the application under test, i.e. the entry point of the test cases to be executed. 
<ul>
   <li> <b> Logs: </b> Placeholder directory for all the logs that will be generated during the test run. Frameworklog.log file will be generated inside this directory during the test run </li>
   <li> <b> Page-Objects: </b> This directory represents the programmatic model of the pages of the application under test. Use this folder for placing all the elements and corresponding functionalities of the pages such as clicking on a button, entering text in a textbox, etc. </li>
   <li> <b> Test-Cases: </b> This directory represents the actual test cases that have been automated. Place all the testcases leveraging the elements from the page object. </li>     
   <li> <b> Reports: </b> Create this directory if reports are required. Allure reporting framework has been used due to its legible and easy to understand user interface. </li>
<li> </b> Utils: </b> This directory contains all the other common elements that can be used in the test cases like logger, a class representing logging functionality, and wrapper functions built over selenium to interact with the elements on the pages. </li>
</ul>
Following are the instructions to get this framework up and running: 
<ul>
   <li>	Ensure that you have python 3 installed. Clone this repository and it will create a folder named “SeleniumDemo”</li>
    <li>Change directory to this folder and run the following command which will create a virtual environment </li>
   <pre>python -m venv VENV</pre>
    <li>3.	Install the required dependencies using the following commands </li>
   <pre> a.	Pip install selenium</pre>
   <pre>b.	Pip install pytest </pre>
   <li> Download allure reports from the following url and add its bin folder to SYSTEM PATH: 
    <pre> https://docs.qameta.io/allure/  </li> </pre> 
</ul>
