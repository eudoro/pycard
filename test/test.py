#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
import pycard

# Create a card
card = pycard.Card(
    number='36085700210619',
    month=11,
    year=2017,
    cvc=309
)

# Validate the card (checks that the card isn't expired and is mod10 valid)
assert card.is_valid

# Perform validation checks individually
assert not card.is_expired
assert card.is_mod10_valid

# The card is a visa
assert card.brand == 'diners_club'
assert card.friendly_brand == 'Diners_club'
#assert card.mask == 'XXXX-XXXXXX-XXXX'

# The card is a known test card
assert card.is_test