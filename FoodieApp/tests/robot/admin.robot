*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Admin Module Flow

    Create Session    foodie    ${BASE_URL}

    # 1️⃣ Create restaurant
    ${rand}=    Generate Random String    5
    ${rname}=   Set Variable    AdminRest${rand}

    ${rest_body}=    Create Dictionary    name=${rname}    location=Vizag

    ${rest}=    POST On Session    foodie
    ...    /api/v1/restaurants
    ...    json=${rest_body}
    ...    expected_status=anything

    Status Should Be    201    ${rest}
    ${rid}=    Set Variable    ${rest.json()}[id]

    # 2️⃣ Approve restaurant
    ${approve}=    PUT On Session    foodie
    ...    /api/v1/admin/restaurants/${rid}/approve
    ...    expected_status=anything

    Status Should Be    200    ${approve}

    # 3️⃣ Disable restaurant
    ${disable}=    PUT On Session    foodie
    ...    /api/v1/admin/restaurants/${rid}/disable
    ...    expected_status=anything

    Status Should Be    200    ${disable}

    # 4️⃣ View feedback
    ${feedback}=    GET On Session    foodie
    ...    /api/v1/admin/feedback
    ...    expected_status=anything

    Status Should Be    200    ${feedback}

    # 5️⃣ View orders
    ${orders}=    GET On Session    foodie
    ...    /api/v1/admin/orders
    ...    expected_status=anything

    Status Should Be    200    ${orders}
