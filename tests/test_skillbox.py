from playwright.sync_api import expect


def test_example(config, home_page, professions_page):
    home_page.load(config.get("url"))
    home_page.see_professions()
    expect(professions_page.qa_enginner_link).to_be_visible()
    # does not work
