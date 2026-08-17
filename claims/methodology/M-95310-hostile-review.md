# M-95310 — Hostile review protocol for the finite odd-core Q4 successor

Review in this order:

1. `L-95310`: check the signs in `d4`, both factors of
   `epsilon+delta_2`, and the six coefficient pairs.
2. Check the physical scale factors
   `1, sqrt(2), 1/2` in the preconditioned observation.
3. `L-95311`: verify the finite kernels and distinguish diagonal energy from
   the deterministic square.
4. `R-95310`: retain the top-band sign-replacement firewall.
5. `T-95310`: treat FOCC as open.

Immediate falsifiers:

```text
one nonzero dyadic coefficient at depth >=6;
a missing logarithmic boundary coefficient B_r;
a preconditioner zero in Re(s)>0;
an unstable inverse coefficient;
a diagonal estimate promoted to a deterministic estimate;
an omission of distinct-core cross terms;
a claim that the replay proves FOCC or RH.
```
