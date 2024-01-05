# Clasa de oferte
class Oferta:
    def __init__(
        self,
        id="0",
        titlu="No title",
        price="0",
        url="No url",
        views="No views",
        page_source=None,
        photo_urls=[],
    ):
        self.id = id
        self.titlu = titlu
        self.price = price
        self.url = url
        self.views = views
        self.page_source = page_source
        self.photo_urls = photo_urls

    def __str__(self):
        return (
            "ID: "
            + self.id
            + "\n"
            + "Titlu: "
            + self.titlu
            + "\n"
            + "Pret: "
            + self.price
            + "\n"
            + "Url: "
            + self.url
            + "\n"
            "Vizualizari: " + self.views + "\n"
        )

    def csv_line(self):
        return (
            self.id
            + ","
            + self.titlu
            + ","
            + self.price
            + ","
            + self.url
            + ","
            + self.views
            + "\n"
        )

    def complete_fields(self):
        pass

    def save_csv(self, file_name):
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(self.csv_line())

    def get_photo_urls(self):
        return self.photo_urls
