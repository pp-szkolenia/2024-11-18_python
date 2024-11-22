quote_items = []
for quote in quote_divs:
    author = quote.find("span", "authorOrTitle").text.strip()
    text = quote.find("div", "quoteText").text.replace(author, "").replace("―", "").strip()

    tag_list = []
    tags = quote.find_all('div', class_="greyText smallText left")
    for tag in tags:
        tag_list = [tag_a.text for tag_a in tag.find_all('a')]

    # compose final result
    single_quote = {
        "text": text,
        "author": author,
        "tags": tag_list
    }
    quote_items.append(single_quote)