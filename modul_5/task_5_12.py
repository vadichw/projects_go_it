import re

def replace_spam_words(text, spam_words):
    for word in spam_words:
        pattern = re.compile(r'\b{}\b'.format(re.escape(word)), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)

    return text