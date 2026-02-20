*** Settings ***
Library     DataDriver    file=../variables/users.csv
Resource    ../resources/common.resource
Resource    ../keywords/login_keywords.robot

Test Setup        Start User Session
Test Teardown     End User Session
Test Template     Ecommerce Flow


*** Variables ***
${BASE_URL}       https://practice.automationtesting.in
${PRODUCT1}       https://practice.automationtesting.in/shop/?add-to-cart=169
${PRODUCT2}       https://practice.automationtesting.in/shop/?add-to-cart=181
${BROWSER}        chrome


*** Test Cases ***
Ecommerce Flow For Users


*** Keywords ***
##################################################
# SESSION CONTROL
##################################################

Start User Session
    Open Application    ${BROWSER}

End User Session
    Take Test Screenshot
    Close Application


##################################################
# MAIN FLOW (PER USER)
##################################################

Ecommerce Flow
    [Arguments]    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}

    Login Validation    ${EMAIL}    ${PASSWORD}
    Search Validation
    Sorting Validation
    Cart Validation
    Billing Validation    ${EMAIL}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}
    Logout Validation


##################################################
# STEP VALIDATIONS (ASSERTIONS MARKED)
##################################################

Login Validation
    [Arguments]    ${EMAIL}    ${PASSWORD}

    Go To    ${BASE_URL}/my-account/
    Login User    ${EMAIL}    ${PASSWORD}

    #assertions
    ${login_success}=    Run Keyword And Return Status
    ...    Page Should Contain    Dashboard

    Run Keyword If    not ${login_success}
    ...    Fail    ❌ Unregistered or Invalid Login for user: ${EMAIL}



Search Validation
    Go To    ${BASE_URL}/shop/
    Wait Until Element Is Visible    id=s
    Input Text    id=s    HTML
    Press Keys    id=s    ENTER
    Wait Until Element Is Visible    css=ul.products

    ${count}=    Get Element Count    css=ul.products li

    #assertions
    Should Be True    ${count} > 0


Sorting Validation
    Select From List By Value    css=select.orderby    price

    Wait Until Keyword Succeeds    3x    3s
    ...    Element Should Be Visible    css=ul.products

    Execute Javascript    document.querySelector('#min_price').value='150';
    Execute Javascript    document.querySelector('#max_price').value='300';
    Execute Javascript    jQuery('body').trigger('price_slider_change');
    Click Button    css=.price_slider_amount button

    #assertions
    Wait Until Element Is Visible    css=.price_label


Cart Validation
    Go To    ${PRODUCT1}
    Go To    ${PRODUCT2}
    Go To    ${BASE_URL}/basket/

    #assertions
    Wait Until Element Is Visible    css=table.shop_table


Billing Validation
    [Arguments]    ${EMAIL}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}

    Go To    ${BASE_URL}/checkout/
    Wait Until Element Is Visible    id=billing_first_name

    Clear Element Text    id=billing_first_name
    Clear Element Text    id=billing_last_name
    Clear Element Text    id=billing_email
    Clear Element Text    id=billing_phone
    Clear Element Text    id=billing_city
    Clear Element Text    id=billing_postcode

    Input Text    id=billing_first_name    ${FIRSTNAME}
    Input Text    id=billing_last_name     ${LASTNAME}
    Input Text    id=billing_email         ${EMAIL}
    Input Text    id=billing_phone         ${PHONE}
    Input Text    id=billing_city          ${CITY}
    Input Text    id=billing_postcode      ${POSTCODE}

    #assertions
    Element Should Be Visible    id=place_order


Logout Validation
    Logout User

    #assertions
    Wait Until Element Is Visible    id=username




#default browser
#robot -d reports tests/

#multiple browsers
#robot -d reports -v BROWSER:firefox tests/
#robot -d reports -v BROWSER:edge tests/

#store the reports with time and date
#robot -d reports/%DATE:~10,4%-%DATE:~4,2%-%DATE:~7,2%_%TIME:~0,2%-%TIME:~3,2% tests/

#it will run directly
#robot --dryrun tests/end_to_end.robot