
# STRING MODULE

import string

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> string.whitespace
        # ' \t\n\r\x0b\x0c'

        # >>> string.ascii_lowercase
        # 'abcdefghijklmnopqrstuvwxyz'

        # >>> string.ascii_uppercase
        # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # >>> string.ascii_letters
        # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # >>> string.digits
        # '0123456789'

        # >>> string.hexdigits
        # '0123456789abcdefABCDEF'

        # >>> string.octdigits
        # '01234567'

        # >>> string.punctuation
        # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        # >>> string.printable
        # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> food_request = string.Template("Hey $name, let's get some $foodType.")

        # >>> food_request.safe_substitute(name='James', food='pizza')
        # "Hey James, let's get some $foodType."

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> capwords('james gorden')
        # 'James Gorden'

        # >>> capwords('monday, january 3rd, 2019')
        # 'Monday, January 3rd, 2019'

        # >>> capwords('jAmes-stEVe-bOB-LAYA-saRah', sep='-')
        # 'James-Steve-Bob-Laya-Sarah'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
