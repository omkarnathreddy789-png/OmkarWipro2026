*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Add Restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=Robot Food    location=Vizag
    ${response}=    POST On Session    foodie    /api/v1/restaurants
    ...    json=${body}
    ...    expected_status=anything
    Status Should Be    201    ${response}

Duplicate Restaurant
    ${body}=    Create Dictionary    name=Robot Food    location=Vizag
    ${response}=    POST On Session    foodie    /api/v1/restaurants
    ...    json=${body}
    ...    expected_status=anything
    Status Should Be    409    ${response}
