# T-24507 — Central-Haar shell descent proposal for RH

Claim ID: `T-24507`  
Status: **FULL PROPOSAL — ONE DYADIC SHELL-VARIATION THEOREM OPEN**  
Scope: elementary full-problem proposal after the failure of pure central positivity  
Issue: #245  
Date: 2026-08-08

## 1. Corrected starting point

`L-24523` gives one completely explicit signed coefficient vector `A_X` using
only central binomial splits and satisfying every integer carry column exactly.
`R-24504` proves that `A_X` is not pointwise nonnegative: the first directed
mutation is already

\[
A_{10050}(11)<0.
\]

Thus the proposed proof may not rely on pure central positivity. The retained
mechanism is signed cancellation followed by exact dyadic shell recombination.

## 2. Exact global potential

`L-24525` constructs

\[
G_X(n)=\sum_{r\ge0}
\sum_{m=2^r(n-1)+1}^{2^rn}U_X(m),
\]

where

\[
U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk).
\]

It proves

\[
A_X(n)=G_X(n)-G_X(n+1)
\tag{T-24507.1}
\]

and the exact factor-two recursion

\[
G_X(n)=U_X(n)+G_X(2n-1)+G_X(2n).
\tag{T-24507.2}
\]

There is no unknown finite flow or inverse in this proposal.

## 3. Dyadic shell coefficient

Put

\[
Y=\lfloor X/2\rfloor
\]

and extend the level-`Y` coefficient vector by zero above `Y`. Define

\[
\boxed{
B_X(n)=A_X(n)-A_Y(n).
}
\tag{T-24507.3}
\]

By exact linearity, `B_X` saturates the logarithmically weighted dyadic target
shell

\[
s_X(q)=w_X(q)-\mathbf1_{q\le Y}w_Y(q):
\]

\[
\boxed{
\sum_{n=q}^{X}B_X(n)\chi_n^{\rm c}(q)=s_X(q).
}
\tag{T-24507.4}
\]

The shell potential is

\[
G_X^{\rm sh}=G_X-G_Y,
\]

and

\[
B_X(n)=G_X^{\rm sh}(n)-G_X^{\rm sh}(n+1).
\tag{T-24507.5}
\]

## 4. Sole theorem — Central-Haar Shell Stability

Define

\[
\boxed{
\mathfrak S_X
=
\sum_{n=2}^{X}\sqrt n\,(-B_X(n))_+.
}
\tag{T-24507.6}
\]

The proposed **Central-Haar Shell Stability theorem** (`CHSS`) is

\[
\boxed{
\forall\varepsilon>0,
\qquad
\mathfrak S_X=O_\varepsilon(X^\varepsilon).
}
\tag{CHSS}
\]

A stronger and especially reviewable form is

\[
\mathfrak S_X=O(\log^A(2X))
\]

for one absolute exponent `A`.

The theorem is explicitly one-sided and is applied only after the upper and
lower dyadic endpoints have been recombined. It does not take a positive part
of either endpoint separately.

## 5. CHSS gives global negative-variation control

By `L-24525`,

\[
A_X=A_Y+B_X.
\]

Therefore

\[
\mathcal V_X^-
\le
\mathcal V_Y^-+\mathfrak S_X,
\tag{T-24507.7}
\]

where

\[
\mathcal V_X^-
=
\sum_n\sqrt n(-A_X(n))_+.
\]

Iterating through the dyadic endpoint chain gives, under CHSS,

\[
\boxed{
\mathcal V_X^-=X^{o(1)}.
}
\tag{T-24507.8}
\]

The harmless logarithmic number of shells is absorbed by replacing
`epsilon` with `epsilon/2`.

## 6. One-sided variation controls the complete signed flow

`L-24524` proves from the exact weighted carry load that

\[
\sum_n\sqrt n\,|A_X(n)|
\ll
(\log X)^2+\mathcal V_X^-.
\tag{T-24507.9}
\]

Hence CHSS gives

\[
\sum_n\sqrt n\,|A_X(n)|=X^{o(1)}.
\tag{T-24507.10}
\]

The positive variation is not a second theorem; it is paid automatically by the
exact all-integer carry load.

## 7. Sharp prime-ramp conclusion

Let

\[
\ell_n=\log\binom n{\lfloor n/2\rfloor},
\qquad
c_n=\sum_{q=2}^{n}\chi_n^{\rm c}(q).
\]

The exact central ledgers are

\[
\mathcal P(X)=\sum_nA_X(n)\ell_n
\]

and

\[
\mathcal C(X)=\sum_nA_X(n)c_n
=4\sqrt X+O(\log X).
\]

Since

\[
|\ell_n-c_n|\ll\sqrt n,
\]

(T-24507.10) gives

\[
\boxed{
\mathcal P(X)=4\sqrt X+X^{o(1)}.
}
\tag{T-24507.11}
\]

In particular

\[
\mathcal P(X)\ge4\sqrt X-X^{o(1)}.
\tag{T-24507.12}
\]

## 8. Completion to RH

At square endpoints the repository's reviewed square-screw identity converts
(T-24507.12) into a subpower upper envelope for the screw function. Critical
square sampling, the one-sided Laplace identity for `xi'/xi`, and the
upper-envelope Landau theorem exclude every nontrivial zero with real part
larger than `1/2`. Functional-equation symmetry gives

\[
\boxed{\mathrm{CHSS}\Longrightarrow\mathrm{RH}.}
\tag{T-24507.13}
\]

## 9. Relation to canonical WSTS

The newest repository consolidation proves that logarithmically weighted
shell-tail stability `WSTS` is equivalent to RH. CHSS is not advertised as a
routine estimate independent of that obstruction. It is a constructive producer
for the same shell arithmetic:

```text
WSTS coordinate:
weighted prime-tail maximum of the parabolic shell;

CHSS coordinate:
weighted upward variation of the exact central-Haar shell potential.
```

Both take the dyadic difference before the positive part. A production proof of
CHSS should export an explicit map to WSTS, the shell prime discrepancy, or the
fixed-ratio Möbius source; it may not hide the logarithmic/von-Mangoldt ray.

## 10. Proposed proof attack

The exact potential formula suggests the following concrete programme.

1. Complete the upper/lower shell at the `U_X-U_Y` level.
2. Partition the dyadic Haar blocks by quotient depth before taking signs.
3. Use the proved continuum shell moat for the smooth block averages.
4. Retain the reciprocal-knot boundary as one signed Mertens shell.
5. Apply factor-two recursion only to the completed boundary source.
6. Prove that the total upward potential variation per shell is polylogarithmic.

The programme fails closed if a boundary term remains at current scale, if an
absolute value precedes shell recombination, or if the mutation
`A_10050(11)<0` is suppressed.

## 11. Review order

1. `L-24523` central square-wave and finite Neumann saturation;
2. `R-24504` directed positivity counterexample;
3. `L-24525` binary Green/Haar potential;
4. `X-24504` exact and directed replay;
5. `L-24524` negative-variation adapter;
6. CHSS itself;
7. the existing square-screw/Landau normalization.

## Exact status

```text
central finite saturation                 PROPOSED COMPLETE
pure central pointwise positivity         REFUTED
binary-tree Green/Haar potential           PROPOSED COMPLETE
factor-two shell decomposition             PROPOSED COMPLETE
CHSS shell negative variation              OPEN / RH-BEARING
CHSS -> prime ramp -> RH                    PROPOSED COMPLETE
Riemann Hypothesis                         UNPROVED
```
