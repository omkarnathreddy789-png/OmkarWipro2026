*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
User Module Full Flow

    Create Session    foodie    ${BASE_URL}

    # 1️⃣ Register user
    ${rand}=    Generate Random String    5
    ${email}=   Set Variable    user${rand}@test.com

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

    # 2️⃣ Create restaurant
    ${rname}=    Set Variable    Rest${rand}
    ${rest_body}=    Create Dictionary    name=${rname}    location=Vizag

    ${rest}=    POST On Session    foodie
    ...    /api/v1/restaurants
    ...    json=${rest_body}
    ...    expected_status=anything

    ${rid}=    Set Variable    ${rest.json()}[id]

    # 3️⃣ Add dish
    ${dish_body}=    Create Dictionary    name=RobotDish    price=200

    ${dish}=    POST On Session    foodie
    ...    /api/v1/restaurants/${rid}/dishes
    ...    json=${dish_body}
    ...    expected_status=anything

    ${did}=    Set Variable    ${dish.json()}[id]

    # 4️⃣ Place order
    ${order_body}=    Create Dictionary
    ...    user_id=${uid}
    ...    restaurant_id=${rid}
    ...    dishes=${did}

    ${order}=    POST On Session    foodie
    ...    /api/v1/orders
    ...    json=${order_body}
    ...    expected_status=anything

    Status Should Be    201    ${order}
    ${oid}=    Set Variable    ${order.json()}[id]

    # 5️⃣ Give rating
    ${rate_body}=    Create Dictionary
    ...    order_id=${oid}
    ...    rating=5
    ...    comment=Nice

    ${rate}=    POST On Session    foodie
    ...    /api/v1/ratings
    ...    json=${rate_body}
    ...    expected_status=anything

    Status Should Be    201    ${rate}
