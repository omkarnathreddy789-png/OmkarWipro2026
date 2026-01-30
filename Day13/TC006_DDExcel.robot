*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    OrangeHRM Login With Excel

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox

*** Keywords ***
OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=//input[@placeholder='Username']    10s
    Input Text    xpath=//input[@placeholder='Username']    ${username}

    Wait Until Element Is Visible    xpath=//input[@placeholder='Password']    10s
    Input Text    xpath=//input[@placeholder='Password']    ${password}

    Click Button    xpath=//button[@type='submit']

    Capture Page Screenshot

    Close Browser

*** Test Cases ***
TC006_DDExcel_Login
