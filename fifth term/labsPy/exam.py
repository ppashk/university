from nltk import FreqDist
from nltk.book import text1
import re


def task05():
    long_words = [wrd for wrd in text1.tokens if len(wrd) >= 5]
    fd = FreqDist(long_words)
    first_five_words = FreqDist(dict(fd.most_common()[:10]))
    first_five_words.plot()


def task06():
    example_codes = ["SW1A 0AA",
                     "SW1A 1AA",
                     "SWA 2AA",
                     "BXZ 2BB",
                     "DH98 1BT",
                     "BBC 007",
                     "B42 1LG",
                     "B28 9AD"
                     ]

    regex = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

    for postcode in example_codes:
        r = re.search(regex, postcode)
        if r:
            print(postcode + " matched!")
        else:
            print(postcode + " is not a valid postcode!")


task05()
task06()
