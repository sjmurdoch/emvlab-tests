import re
from playwright.sync_api import Page, expect

def test_cryptogram(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="cryptogram calc", exact=True).click()
    page.get_by_role("textbox", name="ICC Master Key").click()
    page.get_by_role("textbox", name="ICC Master Key").fill("0123456789ABCDEF0123456789ABCDEF")
    page.get_by_role("textbox", name="Application Transaction").click()
    page.get_by_role("textbox", name="Application Transaction").fill("00B4")
    page.get_by_role("textbox", name="From terminal").click()
    page.get_by_role("textbox", name="From terminal").fill("0000000098760000000000000000800000000000000000000012345678")
    page.get_by_role("textbox", name="From ICC").click()
    page.get_by_role("textbox", name="From ICC").fill("1000xxxxA50006040000")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("form")).to_contain_text("Application cryptogram: DC874EE374EFA582")
