*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Setup        Go To Shop Page


*** Keywords ***
Go To Shop Page
    Go To    https://practice.automationtesting.in/shop/

    #assertions
    Wait Until Page Contains Element    id=content


Select Default Sorting
    Select From List By Label    css=select.orderby    Default sorting
    Sleep    2s

    #assertions
    List Selection Should Be    css=select.orderby    Default sorting


Select Sort By Price Low To High
    Select From List By Value    css=select.orderby    price
    Sleep    2s

    #assertions
    List Selection Should Be    css=select.orderby    Sort by price: low to high


Move Price Slider And Apply Filter
    Execute Javascript    document.querySelector('#min_price').value='150';
    Execute Javascript    document.querySelector('#max_price').value='300';
    Execute Javascript    jQuery('body').trigger('price_slider_change');
    Click Button    css=.price_slider_amount button

    #assertions
    Wait Until Page Contains Element    css=ul.products


Get Price Range Text
    ${text}=    Get Text    css=.price_label

    #assertions
    Should Not Be Empty    ${text}

    RETURN    ${text}


Validate Products Visible
    #assertions
    Element Should Be Visible    css=ul.products li

    ${count}=    Get Element Count    css=ul.products li

    #assertions
    Should Be True    ${count} > 0


*** Test Cases ***
Default Sorting Validation
    Select Default Sorting
    Validate Products Visible


Sort By Price Low To High Validation
    Select Sort By Price Low To High
    Validate Products Visible


Filter By Price Validation
    ${before}=    Get Price Range Text
    Move Price Slider And Apply Filter
    ${after}=     Get Price Range Text

    #assertions
    Should Not Be Equal    ${before}    ${after}

    #assertions
    Element Should Contain    css=.price_label    ₹

    Validate Products Visible


Price Change Filter Validation
    ${initial}=    Get Price Range Text
    Move Price Slider And Apply Filter
    ${changed}=    Get Price Range Text

    Log    Initial Price Range: ${initial}
    Log    Changed Price Range: ${changed}

    #assertions
    Should Not Be Equal    ${initial}    ${changed}

    #assertions
    Element Should Be Visible    css=.price_label

    Validate Products Visible


#robot -d reports tests/03_sorting_filter_validation.robot