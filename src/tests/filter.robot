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

Filter By Publisher
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice all}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  etsi viitteitä
    Input  julkaisijan
    Input  Prentice Hall
    Input  poistu
    Run App
    Output Should Contain  Martin, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
    Output Should Not Contain   Martin, Rober. 2008. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice all.

Filter By Entry Type
    Input  lisää viite
    Input  bibtex
    Input  @article{CBH91, author = {Allan Collins and John Seely Brown and Ann Holum}, title = {Cognitive apprenticeship: making thinking visible}, journal = {American Educator}, year = {1991}, volume = {6}, pages = {38--46} }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  etsi viitteitä
    Input  viitetyypin
    Input  book
    Input  poistu
    Run App
    Output Should Contain  Martin, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
    Output Should Not Contain   Allan Collins and John Seely Brown and Ann Holum. 1991. Cognitive apprenticeship: making thinking visible. American Educator.

Filter By Title
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Rober}, title = {Clean Cod: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice all}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin09, author = {Martin, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Prentice Hall}, }
    Input  etsi viitteitä
    Input  nimen
    Input  Clean Code: A Handbook of Agile Software Craftsmanship
    Input  poistu
    Run App
    Output Should Contain  Martin, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
    Output Should Not Contain   Martin, Rober. 2008. Clean Code: A Handbook of Agile Software Craftsmanship. Prentice all.
