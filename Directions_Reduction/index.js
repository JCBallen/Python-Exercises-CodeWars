function isValidWalk(walk) {
    const newArr = [...walk]
    size = parseInt((newArr.length) / 2)
    code = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    for (x = 0; x < size; x++) {
        i = 0
        while (i <= (newArr.length - 2)) {
            if (newArr[i] == code[newArr[i + 1]]) {
                newArr.splice(i, 1)
                newArr.splice(i, 1)
            } else {
                i++
            }
        }
    }
    return newArr


}
ans = isValidWalk(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])

console.log(ans)

