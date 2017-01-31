# Kiril Kruhskov
# GSÖ1TÖ05AU

main = "Yup"
while main == "Yup":
    print("TXT File *1*")
    print("Exit *2*")
    lidur = int(input("1-2 your choice: "))

    if lidur == 1:

        f = open('Text Document.txt', 'w')
        a = input('Write something on your new text document: ')
        f.write('User wrote: ' + str(a))
        f.close()

    if lidur == 2:
        print("Thank you! :) By ...")
        break

    else:
        print("Great job!")