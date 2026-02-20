*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Setup        Go To Shop Page

*** Keywords ***
Go To Shop Page
    Go To    https://practice.automationtesting.in/shop/
    Wait Until Page Contains Element    id=content

Add First Product By URL
    Go To    https://practice.automationtesting.in/shop/?add-to-cart=169
    Wait Until Page Contains Element    xpath=//a[contains(text(),'View Basket')]
    Page Should Contain    View Basket

Add Second Product By URL
    Go To    https://practice.automationtesting.in/shop/?add-to-cart=181
    Wait Until Page Contains Element    xpath=//a[contains(text(),'View Basket')]
    Page Should Contain    View Basket

Open Cart
    Click Element    xpath=//a[contains(text(),'View Basket')]
    Wait Until Page Contains Element    css=table.shop_table
    Element Should Be Visible    css=table.shop_table

Remove One Product
    Click Element    css=a.remove
    Wait Until Element Is Visible    css=.woocommerce-message
    Element Should Contain    css=.woocommerce-message    removed

Proceed To Checkout
    Click Element    xpath=//a[contains(text(),'Proceed to Checkout')]
    Wait Until Page Contains Element    id=customer_details
    Element Should Be Visible    id=customer_details


*** Test Cases ***
Add Multiple Products In Cart
    Add First Product By URL
    Add Second Product By URL
    Open Cart

    # Assertions
    ${count}=    Get Element Count    css=table.shop_table tbody tr
    Should Be True    ${count} >= 2
    Element Should Be Visible    css=.cart_totals


Remove One Product From Cart
    Add First Product By URL
    Add Second Product By URL
    Open Cart

    ${before}=    Get Element Count    css=table.shop_table tbody tr

    Remove One Product

    ${after}=    Get Element Count    css=table.shop_table tbody tr

    # Assertions
    Should Be True    ${after} < ${before}
    Element Should Be Visible    css=table.shop_table


Proceed To Checkout Product
    Add First Product By URL
    Open Cart
    Proceed To Checkout

    # Assertions
    Page Should Contain Element    id=customer_details
    Page Should Contain Element    id=billing_first_name
    Page Should Contain Element    id=billing_last_name
    Page Should Contain Element    id=place_order
