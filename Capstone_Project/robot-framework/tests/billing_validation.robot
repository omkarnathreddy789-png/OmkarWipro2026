*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Setup        Prepare Checkout With Multiple Items

*** Variables ***
${PRODUCT1}    https://practice.automationtesting.in/shop/?add-to-cart=169
${PRODUCT2}    https://practice.automationtesting.in/shop/?add-to-cart=181

${FIRSTNAME}    Omkar
${LASTNAME}     Reddy
${ADDRESS}      Hyderabad
${CITY}         Hyderabad
${POSTCODE}     500001
${PHONE}        9876543210
${EMAIL}        testuser1@test.com

*** Keywords ***
Prepare Checkout With Multiple Items
    Go To    ${PRODUCT1}
    Go To    ${PRODUCT2}
    Go To    https://practice.automationtesting.in/checkout/
    Wait Until Page Contains Element    css=form.checkout

Fill Billing Details
    [Arguments]    ${fname}    ${lname}    ${email}
    Wait Until Element Is Visible    id=billing_first_name

    Clear Element Text    id=billing_first_name
    Clear Element Text    id=billing_last_name
    Clear Element Text    id=billing_email

    Input Text    id=billing_first_name    ${fname}
    Input Text    id=billing_last_name     ${lname}
    Input Text    id=billing_email         ${email}
    Input Text    id=billing_phone         ${PHONE}
    Input Text    id=billing_address_1     ${ADDRESS}
    Input Text    id=billing_city          ${CITY}
    Input Text    id=billing_postcode      ${POSTCODE}

Select Payment Method
    Click Element    id=payment_method_cheque

Place Order
    Scroll Element Into View    id=place_order
    Click Button    id=place_order

Wait For Checkout Refresh
    Wait Until Page Contains Element    css=form.checkout


*** Test Cases ***
Billing Validation With Multiple Items - Valid Details
    Fill Billing Details    ${FIRSTNAME}    ${LASTNAME}    ${EMAIL}
    Select Payment Method
    Place Order

    Wait Until Location Contains    order-received
    Page Should Contain    Thank you


Billing Validation Missing First Name
    Fill Billing Details    ${EMPTY}    ${LASTNAME}    ${EMAIL}
    Select Payment Method
    Place Order
    Wait For Checkout Refresh


Billing Validation Invalid Email
    Fill Billing Details    ${FIRSTNAME}    ${LASTNAME}    invalidemail
    Select Payment Method
    Place Order
    Wait For Checkout Refresh
