def analyze_text(text: str):
    digits = 0
    letters = 0
    upper = 0
    lower = 0
    symbols = 0

    for ch in text:
        if ch.isdigit():
            digits += 1
        elif ch.isalpha():
            letters += 1
            if ch.isupper():
                upper += 1
            else:
                lower += 1
        else:
            symbols += 1

    return {
        "digits": digits,
        "letters": letters,
        "upper": upper,
        "lower": lower,
        "symbols": symbols
    }
