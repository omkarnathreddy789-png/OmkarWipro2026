*** Settings ***
Resource    ../resources/common.resource

*** Keywords ***
Add Product To Cart
    Wait Until Element Is Visible    xpath=(//a[text()='Add to basket'])[1]
    Click Element    xpath=(//a[text()='Add to basket'])[1]
    Click Element    xpath=//a[text()='View Basket']
    Page Should Contain    Basket Totals
    Take Named Screenshot    cart

Proceed To Billing
    Click Element    xpath=//a[contains(text(),'Proceed to Checkout')]
    Wait Until Page Contains    Billing Details
    Take Named Screenshot    billing

Logout User
    Click Element    xpath=//a[text()='Logout']
    Page Should Contain    Login
    Take Named Screenshot    logout
