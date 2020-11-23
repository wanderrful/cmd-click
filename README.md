# Cmd Click!

This is a demonstration for how we can use Click's nested commands, along with Python's built-in `cmd.Cmd` class for a looping command prompt REPL with nested commands!

This was created as a Poetry project, though I didn't bother with writing tests since it's just a demonstration. Not sure of how acceptance tests would work for a `cmd.Cmd` CLI app. _At time of writing_, anyway.


## How to use this app

1. `poetry install` if you have Poetry
   2. If you don't have Poetry, `pip install click` should suffice
2. `poetry run cmdclick` to demonstrate just the hierarchy of nested commands
   2. To see with the `cmd.Cmd` loop, `python cmdclick.py` should suffice, though the colors may garble your stdout depending on your terminal window.
3. Type `?` to see the available commands
4. Use the `pets` command to see Click's help content and try out the nested Click commands!
5. Type `exit` to quit

## Map of nested commands:

- `pets`
  - `dogs`
    - `labrador`
      - `yellow` (command)
      - `black` (command)
      - `chocolate` (command)
    - `golden`
      - `toasted-marshmallow` (command)
      - `blondie-brownie` (command)
      - `condensed-milk` (command)
      - `copper` (command)
  - `cats`
    - `burmese`
      - `calico` (command)
      - `marmalade` (command)


## Enhancement ideas

To navigate through the Click command interface, maybe we could have a "state" variable at the `cmd.Cmd` subclass level that creates a `MultiCommand` of all Click commands that you should now be able to access.