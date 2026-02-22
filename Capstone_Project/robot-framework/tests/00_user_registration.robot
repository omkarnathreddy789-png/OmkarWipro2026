*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=../variables/registration_users.csv    delimiter=;
Resource          ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Template     Register User

*** Test Cases ***
User Registration    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

*** Keywords ***
Register User
    [Arguments]    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

    # Optional filter if EXPECTED column is used
    IF    '${EXPECTED}' != 'PASS'
        Skip    Not registration user
    END

    Go To    https://practice.automationtesting.in/my-account/

    #assertions
    Wait Until Page Contains Element    id=reg_email

    Input Text    id=reg_email        ${EMAIL}
    #assertions
    Textfield Value Should Be         id=reg_email    ${EMAIL}

    Input Text    id=reg_password     ${PASSWORD}
    #assertions
    Element Should Be Visible         id=reg_password

    Click Button  name=register

    #assertions
    Wait Until Keyword Succeeds    15s    2s    Check Registration Result


Check Registration Result
    ${logout}=    Run Keyword And Return Status
    ...    Page Should Contain    Logout

    ${exists}=    Run Keyword And Return Status
    ...    Page Should Contain    already registered

    #assertions
    IF    ${logout} or ${exists}
        Log    Registration successful (new user or already registered)
    ELSE
        Fail    Registration failed - no expected result found
    END