*** Settings ***
Library     DataDriver    ../variables/login_validation.csv    delimiter=;
Resource    ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Setup        Prepare Checkout With Multiple Items
Test Template     Billing Validation Template


*** Variables ***
${PRODUCT1}    https://practice.automationtesting.in/shop/?add-to-cart=169
${PRODUCT2}    https://practice.automationtesting.in/shop/?add-to-cart=181
${ADDRESS}     Hyderabad


*** Test Cases ***
Billing Validation


*** Keywords ***
Prepare Checkout With Multiple Items
    Go To    ${PRODUCT1}
    Go To    ${PRODUCT2}
    Go To    https://practice.automationtesting.in/checkout/
    Wait Until Page Contains Element    css=form.checkout


Fill Billing Details
    [Arguments]    ${fname}    ${lname}    ${email}    ${phone}    ${city}    ${postcode}

    Wait Until Element Is Visible    id=billing_first_name

    Clear Element Text    id=billing_first_name
    Input Text    id=billing_first_name    ${fname}

    Clear Element Text    id=billing_last_name
    Input Text    id=billing_last_name     ${lname}

    Clear Element Text    id=billing_email
    Input Text    id=billing_email         ${email}

    Input Text    id=billing_phone         ${phone}
    Input Text    id=billing_address_1     Hyderabad
    Input Text    id=billing_city          ${city}
    Input Text    id=billing_postcode      ${postcode}

    # 🔥 VERY IMPORTANT — WAIT FOR AJAX
    Wait Until Page Does Not Contain Element    css=.blockUI    10s

Select Payment Method
    Click Element    id=payment_method_cheque


Place Order
    Wait Until Element Is Visible    id=place_order
    Wait Until Element Is Enabled    id=place_order

    # 🔥 Remove Google vignette / ad overlays if present
    Execute Javascript    document.querySelectorAll('[data-google-vignette]').forEach(e=>e.remove())

    Scroll Element Into View    id=place_order
    Sleep    1s

    # 🔥 Use JS click to avoid overlay interception
    Execute Javascript    document.getElementById('place_order').click()

    # Wait until ajax checkout finishes
    Wait Until Page Does Not Contain Element    css=.blockUI    15s


Billing Validation Template
    [Arguments]    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

    Fill Billing Details    ${FIRSTNAME}    ${LASTNAME}    ${EMAIL}    ${PHONE}    ${CITY}    ${POSTCODE}
    Select Payment Method
    Place Order

    ${order_page}=    Run Keyword And Return Status
    ...    Wait Until Location Contains    order-received    8s

    ${dashboard_page}=    Run Keyword And Return Status
    ...    Wait Until Location Contains    my-account    5s

    IF    ${order_page} or ${dashboard_page}
        Log    Order placed successfully
    ELSE
        Fail    Invalid billing details
    END

#robot -d reports tests/billing_validation.robot