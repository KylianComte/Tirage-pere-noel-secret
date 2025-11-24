# Tirage Père Noël Secret

Simple Python script to run a "Secret Santa" (Tirage au sort du Père Noël secret). The script assigns each participant a recipient at random, ensuring that no one is assigned themselves, and writes one text file per giver with the name of the assigned recipient and the budget reminder.

---

## Features

- Ensures no participant is assigned to themselves (re-shuffles until a valid assignment is found).
- Creates one file per giver named `<GiverName>.txt` containing:
  - The recipient assigned to them.
  - A budget reminder.
- Very small and easy to modify (list of participants and budget are plain Python lists).

---

## Requirements

- Python 3.6+ (uses only standard library modules)

---

## Usage

1. Clone or download the repository.
2. Edit `tirage.py` to set the participants and the desired budget range:
   - Update `liste_donneurs` with the list of participants (strings).
   - Update `budjet` with two numbers: minimum and maximum budget, e.g. `[10, 15]`.
3. Run the script:

```bash
python3 tirage.py
```

After running, a file `<Name>.txt` will be created for each participant in the current directory. Each file contains a short French message such as:

```
Ton cadeau ira à <Recipient>
Rappel du budjet entre <min> et <max>e max
```

---

## Code overview

Key parts of `tirage.py`:

- `liste_donneurs`: list of givers.
- `liste_receveurs`: a shuffled copy of givers used to assign recipients.
- Loop that checks for any giver assigned to themselves; if found the recipients list is re-shuffled until there are no matches (a simple derangement).
- The script writes per-giver files containing the assignment and budget reminder.
