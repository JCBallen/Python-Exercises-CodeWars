
# Given two arrays of strings a1 and a2 return a sorted array r in
# lexicographical order of the strings of a1 which are substrings of strings of a2.

# EX:
# a1 = ["arp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp']


def in_array(a1, a2):
    r = []
    for a in a1:
        for b in a2:
            if a in b and a not in r:  # con el "in" se puede buscar una palabra dentro de una frase
                r.append(a)
    return sorted(r)  # ordena alfabeticamente


print(in_array(["arp", "live", "strong"], [
      "lively", "alive", "harp", "sharp", "armstrong"]))
