# Arbeidskrav 1 – Python

**Navn:** Sevket Suleyman Irtem 
**Emne:** Emne 1 – Grunnleggende backend-programmering
**Modul:** Modul 1 – Python
**Innleveringsdato:** 25.09.2026

## Om innleveringen

This submission currently contains a solution to **Oppgave 1.1** only
(inside `oppgave-1.py`), submitted early with the school's permission due to
time constraints this week. I used AI to help with translation (the
assignment text is in Norwegian, and my Norwegian is not yet strong enough
to read it quickly and precisely) and to help structure this README.md. I
did not copy-paste any code from AI. Because of this, I was not able to
complete all subtasks in time.

Features like `try/except` and classes are taught in Week 39, which I have
not reached yet. My Norwegian is not strong enough to follow Monday's live
lectures directly, so I only listen on Mondays, then work through each
lecture with the transcript on Tuesdays and Wednesdays, and do the exercises
for the rest of the week. This works, but takes time — my GitHub history
shows each week's exercises. I am learning and applying everything Thomas
teaches myself; I will complete and add the remaining subtasks after this
deadline.
## Filstruktur

| Fil                   | Innhold                                             |
|-----------------------|-----------------------------------------------------|
| `oppgave-1.py`        | Solution to Oppgave 1.1 only (1.2-1.4 not yet done) |
| `oppgave-1-notes.py` | Earlier, commented version of oppgave-1.py, kept to show my learning process (not the final submission — see `oppgave-1.py`) |
| `KI-dokumentasjon.md` | AI usage documentation                              |
| `README.md`           | Denne filen                                         |



## Oppgave 1 (`oppgave-1.py`)

**Hva oppgaven går ut på:**
This assignment asks for a single Python program (`oppgave-1.py`) combining
four subtasks using the fundamental building blocks of Python (variables,
data types, operators, `input()`, conditions, and loops):

- 1.1 — Ask the user for the number of study sessions and minutes per
  session, then calculate total study time in hours and minutes.
- 1.2 — Ask for a text and display character count, lowercase version,
  reversed text, and whether it contains "python".
- 1.3 — Ask for a number range and find all even numbers, all numbers
  divisible by 3, and the sum of the range.
- 1.4 — Combine these into a menu (options 1–4), redisplay the menu after
  each action, and only exit on option 4.

At every step, the program must validate input. Invalid input — empty,
text instead of a number, negative or zero where not allowed, or an
invalid range (`start > end`) — must not crash the program; it should show
a clear error message and ask again.

**Hvordan jeg løste det:**
- I wrote separate functions (`print_error`, `is_valid_integer`,
  `get_positive_integer`, `calculate_used_time`) to keep the code organized
  and reusable. So far I have only completed Task 1.1 fully and correctly.
  I did not have time to study Week 39's material, so I deliberately limited
  myself to concepts from Weeks 35–38 and avoided `try/except`, classes,
  `.isdigit()`, `continue`, and `break`.
- Input validation uses my own `is_valid_integer()` function instead of
  `try/except` or `.isdigit()`: I check each character is between `"0"` and
  `"9"`, handling a leading `-` separately so negative numbers are still
  recognized as valid integers (just not positive ones). Only after
  validation do I convert with `int()`.
- For the validation loop, I used the flag pattern from class (similar to
  `guessed_correctly` in the guessing game): `valid = False` with
  `while not valid:`, so the program keeps asking until a valid value is
  entered. No `continue` or `break`.
- I plan to use the same flag pattern for the main menu loop in 1.4
  (`program_running = True/False`).

**Testet med:**

- Empty input
- 3.5
- Letters (`abc`)
- Negative numbers (`-3`)
- Zero (`0`)
- Valid input (`5` sessions × `45` minutes → "3 hours and 45 minutes")

In all cases, the program behaved as expected: invalid input showed a clear
error message and asked again; valid input produced the correct result.

## Known issues / limitations
- Only Oppgave 1.1 is implemented; the rest of Arbeidskrav 1 will be
  completed and added after this initial deadline, with the school's
  agreement.
- User-facing text is in English; the assignment text allows this
  ("Tekst som vises til brukeren ... kan være på norsk" — Norwegian was
  optional, not required).

---

## Video

Video eller videolenke:
https://gokstadakademietas-my.sharepoint.com/:v:/g/personal/sev_irt015_gokstadakademiet_no/IQBe-VYXf1RXRJ1iKc7MTfdIAYJ03HaITtWapIBhl-99Yio?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=YrtxAa 
---

## Git repository
GitHub: https://github.com/sevketirtem/ga-emne1-student-work.git
Alt arbeid er committet og pushet til `ga-emne1-student-work` på GitHub (bruker: sevketirtem).
Git history is also included as `git-history.txt` in this submission.