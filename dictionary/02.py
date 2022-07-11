values = dict()
counter = int(1)

while True:

    value = str(input("Enter with a number or type q to quit: "))

    if value in "Qq":
        print(values)
        break
    else:
        values[f"{counter}º number"] = value
        counter += 1
