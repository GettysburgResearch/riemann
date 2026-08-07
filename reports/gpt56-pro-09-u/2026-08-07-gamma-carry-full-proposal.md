# Full proposal: Gamma–carry convolution packing for RH

Agent: `gpt56-pro-09-u`  
Date: 2026-08-07  
Issue: #238  
Parent branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: **FULL PROPOSED PROOF WITH ONE ISOLATED POSITIVITY THEOREM; RH NOT CLAIMED**

## 1. Step back

The repository's live arithmetic routes now agree on one point: after Type-I and
endpoint terms are removed, the remaining obstruction is a signed reciprocal-
zeta/Möbius correlation. The reflected Selberg, BTP, fixed-ratio Mertens,
analytic-totient, prime-energy, and square-screw formulations all retain that
same core.

The carry programme offers a potentially shorter coordinate system. Its exact
finite identity already converts prime-power weights into nonnegative average
carry counts and binomial entropies. The previous carry branch correctly
weakened pointwise triangular-inverse positivity to a nonnegative packing
problem, but it did not identify the sharp packing profile.

This pass finds that profile.

## 2. New exact object

The continuum carry kernel is

\[
K(x)={\lfloor x\rfloor(\lfloor x\rfloor+1-x)\over x}.
\]

It has exact Mellin transform

\[
\int_1^\infty K(x)x^{-s-2}dx
={s\zeta(s+1)\over(s+1)(s+2)}
\]

and exact mass `1/2` at `s=0`.

The normalized logarithmic density

\[
p(t)=2e^{-t}K(e^t)
\]

is an explicit probability law. One realization is

```text
P(M=m)=1/[m(m+1)],
V~Beta(2,1),
X=M(M+1)/(M+V),
T=log X.
```

The sharp logarithmic target is the `Gamma(2,1/2)` law. Dividing its transform
by the carry transform produces

\[
A(s)={(s+1)(s+2)
\over8s(s+1/2)^2\zeta(s+1)}.
\]

Its exact physical inverse is the Möbius–Riesz density

\[
\begin{aligned}
a(t)=\sum_{n\le e^t}{\mu(n)\over n}
\bigg[&1-{7\over8}e^{-(t-\log n)/2}\\
&-{3\over16}(t-\log n)e^{-(t-\log n)/2}\bigg].
\end{aligned}
\]

The proposal's sole hinge is

\[
\boxed{a(t)\ge0\quad(t\ge0).}
\]

Equivalently, the carry variable `T` is an additive convolution factor of an
independent `Gamma(2,1/2)` variable.

## 3. Why this is the correct amount of smoothing

A single exponential target would leave a signed atomic inverse. Shape two
removes those atoms and produces an ordinary density. This explains why the
full logarithmic ramp may admit a positive packing even though a separate
unit-ramp packing need not attain its formal dual constant.

The gamma quotient is not decorative. Its double pole at `s=-1/2` produces the
exact logarithmic main profile needed for the `4 sqrt(X)` cancellation, while
the reciprocal zeta factor preserves the complete balanced Möbius obstruction.

## 4. Exact finite packing

Assuming the density sign, define

\[
d_X(n)=8\sqrt X\int_n^{n+1}
y^{-2}a(\log(X/y))dy.
\]

The finite carry coefficient satisfies exactly

\[
\beta_{nq}=K_-((n+1)/q),
\]

and this endpoint sample is the minimum of `K(y/q)` over the whole cell
`[n,n+1]`. Therefore

\[
\sum_{n=q}^Xd_X(n)\beta_{nq}
\le q^{-1/2}\log(X/q)
\]

with no discretization remainder.

The gamma exponential moments then give

\[
\sum_n d_X(n)G_n
\ge4\sqrt X-O_\epsilon(X^\epsilon).
\]

Hence the complete prime-power ramp satisfies the same lower bound.

## 5. RH deduction

At `X=N^2`, the exact square-screw formula is

\[
\Psi(2\log N)
=4(N+N^{-1}-2)-\mathcal P(N^2)+O(\log N).
\]

The carry packing gives

\[
\Psi(2\log N)\le N^{o(1)}.
\]

The unconditional derivative bound propagates this upper envelope between
adjacent square samples. The upper-envelope form of Landau's one-sign theorem
then excludes every pole of `xi'/xi` to the right of the critical line.
Functional-equation symmetry gives RH.

## 6. Why this proposal is genuinely new

The proposal does not:

- assert the exact triangular carry inverse is pointwise positive;
- require a full Heath--Brown packet dictionary;
- use a generic Farey-spacing estimate;
- assume a positive-Hankel stop-loss adjoint;
- import the affine central-block gate;
- smooth away fixed off-line modes.

Instead it asks whether one completely explicit arithmetic probability law is a
convolution factor of one gamma law. All finite and analytic consequences of
that factorization are exact.

## 7. Falsifiability

The theorem can be rejected by one exact negative value of `a(t)`. On each
quotient interval the density has the form

\[
A_r-e^{-t/2}[7B_r/8+3(tB_r-C_r)/16]
\]

and has at most one interior critical point. Thus a complete adversarial search
requires only endpoints and one possible critical value per layer.

Alternatively, a reviewer may attack the all-order Hausdorff moments

\[
{(k+1)(k+2)
\over8k(k+1/2)^2\zeta(k+1)}.
\]

Finite positive tables are not a proof; one exact failed difference rejects the
factor interpretation.

## 8. Connection to BTP and reflected Selberg

GCF is not pretending the balanced Möbius core disappeared. The reciprocal-zeta
factor is explicit in `A(s)`. A proof of GCF may well be obtained by specializing
the reflected Hermitian Selberg identity or BTP to this single shape-two
profile.

The advantage is compression: every Type-I and endpoint channel has already
been integrated into the carry probability law, leaving a one-variable sign
rather than a growing packet schema.

## 9. Exact status

```text
L-23804 carry Mellin/probability law      PROPOSED COMPLETE
L-23805 quotient/density identities       PROPOSED COMPLETE
GCF density positivity                    OPEN / RH-BEARING
L-23806 finite packing from GCF            PROPOSED COMPLETE
T-23801 full deduction to RH               PROPOSED COMPLETE
X-23801 exact normalization replay         PASS
Riemann Hypothesis                         NOT PROVED
```

This is the final review package: a full proof architecture with one explicit,
falsifiable arithmetic theorem and no hidden residual estimate.
