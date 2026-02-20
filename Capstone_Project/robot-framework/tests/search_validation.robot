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


*** Test Cases ***
Search With Valid Product
    [Documentation]    Verify search works with valid product
    Input Text    id=s    ${VALID_PRODUCT}
    Press Keys    id=s    ENTER
    Wait Until Element Is Visible    css=ul.products

    # Assertions
    Element Should Be Visible    css=ul.products
    Page Should Contain    ${VALID_PRODUCT}
    ${count}=    Get Element Count    css=ul.products li
    Should Be True    ${count} > 0


Search With Invalid Product
    [Documentation]    Verify no products displayed for invalid search
    Input Text    id=s    ${INVALID_PRODUCT}
    Press Keys    id=s    ENTER
    Wait Until Page Contains Element    id=content

    # Assertions
    Page Should Contain    Sorry, nothing found
    Page Should Not Contain Element    css=ul.products li





Search With Empty Value
    [Documentation]    Verify empty search loads default product list
    Input Text    id=s    ${EMPTY}
    Press Keys    id=s    ENTER
    Wait Until Element Is Visible    css=ul.products

    # Assertions
    Element Should Be Visible    css=ul.products
    ${count}=    Get Element Count    css=ul.products li
    Should Be True    ${count} > 0
