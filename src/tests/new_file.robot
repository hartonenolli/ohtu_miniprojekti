*** Settings ***
Resource  resource.robot

*** Test Cases ***
Adding To New File
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Cod: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice all}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  siirrä viitteitä tiedostoon
    Input List  kirja. Martin09. Martin, Rober. 2008. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice all.
    Input  uusi
    Input  poistu
    Run App
    Output Should Contain  Viitteiden kirjoittaminen uuteen tiedostoon onnistui suoritettu. 
