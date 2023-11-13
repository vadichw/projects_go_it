# Початок гіперпосилання може бути http:// або https://
#доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
#символи точок . не можуть зустрічатися поруч

import re

def find_all_links(text):
    result = []
    iterator = re.finditer(r'https?://(?:[\w_]+\.)*[\w_]+\.\w+', text)
    for match in iterator:
        result.append(match.group())
    return result