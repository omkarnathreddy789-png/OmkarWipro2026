*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Setup        Go To Shop Page

*** Keywords ***
Go To Shop Page
    Go To    https://practice.automationtesting.in/shop/
    Wait Until Page Contains Element    id=content

Select Default Sorting
    Select From List By Label    css=select.orderby    Default sorting
    Sleep    2s

Select Sort By Price Low To High
    Select From List By Value    css=select.orderby    price
    Sleep    2s

Move Price Slider And Apply Filter
    Execute Javascript    document.querySelector('#min_price').value='150';
    Execute Javascript    document.querySelector('#max_price').value='300';
    Execute Javascript    jQuery('body').trigger('price_slider_change');
    Click Button    css=.price_slider_amount button
    Wait Until Page Contains Element    css=ul.products

Get Price Range Text
    ${text}=    Get Text    css=.price_label
    RETURN    ${text}

Validate Products Visible
    Element Should Be Visible    css=ul.products li
    ${count}=    Get Element Count    css=ul.products li
    Should Be True    ${count} > 0


*** Test Cases ***
Default Sorting Validation
    Select Default Sorting

    # Assertions
    List Selection Should Be    css=select.orderby    Default sorting
    Validate Products Visible


Sort By Price Low To High Validation
    Select Sort By Price Low To High

    # Assertions
    List Selection Should Be    css=select.orderby    Sort by price: low to high
    Validate Products Visible


Filter By Price Validation
    ${before}=    Get Price Range Text
    Move Price Slider And Apply Filter
    ${after}=     Get Price Range Text

    # Assertions
    Should Not Be Equal    ${before}    ${after}
    Element Should Contain    css=.price_label    ₹
    Validate Products Visible


Price Change Filter Validation
    ${initial}=    Get Price Range Text
    Move Price Slider And Apply Filter
    ${changed}=    Get Price Range Text

    Log    Initial Price Range: ${initial}
    Log    Changed Price Range: ${changed}

    # Assertions
    Should Not Be Equal    ${initial}    ${changed}
    Element Should Be Visible    css=.price_label
    Validate Products Visible

#robot -d reports tests/sorting_filter_validation.robot
