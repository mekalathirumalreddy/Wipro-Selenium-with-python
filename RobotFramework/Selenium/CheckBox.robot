*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
verify login scenaio with valid creadentails
        Open Browser    ${url}    chrome
        #maximize the browser window
        Maximize Browser Window
        #wait until element is loaded
        sleep   5s
        Wait Until Element Is Visible    c_bs_1
#click radio
        Click Element    c_bs_1
        #click on check box 3
        Click Element    c_bs_2
        #close browser
        Sleep    20s
        Close Browser