*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Login
    Log    Enter username
    Log    Enter password
    Log    Click on login button
    Log    User is on the home page


Launch Browser
        Log   Launching the browser
Close the Browser
        Log   Closing the browser

Open DB
        Log   Launching the browser
Close DB
        Log   Closing the browser