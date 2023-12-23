# Different approach with helps of GitHub Copilot

def parse_card(card):
    parts = card.split('|')
    return set(map(int, parts[0].split())), set(map(int, parts[1].split()))

def count_matches(card):
    return len(card[0] & card[1])

def process_card(card, cards):
    matches = count_matches(card)
    new_cards = cards[cards.index(card)+1:cards.index(card)+1+matches]
    return new_cards

def solve(cards):
    cards = [parse_card(card) for card in cards]
    total_cards = cards.copy()
    i = 0
    while i < len(total_cards):
        new_cards = process_card(total_cards[i], cards)
        total_cards.extend(new_cards)
        i += 1
    return len(total_cards)

file = open("../input.txt", "r")
cards = [line.split(': ')[1] for line in file]
print(solve(cards))
file.close()
