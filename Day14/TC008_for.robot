*** Variables ***
@{USERS}    admin    user
@{PWDS}     admin123    user123

*** Test Cases ***
ZIP Alternative
    FOR    ${i}    IN RANGE    0    2
        Log To Console    ${USERS}[${i}] / ${PWDS}[${i}]
    END



*** Test Cases ***
Print Names using for loop
    FOR    ${name}     IN    Ram Ravi Tej
        log to console    ${name}
    END

*** Variables ***
@{COLORS}    Red    Green    Blue

*** Test Cases ***
FOR Loop With List
    FOR    ${color}    IN    @{COLORS}
        Log    Color: ${color}
    END

FOR Loop Basic
    FOR    ${item}    IN    one    two    three
        Log    Item: ${item}
    END

FOR Loop With Step
    FOR    ${i}    IN RANGE    0    10    2
        Log    Value: ${i}
    END

FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log    ${index} = ${value}
    END


Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log    i=${i}, j=${j}
        END
    END

FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log    Found 3
        END
    END




Print Names using while loop
    ${i}=    Set Variable    1

    WHILE    ${i} <= 5
        Log    ${i}
        ${i}=    Evaluate    ${i} + 1
    END

If Condition Example
    ${age}=    Set Variable    20

    IF    ${age} >= 18
        Log    Eligible to vote
    END


If Else Example
    ${num}=    Set Variable    5

    IF    ${num} > 0
        Log    Positive Number
    ELSE
        Log    Zero or Negative Number
    END

IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log    Grade A
    ELSE IF    ${marks} >= 75
        Log    Grade B
    ELSE
        Log    Grade C
    END



Break Loop Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log    ${i}
    END


Continue Loop Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log    ${i}
    END

Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log    Test Passed


Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END

