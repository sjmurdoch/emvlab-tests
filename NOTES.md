cd C:\Users\sjmur\w\emvlab-test
pnpm exec playwright codegen https://emvlab.org/

pytest
PWDEBUG=1 pytest -s tests/test_asn1decode.py

pytest --base-url=http://192.168.64.1:9004