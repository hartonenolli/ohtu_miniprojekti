# Käyttöohje

## Asennus

### Kopioi projekti omalle koneellesi

Asenna riippuvuudet komennolla:
```bash
poetry install
```

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

Suorita pylint komennolla:
```bash
poetry run invoke lint
```
