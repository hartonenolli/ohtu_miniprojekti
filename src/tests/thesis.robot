*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Thesis
    Input Start App
    Input Human Format
    Add Reference  Matti15  Gradu  Matti Meikäläinen  2015  Parasjulkaisu
    Input  poistu
    Run App
    Output Should Contain  Lisätään Matti Meikäläinen. 2015. Gradu. Parasjulkaisu.

Add Bibtex Thesis
    Input Start App
    Input Bibtex Format
    Add Reference Bibtex  @MastersThesis{Nannen:Thesis:2003, author = {Volker Nannen}, title = {{The Paradox of Overfitting}}, school = {Rijksuniversiteit Groningen}, address = {the Netherlands}, year = {2003}, }
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Thesis
    Input Start App
    Input Human Format
    Add Reference  Matti16  Gradu  Matti Meikäläinen  2016  Parasjulkaisu
    Input  listaa viitteet
    Input  poistu
    Run App
    Output Should Contain  Matti Meikäläinen. 2016. Gradu. Parasjulkaisu.
