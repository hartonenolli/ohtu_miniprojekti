*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Article
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  lehtiartikkeli  Matti15  Hieno artikkeli, vai onko?  Matti Meikäläinen  2015  Parasjulkaisu
    Input  poistu
    Run App
    Output Should Contain  Lisätään lehtiartikkeli. Matti15. Matti Meikäläinen. 2015. Hieno artikkeli, vai onko?. Parasjulkaisu. 

Add Bibtex Article
    Input  lisää viite
    Input  bibtex
    Input  @article{CBH91, author = {Allan Collins and John Seely Brown and Ann Holum}, title = {Cognitive apprenticeship: making thinking visible}, journal = {American Educator}, year = {1991}, volume = {6}, pages = {38--46} }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Article
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  lehtiartikkeli  Matti16  Hienon artikkelin jatko-osa: Uusi Toivo  Matti Meikäläinen  2016  Parasjulkaisu
    Input  listaa viitteet
    Input  lisäysjärjestys
    Input  poistu
    Run App
    Output Should Contain  lehtiartikkeli. Matti16. Matti Meikäläinen. 2016. Hienon artikkelin jatko-osa: Uusi Toivo. Parasjulkaisu. 