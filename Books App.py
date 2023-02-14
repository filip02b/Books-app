# Main Program
keys = ("titlu", "autor", "limba", "nrpagini")
KEY_TITLE = keys[0]
KEY_AUTHOR = keys[1]
KEY_LANG = keys[2]
KEY_PAGES = keys[3]
FRENCH = 'FR'

# Description: read the list of books
# Returns: a list of dictionary items that represents the books
# {titlu, autor, limba, nrpagini}
def ReadListOfBooks():

    list_carti = []

    while True:
        carte = input("Date carte: ").split(",")
        if carte == ['']:
            break
        dict_carte = dict()
        for i in range(4):
            dict_carte[keys[i]] = carte[i].strip()
        list_carti.append(dict_carte)
    return list_carti


# Description: computes the number of books that will be donated
# Input: list_carti - the list of books to be processed
# Returns: nr_books - the number of books for donations
def NrBooksDonations(list_carti):
    nr_books = 0
    for carte in list_carti:
        if int(carte[KEY_PAGES]) > 200 and carte[KEY_LANG] != FRENCH:
            nr_books += 1
    return nr_books


# Description: builds the list of books that will be given to the brother
# Input: list_carti - the list of books to be procesed
# Returns - list_authors - the list of the authors of the books that the brother will receive
def BooksForBrother(list_carti):
    list_authors = []
    for carte in list_carti:
        if carte[KEY_LANG] == FRENCH and int(carte[KEY_PAGES]) <= 200:
            list_authors.append(carte[KEY_AUTHOR])
    return list_authors


# # Description: builds the list of books that will remain to Ion
# # Input: list_carti - the list of books to be processed
# # Returns: list_titles - the list of the authors of the books that the briother will receive
# def RemainingBooks(list_carti):
#     list_titles = []
#     for carte in list_carti:
#         if int(carte[KEY_PAGES]) <= 200 and carte[KEY_LANG] != FRENCH:
#             list_titles.append(carte[KEY_TITLE])  
#     return list_titles


# Description: builds the list of books that will be donated
# Input: list_carti - the list of books to be processed
# Returns: list_dontation_books - the list of the books that will be donated
def GetBooksForDonations(list_carti):
    list_dontation_books = []
    for carte in list_carti:
        if int(carte[KEY_PAGES]) > 200:
            list_dontation_books.append(carte[KEY_TITLE])
    return list_dontation_books


def RemainingBooks(list_carti):
    list_titles_ion = []
    list_brother = BooksForBrother(list_carti)
    list_donations = GetBooksForDonations(list_carti)
    for carte in list_carti:
        if carte[KEY_AUTHOR] not in list_brother and carte[KEY_TITLE] not in list_donations:
            list_titles_ion.append(carte[KEY_TITLE])  
    return list_titles_ion




list_carti = ReadListOfBooks()
print("Se doneaza:", NrBooksDonations(list_carti))
print("Fratele lui Ion primeste: ", BooksForBrother(list_carti))
print("Ion ramane cu: ", RemainingBooks(list_carti))
print("Urmatoarele carti se vor dona: ", GetBooksForDonations(list_carti))