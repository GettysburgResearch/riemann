# T-100720 — Cubic hinge coarea and a source-owned two-certificate frontier

Claim ID: `T-100720`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; TWO COMPLEMENTARY COLLAR ESTIMATES OPEN**  
Created: 2026-08-21  
Base: PR #691 at `be9a4168fa0df971a2fc63176f07ce3beee6c3d4`  
RH status: **unproved**

The live implication matrix had isolated long mixed-activation cubic collars,
but their physical entries still obscured the underlying arithmetic.  The
lemmas `L-100720--L-100724` give a complete exact normal form and enlarge the
unconditionally positive matrix region.

## 1. Exact source packet

Every double-owner cubic entry is

\[
H_{p,q;\mathcal P}(t)
=M_{p,q;\mathcal P}(t)
+64\Delta_p\Delta_qE_{\mathcal P}(1-t)_+^3,
\]

where `M>=0` is the explicit deep carrier.  The centered packet is one compact
cubic spline and has no hidden fully active term.

## 2. Exact arithmetic derivative

Its derivative is

\[
H'_{p,q;\mathcal P}(t)
=384\int_0^1(1-s)
 \mathcal B_{p,q;\mathcal P}((t/s)^2)ds,
\]

where

\[
\begin{aligned}
\mathcal B_{p,q;\mathcal P}(x)
={}&A_{\mathcal P}(x)
-p^{-1/2}A_{\mathcal P}(x/p)\\
&-q^{-1/2}A_{\mathcal P}(x/q)
+(pq)^{-1/2}A_{\mathcal P}(x/(pq))
\end{aligned}
\]

and `A_P` is the literal reciprocal-Möbius prefix on the finite interior prime
semigroup.

Tao's elementary theorem gives a uniform bound for every such prefix, hence a
uniform derivative bound independent of interval depth.

## 3. New positive interval theorem

Let

\[
S_{p,q}=\sum_{p<\ell<q}\ell^{-1}.
\]

Euler-level double counting proves

\[
1-S_{p,q}\le A_{\mathcal P}(x)\le1
\qquad(x\ge1)
\]

whenever `S_(p,q)<1`. Therefore

\[
\mathcal B_{p,q;\mathcal P}(x)
\ge1-S_{p,q}-p^{-1/2}-q^{-1/2}.
\]

Consequently

\[
S_{p,q}+p^{-1/2}+q^{-1/2}<1
\Longrightarrow
H_{p,q;\mathcal P}(t)\ge0
\quad(t\ge0).
\]

Mertens' theorem now gives the asymptotic pointwise region

\[
\boxed{
q\le p^A,\quad A<e,\quad p\ge p_0(A)
\Longrightarrow
H_{p,q;\mathcal P}\ge0.
}
\]

Thus only endpoint intervals satisfying

\[
\log q\ge(e-o(1))\log p
\]

can remain in the negative collar matrix.  This strictly enlarges the earlier
`A<exp(3/4)` theorem.

## 4. Exact summable high derivative

The centered packet has the step-source third derivative

\[
\widetilde H'''(t)
=-384\sum_d{\mu(d)\over d^2}
 [1_{t<\sqrt d}-p^{-3/2}1_{t<\sqrt{pd}}
  -q^{-3/2}1_{t<\sqrt{qd}}+(pq)^{-3/2}1_{t<\sqrt{pqd}}].
\]

Its total variation is governed by the convergent prime `3/2` mass, and the
joint min--max average of that variation is uniformly bounded.

## 5. The exact AND gate

For one interval define the left and right Taylor certificates

\[
\mathcal L(t)={1\over2}\int_0^t(t-u)^2|\widetilde H'''(u)|du,
\]

\[
\mathcal R(t)={1\over2}\int_t^\infty(u-t)^2|\widetilde H'''(u)|du.
\]

Then

\[
\boxed{H(t)_-^2\le\mathcal L(t)\mathcal R(t).}
\]

The first certificate uses the exact positive quadratic initialization at the
activation origin.  The second uses the exact nonnegative deep carrier and the
vanishing compact collar at infinity.

After averaging with the literal joint min--max probabilities, the two
terminal statements `LPCC100723` and `FPCC100723` satisfy

\[
\boxed{
\mathrm{LPCC100723}\wedge\mathrm{FPCC100723}
\Longrightarrow RH.
}
\]

## 6. Relationship to existing routes

```text
LPCC100723:
  compensated finite-prefix / first-owner / activation-endpoint geometry;

FPCC100723:
  future product boundary / largest-prime squaring / positive renewal;

both together:
  exact negative cubic collar -> centered-cubic Mellin--Landau detector.
```

The two certificates are attached to the same occurrence before any marginal
or physical collapse.  This avoids both refuted mechanisms:

```text
unbalanced one-sided owner Schur sums;
short/long absolute norms before carrier cancellation.
```

## 7. Exact boundary

```text
cubic hinge representation                    PROVED EXACT
carrier/collar separation                     PROVED EXACT
compensated reciprocal-prefix coarea           PROVED EXACT
uniform semigroup-prefix derivative bound      PROVED
positive endpoint intervals q<=p^A, A<e        PROVED ASYMPTOTICALLY
summable third-variation source                PROVED EXACT
finite-cutoff source exhaustion                PROVED
left/right pointwise Taylor AND gate           PROVED EXACT
regularity-only shortcut                       REFUTED
LPCC100723                                     OPEN / RH-BEARING
FPCC100723                                     OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```

The packet does not claim that bounded rough prefixes or bounded third
variation prove either terminal estimate.  Their conjunction on the remaining
supercritical intervals is the new, fully typed implication-matrix frontier.
