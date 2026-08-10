# T-90204 — The frozen binary–ternary producer has polynomial positive and negative oscillations

Claim ID: `T-90204`  
Status: **PROPOSED COMPLETE REFUTATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90207`; standard Landau one-sign theorem for Mellin transforms; exact producer identity `L-23811`  
Scope: the specific frozen half-binary/half-ternary producer of `L-23811`; no statement about all balanced fragmentation flows and no RH claim

## 1. Statement

Let `A_X(n)` be the explicit descending producer of `L-23811`.  Then the fixed
bottom coordinate satisfies

\[
 \boxed{
 A_X(2)=\Omega_+(X^\theta)
 \quad\text{and}\quad
 A_X(2)=\Omega_-(X^\theta)
 }
\tag{T-90204.1}
\]

along **integer endpoints** for every

\[
 \boxed{
 0\le\theta<0.4493558205795862.
 }
\tag{T-90204.2}
\]

More explicitly, for every such `theta` and every `C>0`, there are arbitrarily
large integers `X` with

\[
 A_X(2)>CX^\theta
\]

and arbitrarily large integers `X` with

\[
 A_X(2)<-CX^\theta.
\]

Consequently:

1. pointwise positivity of this producer is false;
2. the producer coefficient changes sign infinitely often;
3. the coordinatewise GFEP theorem is false, because `2A_X(2)` is a positive combination of its two first-entrance exits;
4. the binary–ternary total-variation theorem
   \[
   \sum_{n=2}^X|A_X(n)|\sqrt n=X^{o(1)}
   \]
   proposed in `L-23811/T-23803` is false;
5. any variant asking only for subpower **negative** weighted variation of this same frozen producer is also false.

The theorem does **not** refute existential balanced fragmentation, Cycle Debt,
or the newer endpoint/prime-power criteria.  It closes one specific deterministic
producer route.

## 2. The fixed scalar and its transform

By `L-90207`,

\[
 F(X):=2A_X(2)
\tag{T-90204.3}
\]

has an integer-step interpolation `F#` whose Mellin transform has a genuine
nonreal pole

\[
 s_*=\sigma_*+it_*,
\qquad
 \boxed{\sigma_*>0.4493558205795862,}
\tag{T-90204.4}
\]

while the continued transform is holomorphic at **every positive real** `s`.
Moreover

\[
 F^\#(x)=O(\sqrt x\log^2(2x)),
\tag{T-90204.5}
\]

so its Mellin transform has a finite abscissa of convergence `sigma_c<=1/2`.
The pole forces

\[
 \sigma_c\ge\sigma_*>0.
\tag{T-90204.6}
\]

## 3. Eventual one-sign is impossible

Suppose first that `F(X)>=0` for every sufficiently large integer endpoint.
Then `F#(x)>=0` for every sufficiently large real `x`.  Removing the finite
initial segment changes its Mellin transform by an entire function.

Landau's one-sign theorem says that the real point `s=sigma_c` must be a
singularity of the Mellin transform of an eventually nonnegative function.
But `sigma_c>0`, and `L-90207` proves that the continued transform is
holomorphic at every positive real point.  Contradiction.

Applying the same argument to `-F` rules out eventual nonpositivity.  Therefore

\[
 \boxed{
 F(X)\text{ changes sign infinitely often on integer endpoints.}
 }
\tag{T-90204.7}
\]

This already refutes producer positivity and, because

\[
 F(X)=\Sigma_{X,2}(2)+\frac23\Sigma_{X,2}(3),
\tag{T-90204.8}
\]

also refutes GFEP-full: whenever `F(X)<0`, at least one of the two exits is
negative.

## 4. Polynomial oscillation by the shifted Landau trick

Fix

\[
 0\le\theta<\sigma_*
\]

and `C>0`.  Suppose, toward a contradiction, that

\[
 F(X)\ge-CX^\theta
\tag{T-90204.9}
\]

for every sufficiently large integer `X`.  Then

\[
 G(x):=F^\#(x)+Cx^\theta
\]

is eventually nonnegative.  Its Mellin transform is

\[
 \widehat G(s)
 =\widehat{F^\#}(s)+\frac{C}{s-\theta}
\tag{T-90204.10}
\]

up to an entire initial-segment correction.

The added real pole is at `s=theta`, strictly to the **left** of the certified
nonreal pole `s_*`.  Hence the abscissa of convergence of `G` is at least
`sigma_*>theta`.  Landau again requires a singularity on the positive real axis
at that abscissa.  The first term has no positive-real singularity and the added
term has only the pole at `theta<sigma_*`, a contradiction.

Thus for every `C>0`,

\[
 F(X)<-CX^\theta
\]

at arbitrarily large integer endpoints.  The identical argument applied to
`-F` proves arbitrarily large positive excursions.  This proves
(T-90204.1)--(T-90204.2).

## 5. Refutation of the frozen BTF targets

The original explicit producer theorem `L-23811/T-23803` asks for

\[
 \operatorname{BTF}(X)
 =\sum_{n=2}^X|A_X(n)|\sqrt n
 =X^{o(1)}.
\tag{T-90204.11}
\]

But

\[
 \operatorname{BTF}(X)
 \ge\sqrt2\,|A_X(2)|.
\]

By Section 4, for every `theta<0.4493558205795862`, the right side exceeds
`C X^theta` along arbitrarily large endpoints, for arbitrary `C`.  Therefore

\[
 \boxed{
 \operatorname{BTF}(X)\ne X^{o(1)}.
 }
\tag{T-90204.12}
\]

Likewise, if a later adapter asks only for the negative ledger

\[
 \sum_n\sqrt n\,[-A_X(n)]_+,
\]

then along the negative subsequence

\[
 \sum_n\sqrt n\,[-A_X(n)]_+
 \ge\sqrt2\,[-A_X(2)]_+
 =\Omega(X^\theta)
\]

for every `theta` below the same exponent.  Hence a subpower-negative-debt
claim for **this fixed producer** also fails.

This does not address a cycle-optimized or state-dependent producer: the
oscillation is tied to the deterministic half-binary/half-ternary transfer.

## 6. Why long finite positivity was misleading

The certified resonance has exponent only slightly below `1/2`, but its residue
is small.  Direct reconnaissance still gives

```text
2 A_X(2) > 0
```

through millions of endpoints and shows roughly logarithmic growth on that
range.  The resonance term is therefore invisible until very large scales.
This is exactly the failure mode anticipated in `T-23803`'s review protocol:
a finite positive table cannot certify the cofinal rate.

The new result is stronger than a finite counterexample.  It identifies the
analytic mechanism forcing infinitely many remote counterexamples and gives a
quantitative oscillation exponent.

## 7. Route consequences

The repository map should now read

```text
frozen binary/ternary pointwise producer positivity     REFUTED
GFEP-full                                                REFUTED
frozen binary/ternary BTF total variation                REFUTED
frozen binary/ternary subpower negative debt             REFUTED
Pascal-cycle optimized / state-dependent fragmentation   NOT REFUTED HERE
prime endpoint / positive occupancy route                UNAFFECTED
factor-64 annular endpoint criterion                     UNAFFECTED
Riemann Hypothesis                                       UNPROVED
```

The transform factorization also explains the failure structurally.  The
arithmetic reciprocal-zeta factor is multiplied by a deterministic
fragmentation transfer with its own nonreal resonances arbitrarily close to the
critical scaling line (`L-90206`).  `L-90207` proves that the actual producer
boundary excites at least one such resonance rather than canceling it.

## 8. Proof boundary

The only numerical input is the fail-closed root/numerator/zeta certificate of
`L-90207/X-90204`, with analytic infinite-tail bounds and a margin exceeding
`9e-3`.  All oscillation and BTF consequences are exact applications of the
standard Landau one-sign theorem.

This theorem proves no statement about RH itself.  It is a route refutation and
a quantitative description of why the frozen producer ultimately fails.