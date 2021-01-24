#!/bin/env python
"""Generate Random Code Names/Pseudonyms"""

import random

first = (
    'xenophobic',
    'humongous',
    'voodoo',
    'ravenous',
    'fiery',
    'shadowy',
    'slimy',
    'morphogenic',
    'phantom',
    'scathing'
)

last = (
    'kraken',
    'homonculus',
    'zombie',
    'drake',
    'wyrm',
    'ogre',
    'hollow',
    'minotaur',
    'elf',
    'juggernaut'
)

def main():
    """Main Function / Entry Point"""
    keep_going = True
    while keep_going:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("+-----------------------------------+")
        print(F"| {first_name} {last_name}")
        print("+-----------------------------------+")

        again = input("\nAnother? ")
        if again in ('n', 'no'):
            keep_going = False


if __name__ == "__main__":
    main()
