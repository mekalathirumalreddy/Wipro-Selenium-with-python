#*** Settings ***
# *** variables ***
# *** Test Cases ***
# *** Keywords *** (OPTIONAL)

# 1.Create a scalar variable ${NAME} and print it.

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${NAME}    Thirumal
${CITY}    Hyderabad
@{FRUITS}  Apple  Banana  Mango
&{USER}    name=John    age=25

*** Test Cases ***

#1. Create Scalar Variable And Print
    Log    ${NAME}

#2. Assign Two Numbers And Print Sum
    ${a}=    Set Variable    10
    ${b}=    Set Variable    20
    ${sum}=    Evaluate    ${a}+${b}
    Log    Sum is ${sum}

#3. Use Variable Inside Sentence
    Log    I live in ${CITY}

#4. Reassign Variable And Print Updated Value
    ${CITY}=    Set Variable    Bengaluru
    Log    Updated city is ${CITY}

#5. List Variable First Item
    Log    ${FRUITS}[0]

#6. Loop Through List Variable
    FOR    ${fruit}    IN    @{FRUITS}
        Log    ${fruit}
    END

#7. Length Of List Variable
    ${length}=    Get Length    ${FRUITS}
    Log    Length of fruits list is ${length}

#8. Dictionary Variable Print One Key Value
    Log    ${USER}[name]

#9. Add New Key-Value Pair To Dictionary
    Set To Dictionary ${USER}    city=Delhi
    Log    ${USER}

#10. Loop Through Dictionary And Print Key And Value
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} : ${value}
    END
