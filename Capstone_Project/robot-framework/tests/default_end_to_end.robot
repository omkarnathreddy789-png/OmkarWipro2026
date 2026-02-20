*** Settings ***
Resource    ../resources/common.resource
Resource    ../keywords/login_keywords.robot
Suite Setup       Open Application    ${BROWSER}
Suite Teardown    Close Application

*** Variables ***
${BASE_URL}       https://practice.automationtesting.in
${EMAIL}          testuser1@test.com
${PASSWORD}       Omkar@2003
${PRODUCT1}       https://practice.automationtesting.in/shop/?add-to-cart=169
${PRODUCT2}       https://practice.automationtesting.in/shop/?add-to-cart=181
${BROWSER}        chrome


*** Test Cases ***
Login Validation
    Go To    ${BASE_URL}/my-account/
    Login User    ${EMAIL}    ${PASSWORD}

    # assertions
    Wait Until Page Contains Element    css=div.woocommerce-MyAccount-content
    Page Should Contain    Dashboard


Search Validation
    Go To    ${BASE_URL}/shop/

    Wait Until Page Contains Element    id=s

    Input Text    id=s    HTML
    Press Keys    id=s    ENTER

    Wait Until Keyword Succeeds    3x    5s
    ...    Element Should Be Visible    css=ul.products

    # assertions
    ${count}=    Get Element Count    css=ul.products li
    Should Be True    ${count} > 0



Sorting And Price Filter Validation
    Go To    ${BASE_URL}/shop/

    # ---------- SORTING ----------
    Select From List By Value    css=select.orderby    price
    Wait Until Page Contains Element    css=ul.products

    ${count}=    Get Element Count    css=ul.products li

    # assertions
    Should Be True    ${count} > 0

    # ---------- PRICE FILTER ----------
    Execute Javascript    document.querySelector('#min_price').value='150';
    Execute Javascript    document.querySelector('#max_price').value='300';
    Execute Javascript    jQuery('body').trigger('price_slider_change');
    Click Button    css=.price_slider_amount button

    # assertions
    Wait Until Page Contains Element    css=ul.products
    Element Should Be Visible    css=.price_label


Cart Validation
    Go To    ${PRODUCT1}
    Go To    ${PRODUCT2}
    Go To    ${BASE_URL}/basket/

    Wait Until Page Contains Element    css=table.shop_table

    ${before}=    Get Element Count    css=table.shop_table tbody tr
    Click Element    css=a.remove
    Sleep    2s
    ${after}=    Get Element Count    css=table.shop_table tbody tr

    # assertions
    Should Be True    ${after} < ${before}


Checkout Billing Validation
    Go To    ${BASE_URL}/checkout/
    Wait Until Page Contains Element    id=billing_first_name

    Clear Element Text    id=billing_first_name
    Clear Element Text    id=billing_last_name
    Clear Element Text    id=billing_email

    Input Text    id=billing_first_name    Omkar
    Input Text    id=billing_last_name     Reddy
    Input Text    id=billing_email         ${EMAIL}
    Input Text    id=billing_phone         9876543210
    Input Text    id=billing_address_1     Hyderabad
    Input Text    id=billing_city          Hyderabad
    Input Text    id=billing_postcode      500001

    Scroll Element Into View    id=place_order
    Execute Javascript    document.getElementById("place_order").click();

    # assertions
    Wait Until Location Contains    checkout
    Page Should Contain Element    css=form.checkout


Logout Validation
    Go To    ${BASE_URL}/my-account/
    Logout User

    # assertions
    Wait Until Page Contains Element    id=username
    Page Should Contain Element    css=input[name="login"]
    Page Should Not Contain Element    css=div.woocommerce-MyAccount-content




#for default browser
#robot -d reports tests/end_to_end.robot

#for multiple browsers
#robot -v BROWSER:chrome tests/end_to_end.robot
#robot -v BROWSER:edge tests/end_to_end.robot
#robot -v BROWSER:firefox tests/end_to_end.robot

