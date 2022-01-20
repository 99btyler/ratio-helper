

def ask(question, requires_number=False):
	answer = input(f"{question}: ")
	while requires_number and not answer.isdigit():
		answer = input(f"{question}: ") # asking again
	return int(answer) if requires_number else answer


things = {}
amount_total = 0

while True:

	name = ask("name")
	amount = ask("amount", True)
	things[name] = amount
	amount_total += amount

	if ask("DONE?(press y)") == "y":
		break

for key in things:
	print(f"{key}({things[key]})")


things_to_isolate = []
amount_isolated = 0

while True:

	thing_to_isolate = ask("thing_to_isolate")
	while thing_to_isolate not in things.keys():
		thing_to_isolate = ask("thing_to_isolate") # asking again
	things_to_isolate.append(thing_to_isolate)
	amount_isolated += things[thing_to_isolate]

	if ask("DONE?(press y)") == "y":
		break


isolated_name = "".join(things_to_isolate)
amount_non_isolated = amount_total-amount_isolated

print(f"{amount_isolated} {isolated_name} vs. {amount_non_isolated} non-{isolated_name}")
print(f"1 {isolated_name} = {amount_non_isolated/amount_isolated} non-{isolated_name}")
print(f"{round((amount_isolated/amount_total)*100)}% {isolated_name}, {round((amount_non_isolated/amount_total)*100)}% non-{isolated_name}")
