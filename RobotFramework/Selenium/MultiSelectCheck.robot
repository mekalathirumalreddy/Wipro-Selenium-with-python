*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
verify login scenaio with valid creadentails
        Open Browser    ${url}    chrome
        #maximize the browser window
        Maximize Browser Window
        #identify the common elements attribute //type[@type='checkbox']
        ${elements}=     Get WebElements     xpath://input[@type='checkbox']
         FOR     ${element}     IN      @{elements}
            Click Element    ${element}
            Sleep    3s
         END
        #close browser
        Sleep    20s
        Close Browser