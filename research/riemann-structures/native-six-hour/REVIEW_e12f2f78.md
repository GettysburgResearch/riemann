# Independent review of full-support one-sided faithfulness

I read the complete `NATIVE_ONE_SIDED_FULL_SUPPORT_FAITHFULNESS.md`, frozen at `e12f2f7865809281f6fed50f5b091fccfd996864`, blob `c510f50f07256b01aec9d756ea76a89b8ab8af81`. The reviewed working bytes agree with the freeze. No proof blocker was found.

The local independence argument is sound. If all positive Laurent coefficients vanish, the remaining series extends holomorphically to `|w|>q`. Monodromy around the outer branch point `-1` removes both outer-`A` coefficients, and monodromy around `+1` removes both outer-`C` coefficients. The inner ratio `sqrt(1+q/w)` is nonconstant for `q>0`, so neither cancellation leaves a nonzero pair of constants. This proves independence of the four positive-shift sequences, rather than merely independence of the full Laurent functions.

The normalization `q=1/p`, `w=p^(-1/2) exp(-it log p)` correctly identifies positive shifts with physical ratios `1/b`; the inner alias weight is exactly `1/d`, followed by the nonzero physical row factor `1/sqrt(b)`. Absolute convergence justifies tensoring. The Kronecker evaluation matrix therefore gives an existential set of `4^r` full-support rows faithful on the full tensor source, and an existential 20-row restriction faithful on the actual three-prime curvature directions.

The eventual finite-horizon conclusion follows from entrywise convergence to a nonzero finite determinant. The note correctly supplies no effective shifts, threshold, conditioning estimate or stable coefficient-extraction operator. It does not rescue the previously selected singular limiting minor or identify the full retained-gamma decoder. I ran no scientific computation; this is an independent proof review of the separately authored note.
