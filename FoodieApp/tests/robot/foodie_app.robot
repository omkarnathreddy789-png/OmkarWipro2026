*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Full Foodie App Flow

    Create Session    foodie    ${BASE_URL}

    # -------------------------------------------------
    # 1️⃣ RESTAURANT MODULE
    # -------------------------------------------------
    ${rand}=    Generate Random String    5
    ${rname}=   Set Variable    Rest${rand}

    ${rest_body}=    Create Dictionary    name=${rname}    location=Vizag

    ${rest}=    POST On Session    foodie
    ...    /api/v1/restaurants
    ...    json=${rest_body}
    ...    expected_status=anything

    Status Should Be    201    ${rest}
    ${rid}=    Set Variable    ${rest.json()}[id]

    ${view}=    GET On Session    foodie
    ...    /api/v1/restaurants/${rid}
    ...    expected_status=anything

    Status Should Be    200    ${view}

    # -------------------------------------------------
    # 2️⃣ DISH MODULE
    # -------------------------------------------------
    ${dish_body}=    Create Dictionary    name=Biryani    price=250

    ${dish}=    POST On Session    foodie
    ...    /api/v1/restaurants/${rid}/dishes
    ...    json=${dish_body}
    ...    expected_status=anything

    Status Should Be    201    ${dish}
    ${did}=    Set Variable    ${dish.json()}[id]

    ${upd_body}=    Create Dictionary    price=300

    ${upd}=    PUT On Session    foodie
    ...    /api/v1/dishes/${did}
    ...    json=${upd_body}
    ...    expected_status=anything

    Status Should Be    200    ${upd}

    ${status_body}=    Create Dictionary    enabled=False

    ${dis}=    PUT On Session    foodie
    ...    /api/v1/dishes/${did}/status
    ...    json=${status_body}
    ...    expected_status=anything

    Status Should Be    200    ${dis}

    # -------------------------------------------------
    # 3️⃣ ADMIN MODULE
    # -------------------------------------------------
    ${approve}=    PUT On Session    foodie
    ...    /api/v1/admin/restaurants/${rid}/approve
    ...    expected_status=anything

    Status Should Be    200    ${approve}

    ${adm_disable}=    PUT On Session    foodie
    ...    /api/v1/admin/restaurants/${rid}/disable
    ...    expected_status=anything

    Status Should Be    200    ${adm_disable}

    ${feedback}=    GET On Session    foodie
    ...    /api/v1/admin/feedback
    ...    expected_status=anything

    Status Should Be    200    ${feedback}

    ${orders_admin}=    GET On Session    foodie
    ...    /api/v1/admin/orders
    ...    expected_status=anything

    Status Should Be    200    ${orders_admin}

    # -------------------------------------------------
    # 4️⃣ USER MODULE
    # -------------------------------------------------
    ${email}=    Set Variable    user${rand}@test.com

    ${user_body}=    Create Dictionary
    ...    name=RobotUser
    ...    email=${email}
    ...    password=1234

    ${user}=    POST On Session    foodie
    ...    /api/v1/users/register
    ...    json=${user_body}
    ...    expected_status=anything

    Status Should Be    201    ${user}
    ${uid}=    Set Variable    ${user.json()}[id]

    # 🔥 FIXED SEARCH CALL (NO URL WARNINGS)
    ${params}=    Create Dictionary
    ...    name=
    ...    location=
    ...    dish=
    ...    rating=

    ${search}=    GET On Session    foodie
    ...    /api/v1/restaurants/search
    ...    params=${params}
    ...    expected_status=anything

    Status Should Be    200    ${search}

    # -------------------------------------------------
    # 5️⃣ ORDER MODULE
    # -------------------------------------------------
    ${dish_list}=    Create List    ${did}

    ${order_body}=    Create Dictionary
    ...    user_id=${uid}
    ...    restaurant_id=${rid}
    ...    dishes=${dish_list}

    ${order}=    POST On Session    foodie
    ...    /api/v1/orders
    ...    json=${order_body}
    ...    expected_status=anything

    Status Should Be    201    ${order}
    ${oid}=    Set Variable    ${order.json()}[id]

    ${rate_body}=    Create Dictionary
    ...    order_id=${oid}
    ...    rating=5
    ...    comment=Nice

    ${rate}=    POST On Session    foodie
    ...    /api/v1/ratings
    ...    json=${rate_body}
    ...    expected_status=anything

    Status Should Be    201    ${rate}

    ${rview}=    GET On Session    foodie
    ...    /api/v1/restaurants/${rid}/orders
    ...    expected_status=anything

    Status Should Be    200    ${rview}

    ${uview}=    GET On Session    foodie
    ...    /api/v1/users/${uid}/orders
    ...    expected_status=anything

    Status Should Be    200    ${uview}

    # cleanup
    ${del}=    DELETE On Session    foodie
    ...    /api/v1/dishes/${did}
    ...    expected_status=anything

    Status Should Be    200    ${del}
