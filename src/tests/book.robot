*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Book
    Input Start App
    Input Human Format
    Add Reference  kirja  Kalle11  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
    Input  poistu
    Run App
    Output Should Contain  Lisätään Kalle Kirjailija. 2011. Kivakirja. Kaverijulkaisu.

Add Bibtex Book
    Input Start App
    Input Bibtex Format
    Add Reference Bibtex  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Book
    Input Start App
    Input Human Format
    Add Reference  kirja  Kalle12  Kivakirja osa 2  Kalle Kirjailija  2012  Kaverijulkaisu
    Input  listaa viitteet
    Input  poistu
    Run App
    Output Should Contain  Kalle Kirjailija. 2012. Kivakirja osa 2. Kaverijulkaisu.
