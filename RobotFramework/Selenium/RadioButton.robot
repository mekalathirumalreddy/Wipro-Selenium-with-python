*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
verify login scenaio with valid creadentails
        Open Browser    ${url}    chrome
        #maximize the browser window
        Maximize Browser Window
        #wait until element is loaded
        sleep   5s
        Wait Until Element Is Visible    //input[@value='radio1']
#click radio
        Click Element    //input[@value='radio1']
        #click on check box 3
        Click Element    id attribute is not available for this element
        #close browser
        Sleep    20s
        Close Browser