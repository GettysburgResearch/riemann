# Separate exact-head review of PR #520

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-16T01:57:56Z
main at cutoff:   9c7538559d7f56c2914b39aed5a1fb3fbf7ce131

shared dependency only:
PR #498           6cc0da2fa5711017e260ebdcea4ba8c22e453288

proposal:
PR #520           41db5f783c751e66c786f18fa7fbd6d9bf229a8d
branch:           research/gpt56-pro/94050-phase-locked-hermite-q4-frontier
base:             PR #498 exact head
```

This review is separate from the PR #519/#523 comparison. No wavelet/Vaughan
claim is used to corroborate the phase-locked First-Hermite construction.

The first-Hermite explicit formula and terminal-pair theorem are inherited from
PR #379 at `589f1c05ccaf248cf08c87fefa7d5ab6d2380708`; they are treated as one
frozen proposed analytic dependency, not reproved here. The finite replay was
inspected. No broad prime scan, zero scan or high-order numerical campaign was
rerun.

## Executive verdict

```text
PR #520:
  VERIFIED WITH FIXES

mathematical type:
  RH-EQUIVALENT FILTERED CRITERIA
  + PROPOSED UNCONDITIONAL FIRST-HERMITE FRONTIER THEOREM

exact proof defect:
  T-94051.10 is FALSE AS WRITTEN for arbitrary non-locally-bounded Delta

repair:
  replace the global compact-interval supremum by a tail supremum,
  or assume eventual local boundedness; qualify effectiveness

Riemann Hypothesis:
  UNPROVEN
```

No Fourier-sign, translation-sign, Hermite-power, gamma-scale or
terminal-dominance contradiction was found. The arbitrary-Delta quantifier
contains an exact but repairable logical error.

# 1. Phase-lock factor and strip signs

Put

\[
L=\log4,
\qquad
P(u)=5-4\cos(Lu).
\]

The Laurent factorization is exact:

\[
\boxed{
P(u)=(2-e^{iLu})(2-e^{-iLu}).
}
\]

For real `u`,

\[
1\le P(u)\le9.
\]

For a vertical point `u=iy`,

\[
P(iy)=5-4\cosh(Ly).
\]

Since

\[
\cosh(L/2)=\cosh(\log2)=5/4,
\]

one has

\[
P(iy)>0\quad(|y|<1/2),
\qquad
P(\pm i/2)=0.
\]

With

\[
z=\frac{s-1/2}{i},
\]

direct substitution gives

\[
\boxed{
P(z)=4(1-4^{s-1})(1-4^{-s}).
}
\]

The factor is therefore nonzero at every nontrivial zeta zero in the open
critical strip.

# 2. Fourier and translation signs

PR #379 uses the convention

\[
\widehat f(v)=\int_{\mathbb R}f(u)e^{ivu}\,du
\]

and the translated prime kernel contains `e^(-ixu)`.

Define

\[
(T_af)(u)=f(u-a).
\]

Multiplication of the spectral test by `e^{iL(v-x)}` gives

\[
e^{-ixu}h_q(u-L)
\]

on the prime-log side. Multiplication by `e^{-iL(v-x)}` gives

\[
e^{-ixu}h_q(u+L).
\]

Consequently the operator attached to `P(v-x)` is exactly

\[
\boxed{
D_L=5I-2T_L-2T_{-L}.
}
\]

There is no swap of `T_L` and `T_-L`, and no missing carrier phase.

Let

\[
H_q(u)=e^{u/2}h_q(u).
\]

Then

\[
e^{u/2}T_Lh_q(u)=2H_q(u-L),
\]

\[
e^{u/2}T_{-L}h_q(u)=\frac12H_q(u+L).
\]

Therefore

\[
\begin{aligned}
e^{u/2}D_Lh_q(u)
&=5H_q(u)-4H_q(u-L)-H_q(u+L)\\
&=[(I-T_L)(4I-T_{-L})H_q](u).
\end{aligned}
\]

Thus

\[
\boxed{
e^{u/2}D_L^{2m}h_q
=
(I-T_L)^{2m}(4I-T_{-L})^{2m}H_q.
}
\]

The order-`2m` backward difference is genuine.

# 3. Fixed and growing Hermite bounds

Completing the square gives

\[
H_q(u)
=
e^{q/4}
\left(1-\frac{u^2}{2q}\right)
e^{-(u-q)^2/(4q)}.
\]

Set

\[
v=\frac{u-q}{2\sqrt q}.
\]

The polynomial factor becomes

\[
1-\frac q2-2\sqrt q\,v-2v^2.
\]

After `r` derivatives in `u` and the change of variables in the `L1` norm, the
leading scale is

\[
e^{q/4}q^{3/2-r/2}.
\]

Cauchy--Schwarz with the exact Hermite `L2` norm supplies an effective uniform
bound of the form

\[
\boxed{
\|H_q^{(r)}\|_1+\|H_q^{(r+1)}\|_1
\le
A e^{q/4}q^{3/2-r/2}
(A\sqrt{r+2})^{r+2}.
}
\]

Repeated finite-difference integration gives

\[
\|(I-T_L)^rF\|_{W^{1,1}}
\le
L^r(\|F^{(r)}\|_1+\|F^{(r+1)}\|_1),
\]

while

\[
\|(4I-T_{-L})^r\|_{L^1\to L^1}\le5^r.
\]

For `r=2m`, all order-dependent factors are absorbed by `(C m)^m`. The
Chebyshev shell lemma then yields

\[
\boxed{
|S_m(q,x)|
\le
C_0e^{q/4}q^{3/2}
\left(\frac{C_0m}{q}\right)^m
}
\]

for `1<=m<=q/C0`, uniformly in the carrier `x`. For fixed `m` this reduces to

\[
|S_m(q,x)|\ll_m e^{q/4}q^{3/2-m}.
\]

The power of `q` and the finite-difference order are consistent. The retained
finite checker does not prove this analytic estimate; the proof must stand on
the displayed Hermite bounds.

# 4. Chebyshev shell transfer

For

\[
G(u)=e^{u/2}g(u)\in W^{1,1},
\]

split the prime powers into `e^j<=n<e^(j+1)`. The factor
`Lambda(n)/sqrt(n)` and the relation `g(log n)=n^(-1/2)G(log n)` give an
effective weight `Lambda(n)/n`. Chebyshev's bound for the Mangoldt mass in one
shell then gives

\[
\boxed{
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}|g(\log n)|
\ll
\|G\|_1+\|G'\|_1.
}
\]

The two critical half-weights are load bearing. Omitting either would leave an
exponentially growing shell.

# 5. Gamma reserve and pole term

On the real line,

\[
P(u)^{2m}\ge1.
\]

Restricting the archimedean integral to

\[
|u|\le q^{-1/2}
\]

therefore gives a positive contribution of scale

\[
q^{-3/2}\log(2+|x|).
\]

The completed-zeta gamma density has a global finite lower bound. Since
`P(u)<=9` on the real line, the remaining negative constant part is at most

\[
Ce^{Cm}q^{-3/2}.
\]

Thus, for the stated high-centre range,

\[
\boxed{
\operatorname{gamma}_m(q,x)
\ge
c q^{-3/2}\log(2+|x|)
-
Ce^{Cm}q^{-3/2}.
}
\]

The scale and the growing-order error are correct.

The two pole values lie at imaginary displacement `1/2`. The phase-lock factor
is bounded on that closed line, so

\[
|\operatorname{pole}_m(q,x)|
\le
Ce^{Cm}(1+x^2)e^{-q(x^2-1/4)}.
\]

This is negligible in the high-centre regime.

# 6. Pointwise positivity condition

Comparing the prime envelope with the gamma reserve yields the logarithmic
condition

\[
\boxed{
\frac q4-\ell(x)+\frac32\log q
-m\log\frac{q}{C_0m}
\longrightarrow-\infty,
}
\]

where

\[
\ell(x)=\log\log(2+|x|),
\qquad
m=o(\ell(x)).
\]

For fixed `m>=2`, substitution of

\[
q\le
4\ell(x)
+
(4m-6-\varepsilon)\log(2+\ell(x))
\]

leaves exactly

\[
-\frac{\varepsilon}{4}\log\ell(x)+O_m(1).
\]

The fixed-order frontier is therefore algebraically correct, conditional only
on the reconstructed analytic estimates.

For

\[
m_*(q)=\left\lfloor\frac{q}{\log\log q}\right\rfloor,
\]

one has

\[
m_*(q)\log\frac{q}{C_0m_*(q)}
=
(1+o(1))
\frac{q\log\log\log q}{\log\log q}.
\]

Since `q~4 ell(x)` in the delicate range, the coefficient restriction
`eta<16` in the displayed growing-order corollary is correct.

# 7. Variable-order terminal dominance

Fix a terminal nonreal pair `t+/-iy`, with `0<y<1/2`. Its contribution is

\[
-2y^2e^{qy^2}P(iy)^{2m(q)}.
\]

For any nuisance zero in the closed strip,

\[
|P(z-t)|\le10,
\]

while `P(iy)>0` is fixed. If

\[
m(q)=o(q),
\]

every multiplier ratio is `e^(o(q))`. On a bounded ordinate window the
terminal-pair theorem supplies a fixed strict Gaussian exponent gap. Outside a
large fixed window the Gaussian has a quadratic negative exponent and the
subquadratic zero count is summable. Multiplication by `e^(o(q))` preserves
both limits.

Meanwhile

\[
e^{qy^2}P(iy)^{2m(q)}
=
e^{qy^2-o(q)}.
\]

Thus the terminal negative sign survives. The variable-order RH criterion is
valid for every fixed profile `m(q)=o(q)`.

# 8. Exact quantifier defect in the arbitrary-Delta theorem

PR #520 states:

> Let `Delta(t)>=0` satisfy `Delta(t)=o(t)`. No monotonicity is assumed.
> Define
> \[
> \Delta^*(Q)=\sup_{1\le t\le Q}\Delta(t).
> \]
> Then `Delta^*(Q)=o(Q)`.

This intermediate statement is false without a local-boundedness assumption.

Take

\[
\Delta(t)=
\begin{cases}
|t-2|^{-1},&t\ne2,\\
0,&t=2.
\end{cases}
\]

Then

\[
\Delta(t)=o(t)\qquad(t\to\infty),
\]

but for every `Q>2`,

\[
\sup_{1\le t\le Q}\Delta(t)=+\infty.
\]

Therefore `(T-94051.10)` and the written definition of `m_Delta` are invalid
for the theorem's stated class of arbitrary functions.

This is an exact contradiction to the displayed envelope claim. It is not a
counterexample to the intended eventual positivity conclusion.

## Repair

Choose a tail threshold `T_Delta` such that

\[
\Delta(t)\le t\qquad(t\ge T_\Delta),
\]

which exists from `Delta(t)=o(t)`. For `Q>=T_Delta`, define

\[
\boxed{
\Delta^\sharp(Q)
=
\sup_{T_\Delta\le t\le Q}\Delta(t).
}
\]

This supremum is finite because every value in its domain is at most `Q`.
Moreover,

\[
\Delta^\sharp(Q)=o(Q).
\]

Set the order profile to zero below a fixed threshold and, for large `q`, choose
the least integer `m` satisfying

\[
m\log\frac{q}{C_0m}
\ge
\frac{\Delta^\sharp(q)}4+3\log q.
\]

The least crossing is `o(q)` by the same argument in PR #520. For all
sufficiently large `x`, `ell(x)>=T_Delta`, and

\[
\Delta(\ell(x))
\le
\Delta^\sharp(q)
\]

whenever `q>=ell(x)`. The remainder of the proof is unchanged.

If the theorem is advertised as **effective** or the profile as computable,
one must additionally assume an effective modulus for `Delta(t)/t -> 0` and
effective access to the tail supremum. For an arbitrary noncomputable
function, the existence theorem is non-effective.

Disposition:

```text
T-94051.10 global-envelope subclaim:
  FALSE

T-94051 arbitrary-Delta conclusion:
  VERIFIED WITH THE TAIL-ENVELOPE FIX
```

# 9. Maximum-modulus firewall

For

\[
G_{q,m}(z)=e^{-qz^2}P(z)^{2m}
\]

in the half-strip `0<=Im z<=1/2`, the Gaussian kills the vertical sides.
Maximum modulus gives

\[
e^{qy^2}P(iy)^{2m}
\le
\max\left\{
9^{2m},
\sup_t e^{q/4-qt^2}|P(t+i/2)|^{2m}
\right\}.
\]

For fixed `m`, or `m=o(q)`, a fixed terminal depth eventually exceeds the real
boundary. The shifted critical-line boundary must then be at least as large as
the terminal signal. This correctly blocks a purely scalar absolute
strip-majorant proof of a fixed leading-constant improvement.

It does not block signed arithmetic cancellation, bilinear dispersion or a
non-scalar positive construction.

# 10. Coefficient variance

For fixed `m`, the energy scale is `log n~sqrt(q)`. A fixed translation by
`log4` is `O(q^(-1/2))` after rescaling, while

\[
D_L1=1.
\]

The claimed asymptotic

\[
V_m(q)=q+O_m(\sqrt q)
\]

therefore has the correct leading normalization, conditional on the same
classical coefficient-energy input imported from PR #390. Grouping all powers
of one prime gives

\[
\sum_p|Y_{p,q,m}(x)|^2\ll_m q+1.
\]

This remains an inverse/diagonal theorem. It does not upper-bound a coherent
prime sum; `R-93254` remains binding.

# 11. Computational scope

The retained `X-94050` checker authenticates:

- finite Laurent and translation algebra;
- conjugated shift coefficients and vanishing moments;
- cubic endpoint fixtures;
- fixed-order exponent arithmetic;
- selected sublinear-profile fixtures;
- finite diagnostics and mutations.

It explicitly does not authenticate:

- the Chebyshev shell theorem;
- the terminal-pair theorem;
- uniform growing-order Hermite bounds;
- gamma asymptotics;
- coefficient variance;
- the arbitrary-function quantifier;
- RH.

The new review regression includes the exact pathological-Delta witness and the
tail-envelope repair.

# Claim status

| Claim | Verdict | Surviving scope |
|---|---|---|
| `L-94049` | `VERIFIED WITH FIXES` | inherited centered criterion |
| `L-94050` | `VERIFIED` | exact phase-lock/translation dictionary |
| `T-94050` | `VERIFIED WITH FIXES` | RH-equivalent criterion on frozen terminal theorem |
| `L-94051` | `VERIFIED WITH FIXES` | analytic envelope; constants must be kept effective |
| `T-94051` fixed order | `VERIFIED WITH FIXES` | unconditional filtered wedge |
| `T-94051` explicit growing order | `VERIFIED WITH FIXES` | sublinear extension |
| `T-94051.10` | `FALSE` | global supremum need not be finite |
| `T-94051` arbitrary Delta | `VERIFIED WITH FIX` | use tail supremum; effectiveness qualified |
| `L-94052` | `CONDITIONAL IMPLICATION` | fixed-order coefficient energy |
| `R-94054` | `VERIFIED WITH FIXES` | scalar absolute-majorant no-go |
| `R-94055` | `VERIFIED WITH FIXES` | positivity shortcut blocked |
| `X-94050` | `EMPIRICAL / FINITE ALGEBRA ONLY` | no analytic proof |
| RH | `UNPROVEN` | no conclusion |

# Integration recommendation

Retain the phase-lock hierarchy and its fixed/growing-order analytic estimates
as a serious First-Hermite advance. Before integration:

1. replace the global `Delta^*` by the tail envelope `Delta^sharp`;
2. distinguish existence from effective computability;
3. pin the PR #379 terminal theorem and explicit-formula normalization as one
   conjunctive dependency;
4. do not describe the filtered positivity frontier as an RH proof;
5. preserve the fixed-leading-constant obstruction as the first open theorem.

The first live theorem remains a genuinely signed, carrier-specific estimate
that crosses

\[
q=(4+\delta)\ell(x)
\]

for some fixed `delta>0`. Absolute phase-blind filtering alone does not
provide it.
