from pyfiglet import Figlet, CharNotPrinted


class TextRenderer:
    def __init__(self, no_figlet, font, title_font):
        self.no_figlet = no_figlet
        self.counter_figlet = Figlet(font=font)
        if not title_font:
            title_font = font
        self.title_figlet= Figlet(font=title_font)

    def render_title(self, text):
        if self.no_figlet or not text:
            return text

        try:
            return self.title_figlet.renderText(text)
        except CharNotPrinted:
            return ""

    def render_counter(self, text):
        if self.no_figlet:
            return text

        return self.counter_figlet.renderText(text)

    def update_width(self, width):
        self.counter_figlet.width = width
        self.title_figlet.width = width
