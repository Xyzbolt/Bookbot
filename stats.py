
def count_words(contents):
    words = contents.split()
    wcount = len(words)
    return wcount

def count_chars(contents):
    filestring = contents.lower()
    charcount = {}
    for char in filestring:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1
    return charcount

def sorting(charcount):
    items = []
    for char in charcount:
        if char.isalpha():
            items.append({"char": char, "num": charcount[char]})
    
    def sort_on(item):
        return item["num"]
    items.sort(reverse=True, key=sort_on)
    return items
