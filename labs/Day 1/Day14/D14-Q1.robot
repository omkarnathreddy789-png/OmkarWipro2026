*** Settings ***
Documentation     Sample Robot Framework Suite with all setups and teardowns
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Start Test
Test Teardown     End Test

Library           BuiltIn

*** Variables ***
${APP_NAME}       DemoApp

*** Test Cases ***
Login Test
    [Tags]    smoke    login
    Log    Logging into ${APP_NAME}
    ${result}=    Evaluate    2+2
    Should Be Equal As Integers    ${result}    4

Search Test
    [Tags]    regression    search
    Log    Performing search
    Should Be True    ${True}

*** Keywords ***
Open Application
    Log    Suite setup: Opening application

Close Application
    Log    Suite teardown: Closing application

Start Test
    Log    Test setup: Preparing test data

End Test
    Log    Test teardown: Cleaning up after test
