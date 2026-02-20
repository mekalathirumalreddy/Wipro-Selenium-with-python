📄 testcases2.robot (Only Log Report)
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify Login - Log Only
    Log    Enter Username
    Log    Enter Password
    Log    Click on login button
    Log    User is on the home page