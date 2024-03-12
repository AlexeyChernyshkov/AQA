*** Settings ***
Documentation   Сalculation of the required amount of gasoline
Library     SeleniumLibrary

*** Test Cases ***
Сalculation of the required amount of gasoline
    Open browser    https://calcus.ru/kalkulyator-rashoda-topliva
    Input text    name:average_consumption      10
    Input text    name:distance     330
    Input text    name:cost     47,50
    Click button    class:calc-submit
    Sleep   3 seconds
    Close browser



