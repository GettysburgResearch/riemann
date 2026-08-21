# X-104100 exact replay

This standard-library replay checks the finite algebra in `T-104100` and its
countermodels.  It does not attempt to prove either terminal arithmetic input.

Run:

```bash
python3 verify.py
python3 tests/test_verify.py
```

Expected:

```text
PASS_T104100_ROOT_RETURN_ROOT_FREE_QUOTIENT
```
