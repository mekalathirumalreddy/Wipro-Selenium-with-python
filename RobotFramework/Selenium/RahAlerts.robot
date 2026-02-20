*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
verify dropdown selections
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible      alertbtn
    Click Element    alertbtn
    Handle Alert     action=ACCEPT    timeout=6
    sleep    10s

    Click Element    confirmbtn
    Handle Alert     action=DISMISS    timeout=6
    sleep    10s


    Close Browser



