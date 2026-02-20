*** Settings ***
Library     DataDriver    ../variables/login_validation.csv    delimiter=;
Resource    ../resources/common.resource
Resource    ../keywords/login_keywords.robot
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To Fresh Login Page
Test Template     Login Validation Template

*** Test Cases ***
Login Validation

*** Keywords ***
Go To Fresh Login Page
    Go To    https://practice.automationtesting.in/my-account/
    Run Keyword And Ignore Error    Logout User
    Go To    https://practice.automationtesting.in/my-account/
    Wait Until Element Is Visible    id=username


Login Validation Template
    [Arguments]    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

    Login User    ${EMAIL}    ${PASSWORD}

    # 🔥 STRICT ASSERTION
    # Dashboard must appear after login
    Wait Until Element Is Visible    css=div.woocommerce-MyAccount-content    10s

    Location Should Contain    my-account
    Page Should Contain        Dashboard

#robot -d reports tests/login_validation.robot