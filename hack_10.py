"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"

    arr = []
    for i in range(len(result)):
        if result[i] == 'o':
            arr.append(str(0))
        elif result[i] == 'i':
            arr.append(str(1))
        elif result[i] == 'a':
            arr.append('@')
        else:
            arr.append(result[i].upper())

    return arr  