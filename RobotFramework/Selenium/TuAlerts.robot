*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://www.tutorialspoint.com/selenium/practice/alerts.php

*** Test Cases ***
verify dropdown selections
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible      //button[normalize-space()='Alert']
    Click Element    //button[normalize-space()='Alert']
    Handle Alert      timeout=6       action=ACCEPT
    sleep    10s

    Click Element    //button[@onclick='myMessage()']
    Handle Alert     action=ACCEPT    timeout=6
    sleep    10s

    Click Element    desk
    Handle Alert     action=ACCEPT    timeout=6
    sleep    10s

    Click Element    //button[@onclick='myPromp()']
    Input Text Into Alert    Hello
    Sleep    10s

    Close Browser



