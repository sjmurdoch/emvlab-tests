import re
from playwright.sync_api import Page, expect

def test_capcalc(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="CAP calculator", exact=True).click()
    page.get_by_role("textbox", name="ICC Master Key").click()
    page.get_by_role("textbox", name="ICC Master Key").fill("0123456789ABCDEF0123456789ABCDEF")
    page.get_by_role("textbox", name="Application Transaction").click()
    page.get_by_role("textbox", name="Application Transaction").fill("00B4")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("form")).to_match_aria_snapshot("- group \"Result\":\n  - paragraph:\n    - text: \"Input to cryptogram calculation:\"\n    - code: /\\d+/\n    - text: (from terminal)\n    - code: 100000B4A50006040000\n    - text: (from ICC)\n  - paragraph:\n    - text: \"Result of GENERATE AC (excluding tag and length):\"\n    - code: 8000B47F32A79FDA94564306770A03A48000\n  - paragraph:\n    - text: \"With bitmask applied:\"\n    - code: /\\.\\.\\.\\.\\d+\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\d+\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.8\\.\\.\\./\n  - paragraph:\n    - text: \"Bitmask:\"\n    - code: ....1F...........FFFFF..........8...\n  - paragraph:\n    - strong:\n      - text: \"CAP response:\"\n      - code: /\\d+ \\(0x288AC87\\)/")
