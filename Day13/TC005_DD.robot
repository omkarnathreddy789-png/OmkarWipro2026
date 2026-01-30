*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s

OrangeHRM Login
    [Arguments]    ${USERNAME}    ${PASSWORD}

    Input Text    name=username    ${USERNAME}
    Input Text    name=password    ${PASSWORD}

    Capture Page Screenshot    beforelogin.png

    Click Button    xpath=//button[@type='submit']

    Wait Until Page Contains    Dashboard    10s
    Capture Page Screenshot    afterlogin.png

    Close Browser

*** Test Cases ***
TC005_DD
    Open OrangeHRM
    OrangeHRM Login    Admin    admin123
