*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
verify login scenaio with valid creadentails
        Open Browser    ${url}    chrome
        #maximize the browser window
        Maximize Browser Window
        #wait until element is loaded
        Wait Until Element Is Visible    xpath://input[@name='username']
        #enter the username in the username field
        Input Text    xpath://input[@name='username']    admin
        #enter text into the password
        Input Text    xpath://input[@name='password']    admin123
        #click the log in button
        Click Element    xpath://button[@type='submit']
        #validate that the user is on the home page
        Wait Until Element Is Visible    //h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
        Element Should Be Visible    //h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
        #close browser
        Sleep    10s
        Close Browser