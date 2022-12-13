*** Settings ***
Resource  resource.robot

*** Test Cases ***
Sort By Year
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin08, author = {Martin, Robert}, title = {Better Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin07, author = {Collins, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Apprentice Hall}, }
    Input  listaa viitteet
    Input  vuoden
    Input  poistu
    Run App
    First Output Filter  kirja. Martin07. Collins, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Apprentice Hall.

Sort By Author
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin08, author = {Martin, Robert}, title = {Better Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin07, author = {Collins, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Apprentice Hall}, }
    Input  listaa viitteet
    Input  tekijän
    Input  poistu
    Run App
    First Output Filter  kirja. Martin07. Collins, Robert. 2007. Clean Code: A Handbook of Agile Software Craftsmanship. Apprentice Hall.

Sort By Reference Type
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin08, author = {Martin, Robert}, title = {Better Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin07, author = {Collins, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Apprentice Hall}, }
    Input  listaa viitteet
    Input  viitetyypin
    Input  poistu
    Run App
    First Output Filter  kirja. Martin08. Martin, Robert. 2008. Better Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.

Sort By Title
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin08, author = {Martin, Robert}, title = {Better Code: A Handbook of Agile Software Craftsmanship}, year = {2008}, publisher = {Prentice Hall}, }
    Input  lisää viite
    Input  bibtex
    Input  @book{Martin07, author = {Collins, Robert}, title = {Clean Code: A Handbook of Agile Software Craftsmanship}, year = {2007}, publisher = {Apprentice Hall}, }
    Input  listaa viitteet
    Input  nimen
    Input  poistu
    Run App
    First Output Filter  kirja. Martin08. Martin, Robert. 2008. Better Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.
