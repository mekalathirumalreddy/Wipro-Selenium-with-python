*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://the-internet.herokuapp.com/download

*** Test Cases ***
Verify file download
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    //a[normalize-space()='upload.txt']
    Click Element    //a[normalize-space()='upload.txt']

    Sleep    5s
    Close Browser
