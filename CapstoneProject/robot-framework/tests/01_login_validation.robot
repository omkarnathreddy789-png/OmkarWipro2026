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

    #assertions
    Wait Until Page Contains Element    id=username

    Run Keyword And Ignore Error    Logout User

    Go To    https://practice.automationtesting.in/my-account/

    #assertions
    Wait Until Element Is Visible    id=username


Login Validation Template
    [Arguments]    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

    Login User    ${EMAIL}    ${PASSWORD}

    ${dashboard_visible}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    css=div.woocommerce-MyAccount-content    5s

    #assertions
    IF    '${EXPECTED}'=='PASS'
        Should Be True    ${dashboard_visible}

        # logout immediately after successful login
        Logout User

        #assertions
        Wait Until Element Is Visible    id=username
    END

    #assertions
    IF    '${EXPECTED}'=='FAIL'
        Should Not Be True    ${dashboard_visible}
    END

#robot -d reports tests/01_login_validation.robot