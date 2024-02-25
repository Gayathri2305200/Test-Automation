*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${url}    https://omayo.blogspot.com/
${browser}    Edge

*** Test Cases ***
Test Case 1
    [Tags]   sanity   smoke
    open browser    ${url}       ${browser}
    maximize browser window
    set selenium implicit wait    10

    ${MultiSelectionlist}    MultiSelectionlist
    log to console    ${MultiSelectionlist}

Test Case 2
    [Tags]  regression
    ${dropdown}    dropdown
    log to console    ${dropdown}

Test Case 3
    [Tags]  regression   sanity
    enter test
    clear text


*** Keywords ***

MultiSelectionlist
     select from list by value    multiselect1   volvox
     select from list by label    multiselect1   Swift
     select from list by index    multiselect1   3
     unselect from list by value    multiselect1   volvox
     ${selected_list}    get selected list labels    id:multiselect1
     [Return]          ${selected_list}

dropdown
    select from list by value     drop1    def
    ${selected_dropdown}   get selected list label       id:drop1
    [Return]             ${selected_dropdown}

enter test
    input text   id:ta1    The cat was playing in the garden.

clear text
    clear element text   name:fname


