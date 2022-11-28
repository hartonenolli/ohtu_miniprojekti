*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Start App
    Input  lisää viite

Add Reference
    [Arguments]  ${nimi}  ${kirjailija}  ${julkaisuvuosi}  ${julkaisija}
    Input  ${nimi}
    Input  ${kirjailija}
    Input  ${julkaisuvuosi}
    Input  ${julkaisija}
    Start App
