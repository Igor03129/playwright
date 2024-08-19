from playwright.sync_api import Page

class ProfessionsPage:
    def __init__(self, page: Page):
        self.page = page
        self.qa_engineer_link = page.get_by_role("link", name="Инженер по тестированию")
