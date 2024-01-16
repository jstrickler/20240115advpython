
states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt", "w") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        states_out.write(state + "\n")  # write() does not automatically add newline

with open("../DATA/fruit1.txt") as fruit1_in:
    with open("fruitstuff.txt", "w") as fruit_out:
        for fruit in fruit1_in:
            if fruit.startswith("l"):
                fruit_out.write(fruit)
