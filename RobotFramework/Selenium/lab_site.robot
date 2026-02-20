*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}     https://www.saucedemo.com/

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser     ${url}    firefox
    Maximize Browser Window

    Wait Until Element Is Visible    id:user-name
    Input Text    id:user-name    standard_user

    Wait Until Element Is Visible    id:password
    Input Text    id:password    secret_sauce

    Click Button    id:login-button

    Wait Until Element Is Visible    //img[@alt='Sauce Labs Backpack']
    Click Button    //img[@alt='Sauce Labs Backpack']


    Wait Until Element Is Visible    id:checkout
    Click Element    id:checkout

    Wait Until Element Is Visible    id:first-name
    Input Text    id:first-name    Varun
    Input Text    id:last-name     Reddy
    Input Text    id:postal-code   508222

    Click Element    id:continue

    Wait Until Element Is Visible    id:finish
    Click Element    id:finish

    Element Should Be Visible    //img[@alt='Pony Express']

    Close Browser
