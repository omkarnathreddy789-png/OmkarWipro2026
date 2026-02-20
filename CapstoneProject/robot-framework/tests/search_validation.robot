*** Settings ***
Resource    ../resources/common.resource
Resource    ../keywords/shop_keywords.robot
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To Shop Page

*** Variables ***
${VALID_PRODUCT}      HTML
${INVALID_PRODUCT}    XYZINVALID123
${EMPTY}

*** Keywords ***
Go To Shop Page
    Go To    https://practice.automationtesting.in/shop/
    Wait Until Page Contains Element    id=content


Search And Validate Products
    [Arguments]    ${product}

    Input Text    id=s    ${product}
    Press Keys    id=s    ENTER

    # 🔥 STRICT VALIDATION
    Wait Until Element Is Visible    css=ul.products
    ${count}=    Get Element Count    css=ul.products li

    Log    Product Count: ${count}
    Should Be True    ${count} > 0    No products displayed after search


*** Test Cases ***
Search With Valid Product
    Search And Validate Products    ${VALID_PRODUCT}


Search With Invalid Product
    Search And Validate Products    ${INVALID_PRODUCT}


Search With Empty Value
    Search And Validate Products    ${EMPTY}

#robot -d reports tests/search_validation.robot