from task_9_checks import Checks

class Input(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)

class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)

class Title(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)

class Link(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)

email = Input('xammer3500@gmail.com', 'почта')
home = Button('На главную', 'кнопка')
header = Title('Главное меню', 'заголовок')
go_to_youtube = Link('youtube.com', 'ютуб')

print(email.text + ', ' + email.loc + ', ' + home.text + ', ' + home.loc + ', ' + header.text + ', ' + header.loc +
       ', ' + go_to_youtube.text + ', ' + go_to_youtube.loc)

print(f"{email.check_text()}, {home.check_text()}, {header.check_text()}, {go_to_youtube.check_text()}")

