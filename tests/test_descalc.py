import re
from playwright.sync_api import Page, expect

def test_encrypt(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="DES calculator").click()
    page.get_by_role("textbox", name="Key").click()
    page.get_by_role("textbox", name="Key").fill("0123456789ABCDEF")
    page.get_by_role("textbox", name="Input Data").click()
    page.get_by_role("textbox", name="Input Data").fill("0123456789ABCDEF")
    page.get_by_role("radio", name="CBC").check()
    page.get_by_role("button", name="Encrypt").click()
    expect(page.get_by_label("Output Data")).to_match_aria_snapshot("- textbox \"Output Data\": 56CC09E7CFDC4CEF")

def test_decrypt(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="DES calculator").click()
    page.get_by_role("textbox", name="Key").click()
    page.get_by_role("textbox", name="Key").fill("0123456789ABCDEF")
    page.get_by_role("textbox", name="Input Data").click()
    page.get_by_role("textbox", name="Input Data").fill("56CC09E7CFDC4CEF")
    page.get_by_role("button", name="Decrypt").click()
    expect(page.locator("form")).to_match_aria_snapshot("- paragraph:\n  - text: Output Data\n  - textbox \"Output Data\": 0123456789ABCDEF")
