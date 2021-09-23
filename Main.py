# Think of your favorite mode of transport,
# such as a motorcycle or a car,
# and make a lis that stores several examples.
# Use you list to print a series of statements about these
# items, such as, "I would like to own a Honda
# motorcycle."

vehicles = [
            "1994 toyota supra turbo",
            "2021 dodge challenger srt hellcat",
            "2021 ford mustang shelby gt500",
            "2021 chevrolet camaro zl1"
]

message1 = f"I would like to own a {vehicles[0].title()}."
message2 = f"I would like to own a {vehicles[1].title()}."
message3 = f"I would like to own a {vehicles[2].title()}."
message4 = f"I would like to own a {vehicles[3].title()}."

print(message1)
print(message2)
print(message3)
print(message4)
