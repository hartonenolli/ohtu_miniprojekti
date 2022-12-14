*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Tech Report
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  tutkimusraportti  Teemu21  Raportti  Teemu Virtanen  2021  Organisaatio
    Input  poistu
    Run App
    Output Should Contain  Lisätään tutkimusraportti. Teemu21. Teemu Virtanen. 2021. Raportti. Organisaatio.

Add Bibtex Tech Report
    Input  lisää viite
    Input  bibtex
    Input  @techreport{citekey, author = "Example", title = "EsimerkkiTitle", institution = "Instituutio", year = "2022" }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Tech Report
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  tutkimusraportti  Teemu22  Raportti osa 2  Teemu Virtanen  2022  Organisaatio
    Input  listaa viitteet
    Input  lisäysjärjestys
    Input  poistu
    Run App
    Output Should Contain  tutkimusraportti. Teemu22. Teemu Virtanen. 2022. Raportti osa 2. Organisaatio.
