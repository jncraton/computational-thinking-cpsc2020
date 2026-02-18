import random
import doctest

def get_winner(human, bot):
    """
    >>> get_winner('r', 's')
    'human'

    >>> get_winner('r', 'p')
    'bot'
    """
    
    if human == 'r' and bot == 's':
        return 'human'
    else:
        return 'bot'

doctest.testmod()

selection = input("Rock, paper or scissors (r/p/s): ")
bot_selection = random.choice('rps')
