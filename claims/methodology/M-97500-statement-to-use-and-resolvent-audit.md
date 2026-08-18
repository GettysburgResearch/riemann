# M-97500 — Statement-to-use and resolvent audit protocol

For every imported recursion, record:

1. the literal source cone and parity orientation;
2. the raw edge coefficient `r` in the native identity;
3. the proposed recursive coefficient `t`;
4. the leftover source coefficient `r-t` and its owner;
5. the exact current scalar `b-(R-T)f`;
6. whether a proof controls raw exposure `R f` or only contracted exposure `T f`;
7. every activation and first-owner coordinate;
8. the exact consumer inequality.

Immediate rejection conditions are:

```text
raw coefficient r replaced by t without a leftover current source;
parity swap removed from the leftover source;
contracted mass Tm substituted for raw scalar exposure Rf;
local P61 bias applied to a current containing complete rough children;
reserve injection treated as Hall-complement domination;
finite-depth transfer used on a longer history;
paired source positivity promoted to signed scalar positivity;
NCBI67 or an equivalent global producer silently assumed.
```
