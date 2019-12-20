import string

def is_pangram(s):
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s.lower(): return False
    return True




pangram = "Pack my box with five dozen liquor jugs"
# pangram = "This isn't a pangram!"
print(is_pangram(pangram))

