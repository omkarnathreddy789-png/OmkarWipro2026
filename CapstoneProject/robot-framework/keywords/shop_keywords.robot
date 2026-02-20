*** Settings ***
Resource    ../resources/common.resource

*** Keywords ***
Search Product
    Click Element    xpath=//a[text()='Shop']
    Wait Until Element Is Visible    css:input[type='search']
    Handle Ads Popup
    Input Text    css:input[type='search']    HTML
    Press Keys    css:input[type='search']    ENTER
    Page Should Contain    HTML
    Take Named Screenshot    Search

Sort Products
    Wait Until Element Is Visible    class=orderby
    Select From List By Index    class=orderby    1
    Take Named Screenshot    SORT
