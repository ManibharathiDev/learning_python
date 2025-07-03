a = 120;
match a:
    case 10:
        print("a is 10")
    case 20:
        print("a is 20")
    case 30:
        print("a is 30")
    case _: # The underscore (_) acts as a wildcard, matching anything not previously matched
        print("a is something else")