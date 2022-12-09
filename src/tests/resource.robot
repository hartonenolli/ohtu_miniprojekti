*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Start App
    Input  lisää viite

Input Human Format
    Input  ihmisluettava

Input Bibtex Format
    Input  bibtex

Add Reference BibTex
    [Arguments]  ${bibtex}
    Input  ${bibtex}

Add Reference
    [Arguments]  ${tyyppi}  ${avainsana}  ${nimi}  ${kirjailija}  ${julkaisuvuosi}  ${julkaisija}
    Input  ${tyyppi}
    Input  ${avainsana}
    Input  ${nimi}
    Input  ${kirjailija}
    Input  ${julkaisuvuosi}
    Input  ${julkaisija}

