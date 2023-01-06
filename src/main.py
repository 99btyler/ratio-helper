

things = {}
while True:
    thing_name = input("thing_name: ")
    thing_amount = 0
    while True:
        try:
            thing_amount = int(input("thing_amount: "))
            break
        except ValueError:
            continue # ask again
    things[thing_name] = thing_amount
    if input("Done with things?(press y)") == "y":
        break

for key in things.keys():
    print(f"{key}({things[key]})")

things_to_isolate = []
while True:
    thing_to_isolate_name = input("thing_to_isolate_name: ")
    if (thing_to_isolate_name not in things) or (thing_to_isolate_name in things_to_isolate):
        continue
    things_to_isolate.append(thing_to_isolate_name)
    if input("Done with things?(press y)") == "y":
        break


things_amount = 0
things_to_isolate_amount = 0

for key in things.keys():
    things_amount += things[key]
    if key in things_to_isolate:
        things_to_isolate_amount += things[key]

things_not_isolated_amount = things_amount - things_to_isolate_amount

things_to_isolate_name = "".join(things_to_isolate)


print(f"{things_to_isolate_amount} {things_to_isolate_name} vs. {things_not_isolated_amount} non-{things_to_isolate_name}")
print(f"1 {things_to_isolate_name} = {things_not_isolated_amount/things_to_isolate_amount} non{things_to_isolate_name}")
print(f"{(things_to_isolate_amount/things_amount)*100}% {things_to_isolate_name} vs. {(things_not_isolated_amount/things_amount)*100}% non-{things_to_isolate_name}")