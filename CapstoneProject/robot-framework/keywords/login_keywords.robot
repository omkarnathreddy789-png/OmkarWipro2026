*** Settings ***
Resource    ../resources/common.resource

*** Keywords ***
Login Scenario
    [Arguments]    ${EMAIL}    ${PASSWORD}

    Login User    ${EMAIL}    ${PASSWORD}

    # Check if dashboard exists (valid login)
    ${success}=    Run Keyword And Return Status
    ...    Page Should Contain    Dashboard

    #ASSERTIONS
    Should Be True    ${success}    ❌ Invalid login credentials for ${EMAIL}



Login User
    [Arguments]    ${EMAIL}    ${PASSWORD}

    Input Text    id=username    ${EMAIL}
    Input Text    id=password    ${PASSWORD}
    Click Button    name=login



Logout User
    # Always go to My Account first
    Go To    https://practice.automationtesting.in/my-account/

    # Wait for page to load fully
    Wait Until Page Contains Element    css=body

    # Sometimes user is already logged out, so ignore error
    Run Keyword And Ignore Error    Click Element    xpath=//a[text()='Logout']

    # Confirm logout page is shown
    Wait Until Element Is Visible    id=username    15s

