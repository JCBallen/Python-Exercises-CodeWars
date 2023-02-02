def capitals(word):
    positions=[]
    for idx,letter in enumerate(word):
        if letter.isupper():
            positions.append(idx)
    return positions

ans=capitals('CodEWaRs')
print(ans)