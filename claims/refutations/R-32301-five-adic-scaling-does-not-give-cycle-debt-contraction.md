# R-32301 — Five-adic scaling alone does not give a `1/5` Cycle-Debt contraction

Claim ID: `R-32301`  
Title: The square-root critical dual potential is exactly neutral under the five-adic source scaling, so the proposed residue renewal needs a genuinely source-specific transport theorem  
Status: **EXACT SCOPE REFUTATION / FIREWALL**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27205-cycle-optimized-capacity-debt-and-duality.md`; PR #322 five-adic block identity  
Scope: refutes the inference `five-adic scaling => 1/5 debt contraction`; does not refute a future source-specific five-adic certificate

## 1. Cycle-Debt dual

Fix the `1/5`-balanced split space.  For a split

\[
 e=(n,j),
 \qquad \frac n5\le j\le\frac n2,
\]

put

\[
 \omega_e=\sum_{q=2}^{n}\frac{\chi_e(q)}{\sqrt q}.
\]

PR #272 proves that the optimized negative capacity debt has the exact dual

\[
 \mathfrak N(r)
 =\max_F\left[-\sum_m r(m)F(m)\right],
\tag{R-32301.1}
\]

where every allowed split obeys

\[
 0\le
 \delta_eF:=F(n)-F(j)-F(n-j)
 \le\omega_e.
\tag{R-32301.2}
\]

The five-adic proposal on PR #322 uses the exact critical scaling

\[
 (\mathcal S_5r)(5m)=5^{-1/2}r(m),
 \qquad
 (\mathcal S_5r)(n)=0\quad(5\nmid n),
\tag{R-32301.3}
\]

on the coarse source channel.

## 2. An explicit admissible critical potential

Define

\[
\boxed{
 F_*(n)=\frac14\left(n-\sqrt n\right).
}
\tag{R-32301.4}

For every binary split,

\[
 \delta_eF_*
 =\frac14
 \left(
  \sqrt j+\sqrt{n-j}-\sqrt n
 \right)
 \ge0.
\tag{R-32301.5}

On a `1/5`-balanced split, every integer

\[
 \max(j,n-j)<q\le n
\]

is a carry.  There are at least `n/5` such integers in the real-length sense, and each contributes at least `n^{-1/2}`.  Hence

\[
 \omega_e\ge\frac15\sqrt n.
\tag{R-32301.6}

On the other hand

\[
 \sqrt j+\sqrt{n-j}-\sqrt n
 \le(\sqrt2-1)\sqrt n
 <\frac12\sqrt n.
\]

Therefore

\[
 \delta_eF_*<\frac18\sqrt n<\frac15\sqrt n\le\omega_e.
\tag{R-32301.7}

Thus `F_*` is an admissible dual potential at every endpoint.  No limiting argument is used.

## 3. Exact scale neutrality

Every fragmentation source has the size-conservation identity

\[
 \sum_m m\,r(m)=0.
\tag{R-32301.8}

For such a source,

\[
 \sum_m r(m)F_*(m)
 =-\frac14\sum_m\sqrt m\,r(m).
\tag{R-32301.9}

Now apply the coarse five-adic scaling (R-32301.3):

\[
\begin{aligned}
 \sum_n(\mathcal S_5r)(n)F_*(n)
 &=\frac1{\sqrt5}
   \sum_mr(m)\frac14(5m-\sqrt{5m})\\
 &=\frac{\sqrt5}{4}\sum_m m r(m)
   -\frac14\sum_m\sqrt m\,r(m)\\
 &=\boxed{
   \sum_mr(m)F_*(m).}
\end{aligned}
\tag{R-32301.10}

The critical square-root dual pairing is **exactly invariant** under the five-adic source scaling.

## 4. Consequence for PR #322

The block identity

\[
 \sum_{j=0}^{4}r_X(5a+j)=5^{-1/2}r_{X/5}(a)
\]

is exact and valuable.  What does **not** follow from it is a debt reserve

\[
 D_X\le\frac15D_{X/5}+\cdots
\]

merely by dimensional scaling.

Equation (R-32301.10) exhibits an admissible Cycle-Debt dual mode on which the coarse critical source has gain exactly one.  Therefore any strict contraction must be created by the **complete four residue commutators and their source-specific signed recombination**.  It cannot come from the factor `5^{-1/2}` by itself, from a source-blind norm estimate, or from quotienting out an allegedly harmless scaling direction without checking this dual mode.

In particular, a finite automaton `K` advertised as a universal residue contraction must emit an exact calculation showing how it defeats or exports the pairing (R-32301.10).  Omitting that row is a fail-closed error.

## 5. Relation to the half-moment firewall

For the actual critical target divergence `R_X`, the same pairing is the half-moment

\[
 \sum_mR_X(m)F_*(m)
 =\frac14\mathfrak H_X,
\]

where

\[
 \mathfrak H_X=-\sum_mR_X(m)\sqrt m.
\]

PR #277 already identifies `mathfrak H_X` as a reciprocal-zeta scalar.  Thus the neutral mode in (R-32301.10) is not an artificial adversarial vector; it is the exact critical arithmetic mode previously isolated by the fragmentation programme.

## 6. Corrected five-adic production target

The viable theorem is therefore source-specific:

```text
coarse five-adic source, neutral in the sqrt dual
+ all four exact residue commutators
+ legal Pascal-cycle recombination
-> strict contraction of the COMPLETE source pairing/debt.
```

A rational transition matrix may still exist for the actual critical source.  But its contraction must be proved after the neutral coarse component and the residue commutators are assembled.  A generic five-state spectral-radius claim is not enough.

## 7. Proof boundary

Proved exactly:

1. admissibility of the critical potential `F_*`;
2. exact scale invariance of its source pairing;
3. the resulting failure of `1/5` as a source-blind scaling reserve.

Not refuted:

1. a source-specific five-adic Pascal-cycle certificate using all residue commutators;
2. Cycle Debt for the actual critical source;
3. RH.
