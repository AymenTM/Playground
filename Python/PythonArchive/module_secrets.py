
# SECRETS MODULE

from secrets import *

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> choice(range(1, 1001))
		160

		>>> choice(range(1, 1001))
		400

		>>> choice(range(1, 1001))
		392

		>>> choice(range(1, 1001))
		564

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> choice(['John', 'Michael', 'Sebastian', 'Steve'])
		'John'

		>>> choice(['John', 'Michael', 'Sebastian', 'Steve'])
		'Sebastian'

		>>> choice(['John', 'Michael', 'Sebastian', 'Steve'])
		'Michael'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> randbelow(1000)
		789

		>>> randbelow(1000)
		236

		>>> randbelow(1000)
		27

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> randbits(256)
		28727144655371019307325766041853451455181453657285866906598843954373625612205

		>>> randbits(256)
		107504555360007060300252167596448575079367155333465641602198409572411481613576

		>>> randbits(32)
		1596323343

		>>> randbits(32)
		3398860330

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> token_bytes(nbytes=16)
		b'\xc0VTc7\xd3\x9e`gQ\xecP\xb4\xcb\xb1\xb9'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> token_hex(32)
		'd04de9b8280ce5435dff91efefec7d2c800ff63fbfc16479bb202b33a0fefc10'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> token_urlsafe(32)
		'Ii6T3RASzst1reP0MEy1CyhYV89DwislJYaICP193hQ'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> compare_digest(token_bytes(23), token_bytes(23))
		False

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

		>>> a = token_bytes(30)
		>>> b = a

		>>> compare_digest(a, b)
		True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
