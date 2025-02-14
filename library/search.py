'''Card searching'''
from difflib import get_close_matches

from library.cards import cards

DEFAULT_RESULTS = 25

async def fuzzy(comparate, comparables, results=DEFAULT_RESULTS):
    '''Compare the comparate with the comparables and return results'''
    return get_close_matches(comparate, comparables, cutoff=0.1, n=results)

async def autocomplete(ctx):
    '''Return autocompletions from a current search term'''
    term = ctx.options['card'].lower()

    return await fuzzy(term, [
            card for card in cards
            if card.startswith(term[0]) or term in card
        ]
    ) if term else []

async def lookup(term, results=DEFAULT_RESULTS):
    '''Lookup a search term in the lookup table and return the closest results or None'''
    if matches := await fuzzy(term.lower(), cards.keys(), results):
        return [cards[match] for match in matches]
