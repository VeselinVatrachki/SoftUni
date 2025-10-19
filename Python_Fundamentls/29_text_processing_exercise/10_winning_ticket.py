def checking_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbol = ["@", "#", "$", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbol:
        for uninterrupted_winning_symbol in range(10, 5, -1):
            winning_symbol_repetition = current_winning_symbol * uninterrupted_winning_symbol
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                if uninterrupted_winning_symbol == 10:
                    return f'ticket "{ticket}" - {uninterrupted_winning_symbol}{current_winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_winning_symbol}{current_winning_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(checking_ticket(current_ticket))
