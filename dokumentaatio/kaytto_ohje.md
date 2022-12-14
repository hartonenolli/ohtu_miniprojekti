# Käyttöohje

## Asennus

Avaa tietokoneen komentorivi

Linuxilla painamalla
<kbd>control</kbd> <kbd>alt</kbd> <kbd>t</kbd>

Tarkista tämän jälkeen onko python ladattuna komennolla
```bash
python3 --version
```
Jos python on ladattuna pitäisi komentorivillä lukea
```bash
Python 3.8.10
```
Tai jokin muu numerosarja

Jos lukee
```bash
Python: command not found
```
Pitää tietokoneelle asentaa Python.
Tämä onnistuu kirjoittamalla komento riville
```bash
sudo apt-get update
```
```bash
sudo apt-get install python3.8
```

Nyt voi tarkistaa onnistuiko lataus suorittamalla
```bash
python3 --version
```

Tämän jälkeen ladataan poetry pythoniin komennolla
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Poetryn käytön helpottamiseksi luomme polun kutsua sitä nopeammin komennolla
```bash
export PATH="/home/käyttäjätunnus/.local/bin:$PATH"
```
Nyt voi tarkistaa onnistuiko lataus suorittamalla
```bash
poetry --version
```

Nyt voimme ladata käyttöjärjestelmän [Githubin repositoriosta](https://github.com/hartonenolli/ohtu_miniprojekti)
<> Code : valikon alta lataamalla zip tiedoston (DOWNLOAD ZIP)
Tiedoston ladattua se pitää purkaa painamalla extract painiketta ja osoittamalla purkamisen Home välilehdelle

Tämän jälkeen avataan tiedosto komentorivillä komennolla
```bash
cd ohtu_miniprojekti-main
```

Nyt ladataan sovelluksen riippuvuudet komennolla

```bash
poetry install
```

### Sovelluksen käyttäminen

#### Komennot

Aloita sovellus komennolla:
```bash
poetry run invoke start
```

Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```

Testikattavuusraportin voi luoda komennolla:
```bash
poetry run invoke coveragereport
```

Robot Framework testit voi suorittaa komennolla:
```bash
poetry run invoke robot
```


Suorita pylint komennolla:
```bash
poetry run invoke lint
```

#### Miten navigoida
Sovellusta käytetään nuolinäppäimillä <kbd>&uarr;</kbd><kbd>&darr;</kbd>.

Valitaksesi seuraavan asian paina <kbd>enter</kbd>.

Valitse tiedostoja uuteen tiedostoon ja poistaessasi tiedostoja valitse tiedostot painamalla <kbd>space</kbd>
