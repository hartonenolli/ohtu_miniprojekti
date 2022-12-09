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
    [Arguments]  ${kirja}  ${avainsana}  ${nimi}  ${kirjailija}  ${julkaisuvuosi}  ${julkaisija}
    Input  ${kirja}
    Input  ${avainsana}
    Input  ${nimi}
    Input  ${kirjailija}
    Input  ${julkaisuvuosi}
    Input  ${julkaisija}
