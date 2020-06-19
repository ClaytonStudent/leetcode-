def replace_string(S):
    return S.replace(' ','%20')

import re
def replace_string_(S):
    pattern = re.compile(' ')
    return pattern.sub('%20',S)

S = 'We are happy'
print(replace_string(S))
print(replace_string_(S))
