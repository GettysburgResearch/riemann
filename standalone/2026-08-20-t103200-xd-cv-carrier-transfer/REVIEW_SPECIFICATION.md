# Review specification — T-103200

Frozen heads:

```text
PR #684  4669183704a8f51b7d0377200a46f90ed023fe2c
PR #685  4f69b7656f42dcb5ff250d13adc9f88e8d18f315
PR #688  24a2a748b8b36a70382c88843bb7779caac97e07
PR #689  1751b5d63d981f1d39e0679a5997a7e32d2f1649
PR #691  a082ec6c97436ccfd9333d5b5d88b965ce8200cd
PR #692  50c4862c801b6388a30363c336d275270025eff4
PR #694  e6d923c1069f5a481abdf0769ca6d870a8b5ae4b
PR #697  e878c3717cd8124564e5400b2ec5db035e3a4088
PR #698  a10d6a40105142de2708632589c458d7534f556a
```

Mandatory checks:

1. Verify \(G_1=G_0-\sqrt2G_0(X/2)\).
2. Recompute the prime PNT expansion and the sign of
   \(\widehat K_1'(1/2)\).
3. Rebuild largest-prime ownership directly for \(K_1\).
4. Rebuild Vaughan for the same \(K_1\).
5. Verify the two closed errors lie in \(L^1(dX/X)\).
6. Verify the exact prime-packet quotient.
7. Reconstruct corrected PR #684's inactive-tail scope.
8. Verify the moving-cutoff source identity.
9. Verify commutation with \(JP_2\).
10. Confirm `CPXD103200`, `SCTV103210`, and RH are not marked proved.
