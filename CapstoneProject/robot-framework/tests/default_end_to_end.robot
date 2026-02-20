*** Settings ***
Library    Process
Documentation    Master Runner - Executes All Validation Suites In Order

*** Test Cases ***
Run Full Flow In Order
    Run Process    robot    tests/login_validation.robot    shell=True
    Run Process    robot    tests/search_validation.robot    shell=True
    Run Process    robot    tests/sorting_filter_validation.robot    shell=True
    Run Process    robot    tests/cart_validation.robot    shell=True
    Run Process    robot    tests/billing_validation.robot    shell=True
    Run Process    robot    tests/logout_validation.robot    shell=True