def response(hey_bob):
    cleaned_string = hey_bob.strip();
    if cleaned_string.endswith("?") and cleaned_string.isupper():
        return "Calm down, I know what I'm doing!"
    if cleaned_string.endswith("?"):
        return "Sure."
    if cleaned_string.isupper():
        return "Whoa, chill out!"
    if cleaned_string == "":
        return "Fine. Be that way!"
    return "Whatever."
