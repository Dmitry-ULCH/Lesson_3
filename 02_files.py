def main():
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        text = referat.read()
        text_len = len(text)
        lines = text.split()
        words_count = len(lines)
        edited = text.replace('.', '!')
        print (text_len)
        print (words_count)
    with open('referat2.txt', 'w', encoding='utf-8') as referat2:
        referat2.write(edited)


if __name__ == "__main__":
    main()
