# X-105450 replay

Run:

```bash
python3 verify.py
python3 tests/test_verify.py
```

The replay checks exact common-owner extraction, including a shared-second-owner
fixture; renewal path products; prime augmentation Gram identities; double
nonzero phases; owner-weight/cardinality cancellation; and Plücker rectangle
factorization.

It does not prove the coherent `F1BPT105450/BQSP102870` sum or RH.
