*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Thesis
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  gradu  Matti15  Gradu  Matti Meikäläinen  2015  HY
    Input  poistu
    Run App
    Output Should Contain  Lisätään gradu. Matti15. Matti Meikäläinen. 2015. Gradu. HY.

Add Bibtex Thesis
    Input  lisää viite
    Input  bibtex
    Input  @MastersThesis{Nannen:Thesis:2003, author = {Volker Nannen}, title = {{The Paradox of Overfitting}}, school = {Rijksuniversiteit Groningen}, address = {the Netherlands}, year = {2003}, }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Thesis
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  gradu  Matti16  Gradu  Matti Meikäläinen  2016  HY
    Input  listaa viitteet
    Input  lisäysjärjestys
    Input  poistu
    Run App
    Output Should Contain  gradu. Matti16. Matti Meikäläinen. 2016. Gradu. HY.
