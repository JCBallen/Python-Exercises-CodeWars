import os
os.system("cls")

# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

#  For seconds = 62, your function should return
#     "1 minute and 2 seconds"
#  For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"


def format_duration(seconds):

    if seconds == 0:  # in case 0 seconds return "now"
        return "now"

    # Normal cases

    full_time = [0, 0, 0, 0, seconds]
    full_text = [" year", " day", " hour", " minute", " second"]
    final_text = ""
    final = ""

    if full_time[4] >= 60:
        aux = full_time[4]
        full_time[4] = aux % 60
        full_time[3] = aux//60
    if full_time[3] >= 60:
        aux = full_time[3]
        full_time[3] = aux % 60
        full_time[2] = aux//60
    if full_time[2] >= 24:
        aux = full_time[2]
        full_time[2] = aux % 24
        full_time[1] = aux//24
    if full_time[1] >= 365:
        aux = full_time[1]
        full_time[1] = aux % 365
        full_time[0] = aux//365

# Until here we have separate years, days, hours, minutes, seconds. Only the "string part" is not done yet

    final_text = list(zip(full_time, full_text))
    aux_text = [list(x) for x in final_text]

    indx = 0
    i = 0

    # In this while we pop the items when they are zero (ex. 0 years, 0 seconds)
    while i < 5:
        if final_text[i][0] == 0:
            aux_text.pop(indx)
        else:
            # and also add de plural "s" if corresponds (ex. 5 hour -> 5 hours)
            if aux_text[indx][0] > 1:
                aux_text[indx][1] += "s"
            indx += 1
        i += 1

    aux_text.reverse()
    aux_text = [f"{x[0]}{x[1]}" for x in aux_text]

    # If the actual answer is just 1 item (ex. 3 years), return it now
    if len(aux_text) == 1:
        return aux_text[0]

    for i in range(len(aux_text)-1):
        if i == 0:
            final = aux_text[i+1]+" and "+aux_text[i]
        else:
            final = aux_text[i+1]+", "+final

    return final


print(format_duration(86401))