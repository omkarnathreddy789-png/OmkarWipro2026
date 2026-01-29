*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google

*** Test Cases ***
TestCase1.robot
    Open Application
    Title Should Be    Google
    Close Browser