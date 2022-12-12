*** Settings ***
Resource  resource.robot

*** Test Cases ***
Filter By Year
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  etsi viitteitä
    Input  vuoden
    Input  2007
    Input  poistu
    Run App
    Output Should Contain  Martin, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
    Output Should Not Contain   Martin, Robert. 2008. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.

Filter By Author
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  etsi viitteitä
    Input  tekijän
    Input  Martin, Robert
    Input  poistu
    Run App
    Output Should Contain  Martin, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
    Output Should Not Contain   Martin, Rober. 2008. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
