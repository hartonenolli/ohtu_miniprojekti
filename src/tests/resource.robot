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
    [Arguments]  ${kirja}  ${nimi}  ${kirjailija}  ${julkaisuvuosi}  ${julkaisija}  ${avainsana}  ${poistu}
    Input  ${kirja}
    Input  ${nimi}
    Input  ${kirjailija}
    Input  ${julkaisuvuosi}
    Input  ${julkaisija}
    Input  ${avainsana}
    Input  ${poistu}
