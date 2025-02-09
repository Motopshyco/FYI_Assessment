QA Assessment Mateo Florez

This is the QA assessment created by Mateo Florez and here you can find 4 different scenarios: 

- Terms of Service Page Displays "©2024 FYI.FYI, Inc." at the Bottom
- Hamburger Menu Contains Correct User Selection Options
- Contact Support Button Redirects User to the Submit Request Page
- Verify Search Results for "AI" on the Submit a Request Page

For each scenario you can find 2 different approaches one of them with BDD and the other one just a test script
implemented in a page object model framework

You can find the test scripts in the folder "tests_scripts" and all the related methods for each page in the folder 
"pages". To execute the scenarios with this approach you will need:

- Python: install python in your pc
- If you are in a venv use "deactivate"
- Create a new venv using "python -m venv env_name" and activate it using ".\env_name\Scripts\activate"
- Copy the chromedriver in ".venv\Scripts"
- Selenium: run the command "pip install selenium"

Now you can run the tests executing the command "python -m unittest tests_scripts/fyi_tests.py" in your console or using
the run option in your IDE

The structure of the BDD framework is as follows:

- Project
  - Features (In this folder you can find the feature files with the scenarios e.g. "fyi_common_tests.feature" and the 
  environment.py file with the hooks that are executed before or after each scenario or step)
    - steps (In this folder you can find the different steps for each page e.g. "common_steps.py")
  - pages(In this folder you can find the pages with their methods to use in the steps e.g. "common_page.py")

 To execute the scenarios with BDD you will need:

- Python: install python in your pc
- Selenium: run the command "pip install selenium"
- Gherkin plugin in your IDE
- Behave: run the command "pip install behave selenium"
- Hamcrest: run the command "pip install PyHamcrest"

After this configuration you can execute the BDD scenarios running the command "Behave" in your console

For the BDD scenarios is also able the option to get the execution report and a screenshot if any step fails, to get
this reports you will need:

- Java: install java in your pc and configure the JAVA_HOME environment variable
- Allure: run the command "pip install allure-behave"
- Allure CLI: download the allure-framework in your pc and the path of the bin folder in your Path environment variable
- Execute the scenarios using "behave -f allure_behave.formatter:AllureFormatter -o allure-results"
- Generate the report using "allure generate allure-results -o allure-report --clean"
- Open the report using "allure open allure-report"

Using this steps you can see the report and check the screenshots if something fails in the execution
