*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://www.saucedemo.com/

*** Test Cases ***
verify login scenario with valid creadentails
        Open Browser    ${url}    chrome
        #maximize the browser window
        Maximize Browser Window
        #wait until element is loaded
        Wait Until Element Is Visible    //input[@id='user-name']
        #enter the username in the username field
        Input Text    //input[@id='user-name']    standard_user
        #enter text into the password
        Input Text    //input[@id='password']    secret_sauce
        #click the log in button
        Click Element    //input[@id='login-button']
        #validate that the user is on the home page
        Wait Until Element Is Visible    //div[@class='app_logo']
        Element Should Be Visible    //div[@class='app_logo']
        #close browser
        Sleep    10s
        Close Browser