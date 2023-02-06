"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]

    i = 0
    while i < 6:
        if i % 2 != 0:
            result.insert(i, '@')
        i += 1

    return result  

print(fn_hack_9())
