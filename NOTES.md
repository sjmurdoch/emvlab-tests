cd C:\Users\sjmur\w\emvlab-test
pnpm exec playwright codegen https://emvlab.org/

pytest
PWDEBUG=1 pytest -s tests/test_asn1decode.py