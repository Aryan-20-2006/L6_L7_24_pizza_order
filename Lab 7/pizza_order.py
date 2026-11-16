TOPPINGS = {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}
SIZES = {"S": 8, "M": 10, "L": 12}

# Fixes after fuzz testing: every function now rejects bad input with a
# ValueError instead of crashing with KeyError / AttributeError /
# ZeroDivisionError / OverflowError.


def toppings_price(toppings_csv):
    if not isinstance(toppings_csv, str):
        raise ValueError("toppings must be a string")
    total = 0
    for t in toppings_csv.split(','):
        name = t.strip().lower()
        if name not in TOPPINGS:
            raise ValueError(f"unknown topping: {t.strip()!r}")
        total += TOPPINGS[name]
    return total


def pizza_inches(size):
    if not isinstance(size, str):
        raise ValueError("size must be a string")
    key = size.strip()
    # isascii() guard: 'ſ'.upper() == 'S' would otherwise be accepted as small
    if not key.isascii() or key.upper() not in SIZES:
        raise ValueError(f"unknown size: {size!r}")
    return SIZES[key.upper()]


def split_bill(text):
    if not isinstance(text, str):
        raise ValueError("bill must be a string like '900/3'")
    parts = text.split('/')
    if len(parts) != 2:
        raise ValueError("bill must be in the form total/people")
    total, people = int(parts[0]), int(parts[1])  # int() raises ValueError itself
    if people <= 0:
        raise ValueError("number of people must be positive")
    if total < 0:
        raise ValueError("total cannot be negative")
    try:
        return round(total / people, 2)
    except OverflowError:
        raise ValueError("total is too large")


def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)
    print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)
    print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)
    print("Per Person:", result)


if __name__ == "__main__":
    main()
