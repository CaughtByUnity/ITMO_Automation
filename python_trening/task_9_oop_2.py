class Page:

    def __init__(self, url):
        self.url = url
    def get(self):
        print(self.url)

home = Page('some_url.com')
home.get()