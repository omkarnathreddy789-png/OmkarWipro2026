*** Settings ***
Library    RequestsLibrary
Library    Collections

Suite Setup    Create API Session

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Keywords ***
Create API Session
    Create Session    api    ${BASE_URL}

*** Test Cases ***
Get Home Page
    ${res}=    GET On Session    api    /
    Status Should Be    200    ${res}

Get All Users
    ${res}=    GET On Session    api    /users
    Status Should Be    200    ${res}
    ${count}=    Get Length    ${res.json()}
    Should Be True    ${count} > 0

Create User
    ${body}=    Create Dictionary    name=TestUser
    ${res}=    POST On Session    api    /users    json=${body}
    Status Should Be    201    ${res}
    Set Suite Variable    ${USER_ID}    ${res.json()}[id]

Get Created User
    ${res}=    GET On Session    api    /users/${USER_ID}
    Status Should Be    200    ${res}
    Should Be Equal    ${res.json()}[name]    TestUser

Update User Using PUT
    ${body}=    Create Dictionary    name=UpdatedUser
    ${res}=    PUT On Session    api    /users/${USER_ID}    json=${body}
    Status Should Be    200    ${res}
    Should Be Equal    ${res.json()}[name]    UpdatedUser

Partial Update Using PATCH
    ${body}=    Create Dictionary    name=PatchUser
    ${res}=    PATCH On Session    api    /users/${USER_ID}    json=${body}
    Status Should Be    200    ${res}
    Should Be Equal    ${res.json()}[name]    PatchUser

Delete User
    ${res}=    DELETE On Session    api    /users/${USER_ID}
    Status Should Be    200    ${res}

Get Deleted User (Negative Test)
    ${res}=    GET On Session    api    /users/${USER_ID}    expected_status=404
    Status Should Be    404    ${res}
