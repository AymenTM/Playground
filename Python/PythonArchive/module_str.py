
# STR OBJECT METHODS

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'jAmaica'.capitalize()
		'Jamaica'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Sanfransico ßay AREA'.casefold()
		'sanfransico ssay area'

		>>> 'NEW YorK, 7TH Street'.casefold()
		'new york, 7th street'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'John Doe'.center(30)
		'           John Doe           '

		>>> '> John Doe <'.center(30, '=')
		'=========> John Doe <========='

		>>> 'New York, 7th Street'.center(50, '-')
		'---------------New York, 7th Street---------------'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'George Stevenson'.count('e')
		4

		>>> 'George Stevenson'.count('e', 4, 11)
		2

		>>> 'bathatbathatbathatbathat'.count('bat')
		4

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'James'.endswith('es')
		True

		>>> 'Vancouver'.endswith(('es', 'ing', 'on'))
		False

		>>> 'Vancouver'.endswith(('es', 'ing', 'on', 'er'))
		True

		>>> 'Vancouver'.endswith(('es', 'ing', 'ouv'), 0, -2)
		True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'First\tLast\tGrade\tAcceptance'.expandtabs(4)
		'First   Last    Grade   Acceptance'

		>>> 'Tom\tBroady\t24\tCanadian'.expandtabs(4)
		'Tom Broady  24  Canadian'

		>>> '01\t012\t0123\t01234'.expandtabs(4)
		'01  012 0123    01234'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


		>>> 'Hello, world!'.find('world')
		7

		>>> 'Hey James'.find('Norton')
		-1

		>>> 'Jim is on his way to James house. James is happy.'.find('James', -20)
		34'

		>>> 'Steve Walden — October 19th, 1983'.find('October', 10, -10)
		15

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> "Hello, I'm {} and I'm {} years old.".format('Jack', 12)
		"Hello, I'm Jack and I'm 12 years old."

		>>> "Hello, I'm {1} and I'm {0} years old.".format(12, 'Jack')
		"Hello, I'm Jack and I'm 12 years old."

		>>> "Hello, I'm {name} and I'm {age} years old.".format(age=12, name='Jack')
		"Hello, I'm Jack and I'm 12 years old."

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        >>> '{:02}'.format(1)
        '01'

        >>> '{:03}'.format(1)
        '001'

        >>> '{:05}'.format(1)
        '00001'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> '{:7}'.format(1)
		'      1'

		>>> '{:7}'.format(23)
		'     23'

		>>> '{:7}'.format(2423)
		'   2423'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> '{:5}'.format('Name')
		'Name '

		>>> '{:10}'.format('Name')
		'Name      '

		>>> '{:15}'.format('Name')
		'Name           '

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> date = datetime(2016, 9, 24, 12, 30, 47)

		>>> date.__str__()
		'2016-09-24 12:30:47'

		>>> '{:%B %d, %Y}'.format(date)
		'September 24, 2016'

		>>> '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j}th day of the year.'.format(date)
		'September 24, 2016 fell on a Saturday and was the 268th day of the year.'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> '{name:10}{age:5}{nationality}'.format(name='Mathilda', age='23', nationality='Canadian')
		'Mathilda  23   Canadian'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        >>> 'Pi = {:.2f}'.format(3.14159265)
        'Pi = 3.14'

        >>> 'Pi = {:.3f}'.format(3.14159265)
        'Pi = 3.142'

        >>> 'Pi = {:.5f}'.format(3.14159265)
        'Pi = 3.14159'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Hello, world!'.index('world')
		7

		>>> 'Hello, world!'.index('John')
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		ValueError: substring not found

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> ''.isalnum()
		False

		>>> 'December 2nd, 1948'.isalnum()
		False

		>>> 'JamesGorden1980'.isalnum()
		True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> ''.isalpha()
		False

		>>> 'James'.isalpha()
		True

		>>> 'Decemeber1923'.isalpha()
		False

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> ''.join(['S', 't', 'r', 'i', 'n', 'g'])
		'String'

		>>> ' — '.join(['Jack', 'James', 'Jerry'])
		'Jack — James — Jerry'

		>>> ', '.join([' '.join(['March', '23rd']), '2003'])
		'March 23rd, 2003'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> greeting = 'Hollo'
		>>> greeting = list(greeting)
		>>> greeting[1] = 'e'

		>>> ''.join(greeting)
		'Hello'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Name: '.ljust(30, '_')
		'Name: ________________________'

		>>> 'January 2019 <'.ljust(50, '=')
		'January 2019 <===================================='

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'JAMES'.lower()
		'james'

		>>> 'DECEMBER 23ND, 1862'.lower()
		'december 23nd, 1862'

		>>> 'Sanfransico ßay AREA'.lower()
		'sanfransico ßay area'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Louis Selbi'.partition('-')
		('Louis Selbi', '', '')

		>>> 'Louis Selbi'.partition(' ')
		('Louis', ' ', 'Selbi')

		>>> 'James Dunkens-Chairman & CEO'.partition('-')
		('James Dunkens', '-', 'Chairman & CEO')

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Hey James!'.replace('James', 'John')
		'Hey John!'

		>>> 'I I I'.replace('I', 'You', 2)
		'You You I'

		>>> 'Name\tAge\tDate\tYear'.replace('\t', '    ')
		'Name    Age    Date    Year'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Hello world! Bye world!'.rfind('world')
		17

		>>> 'Hey Norton'.rfind('James')
		-1

		>>> 'See you Friday.. but are you coming ?'.rfind('you', 4, -1)
		25

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Hey Norton'.rindex('Norton')
		4

		>>> 'Hey Norton'.rindex('James')
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		ValueError: substring not found

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'John Doe'.rjust(30)
		'                      John Doe'

		>>> '> James Kaldon'.rjust(30, '=')
		'================> James Kaldon'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Steve Belger Natalo'.rpartition(' ')
		('Steve Belger', ' ', 'Natalo')

		>>> 'December 16th, 2018'.rpartition(', ')
		('December 16th', ', ', '2018')

		>>> 'Lenard Arnold-8 years-Chairman & CEO'.rpartition('-')
		('Lenard Arnold-8 years', '-', 'Chairman & CEO')

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Once upon a time, there was ...'.rsplit()
		['Once', 'upon', 'a', 'time,', 'there', 'was', '...']

		>>> 'Sam Carter Hubenston'.rsplit(maxsplit=1)
		['Sam Carter', 'Hubenston']

		>>> 'Monday, January 3rd, 2019'.rsplit(sep=', ', maxsplit=1)
		['Monday, January 3rd', '2019']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Yesterday we went out to the mall.'.split()
		['Yesterday', 'we', 'went', 'out', 'to', 'the', 'mall.']

		>>> 'Samuel Bulken Jirno'.split(maxsplit=1)
		['Samuel', 'Bulken Jirno']

		>>> 'January 3rd, 2019'.split(sep=', ', maxsplit=1)
		['January 3rd', '2019']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Sentence 1\n\nSentence 2\rSentence 3\r\n'.splitlines()
		['Sentence 1', '', 'Sentence 2', 'Sentence 3']

		>>> 'Sentence 1\n\nSentence 2\rSentence 3\r\n'.splitlines(keepends=True)
		['Sentence 1\n', '\n', 'Sentence 2\r', 'Sentence 3\r\n']

		>>> "".splitlines()
		[]

		>>> 'Sentence 1\n'.splitlines()
		['Sentence 1']

		>>> ''.split('\n')
		['']

		>>> 'Sentence 1\n'.split('\n')
		['Sentence 1', '']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'George'.startswith('Ge')
		True

		>>> 'Vancouver'.startswith(('Que', 'Sas', 'Ont'))
		False

		>>> 'Vancouver'.startswith(('Que', 'Sas', 'Ont', 'Van'))
		True

		>>> 'Vancouver'.startswith(('Que', 'Sas', 'Ont', 'couv'), 3, -1)
		True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> '   spacious   '.strip()
		'spacious'

		>>> 'www.example.com'.strip('cmowz.')
		'example'

		>>> comment_string = '#....... Section 3.2.1 Issue #32 .......'

		>>> comment_string.strip('.#! ')
		'Section 3.2.1 Issue #32'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'James Smith - CEO & Chairman'.swapcase()
		'jAMES sMITH - ceo & cHAIRMAN'

		>>> 'tUESDAY, dECEMBER 3RD, 1532'.swapcase()
		'Tuesday, December 3rd, 1532'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'heLLo woRld'.title()
		'Hello World'

		>>> 'stAr wArs — tHE clone wars: episODe #2'.title()
		'Star Wars — The Clone Wars: Episode #2'

		>>> "they're bill's friends from the UK".title()
		"They'Re Bill'S Friends From The Uk"

		>>> import re
		>>> def titlecase(string):
		...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
		...                   lambda mo: mo.group(0)[0].upper() +
		...                              mo.group(0)[1:].lower(),
		...                   string)

		>>> titlecase("they're bill's friends.")
		"They're Bill's Friends."

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'Hello'.translate(str.maketrans('el', 'pz'))
		'Hpzzo'

		>>> 'mnssz'.translate(str.maketrans('zmsn', 'oHle'))
		'Hello'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> 'james'.upper()
		'JAMES'

		>>> 'december 22nd, 1872'.upper()
		'DECEMBER 22ND, 1872'

		>>> 'sanfransico bay area'.upper()
		'SANFRANSICO BAY AREA'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
