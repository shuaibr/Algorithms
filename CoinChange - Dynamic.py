# USD - $1, $5, $10, etc.
currency = [1, 5, 10, 20, 50, 100]

# the amount to change - $120
amount = 16

# initialize arrays for $0
minimum_number_of_currency = [0]
currency_composition = [[]]

for i in range(1, amount + 1):
    best = 10000
    best_currency_composition = None

    for j in currency:
        if i - j > -1 and minimum_number_of_currency[i - j] + 1 < best:
            print("i: ", i, " j: ", j, " i - j: ", (i-j), " min_num[i-j]: ", minimum_number_of_currency[i - j])
            best = minimum_number_of_currency[i - j] + 1
            best_currency_composition = currency_composition[i - j] + [j]

    minimum_number_of_currency.append(best)
    currency_composition.append(best_currency_composition)

print("comp: ",best_currency_composition, " best: ", best)
