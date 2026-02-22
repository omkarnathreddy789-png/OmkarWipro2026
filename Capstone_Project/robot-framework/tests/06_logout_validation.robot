*** Settings ***
Resource    ../resources/common.resource
Resource    ../keywords/login_keywords.robot
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To Fresh Login Page

*** Variables ***
${VALID_EMAIL}        testuser1@test.com
${VALID_PASSWORD}     Omkar@2003

*** Keywords ***
Go To Fresh Login Page
    Go To    https://practice.automationtesting.in/my-account/
    Run Keyword And Ignore Error    Logout User
    Go To    https://practice.automationtesting.in/my-account/
    Wait Until Element Is Visible    id=username


*** Test Cases ***
Logout Validation
    Login User    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Wait Until Page Contains Element    css=div.woocommerce-MyAccount-content

    Logout User

    # Logout Assertions (Added)
    Wait Until Element Is Visible    id=username
    Page Should Contain Element      css=input[name="login"]
    Page Should Not Contain Element  css=div.woocommerce-MyAccount-content

#robot -d reports tests/06_logout_validation.robot
