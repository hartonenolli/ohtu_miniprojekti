*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Start App
    Input  lisää viite

Add Reference
    [Arguments]  ${kirja}  ${nimi}  ${kirjailija}  ${julkaisuvuosi}  ${julkaisija}
    Input  ${kirja}
    Input  ${nimi}
    Input  ${kirjailija}
    Input  ${julkaisuvuosi}
    Input  ${julkaisija}
