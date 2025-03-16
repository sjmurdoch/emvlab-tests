import re
from playwright.sync_api import Page, expect

def test_hexdump(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="hex dump", exact=True).click()
    page.locator("#myfile").click()
    page.locator("#myfile").set_input_files("test_asn1.csr")
    page.get_by_role("button", name="Dump File").click()
    expect(page.locator("form")).to_contain_text("0020: 06 03 55 04 0b 0c 04 61 62 63 64 31 0d 30 0b 06")