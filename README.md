# Game of Life Visualisor

## Readme

A data type and graphical visualisation (based on Python Pygame) for implementing Conway's Game of Life.

These files are used in an assignment of the course Behaviour-based Simulation given in the second year of the Bachelor-programme Artificial Intelligence at the HU University of Applied Sciences Utrecht.

For information on how to use, see the appropriate Canvas page.

***

## ChangeLog

In onderstaande ChangeLog zijn de gemaakte wijzigingen beschreven. De commits zijn van recent naar minst recent gesorteerd en zijn voor zover het mogelijk is ingedeeld in de drie gevraagde stappen.

***

### Stap 3

#### 2019.11.29.2

- `get_rules` en `update_cell` in `Simulator.py` herschreven zodat tests werken
- Kleine verbeteringen in `World.py` zodat rekening wordt gehouden met de startleeftijd
- Bugfixes in tests voor simulator en world

#### 2019.11.29.1

- Extra tests geschreven voor de age in `test_update_cell` en `test_get_rules`

### Stap 2

#### 2019.11.28.3

- ChangeLog verplaatst naar `README.md`
- Bugfix in `Simulator.py`

#### 2019.11.28.2

- Functie `update_cell` geïmplementeerd
- Bugfix in `test_simulator.py`

#### 2019.11.28.1

- Tot de realisatie gekomen dat de functie `update` kan worden gesplitst in functies om te testen
- Vervolgens tests geschreven voor de toekomstige functie `update_cell` in `test_simulator.py`

#### 2019.11.25.5

- Unittest slaagde niet door het niet meegeven van een argument

#### 2019.11.25.4

- `Update` in `Simulator.py` aangepast zodat `get_rules` wordt gebruikt
- `get_rules` uitgeschreven in `Simulator.py`
- Gebruiker kan nu een string met de ruleset invullen in `main.py`
- `test_get_rules` bug verwijderd

#### 2019.11.25.3

- Test geschreven voor `get_rules` in `test_simulator.py`

***

### Stap 1

#### 2019.11.25.2

- Functie `fill_world` gemaakt om wereld te vullen
- `Update` in `Simulator.py` aangepast om de cellen te updaten tijdens een generatie
- Wereld groter gemaakt naar 100x100 om populatie levend te houden

#### 2019.11.25.1

- Test geschreven voor `fill_world` in `test_world.py`
- Wereld verkleint naar 10x4 voor sneller debuggen
