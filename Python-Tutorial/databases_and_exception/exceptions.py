def divide_by_zero(num):
    try:
        num = num / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")


def greater_than_zero(num):
    try:
        assert num > 0
    except:
        print("This should throw an assertion error")
    else:  # This will execute if no exception was thrown
        print("Phewww")
    finally:
        print("Finally it did end!!")


def try_finally():
    try:
        print("I tried")
    finally:
        print("Finally i could do it")


def throw_exception():
    try:
        print("It is throwing an exception(raise) cuz it has keeda :P")
        raise Exception("KEEDA")
    except Exception as e:
        print("It did cuz of", e)


divide_by_zero(5)
print()
greater_than_zero(-1)
print()
greater_than_zero(86)
print()
try_finally()
print()
throw_exception()
