# Sumár

Tento repozitár je súčasťou kurzu Pythonu organizovaného SDA.

Modul, ktorého sa tento repozitár týka, je súčasťou kurzu Pythonu, ktorý usporadúva SDA a zaoberá sa témou: Návrhové vzory a good practices.

Tento repozitár obsahuje materiály, ktoré zahŕňajú základné informácie o preberanej látke, prezentované príklady a ďalšie úlohy a materály.


## ✅ Nastavenie Pylintu v PyCharme (External Tools)
	1.	Otvor si v PyCharme:
	•	Settings → Tools → External Tools
	2.	Klikni na tlačidlo + a vyplň nasledovné hodnoty:

Linux / macOS
	•	Name: pylint
	•	Program: $PyInterpreterDirectory$/pylint
	•	Arguments: $FilePath$
	•	Working directory: $ProjectFileDir$

Windows
	•	Name: pylint
	•	Program: $PyInterpreterDirectory$\pylint
	•	Arguments: $FilePath$
	•	Working directory: $ProjectFileDir$

	3.	Spustenie Pylintu:
	•	Prejdi do: Tools → External Tools → pylint
	•	Spustí sa analýza pre aktuálne otvorený súbor

## ✅ Automatická kontrola kódu cez pre-commit hooky (Black + Flake8)
1. Inštalácia nástrojov
```bash
pip install black
pip install flake8
pip install pre-commit
```
2. Vytvor súbor .pre-commit-config.yaml v koreňovom adresári projektu:
````yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-bugbear]
````
3. Aktivácia hookov:
```bash
pre-commit install
```
Odteraz sa pri každom git commit automaticky spustí Black a Flake8 len na zmenené súbory.

4. Manuálne spustenie hookov na celý projekt (voliteľné):
````bash
pre-commit run --all-files
````
