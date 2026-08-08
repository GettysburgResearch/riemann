# R-28301 — Third-Abel producer positivity and the all-stage continuum-monotonicity argument fail

Claim ID: `R-28301`  
Title: The proposed third cumulative producer kernel has an exact negative coefficient, and boundary distributions invalidate the claimed all-stage logarithmic-derivative positivity  
Status: **PROPOSED EXACT REFUTATION / SCOPE CORRECTION PENDING INDEPENDENT REPLAY**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Scope: PRs #279 and #280; no RH conclusion

## 1. Exact third-Abel counterexample

Use the half-binary/half-ternary descending producer of PR #279.  At endpoint

\[
X=Q=1000,
\]

take the quadratic-prefix target

\[
 w(q)=\binom{Q-q+2}{2},
 \qquad 2\le q\le Q.
\tag{R-28301.1}
\]

This is exactly the target defining the proposed third cumulative kernel
`S_X(n,Q)` in `L-27801`.

Perform the finite Möbius inversion

\[
 U(m)=\sum_{k\le Q/m}\mu(k)w(mk),
 \qquad
 r(m)=U(m)-U(m+1),
\tag{R-28301.2}
\]

and the exact descending recurrence

\[
\begin{aligned}
 A(m)=r(m)+\frac12\sum_{M>m}A(M)
 \big[&\mathbf1_{\lceil M/3\rceil=m}
      +\mathbf1_{M-\lceil M/3\rceil=m}\\
      &+\mathbf1_{\lfloor M/2\rfloor=m}
      +\mathbf1_{M-\lfloor M/2\rfloor=m}\big].
\end{aligned}
\tag{R-28301.3}
\]

All quantities are dyadic rationals.  Exact `Fraction` arithmetic gives

\[
 \boxed{A(18)=-\frac{17337}{32}<0,}
\tag{R-28301.4}
\]

and

\[
 \boxed{A(19)=-\frac{740419}{256}<0.}
\tag{R-28301.5}
\]

Therefore

\[
 \boxed{S_{1000}(18,1000)<0,
 \qquad S_{1000}(19,1000)<0.}
\tag{R-28301.6}
\]

The proposed global statement `TACP-I` is false.  The finite positivity scan
through level `80` was pre-asymptotic.  No endpoint collar can repair
(R-28301.6), because the witness is the complete quadratic-prefix column itself,
not a negative third difference of the critical source.

This rejects `T-27801` as written.  It does not refute source-specific positivity
of the actual critical producer or the alternative mixed renewal `MPR`.

## 2. Boundary distributions omitted from the continuum induction

Let

\[
 W(x)=x^{-1/2}\log(1/x)\,\mathbf1_{0<x\le1}
\tag{R-28301.7}
\]

and put

\[
 D=-x\frac d{dx}.
\]

The pointwise formula used in `L-27702`,

\[
 D^mW(x)=x^{-1/2}
 \left(2^{-m}\log(1/x)+m2^{1-m}\right)
 \quad(0<x<1),
\tag{R-28301.8}
\]

is correct only on the open interval.  Distributionally, the cutoff at `x=1`
must be retained.  Since `W(1)=0`, the first derivative has no delta, but the
second derivative does:

\[
 \boxed{
 D^2W=(D^2w)\mathbf1_{x<1}+(Dw)(1)\,\delta_1,
 \qquad (Dw)(1)=1.
 }
\tag{R-28301.9}
\]

For the continuum central residual

\[
 (\mathcal Tf)(x)
 =\sum_{k\ge1}[f(2kx)-f((2k+1)x)],
\tag{R-28301.10}
\]

the boundary atom becomes the signed comb

\[
 \boxed{
 \mathcal T\delta_1
 =\sum_{k\ge1}
 \left[
 {1\over2k}\delta_{1/(2k)}
 -{1\over2k+1}\delta_{1/(2k+1)}
 \right].
 }
\tag{R-28301.11}
\]

Thus the formal induction

```text
D^m W >= 0
and D commutes with T
therefore D^m T^j W >= 0 for all m,j
```

is invalid unless every boundary distribution is included.  The omitted comb
has alternating signs and is exactly the source of the later monotonicity
failures.

In particular, direct evaluation of the normalized continuum iterates gives an
increasing segment in `T^2W`; at the rational grid `x=q/100`,

\[
 (\mathcal T^2W)(13/100)
 <(\mathcal T^2W)(14/100)
 <(\mathcal T^2W)(15/100)
 <(\mathcal T^2W)(16/100).
\tag{R-28301.12}
\]

The corresponding scaled sample values are approximately

```text
q=13   0.34417866745628856
q=14   0.39434477264314650
q=15   0.43735357460152250
q=16   0.47453133090442760
```

after multiplication by `sqrt(100)`.  The strict margins are far larger than
the displayed rounding and admit a routine directed log/square-root interval
replay.

Therefore the all-stage continuum monotonicity assertion in `L-27702` is false.
The first residual monotonicity and the unconditional two-pass packing of
`L-27701` are not affected.

## 3. Correct surviving geometry

The continuum interior is still useful.  The exact separation is

```text
smooth dilation interior
+
source-bound boundary-jet comb.
```

Any valid continuation must carry the boundary distributions through every
iteration, or absorb them with an explicit positive endpoint/Pascal dictionary.
They cannot be relabeled as the lattice commutator alone: they are already
present in the continuum cutoff model.

## 4. Classification

```text
PR #279 third-Abel global kernel positivity       REJECTED
PR #280 all-stage continuum monotonicity proof    REJECTED AS WRITTEN
PR #280 exact central residual formula            UNAFFECTED
PR #280 unconditional two-pass packing            UNAFFECTED
source-specific MPR/BTF routes                    UNAFFECTED
Riemann Hypothesis                                UNPROVED
```
