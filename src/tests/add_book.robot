*** Settings ***
Resource  resource.robot
#Test Setup  Add Book And Input

*** Test Cases ***
Add One Book
    Input Start App
    Add reference  kirja  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
    Run App
    Output Should Contain  Kalle Kirjailija, Kivakirja. Kaverijulkaisu, 2011.





#*** Keywords ***
#Add Book And Input
#    Add Book  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
