# Test Automation Framework Using Selenium 4

Proof of concept of a test automation framework with selenium over python 3 (v3.10) as language binding. The following codebase is built upon the popular page object model design pattern to keep the test cases and pages decoupled from each other and comprises of the following directories:
Configurations: The config.json file comprises of initial configurations such as the base URL of the application under test, i.e. the entry point of the test cases to be executed. 
<ul>
   <li>
      <b>Configurations:</b> The config.json file comprises of initial configurations such as the base URL of the application under test, i.e. the entry point of the test cases to be executed. Please provide the username and password as base64 encoded strings in this file. They will be decoded to plain text during the test runs
   </li>
   <li> <b> Logs: </b> Placeholder directory for all the logs that will be generated during the test run. Frameworklog.log file will be generated inside this directory during the test run </li>
   <li> <b> Page-Objects: </b> This directory represents the programmatic model of the pages of the application under test. Use this folder for placing all the elements and corresponding functionalities of the pages such as clicking on a button, entering text in a textbox, etc. </li>
   <li> <b> Test-Cases: </b> This directory represents the actual test cases that have been automated. Place all the testcases leveraging the elements from the page object. </li>     
   <li> <b> Reports: </b> Create this directory if reports are required. Allure reporting framework has been used due to its legible and easy to understand user interface. </li>
<li> <b> Utils: </b> This directory contains all the other common elements that can be used in the test cases like logger, a class representing logging functionality, and wrapper functions built over selenium to interact with the elements on the pages. </li>
</ul>
Following are the instructions to get this framework up and running: 
<ul>
   <li>	Ensure that you have python 3 installed. Clone this repository and it will create a folder named “SeleniumDemo”</li>
    <li>Change directory to this folder and run the following command which will create a virtual environment </li>
   <pre>python -m venv VENV</pre>
   Open command command prompt inside the created virtual environment folder and change the directory to "Scripts" type "activate.bat" to activate the virtual enviroment before proceeding. 
   <b>Note:</b> If you get an error then you have to open Windows Powershell as an admin and set the execution policy to Unrestricted. Use the following command to do so: <code>Set-ExecutionPolicy Unrestricted </code> and try again activation the environemnt
    <li>3.	Install the required dependencies using the following commands </li>
   <pre><code>Pip install selenium </code></pre>
   <pre><code>Pip install pytest </code> </pre>
   <pre><code>Pip install allure-pytest </code> </pre>
   If you're using an IDE like PyCharm then add these dependencies to the cloned project repository accordingly 
   <li> Download allure reports from the following url and add its bin folder to SYSTEM PATH: 
    <pre> https://docs.qameta.io/allure/  </li> </pre> 
</ul>

## Executing the Test Cases

In order to execute the test cases please use either of the following commands: 
<pre>pytest -v -s TestCases\ </pre>

### Executing the Test Cases & Generating Allure Reports 
This command will only execute the test cases, no allure reports will be generated and the default browser is configured to be Edge 
<pre>pytest -v -s TestCases\ --alluredir=".\Reports"</pre>

### Viewing Generated Allure Reports 
This command will execute the test cases as well as generate the allure reports. In order to see the generated reports run the following commands from the terminal
<pre>
   cd Reports
   allure serve .
</pre>

## Changing The Browser For Test Execution
This supports the following browsers
<ul>
   <li>Edge Browser (Chromium Based)</li>
   <li>Google Chrome</li>
   <li>Mozilla Firefox</li>
</ul>

Use the <code>--browser</code> option to specify a browser, if no browser is specified the test cases will run on Edge by default. Below is the actual usage of the option

<pre>
   pytest -v -s TestCases\ --alluredir=".\Reports" --browser [chrome|firefox]
</pre>

## Adding A Github Token 
When using firefox, you might encounter an error stating that the maximum limit has reached and authentication is required, in such a case you need to generate a gurhub authorization token and add it as a USER PATH variable. In order to generate a github token follow the given steps:

<ol>
   <li>Login to your Github Account</li>
   <li>Click on your profile picture</li>
   <li>Select "Settings" from the menu</li>
   <li>Scroll to the bottom and click "Developer Settings"</li>
   <li>Click on Personal access tokens</li>
   <li>Click on "Generate new token" button</li>
   <li>Add a note (optional)</li>
   <li>Click on "Generate Token"</li>
</ol>

copy the value of the token and save it as a user path variable named GH_TOKEN (This name has to be GH_TOKEN). Follow the steps below to do the same:

<ol>
   <li>Click on Start Menu and open Run</li>
   <li>Type in "sysdm.cpl" (without quotes) and hit enter</li>
   <li>Select "Advanced" tab and click on "Environment Variables"</li>
   <li>In the User variables section, Click on "New"</li>
   <li>Provide the name as GH_TOKEN (The name is important!)</li>
   <li>Paste the token you copied from Github in the value field and click "OK"</li>
   <li>Click OK again</li>
</ol>
