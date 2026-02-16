*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Add Update Disable Delete Dish

    Create Session    foodie    ${BASE_URL}

    # ------------------------------------------------
    # 1️⃣ Create Restaurant (SAFE JSON)
    # ------------------------------------------------
    ${rand}=    Generate Random String    6
    ${rname}=   Set Variable    RobotRest${rand}

    ${rest_body}=    Create Dictionary    name=${rname}    location=Vizag

    ${rest}=    POST On Session    foodie
    ...    /api/v1/restaurants
    ...    json=${rest_body}
    ...    expected_status=anything

    Status Should Be    201    ${rest}
    ${rest_json}=    Set Variable    ${rest.json()}
    ${rid}=    Set Variable    ${rest_json['id']}

    # ------------------------------------------------
    # 2️⃣ Add Dish
    # ------------------------------------------------
    ${dish_body}=    Create Dictionary    name=RobotDish    price=150

    ${dish}=    POST On Session    foodie
    ...    /api/v1/restaurants/${rid}/dishes
    ...    json=${dish_body}
    ...    expected_status=anything

    Status Should Be    201    ${dish}
    ${dish_json}=    Set Variable    ${dish.json()}
    ${did}=    Set Variable    ${dish_json['id']}

    # ------------------------------------------------
    # 3️⃣ Update Dish
    # ------------------------------------------------
    ${upd_body}=    Create Dictionary    price=180

    ${upd}=    PUT On Session    foodie
    ...    /api/v1/dishes/${did}
    ...    json=${upd_body}
    ...    expected_status=anything

    Status Should Be    200    ${upd}

    # ------------------------------------------------
    # 4️⃣ Disable Dish
    # ------------------------------------------------
    ${status_body}=    Create Dictionary    enabled=False

    ${dis}=    PUT On Session    foodie
    ...    /api/v1/dishes/${did}/status
    ...    json=${status_body}
    ...    expected_status=anything

    Status Should Be    200    ${dis}

    # ------------------------------------------------
    # 5️⃣ Delete Dish
    # ------------------------------------------------
    ${del}=    DELETE On Session    foodie
    ...    /api/v1/dishes/${did}
    ...    expected_status=anything

    Status Should Be    200    ${del}
