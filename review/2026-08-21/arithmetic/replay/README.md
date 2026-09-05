# Light replay

Run both lightweight checks from this directory:

```bash
python3 verify_review_packet.py
python3 verify_review.py
```

`verify_review_packet.py` validates schemas, exact-base metadata, the controlling PR #705 same-kernel correction, verdict consistency, and the fail-closed RH boundary. The retained `verify_review.py` additionally checks representative exact rows-2/3, half-divisor, one-prime source, and proved-only graph fixtures. Neither script reruns a broad prime scan, high-zero verification, MPFR campaign, or retained heavy certificate.
