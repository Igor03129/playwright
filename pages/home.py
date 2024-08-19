from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.see_professions_link = self.page.get_by_role("link", name="Смотреть всё")

    def load(self, url):
        self.page.goto(url)

    def see_professions(self):
        self.see_professions_link.click()
