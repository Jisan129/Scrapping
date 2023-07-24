response.css("div.quote")

quote=response.css("div.quote")[0]
text=quote.css("span.text::text").get()
author=quote.css("small.author::text").get()

tags=quote.css("div.tags a.tag::text").getall()

for quote in response.css("div.quote"):
    text=quote.css("span.text::text").get()
    author=quote.css("small.author::text").get()
    tags=quote.css("div.tags a.tag::text").getall()
    print(dict(text=text,author=author,tags=tags))