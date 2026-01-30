*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome
${DATAFILE}  data_login.csv

*** Test Cases ***
Login Tests From CSV
    ${content}=    Get File    ${DATAFILE}
    @{rows}=       Split To Lines    ${content}
    ${total}=      Get Length    ${rows}

    FOR    ${i}    IN RANGE    1    ${total}
        ${row}=    Split String    ${rows}[${i}]    ,
        Run Login Test
        ...    ${row}[0]
        ...    ${row}[1]
        ...    ${row}[2]
    END

*** Keywords ***
Run Login Test
    [Arguments]    ${username}    ${password}    ${expected}
    Open Application
    Perform Login    ${username}    ${password}
    Validate Result    ${expected}
    Close Browser

Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@placeholder='Username']    10s

Perform Login
    [Arguments]    ${username}    ${password}
    Input Text    xpath=//input[@placeholder='Username']    ${username}
    Input Text    xpath=//input[@placeholder='Password']    ${password}
    Click Button    xpath=//button[@type='submit']

Validate Result
    [Arguments]    ${expected}

    IF    '${expected}' == 'success'
        Wait Until Page Contains    Dashboard    10s
    ELSE
        Wait Until Page Contains    Invalid credentials    10s
    END
