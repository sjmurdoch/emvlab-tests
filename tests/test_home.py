import re
from playwright.sync_api import Page, expect

def test_home(page: Page) -> None:
    page.goto("/")
    expect(page.locator("center")).to_match_aria_snapshot("- table:\n  - rowgroup:\n    - row \"EMV tag search Look up EMV tags in this handy database. Search by keyword e.g. for all tags that contain the word \\\"currency\\\" or \\\"cryptogram\\\" in the description, or look up a hex tag e.g \\\"9F20\\\".\":\n      - cell \"EMV tag search\":\n        - link \"EMV tag search\"\n      - cell \"Look up EMV tags in this handy database. Search by keyword e.g. for all tags that contain the word \\\"currency\\\" or \\\"cryptogram\\\" in the description, or look up a hex tag e.g \\\"9F20\\\".\"\n    - row \"TLV decoder Decode EMV TLV (Tag, Length Value) byte strings into their constituent tags and sub-tags. Useful for analysing APDU traces, responses and so on.\":\n      - cell \"TLV decoder\":\n        - link \"TLV decoder\"\n      - cell \"Decode EMV TLV (Tag, Length Value) byte strings into their constituent tags and sub-tags. Useful for analysing APDU traces, responses and so on.\"\n    - row \"CAP calculator Generate CAP codes using an emulated banking card and CAP calculator, to test against real gadgets or for testing authentication servers.\":\n      - cell \"CAP calculator\":\n        - link \"CAP calculator\"\n      - cell \"Generate CAP codes using an emulated banking card and CAP calculator, to test against real gadgets or for testing authentication servers.\"\n    - row \"Cryptogram calculator Generate and verify EMV ARQC, ARPC and TC cryptograms, calculated using the vital parameters of the card, UDKs, ATC etc.\":\n      - cell \"Cryptogram calculator\":\n        - link \"Cryptogram calculator\"\n      - cell \"Generate and verify EMV ARQC, ARPC and TC cryptograms, calculated using the vital parameters of the card, UDKs, ATC etc.\"\n    - row \"DES calculator Encrypt and decrypt hex strings using DES and 3DES, using the basic modes of operation, ECB, CBC.\":\n      - cell \"DES calculator\":\n        - link \"DES calculator\"\n      - cell \"Encrypt and decrypt hex strings using DES and 3DES, using the basic modes of operation, ECB, CBC.\"\n    - row \"ASN1 decoder Decode a binary file into an ASN1 dump using an online interface to Peter Gutmann's dumpasn1 tool\":\n      - cell \"ASN1 decoder\":\n        - link \"ASN1 decoder\"\n      - cell \"Decode a binary file into an ASN1 dump using an online interface to Peter Gutmann's dumpasn1 tool\"\n    - row \"PIN translation tools Encrypt, decrypt and translate ISO PINblocks between different encryption keys. PINs, PANs, padding... all sorts of fun!\":\n      - cell \"PIN translation tools\":\n        - link \"PIN translation tools\"\n      - cell \"Encrypt, decrypt and translate ISO PINblocks between different encryption keys. PINs, PANs, padding... all sorts of fun!\"\n    - row \"Keyshare generation tools Automatically generate test keys of various lengths, and split into components. KCVs are automatically provided for each component and the whole key.\":\n      - cell \"Keyshare generation tools\":\n        - link \"Keyshare generation tools\"\n      - cell \"Automatically generate test keys of various lengths, and split into components. KCVs are automatically provided for each component and the whole key.\"\n    - row \"Truecolour hex dump tool This hex dump tool will create a multicoloured, annotated hex dump of the provided file, making it easy to spot strings, markers, and high and low entropy areas of the file. Very useful for when you don't have your favourite hex dump tool to hand.\":\n      - cell \"Truecolour hex dump tool\":\n        - link \"Truecolour hex dump tool\"\n      - cell \"This hex dump tool will create a multicoloured, annotated hex dump of the provided file, making it easy to spot strings, markers, and high and low entropy areas of the file. Very useful for when you don't have your favourite hex dump tool to hand.\"\n    - row \"Character set encoding conversion Convert strings of text and hex between ASCII, ECBDIC and hex representations. Suprising how often you need one of these!\":\n      - cell \"Character set encoding conversion\":\n        - link \"Character set encoding conversion\"\n      - cell \"Convert strings of text and hex between ASCII, ECBDIC and hex representations. Suprising how often you need one of these!\"\n    - row \"ePassport MRZ calculator Generate passport Machine Readable Zones (MRZs) from biographical details including name, date of birth, and passport numbers, expiry dates etc. Randomly created identities can also be used.\":\n      - cell \"ePassport MRZ calculator\":\n        - link \"ePassport MRZ calculator\"\n      - cell \"Generate passport Machine Readable Zones (MRZs) from biographical details including name, date of birth, and passport numbers, expiry dates etc. Randomly created identities can also be used.\"")
