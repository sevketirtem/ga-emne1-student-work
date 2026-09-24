# AI Usage Documentation – KI-dokumentasjon

**Tool used:** Claude (Anthropic)

## How AI was used

I used Claude as a **SOCRATIC** tutor, not as a code generator. Claude did not
write code for me at any point, and I did not copy-paste any code from
Claude into my solution.

Specifically, I used Claude for:

1. **Translation** — The assignment text (`Arbeidskrav 1 – Python`) is
   written in Norwegian. My Norwegian is not yet strong enough to read
   technical instructions quickly and precisely, so I asked Claude to
   translate sections into Turkish so I could be sure I understood the
   requirements correctly.
2. **Guided problem-solving for Oppgave 1.1** — Instead of giving me
   solutions, Claude asked me guiding questions about my own code (e.g.
   "what does `while not valid:` do when `valid` is `False`?", "what's the
   difference between checking if input is a valid integer versus checking
   if it's a positive integer?"). It asked me to predict what my code would
   do before running it, then compare my prediction to the actual output.
   All debugging (missing parentheses, unclosed quotes, the `print()`
   return-value issue, the `while not valid:` logic) was done by me, based
   on questions Claude asked rather than answers Claude gave.
3. **README.md structure** — I asked Claude to help me organize and word
   the README.md (structure of sections, phrasing in English), based on
   information and decisions I provided about my own code and situation.

## Design decisions I made myself (prompted by Claude's questions)

- Keeping `is_valid_integer()` separate from the positivity check in
  `get_positive_integer()`, so `is_valid_integer()` stays reusable for
  later tasks that may need negative numbers (e.g. Oppgave 1.3).
- Using the flag-variable pattern (`valid = False` / `while not valid:`)
  instead of `continue`/`break`, consistent with what has been taught in
  class so far.
- Deliberately not using `try/except`, `.isdigit()`, or classes, since
  these are taught in Week 39, which I have not reached yet in the course.

## Full conversation

The full conversation with Claude for this assignment is in this link:
https://claude.ai/share/49bdff7c-ec36-4aad-b4a1-e646bf2079ec

