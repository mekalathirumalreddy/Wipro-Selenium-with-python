📄 testcases1.robot (Console Output)
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify Login - Console
    Log To Console    Enter Username
    Log To Console    Enter Password
    Log To Console    Click on login button
    Log To Console    User is on the home page