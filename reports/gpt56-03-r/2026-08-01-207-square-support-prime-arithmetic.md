# Report — square-support arithmetic factorization and the irreducible D-0001 sign

Agent: `gpt56-03-r`  
Issue: #207  
PR: #208  
Date: 2026-08-01

## Requested objective

The attempted target was an explicit unbounded schedule `(N_j,c_j)` with
directed proofs

\[
A_{WW,j}\succ0,
\]

\[
S_{R,j}
=A_{RR,j}-A_{RW,j}A_{WW,j}^{-1}A_{WR,j}
\succeq-\varepsilon_jG_{R,j},
\]

and

\[
\Lambda_j\varepsilon_j+\delta_j\to0.
\]

Frame conditioning and Schur bookkeeping had already been removed by
`L-20701`--`L-20703`, so this pass tested support averaging and an exact
prime/pole factorization.

## Explicit schedule selected

The natural all-integer schedule is

\[
\boxed{(N_M,c_M)=(M,M^2),\quad M=2,3,4,\ldots .}
\]

It has `log c=2 log N`, matches the polynomial-support frame geometry, and is
dense enough for the square-screw sampling theorem.

## Exact scalar embedding

`L-20704` proves term by term that

\[
\boxed{
\mathcal S(M)
=\log M\,e_0^{\mathsf T}A_{N,M^2}e_0
}
\]

for every packet dimension `N`. The proof separately matches:

1. the hyperbolic polar term;
2. every prime power through `M^2`;
3. the cutoff-free digamma/trigamma and geometric archimedean correction.

The order-one Lerch sum is evaluated by

\[
M^{-1}\Phi(M^{-4},1,1/4)
=\log{M+1\over M-1}+2\arctan(M^{-1}).
\]

Cross-branch `T-19801` identifies `mathcal S(M)` as an RH-equivalent finite
prime-power scalar. Hence the requested matrix floor on the all-integer square
schedule already proves an RH-equivalent inequality on one principal
coordinate.

This is not a reason to abandon the matrix route: a prime-side LDL factorization
would be a new proof of that scalar inequality. It is a reason not to expect the
remaining sign from generic conditioning or a phase-blind prime estimate.

## Exact centered-prime factorization

For the D-0001 autocorrelation kernel

\[
K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)dt,
\]

`L-20705` proves

\[
\begin{aligned}
\langle v,(A^{\rm pole}+A^{\rm pp})v\rangle
={}&\int_0^L2\cosh(y/2)K_v(1-y/L)dy\\
&-\sum_{q\le e^L}{\Lambda(q)\over\sqrt q}
K_v(1-\log q/L).
\end{aligned}
\]

With

\[
\Theta(y)=\sum_{q\le e^y}{\Lambda(q)\over\sqrt q}-4\sinh(y/2),
\]

this becomes the exact Stieltjes identity

\[
\boxed{
-{1\over L}\int_0^L
\Theta(y)K_v'(1-y/L)dy.
}
\]

The main polar and prime masses are therefore canceled before any widening. A
support average has the exact kernel

\[
\mathcal J_{v,W}(y)
=\int_{L\ge y}{W(L)\over L}K_v'(1-y/L)dL.
\]

For the constant coordinate, `K'=2`; the resulting Riesz discrepancy is exactly
the scalar square-screw channel after the archimedean term is restored.

## Support-average audit

The beta square-cell matrix average has constant principal coordinate equal to
the beta square-cell scalar of `T-19804`, another RH-equivalent arithmetic
criterion.

Moreover, `lambda_min` and the Schur complement are concave. Positivity of an
averaged matrix or averaged block does not imply that one member of the support
family is positive. A valid selection theorem would need a bound on the average
negative part or a strict pointwise moat plus continuity.

Thus support averaging improves the arithmetic kernel but does not supply the
missing sign automatically.

## New finite reconnaissance

`X-20705` evaluates the complete matrices on the square schedule through
`M=13` at 70 ordinary decimal digits. Every prime power is included.

All matrices, positive-sector blocks, and joint Schur pivots are positive in the
retained table. The final pivots range from approximately

```text
9.7510e-7   at M=2
```

to

```text
5.6114e-48  at M=13.
```

The exact scalar identity agrees below `1.2e-69` in every row. The smallest
rational-Leja pivot remains approximately `1.58e-3`, while the graph metric
reaches approximately `5.77e42`.

This table is nondirected reconnaissance. It strongly indicates that adaptive
precision and joint LDL are necessary; it does not prove an asymptotic sign.

## Why the requested proof was not completed

The exact all-integer square schedule would imply

\[
\mathcal S(M)
\ge-\log M\,(\Lambda_M\varepsilon_M+\delta_M).
\]

The requested rate would make the negative square-screw excursions
subpolynomial, which is exactly the open arithmetic condition in `T-19801`.

The centered factorization does not reveal a positive Gram factor for the
remaining discrepancy. A hypothetical off-line zero appears in the exact
causal/anti-causal factorization as a nonzero reflection channel and forces a
negative direction on a complete hierarchy. Any unconditional estimate that
bounds this channel by `o(1)` is therefore a proof of RH, not a consequence of
the ordinary prime number theorem.

## Precise remaining obstruction

On the explicit schedule `(N_M,c_M)=(M,M^2)`, produce directed complete-source
blocks satisfying

\[
\boxed{A_{WW,M}\succ0,}
\]

\[
\boxed{
A_{RR,M}-A_{RW,M}A_{WW,M}^{-1}A_{WR,M}
\succeq-\varepsilon_MG_{R,M},
}
\]

and

\[
\boxed{
\Lambda_M\varepsilon_M+\delta_M\to0.
}
\]

Equivalently, prove the joint centered prime-power/polar/archimedean LDL pivots
have subpolynomial negative part. The constant pivot must simultaneously prove

\[
(-\mathcal S(M))_+=M^{o(1)}.
\]

No valid proof of this final arithmetic sign was obtained in this pass.

## Artifacts

- `L-20704` — exact square-screw principal-coordinate identity;
- `L-20705` — exact centered-prime and support-average factorization;
- `T-20701` — square-support D-0001 criterion;
- `R-20701` — support-average shortcut refutation;
- `O-20702` / `X-20705` — complete square-schedule reconnaissance;
- updated `M-20701` production protocol.

RH is not claimed proved.
