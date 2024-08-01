counts, visited = [], {}

def solution(cards):
    for card in cards:
        if card not in visited:
            openCard(cards, card, 1)
    
    if len(counts) == 1:
        return 0
    
    counts.sort(reverse = True)
    return counts[0] * counts[1]

def openCard(cards, cur, depth):
    visited[cur] = True
    
    if cards[cur - 1] not in visited:
        openCard(cards, cards[cur - 1], depth + 1)
    else:
        counts.append(depth)
