*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Book
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  kirja  Kalle11  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
    Input  poistu
    Run App
    Output Should Contain  Lisätään kirja. Kalle11. Kalle Kirjailija. 2011. Kivakirja. Kaverijulkaisu.

Add Bibtex Book
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Book
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  kirja  Kalle12  Kivakirja osa 2  Kalle Kirjailija  2012  Kaverijulkaisu
    Input  listaa viitteet
    Input  lisäysjärjestys
    Input  poistu
    Run App
    Output Should Contain  kirja. Kalle12. Kalle Kirjailija. 2012. Kivakirja osa 2. Kaverijulkaisu.
