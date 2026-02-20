*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
verify dropdown selections
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible      //button[@onclick='jsAlert()']
    Click Element    //button[@onclick='jsAlert()']
    Handle Alert     action=ACCEPT    timeout=6
    sleep    10s

    Click Element    //button[@onclick='jsConfirm()']
    Handle Alert     action=DISMISS    timeout=6
    sleep    10s


    Click Element    //button[@onclick='jsPrompt()']
    Input Text Into Alert    Hello
    Sleep    10s

    sleep    10s

    Close Browser



