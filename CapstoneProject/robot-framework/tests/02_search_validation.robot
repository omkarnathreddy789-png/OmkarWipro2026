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

    #assertions
    Wait Until Page Contains Element    id=content


Search And Validate Products
    [Arguments]    ${product}    ${EXPECTED}

    # Enter search value
    Input Text    id=s    ${product}

    #assertions
    Textfield Value Should Be    id=s    ${product}

    Press Keys    id=s    ENTER

    # Check product list safely (do not fail execution)
    # wait until products container is fully loaded
Wait Until Keyword Succeeds    3x    3s
...    Element Should Be Visible    css=ul.products

${list_visible}=    Set Variable    True

    # Get product count safely
    ${count}=    Run Keyword If    ${list_visible}
    ...    Get Element Count    css=ul.products li
    ...    ELSE    Set Variable    0

    Log    Product Count: ${count}

    #assertions
    # VALID PRODUCT → filtered results must exist
    Run Keyword If    '${EXPECTED}'=='PASS'
    ...    Should Be True    ${count} > 0    Expected products but none displayed

    #assertions
    # INVALID PRODUCT → zero results
    Run Keyword If    '${EXPECTED}'=='NORESULT'
    ...    Should Be True    ${count} == 0    Products displayed when none expected

    #assertions
    # EMPTY SEARCH → WooCommerce shows all products
    Run Keyword If    '${EXPECTED}'=='ALL'
    ...    Should Be True    ${count} > 0    Empty search should display products


*** Test Cases ***
Search With Valid Product
    Search And Validate Products    ${VALID_PRODUCT}    PASS

Search With Invalid Product
    Search And Validate Products    ${INVALID_PRODUCT}    NORESULT

Search With Empty Value
    Search And Validate Products    ${EMPTY}    ALL

#robot -d reports tests/02_search_validation.robot