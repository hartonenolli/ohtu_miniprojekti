*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Add Reference
    [Arguments]  ${tyyppi}  ${avainsana}  ${nimi}  ${kirjailija}  ${julkaisuvuosi}  ${julkaisija}
    Input  ${tyyppi}
    Input  ${avainsana}
    Input  ${nimi}
    Input  ${kirjailija}
    Input  ${julkaisuvuosi}
    Input  ${julkaisija}

