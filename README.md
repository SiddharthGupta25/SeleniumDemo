# Hybrid Test Automation Framework Using Selenium 4

Proof of concept of a test automation framework with selenium over python 3 (v3.10) as language binding. The following codebase is built upon the popular page object model design pattern via PyTest library to keep the test cases and pages decoupled from each other and comprises of the following directories:
<ul>
   <li>
      <b>Configurations:</b> The config.json file in this directory comprises of the initial configurations such as the base URL of the application under test, i.e. the entry point of the test cases to be executed. Please provide the username and password as base64 encoded strings in this file. They will be decoded to plain text during the test runs
   </li>
   <li> <b> Logs: </b> Placeholder directory for all the logs that will be generated during the test run. Frameworklog.log file will be generated inside this directory during the test run </li>
   <li> <b> Page-Objects: </b> This directory represents the programmatic model of the pages of the application under test. Use this folder for placing all the elements and corresponding functionalities of the pages such as clicking on a button, entering text in a textbox, etc. </li>
   <li> <b> Test-Cases: </b> This directory represents the actual test cases that have been automated. Place all the testcases leveraging the elements from the page object. </li>
   <li>
      <b>Test-Data:</b> Place your <code>.csv</code> test data files in this directory and leverage the methods defined in the framework to parameterize your tests accordingly 
   </li>
   <li> <b> Reports: </b> Create this directory if reports are required. Allure reporting framework has been used due to its legible and easy to understand user interface. </li>
<li> <b> Utils: </b> This directory contains all the other common elements that can be used in the test cases like logger, a class representing logging functionality, and wrapper functions built over selenium to interact with the elements on the pages. </li>
</ul>
Following are the instructions to get this framework up and running: 
<ul>
   <li>	Ensure that you have python 3 installed. Clone this repository via terminal. It will create a folder named “SeleniumDemo”</li>
    <li>Change directory to this folder and run the following commands </li>
   <pre>
      <code>python -m venv VENV</code>
      <code>cd VENV\Scripts\</code>
      <code>activate.bat</code> 
   </pre>
 
   <b>Note:</b> If you get an error related to activation of the environment, then you have to open Windows Powershell as an admin and set the execution policy to Unrestricted. Use the following command to do so: <code>Set-ExecutionPolicy Unrestricted </code> and try again activating the environemnt. 
   <br/> <br/>
    <li>Install the required dependencies using the following commands: </li>
   <pre><code>pip install selenium </code></pre>
   <pre><code>pip install pytest </code> </pre>
   <pre><code>pip install allure-pytest </code> </pre>
   <pre><code>pip install webdriver_manager </code> </pre>
 
   <li> Download allure reports from the following url: </li> <br/>
      <a href="https://docs.qameta.io/allure/"> https://docs.qameta.io/allure/  </a>  <br/>
   Add its bin folder's path to SYSTEM PATH for ease. 
</ul>

## Executing the Test Cases

In order to execute the test cases please use either of the following commands: 

<pre>
<code> pytest -v -s TestCases\ </code>
</pre>

This command however, will only execute the test cases, no allure reports will be generated and the default browser is configured to be Edge. To generate the reports alongside, use the command below: 


### Executing the Test Cases & Generating Allure Reports 

<pre>
   <code>  pytest -v -s TestCases\ --alluredir=".\Reports" </code>
</pre>

### Viewing Generated Allure Reports 
This command will execute the test cases as well as generate the allure reports in a format which is not user friendly enough. In order to see the generated reports in a legible format, run the following commands from the terminal (ensure to run these commands from the project root)
<pre>
   cd Reports
   allure serve .
</pre>

### Screenshots Of Failed Test Cases
Screenshots only for failed test cases will be included automatically in the generated allure reports by a fixture defined in .\TestCases\conftest.py file.

## Changing The Browser For Test Execution
This supports the following browsers
<ul>
   <li>Microsoft Edge </li>
   <li>Google Chrome</li>
   <li>Mozilla Firefox</li>
</ul>

Use the <code>--browser</code> option to specify a browser, if no browser is specified the test cases will run on Edge by default. Below is the actual usage of the option:

<pre>
  <code> pytest -v -s TestCases\ --alluredir=".\Reports" --browser [chrome|firefox] </code>
</pre>

## Generating A Github Token 
When using firefox, you might encounter an error stating that the maximum limit has reached and authentication is required, in such a case you need to generate a Github authorization token and add it as a USER PATH variable. In order to generate a github token follow the given steps:

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

copy the value of the token and save it as a user path variable by Following the steps below to do the same:

## Adding A Github Token In User Path Variable
<ol>
   <li>Click on Start Menu and open Run</li>
   <li>Type in "sysdm.cpl" (without quotes) and hit enter</li>
   <li>Select "Advanced" tab and click on "Environment Variables"</li>
   <li>In the User variables section, Click on "New"</li>
   <li>Provide the name as GH_TOKEN (The name is important!)</li>
   <li>Paste the token you copied from Github in the value field and click "OK"</li>
   <li>Click OK again</li>
</ol>
<hr/>
The codebase is subjected to future improvements.  
