calls = 0
def count_calls():
    global calls
    calls += 1
    return calls-1

def string_info(name_str):
    length = str(len(name_str))
    upp = name_str.upper()
    low = name_str.lower()
    count_calls()
    result = '(' + length + ",'" + upp + "', '" + low + "'" + ')'
    return result

def is_contains(name_str1, list_to_search):
    for i in list_to_search:                                        #поэлементно принимает i значения из списка
        if i.lower() == name_str1.lower():                          #переводим к нижнему регистру сравнеиваемые слова
            a = True
            break
        else:
            a = False
    count_calls()
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)
