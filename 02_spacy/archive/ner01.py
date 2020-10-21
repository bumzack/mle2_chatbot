# https://stackoverflow.com/questions/59972916/named-entity-recognition-relative-date

from dateparser import parse
from dateparser.search import search_dates

print(parse('Tomorrow'))
print(parse('01/01/20'))
print(search_dates("I will go to the show tomorrow"))
print(search_dates("The client arrived to the office for the first time in March 3rd, 2004 and got serviced, after a couple of months, on May 6th 2004, the customer returned indicating a defect on the part"))
