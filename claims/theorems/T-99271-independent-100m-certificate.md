# T-99271 — Independent global-Möbius authentication of the T-99250 all-real certificate

Claim ID: `T-99271`  
Status: **PROVED COMPUTER-ASSISTED WITH OUTWARD INTEGER ENCLOSURES**  
Created: 2026-08-20  
Depends on: primitive coefficient formula only  
RH status: **unproved**

Let

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}(4\sqrt{x/n}-3),
\qquad
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\]

The independent producer in `X-99270` proves

\[
\boxed{h(x)>0\qquad(67\le x<100000001).}
\]

Together with the exact finite base already replayed in T-99250, this gives
`h(x)>0` for every real `1<=x<100000001`.

## Independent algorithm

The producer is deliberately different from the T-99250 scanner:

1. sieve every prime through `10^8` globally;
2. construct the complete Möbius array multiplicatively by prime and
   prime-square passes;
3. form `beta(n)` from the direct two-term definition;
4. compute all square-root floors with a Newton integer square root on
   unsigned 128-bit integers;
5. maintain outward intervals for
   \[
   A_N=\sum_{n\le N}\beta(n)/n,
   \qquad
   B_N=\sum_{n\le N}\beta(n)/\sqrt n;
   \]
6. on every cell `[N,N+1)`, use
   \[
   h(x)=4\sqrt x A_N-3B_N
   \]
   and the sign of the directed `A_N` interval to test the mathematically
   minimizing endpoint; test both endpoints only when that interval straddles
   zero.

The transcript contains 100 exact checkpoint records, one per million
integers.

## Result

```text
nonzero coefficients: 60,806,035
minimum cell:          200
minimum side:          RIGHT_LIMIT
minimum point:         201^-
scale:                 2^50
scale squared:         2^100
```

The exact minimum enclosure is

\[
\frac{1626923303441334483980962730376}{2^{100}}
\le h(201^-)
\le
\frac{1626923303449543135335825015140}{2^{100}}.
\]

The lower endpoint is greater than `1.28341618987788997`.

The final directed prefix intervals also agree exactly with the independent
values retained by T-99250:

```text
Alo 25886968566
Ahi 25948668612
Blo -424443924622558
Bhi -424443862922510
```

## Authentication boundary

The full producer was executed from source and the retained transcript was
hashed.  The companion verifier checks source and transcript hashes, all
metadata and endpoints, the global minimum, the final prefix intervals, a
small exact primitive replay, and fail-closed status flags.  Optional
`--full-scan` recompiles and reruns all `10^8` cells byte-for-byte.

This finite theorem supplies no inference at or above `100000001` and does not
establish RH.
