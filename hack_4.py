"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    arr = []

    for i in range(len(result)):
        if i == len(result) - 1:
            arr.append(result[i].upper())
        else:
            arr.append(result[i])
    
    return "".join(arr)

print(fn_hack_4())