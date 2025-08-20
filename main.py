import sys

from stats import count_chars,count_words, sorting 
def main():
    if len(sys.argv) == 2:
        contents = get_book_text(sys.argv[1])
        wordcount = count_words(contents) 
        charcount = count_chars(contents)
        items = sorting(charcount)
        
        print("============ BOOKBOT ============")
        print(f"book path: {sys.argv[1]}") 
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for item in items:
            print(f"{item["char"]} : {item["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents       

main()

