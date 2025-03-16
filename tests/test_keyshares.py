import re
from playwright.sync_api import Page, expect

def test_split(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="Keyshare generation tools").click()
    page.locator("#combined").click()
    page.locator("#combined").clear()
    page.locator("#combined").fill("64720CD0719686B4F37D37B1A2499F6D")
    page.get_by_role("button", name="Split").click()
    page.locator("#combined").click()
    page.locator("#combined").clear()
    page.get_by_role("button", name="Combine").click()
    expect(page.locator("#combined")).to_contain_text("64720CD0719686B4F37D37B1A2499F6D")

def test_combine(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="Keyshare generation tools").click()
    page.locator("#combined").click()
    page.locator("#combined").clear()
    page.locator("#one").click()
    page.locator("#one").clear()
    page.locator("#one").fill("E94DDDCC3B04389156D1C1576F069B32")
    page.locator("#two").click()
    page.locator("#two").clear()
    page.locator("#two").fill("E9C8C4AEACCAAB3CE9701BB9A2BE41E6")
    page.locator("#three").click()
    page.locator("#three").clear()
    page.locator("#three").fill("64F715B2E65815194CDCED5F6FF145B9")
    page.get_by_role("button", name="Combine").click()
    expect(page.locator("#combined")).to_contain_text("64720CD0719686B4F37D37B1A2499F6D")