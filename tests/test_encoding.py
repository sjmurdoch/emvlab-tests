import re
from playwright.sync_api import Page, expect

def test_encoding(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="char converter").click()
    page.get_by_role("textbox", name="Data to convert").click()
    page.get_by_role("textbox", name="Data to convert").fill("61 62 63 64 31")
    page.get_by_text("From hex (ASCII)").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_label("Result")).to_contain_text("a b c d 1")