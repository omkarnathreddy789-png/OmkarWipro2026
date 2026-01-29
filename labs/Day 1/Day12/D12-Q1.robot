*** Settings ***
Library    BuiltIn

*** Variables ***
${USERNAME}    Omkar
${CITY}        Hyderabad
@{FRUITS}      Apple    Banana    Mango

*** Test Cases ***
Display User Info
    Log    Username is ${USERNAME}
    Log    City is ${CITY}
    Log To Console    User: ${USERNAME} from ${CITY}

Show Fruit List
    Log    Fruits are: ${FRUITS}
    Log To Console    First fruit is ${FRUITS}[0]
    Log To Console    All fruits: ${FRUITS}
