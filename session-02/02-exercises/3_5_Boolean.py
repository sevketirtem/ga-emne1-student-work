has_username = True
accepted_rules = True
is_blocked = True

if has_username and accepted_rules and not is_blocked:
    print("Welcome to the game ")
else:
    print("Access denied.")