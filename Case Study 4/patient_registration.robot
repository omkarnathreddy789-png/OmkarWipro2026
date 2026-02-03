*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Registration Page
Suite Teardown    Close Browser

*** Variables ***
${URL}            http://127.0.0.1:5000/register
${BROWSER}        Chrome

${PATIENT1_NAME}      John
${PATIENT1_AGE}       30
${PATIENT1_GENDER}    Male
${PATIENT1_CONTACT}   9999999999
${PATIENT1_DISEASE}   Flu
${PATIENT1_DOCTOR}    Dr. Smith

${PATIENT2_NAME}      Alice
${PATIENT2_AGE}       25
${PATIENT2_GENDER}    Female
${PATIENT2_CONTACT}   8888888888
${PATIENT2_DISEASE}   Cold
${PATIENT2_DOCTOR}    Dr. Adams

*** Keywords ***
Open Browser To Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.5s

Fill Patient Form
    [Arguments]    ${name}    ${age}    ${gender}    ${contact}    ${disease}    ${doctor}
    Input Text    name=name       ${name}
    Input Text    name=age        ${age}
    Click Element  xpath=//input[@name='gender' and @value='${gender}']
    Input Text    name=contact    ${contact}
    Input Text    name=disease    ${disease}
    Input Text    name=doctor     ${doctor}
    Click Button  xpath=//input[@type='submit']

*** Test Cases ***
Register Patient 1
    Fill Patient Form    ${PATIENT1_NAME}    ${PATIENT1_AGE}    ${PATIENT1_GENDER}    ${PATIENT1_CONTACT}    ${PATIENT1_DISEASE}    ${PATIENT1_DOCTOR}

Register Patient 2
    Fill Patient Form    ${PATIENT2_NAME}    ${PATIENT2_AGE}    ${PATIENT2_GENDER}    ${PATIENT2_CONTACT}    ${PATIENT2_DISEASE}    ${PATIENT2_DOCTOR}
