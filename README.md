# rock-paper-scizor

Juego de consola basado en el clásico "Piedra, Papel o Tijeras", desarrollado en Python usando [Typer](https://typer.tiangolo.com/) y [Rich](https://rich.readthedocs.io/).

## Descripción
Este proyecto permite jugar una versión personalizada de "Piedra, Papel o Tijeras" desde la terminal. Puedes jugar contra la computadora y agregar nuevos elementos y reglas al juego.

## Requisitos
- Python >= 3.13
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://rich.readthedocs.io/)

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Lezard-21/rock_paper_scizor.git
   cd rock_paper_scizor
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install typer rich
   ```

## Uso
El archivo principal es `main.py`. Puedes ejecutar los siguientes comandos:

### Jugar una partida
```bash
python main.py play <item>
```
Donde `<item>` puede ser `rock`, `paper` o `scizor` (o cualquier otro que hayas agregado).

**Ejemplo:**
```bash
python main.py play rock
```

### Agregar un nuevo elemento
```bash
python main.py add <item>
```
El programa te preguntará a qué elementos le gana el nuevo item (por índice).

**Ejemplo:**
```bash
python main.py add spook
```

## Cómo funciona
- El juego utiliza un diccionario para definir las reglas de qué elemento le gana a cuál.
- Puedes agregar nuevos elementos y definir sus relaciones de victoria.
- La lógica principal está en `main.py`.

## Créditos
Desarrollado por David.
