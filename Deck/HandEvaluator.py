from Cards.Card import Card, Rank

# Done (TASK 3) Santiago Vélez Cruz: Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    #rank count
    rank_counts = {}
    for card in hand:
        rank_value = card.rank.value
        if rank_value in rank_counts:
            rank_counts[rank_value] += 1
        else:
            rank_counts[rank_value] = 1

    #suit count
    suit_counts = {}
    for card in hand:
        suit = card.suit
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1

    #flush detecter
    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush_suit = suit
            break
    is_flush = flush_suit is not None

    #straight detecter
    unique_ranks = sorted(list(set([card.rank.value for card in hand])), reverse=True)
    if 14 in unique_ranks:
        unique_ranks.append(1)

    is_straight = False
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i] - unique_ranks[i+4] == 4:
            is_straight = True
            break

    #straight flush detecter
    is_straight_flush = False
    if is_flush:
        suited_ranks = sorted(list(set([card.rank.value for card in hand if card.suit == flush_suit])), reverse=True)
        if 14 in suited_ranks:
            suited_ranks.append(1)
        for i in range(len(suited_ranks) - 4):
            if suited_ranks[i] - suited_ranks[i+4] == 4:
                is_straight_flush = True
                break

    #pairs, trios, pokers, full detecter
    counts = sorted(rank_counts.values(), reverse=True)
    if is_straight_flush:
        return "Straight Flush"
    elif counts[0] == 4:
        return "Four of a Kind"
    elif counts[0] == 3 and len(counts) > 1 and counts[1] >= 2:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif counts[0] == 3:
        return "Three of a Kind"
    elif counts[0] == 2 and len(counts) > 1 and counts[1] == 2:
        return "Two Pair"
    elif counts[0] == 2:
        return "One Pair"
    return "High Card" # If none of the above, it's High Card
