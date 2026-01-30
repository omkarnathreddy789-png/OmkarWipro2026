*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.google.com
${BROWSER}   chrome
${TITLE}     Google

*** Test Cases ***
Open Website And Verify Title
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    ${TITLE}
    Capture Page Screenshot
    Close Browser
