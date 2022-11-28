*** Settings ***
Resource  resource.robot
#Test Setup  Add Book And Input

*** Test Cases ***
Add One Book
    Input Start App  lisää viite
    Add reference  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
    Output Should Contain  Kalle Kirjailija, Kivakirja. Kaverijulkaisu, 2011.





#*** Keywords ***
#Add Book And Input
#    Add Book  Kivakirja  Kalle Kirjailija  2011  Kaverijulkaisu
