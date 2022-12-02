*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Book
    Input Start App
    Add reference  kirja  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu  Kalle11  poistu
    Run App
    Output Should Contain  Lisätään kirja Kivakirja (2011), kirjoittanut Kalle Kirjailija, julkaissut Kaverijulkaisu, avainsanalla Kalle11

Add Wrong Line
    Input  abc
    Input  poistu
    Run App
    output Should Contain  Virheellinen syöte.
