*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php/

*** Test Cases ***
verify dropdown selections
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    //select[@id='state']

    # Get default selected option
    @{labels}=    Get Selected List Labels    //select[@id='state']
    Log    ${labels}

    # Select by visible text (label)
    Select From List By Label    //select[@id='state']    Option3
    Sleep    2s

    # Select by index (0-based)
    Select From List By Index    state    2
    Sleep    2s

    # Select by value
    Select From List By Value    id=dropdown-class-example    option1
    Sleep    2s

    Close Browser
