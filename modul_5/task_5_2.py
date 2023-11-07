articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    list_article =[]

    for acticle in articles_dict:
        author = acticle['author']
        title = acticle['title']

        if not letter_case:
            author = author.lower()
            title = title.lower()
            key = key.lower()

        if key in author or key in title:
            list_article.append(
                {
                'author' : acticle['author'],
                'title' : acticle['title'],
                'year' : acticle['year'],
            }
            )
