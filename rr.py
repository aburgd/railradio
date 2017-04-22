from elizabeth import Personal  # used for names
from random import choice  # used for choosing


person = Personal('en')

synth_gender = choice(['male', 'female'])
numbers = ['one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'zero']
letter = choice(['Alpha', 'Bravo', 'Charlie',
                 'Delta', 'Echo', 'Foxtrot',
                 'Golf', 'Hotel', 'Indigo',
                 'Juliet', 'Kilo', 'Lima', 'Mike',
                 'November', 'Oscar', 'Papa',
                 'Quebec', 'Romeo', 'Sierra',
                 'Tango', 'Uniform', 'Victor',
                 'Whiskey', 'X-ray', 'Yankee', 'Zulu'])

num_1 = choice(numbers)
num_2 = choice(numbers)
num_3 = choice(numbers)

verb = choice(['received by', 'mishandled', 'in transit',
               'signed for by', 'cancelled', 'delivered to'])

safehouse = choice(['Ticon', 'Mercer', 'Dayton'])

identity = person.name(gender=synth_gender)
designation = '{} {} {} {}'.format(letter, num_1, num_2, num_3)

codename = choice(['Fixer', 'Professor', 'Bullseye', 'Charmer', 'Whisper'])

if verb == 'signed for by':
    phrase = '{} {} {}'.format(designation, verb, codename)
    print(phrase)
elif verb == 'received by':
    phrase = '{} {} {}'.format(designation, verb, safehouse)
    print(phrase)
elif verb == 'mishandled' or verb == 'in transit' or verb == 'cancelled':
    phrase = '{} {}'.format(designation, verb)
    print(phrase)
elif verb == 'delivered to':
    phrase = '{} {} {}'.format(designation, verb, identity)
    print(phrase)
