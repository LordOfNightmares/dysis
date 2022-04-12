'''Card searching'''
from difflib import get_close_matches

from library.cards import cards

async def fuzzy(comparate, comparables, results=25):
    '''Compare the comparate with the comparables and return results'''
    return get_close_matches(comparate, comparables, cutoff=0.1, n=results)

async def autocomplete(ctx):
    '''Return autocompletions from a current search term'''
    term = ctx.options['card']

    return await fuzzy(term, [card for card in cards if card.startswith(term[0])]) if term else []

async def lookup(term):
    '''Lookup a search term in the lookup table and return the closest matches or None'''
    if matches := await fuzzy(term.lower(), cards.keys()):
        return [cards[match] for match in matches]
