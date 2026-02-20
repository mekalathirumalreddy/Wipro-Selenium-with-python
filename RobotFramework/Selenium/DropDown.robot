*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
verify dropdown selections
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    id=dropdown-class-example

    # Get default selected option
    @{labels}=    Get Selected List Labels    id=dropdown-class-example
    Log    ${labels}

    # Select by visible text (label)
    Select From List By Label    id=dropdown-class-example    Option3
    Sleep    2s

    # Select by index (0-based)
    Select From List By Index    id=dropdown-class-example    2
    Sleep    2s

    # Select by value
    Select From List By Value    id=dropdown-class-example    option1
    Sleep    2s

    Close Browser
