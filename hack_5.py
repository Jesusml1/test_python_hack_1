"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
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
            arr.append(result[i])
    
    return "".join(arr)

    return result  