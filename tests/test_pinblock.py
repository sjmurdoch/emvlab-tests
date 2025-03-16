import re
from playwright.sync_api import Page, expect

def test_pinblock(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="PIN translation tools").click()
    page.locator("#iepb").click()
    page.locator("#iepb").clear()
    page.locator("#iepb").fill("964FC4F590EBB4C7")
    page.locator("#ipan").click()
    page.locator("#ipan").clear()
    page.locator("#ipan").fill("0000246775866786")
    page.locator("#izpk").click()
    page.locator("#izpk").clear()
    page.locator("#izpk").fill("3A4CDC6100AED1401D27D5F380E658A4")
    page.get_by_role("button", name="Decrypt").click()
    expect(page.locator("#testdata")).to_match_aria_snapshot("- textbox: /DECRYPT EPB 964FC4F590EBB4C7 PAN \\d+ ZPK 3A4CDC6100AED1401D27D5F380E658A4 PB 042641FFFFFFFFFF/")
    page.get_by_role("button", name="Convert").click()
    expect(page.locator("#testdata")).to_match_aria_snapshot("- textbox: CONVERT IPB 042641FFFFFFFFFF OPB 042641FFFFFFFFFF")
    page.locator("#opan").click()
    page.locator("#opan").clear()
    page.locator("#opan").fill("0000246775866786")
    page.locator("#ozpk").clear()
    page.locator("#ozpk").fill("3A4CDC6100AED1401D27D5F380E658A4")
    page.get_by_role("button", name="Encrypt").click()
    expect(page.locator("#testdata")).to_match_aria_snapshot("- textbox: ENCRYPT PB 042641FFFFFFFFFF PAN 0000246775866786 ZPK 3A4CDC6100AED1401D27D5F380E658A4 EPB 964FC4F590EBB4C7")