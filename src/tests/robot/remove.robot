*** Settings ***
Resource  resource.robot

*** Test Cases ***
Remove Reference
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Cod: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice all}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  poista viite
    Input List  kirja. Martin09. Martin, Rober. 2008. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice all.
    Input  poistu
    Run App
    Output Should Contain  Poisto suoritettu. 

Remove Reference Wrong Reference Given
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Cod: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice all}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  poista viite
    Input List  t
    Input  poistu
    Run App
    Output Should Contain  Viiteen t poisto epäonnistui. 

Remove Reference Wrong No Reference Given
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Cod: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice all}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  poista viite
    Input Empty  test
    Input  poistu
    Run App
    Output Should Contain  Ei valittu poistettavia viitteitä 