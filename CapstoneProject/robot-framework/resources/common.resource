*** Settings ***
Library    SeleniumLibrary
Library    String
Variables  ../variables/config.py

*** Keywords ***
Open Application
    [Arguments]    ${browser}=${BROWSER}
    Open Browser    ${URL}    ${browser}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}

Close Application
    Close All Browsers

Handle Ads Popup
    Run Keyword And Ignore Error    Click Element    css:button[aria-label='Close']
    Run Keyword And Ignore Error    Execute Javascript    document.body.classList.remove('modal-open')

Go To Login Page
    Go To    https://practice.automationtesting.in/my-account/
    Wait Until Element Is Visible    id=username
    Handle Ads Popup

Take Test Screenshot
    Capture Page Screenshot    ${TEST NAME}.png

Capture Failed Screenshot
    ${clean}=    Replace String    ${TEST NAME}    ${SPACE}    _
    ${file}=     Set Variable    FAILED_${clean}.png
    Capture Page Screenshot    ${file}

Ensure Logged Out
    Run Keyword And Ignore Error    Click Element    xpath=//a[text()='Logout']