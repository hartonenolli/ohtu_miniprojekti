*** Settings ***
Resource  resource.robot
#Test Setup  Add Book And Input

*** Test Cases ***
Add One Book
    Input Start App
    Add reference  kirja  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu  poistu
    Run App
    Output Should Contain  Lisätään kirja Kivakirja (2011), kirjoittanut Kalle Kirjailija, julkaissut Kaverijulkaisu





#*** Keywords ***
#Add Book And Input
#    Add Book  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
