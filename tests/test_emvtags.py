import re
from playwright.sync_api import Page, expect

def test_emvtags_keyword(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="EMV tag search").click()
    page.locator("#description").click()
    page.locator("#description").fill("CDOL")
    page.get_by_role("group", name="Search by keyword").get_by_role("button").click()
    expect(page.locator("center")).to_match_aria_snapshot("- table:\n  - rowgroup:\n    - row \"Name Description\":\n      - cell\n      - cell \"Name\"\n      - cell \"Description\"\n    - row \"8C Card Risk Management Data Object List 1 (CDOL1) List of data objects (tag and length) to be passed to the ICC in the first GENERATE AC command\":\n      - cell \"8C\"\n      - cell \"Card Risk Management Data Object List 1 (CDOL1)\":\n        - link \"Card Risk Management Data Object List 1 (CDOL1)\":\n          - strong: CDOL\n      - cell \"List of data objects (tag and length) to be passed to the ICC in the first GENERATE AC command\"\n    - row \"8D Card Risk Management Data Object List 2 (CDOL2) List of data objects (tag and length) to be passed to the ICC in the second GENERATE AC command\":\n      - cell \"8D\"\n      - cell \"Card Risk Management Data Object List 2 (CDOL2)\":\n        - link \"Card Risk Management Data Object List 2 (CDOL2)\":\n          - strong: CDOL\n      - cell \"List of data objects (tag and length) to be passed to the ICC in the second GENERATE AC command\"")

def test_emvtags_number(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="EMV tag search").click()
    page.locator("#number").click()
    page.locator("#number").fill("9F16")
    page.get_by_role("group", name="Search by tag number (hex)").get_by_role("button").click()
    expect(page.locator("center")).to_match_aria_snapshot("- table:\n  - rowgroup:\n    - row \"Name Description Source Format Template Tag Length P/C\":\n      - cell \"Name\"\n      - cell \"Description\"\n      - cell \"Source\"\n      - cell \"Format\"\n      - cell \"Template\"\n      - cell \"Tag\"\n      - cell \"Length\"\n      - cell \"P/C\"\n    - row /Merchant Identifier When concatenated with the Acquirer Identifier, uniquely identifies a given merchant Terminal ans \\d+ 9F16 \\d+ primitive/:\n      - cell \"Merchant Identifier\"\n      - cell \"When concatenated with the Acquirer Identifier, uniquely identifies a given merchant\"\n      - cell \"Terminal\"\n      - cell /ans \\d+/\n      - cell\n      - cell \"9F16\"\n      - cell /\\d+/\n      - cell \"primitive\"")

def test_emvtags_all(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="EMV tag search").click()
    page.get_by_role("link", name="show all tags").click()
    expect(page.get_by_role("cell", name="Update in July 2022: The").get_by_role("table")).to_be_visible()
