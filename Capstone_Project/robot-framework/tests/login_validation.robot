*** Settings ***
Resource    ../resources/common.resource
Resource    ../keywords/login_keywords.robot
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To Fresh Login Page

*** Variables ***
${VALID_EMAIL}        testuser1@test.com
${VALID_PASSWORD}     Omkar@2003
${INVALID_PASSWORD}   Wrong123

*** Keywords ***
Go To Fresh Login Page
    Go To    https://practice.automationtesting.in/my-account/
    Run Keyword And Ignore Error    Logout User
    Go To    https://practice.automationtesting.in/my-account/
    Wait Until Element Is Visible    id=username


*** Test Cases ***
Login With Correct Password
    Login User    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Wait Until Page Contains Element    css=div.woocommerce-MyAccount-content

    #ASSERTIONS
    Location Should Contain    my-account
    Page Should Contain        Dashboard
    Page Should Contain        Logout


Login With Incorrect Password
    Login User    ${VALID_EMAIL}    ${INVALID_PASSWORD}
    Wait Until Page Contains Element    css=ul.woocommerce-error

    #ASSERTIONS
    Location Should Contain    my-account
    Page Should Contain        Error
    Page Should Contain Element    css=ul.woocommerce-error


Login With Empty Password
    Login User    ${VALID_EMAIL}    ${EMPTY}
    Wait Until Page Contains Element    css=ul.woocommerce-error

    #ASSERTIONS
    Location Should Contain    my-account
    Page Should Contain        Error
    Page Should Contain Element    css=ul.woocommerce-error

#robot -d reports tests/login_validation.robot
