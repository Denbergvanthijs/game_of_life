# ChangeLog voor Game of Life

## Stap 2

### 2019.11.28.2

- Functie `update_cell` geïmplementeerd
- Bugfix in `test_simulator.py`

### 2019.11.28.1

- Tot de realisatie gekomen dat de functie `update` kan worden gesplitst in functies om te testen
- Vervolgens tests geschreven voor de toekomstige functie `update_cell` in `test_simulator.py`

### 2019.11.25.5

- Unittest slaagde niet door het niet meegeven van een argument

### 2019.11.25.4

- `Update` in `Simulator.py` aangepast zodat `get_rules` wordt gebruikt
- `get_rules` uitgeschreven in `Simulator.py`
- Gebruiker kan nu een string met de ruleset invullen in `main.py`
- `test_get_rules` bug verwijderd

### 2019.11.25.3

- Test geschreven voor `get_rules` in `test_simulator.py`

## Stap 1

### 2019.11.25.2

- Functie `fill_world` gemaakt om wereld te vullen
- `Update` in `Simulator.py` aangepast om de cellen te updaten tijdens een generatie
- Wereld groter gemaakt naar 100x100 om populatie levend te houden

### 2019.11.25.1

- Test geschreven voor `fill_world` in `test_world.py`
- Wereld verkleint naar 10x4 voor sneller debuggen
