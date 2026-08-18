## Corrective successor to PR #577 and hostile reconstruction of PR #566

```text
publication base PR #577: ae85922195c12a29944e624337bae2167091929b
mathematical base PR #566: 2407b4ffe5024a2e3898922cf0b722d5cf69e496
mandatory adversarial PR #574: 74fba7f3e55fa9a53d1eb814e5067f5011ef5e86
mandatory adversarial PR #575: 265c481ebd02807ab7d9a95cb0cf905a22c1876f
head branch: paper/factor67-parity-lorenz-correction-97600
```

This is the materially newer packet recovered after PR #577 was published. It
does not rewrite PR #577: it records the additional native-mass correction
`r-2r^2` and preserves the corrected open status of `CPSL67` on a stacked,
reviewable branch.

This paper uses the manuscript as a hostile reconstruction, not an exposition
pass. It proves every downstream analytic interface and every finite algebraic
interface used in the corrected chain, but it does **not** conceal the remaining
arithmetic producer.

## Decisive findings

1. The unsigned alpha-child causal identity does not conserve one native rough
   coefficient after parity recursion. For one prime `r=p^(-1/2)`, current plus
   recursive alpha-child accounts for `2r^2`, leaving the compulsory source
   `r-2r^2`.
2. The odd-history witness at `X=61841` is independently reproduced with target
   gap `17.0050865382...`; canonical leafwise Hall is impossible.
3. PR #574 is binding: TP2/Cauchy-Binet does not prove global target capacity.
4. PR #575 is binding: scalar exactness does not lift to two nonnegative rows.
5. The correct completed-parity scalar producer is the exact finite Lorenz LP
   `CPSL67`; its one-dimensional dual gives a fail-closed separator.

## Strongest theorem

```text
CPSL67
 -> R_X = 5c_X(2)+3c_X(3) >= 0 eventually
 -> exact reciprocal-zeta Mellin transform
 -> zero-free numerator in Re z>0
 -> Landau
 -> RH.
```

The Mellin/Landau implication is proved fully in the paper. `CPSL67` remains
open and RH-bearing. Therefore this is a rigorous exact reduction and correction,
not a proof of RH.

## Replay

```text
PASS_T97600_PARITY_LORENZ_HOSTILE_RECONSTRUCTION
proof object: f1c87a5d958a6b1145c78da4abdcc0e5f81d0ac2daa52cdbe3f8921e8f1c724e
```

The replay independently encloses the 239-atom odd-history witness, checks exact
finite algebra and Lorenz duality, and runs a non-probative prefix diagnostic.
It explicitly records `cpsl67_proved=false` and `rh_established=false`.
