languages = {
    'jung': ['python', 'ruby', 'JS'],
    'jay': ['ruby', 'java'],
    'johny': ['Js', 'html']
}

for k, v in languages.items():
    print(f"{k} can speak")
    for lan in v:
        print(f"\t{lan}")
