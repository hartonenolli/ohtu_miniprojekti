*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Book
    Input Start App
    Input Human Format
    Add reference  kirja  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu  Kalle11  poistu
    Run App
    Output Should Contain  Lisätään kirja Kivakirja (2011), kirjoittanut Kalle Kirjailija, julkaissut Kaverijulkaisu, avainsanalla Kalle11

Add Bibtex Book
    Input Start App
    Input Bibtex Format
    Add Reference Bibtex  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

Add Wrong Line
    Input  abc
    Input  poistu
    Run App
    output Should Contain  Virheellinen syöte.
