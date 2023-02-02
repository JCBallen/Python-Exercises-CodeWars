
# A man was given directions to go from one point to another.
# The directions were "NORTH", "SOUTH", "WEST", "EAST".
# Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
# Going to one direction and coming back the opposite direction right away is a needless effort.
 
# EX: In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going
# north and coming back right away.
# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other,
# therefore, the final result is [].

# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"],
# "NORTH" and "SOUTH" are not directly opposite but they become directly opposite
# after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].


import os

# Clearing the Screen
os.system('cls')


def dirReduc(arr):
    newArr = arr.copy()
    size = int(len(newArr)/2)
    code = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    for aum in range(size):
        i = 0
        # print(newArr)
        while i <= len(newArr)-2:
            if newArr[i] == code[newArr[i+1]]:
                newArr.pop(i)
                newArr.pop(i)
            else:
                i = i+1

    return newArr


# ans = dirReduc(["NORTH", "WEST", "SOUTH", "EAST","NORTH","WEST","EAST","SOUTH","WEST","NORTH","EAST","SOUTH"])
ans = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
print(ans)
