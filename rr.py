from elizabeth import Personal  # used for names
from random import choice  # used for choosing
from gtts import gTTS  # used for tts


def phrasing(designation, verb, identity, codename, safehouse):
    if verb == 'signed for by':
        phrase = '{} {} {}'.format(designation, verb, codename)
        return phrase
    elif verb == 'received by':
        phrase = '{} {} {}'.format(designation, verb, safehouse)
        return phrase
    elif verb == 'mishandled' or verb == 'in transit' or verb == 'cancelled':
        phrase = '{} {}'.format(designation, verb)
        return phrase
    elif verb == 'delivered to':
        phrase = '{} {} {}'.format(designation, verb, identity)
        return phrase

person = Personal('en')
numbers = ['one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'zero']

for i in range(0, 5):
    filename = "radio_{}.mp3".format(i)

    synth_gender = choice(['male', 'female'])
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
    phrase = phrasing(designation, verb, identity, codename, safehouse)
    tts = gTTS(text=phrase, lang='en', slow=True)
    tts.save(filename)
