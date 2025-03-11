import re
from playwright.sync_api import Page, expect

def test_tlvparsing(page: Page) -> None:
    page.goto("https://emvlab.org/")
    page.get_by_role("link", name="TLV decoder", exact=True).click()
    page.get_by_role("textbox", name="TLV data to decode").click()
    page.get_by_role("textbox", name="TLV data to decode").fill("6F1A840E315041592E5359532E4444463031A5088801025F2D02656E")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("center")).to_match_aria_snapshot("- table:\n  - rowgroup:\n    - row \"6F File Control Information (FCI) Template\":\n      - cell \"6F File Control Information (FCI) Template\":\n        - link \"File Control Information (FCI) Template\"\n    - row /\\d+ Dedicated File \\(DF\\) Name/:\n      - cell\n      - cell /\\d+ Dedicated File \\(DF\\) Name/:\n        - link \"Dedicated File (DF) Name\"\n    - row \"315041592E5359532E4444463031\":\n      - cell\n      - cell\n      - cell \"315041592E5359532E4444463031\"\n    - row \"A5 File Control Information (FCI) Proprietary Template\":\n      - cell\n      - cell \"A5 File Control Information (FCI) Proprietary Template\":\n        - link \"File Control Information (FCI) Proprietary Template\"\n    - row /\\d+ Short File Identifier \\(SFI\\)/:\n      - cell\n      - cell\n      - cell /\\d+ Short File Identifier \\(SFI\\)/:\n        - link \"Short File Identifier (SFI)\"\n    - row /\\d+/:\n      - cell\n      - cell\n      - cell\n      - cell /\\d+/\n    - row \"5F2D Language Preference\":\n      - cell\n      - cell\n      - cell \"5F2D Language Preference\":\n        - link \"Language Preference\"\n    - row \"e n\":\n      - cell\n      - cell\n      - cell\n      - cell \"e n\"")
