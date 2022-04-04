![GitHub Actions](https://github.com/ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti/workflows/Pipeline/badge.svg)
# Software Engineering 2022-Spring Miniproject

## Documentation

- [Product Backlog](https://docs.google.com/spreadsheets/d/1mJlabSWnpCrgyVOKPa34vqNtYNF_JvlXrHQ4NPKWA3c/edit#gid=0)
- [Definition of done](./documentation/definition_of_done.md)

## Asennus- ja käyttöohje

Asennusohje
1.	Kloonaa projekti tietokoneellesi navigoimalla komentorivillä haluamaasi hakemistoon ja syöttämällä komento: git clone git@github.com:ohtu-2022k-minivinkit/ohtu-2022k-miniprojekti.git

2.	Hakemistosta tulisi nyt löytyä kansio nimeltä ’ohtu-2022k-miniprojekti’ – navigoi sinne

3.	Asenna projektin riippuvuudet komennolla: poetry install

Seuraavien riippuvuuksien tulisi asentua: 
  • pyparsing
  • attrs
  • iniconfig
  • lazy-object-proxy
  • packaging
  • pluggy
  • py
  • tomli
  • typing-extensions
  • wrapt 
  • astroid 
  • dill 
  • isort 
  • mccabe 
  • platformdirs
  • pytest 
  • python-dotenv 
  • coverage 
  • invoke 
  • pylint
  • pytest-dotenv 
  • robotframework 
  • robotframework-databaselibrary

Käyttöohje
1.	Käynnistä sovellus komennolla: poetry run python3 src/index.py 
a.	Voit pysäyttää sovelluksen milloin tahansa painamalla control + c2
2.	Sovellus tarjoaa seuraavat vaihtoehdot:
i.	x lopeta
ii.	1 lisää vinkki
iii.	2 tulosta vinkit
3.	Paina 1 + enter jos haluat lisätä vinkin:
a.	Sovellus pyytää sinua kirjoittamaan otsikon ja linkin. 
i.	Kirjoita otsikko ja paina enter 
ii.	Kirjoita linkki ja paina enter
iii.	Huomaa, että linkin täytyy olla sopivassa muodossa!(Jos lisäät linkin väärässä muodossa, lisääminen keskeytyy ja joudut aloittamaan lisäämisen alusta)
4.	Paina 2 + enter jos haluat, että tallennetut linkit tulostuvat
5.	Paina x + enter kun haluat lopettaa

