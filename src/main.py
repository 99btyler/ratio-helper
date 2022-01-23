

def ask(question, requires_number=False):
	answer = input(f"{question}: ")
	while requires_number and not answer.isdigit():
		answer = input(f"{question}: ") # asking again
	return int(answer) if requires_number else answer


print("\n---- ratio-helper ----")

# GET ALL DATA
things = {}
while True:
	thing_name = ask("\nthing_name")
	thing_amount = ask("thing_amount", True)
	things[thing_name] = thing_amount
	if ask("\nDONE?(press y)") == "y":
		break

print("")
for key in things.keys():
	print(f"{key}({things[key]})")

things_to_isolate = []
while True:
	thing_to_isolate_name = ask("\nthing_to_isolate_name")
	while thing_to_isolate_name not in things.keys():
		thing_to_isolate_name = ask("thing_to_isolate_name") # asking again
	if thing_to_isolate_name not in things_to_isolate:
		things_to_isolate.append(thing_to_isolate_name)
	if ask("\nDONE?(press y)") == "y":
		break

# EXTRACT SPECIFIC DATA
things_amount = 0
for key in things.keys():
	things_amount += things[key]

things_to_isolate_name = "".join(things_to_isolate)

things_to_isolate_amount = 0
for key in things.keys():
	if key in things_to_isolate:
		things_to_isolate_amount += things[key]

things_not_isolated_amount = things_amount-things_to_isolate_amount

# FINISH
print(f"\n{things_to_isolate_amount} {things_to_isolate_name} vs. {things_not_isolated_amount} non-{things_to_isolate_name}")
print(f"1 {things_to_isolate_name} = {round(things_not_isolated_amount/things_to_isolate_amount, 2)} non-{things_to_isolate_name}")
print(f"{round((things_to_isolate_amount/things_amount)*100)}% {things_to_isolate_name} vs. {round((things_not_isolated_amount/things_amount)*100)}% non-{thing_to_isolate_name}")


print("\n----------------------\n")

