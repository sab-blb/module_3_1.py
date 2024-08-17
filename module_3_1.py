print(f"{"Задача"} {'"Счётчик вызовов"'}")

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string_ = str(string)
    result = (len(string_), string_.upper(), string_.lower())
    count_calls()
    return result


def is_contains(string, list_to_search):
    string = str(string).upper() #or .lower
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).upper() == string: #or .lower
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))


print(calls)
