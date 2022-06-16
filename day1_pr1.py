##Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down
 #in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
 #Write a function to help Bob locate the card.

cards_str = input()
cards = list(map(int, cards_str.split()))
query = int(input())

def locate_cards(cards, query):
    mid = int(len(cards)/2)
    a = 0
    while a == 0:
        if cards[mid] == query:
            print("located on:", mid+1, "position")
            a = 1
        elif cards[mid] > query:
            mid += 1
            while a == 0:
                if cards[mid] == query:
                    print("located on", mid+1, "position")
                    a = 1
                else:
                    break
        elif cards[mid] < query:
            mid -= 1
            while a == 0:
                if cards[mid] == query:
                    print("located on", mid+1, "position")
                    a = 1
                else:
                    break
locate_cards(cards, query)
