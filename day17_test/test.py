def ticker(text, display, tick):  # tick = 30
    full_text = (display * " ") + text + (display * " ")

    if tick > display + len(text):
        tick = tick - (display + len(text))  # 10,1
        return (full_text[tick:tick + display])

    else:
        return (full_text[tick:tick + display])

text = " an tell each. their before very high call go no? who now animal year light live."
display = 18
tick = 1542

print(ticker(text,display,tick))
# '            three only new then? g'
