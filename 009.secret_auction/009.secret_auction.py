from art import logo

print(logo)
bidders = {}
want_continue = True

while want_continue:
    key = input("What is your name?\n")
    value = int(input("What is your bid?\n$"))
    bidders[key] = value
    answer = input("Are there any bidders? yes or no?\n")
    if answer.lower() == "no":
        want_continue = False
        max_bid = max(bidders.values())
        for name in bidders:
            if bidders[name] == max_bid:
                print(f"The winner is {name} with the bid ${max_bid}")
