# Independent review of PR #376: Brownian high-frequency Bohr instability

**Review cutoff (UTC):** `2026-08-11T12:31:26Z`  
**Base/main SHA:** `3a441dfa2d287b17b22dcd5dbfc0123355ce8232`  
**Reviewed PR:** `#376`  
**Reviewed PR head:** `0ed0e7de3aa1b81bb832df53d861dd6f27f2db8b`  
**Parent raw-Brownian head:** PR #343 at `fed85f2969a5ab9f09890cd89bd6b57ff2115320`  
**Review character:** theorem-level independent delta review; no heavy experiment package rerun  
**RH status:** **unproved and undisproved**

## Executive verdict

```text
PR #376 overall                                  VERIFIED WITH FIXES
L-90601 raw selected-prime Bohr theorem           VERIFIED
R-90601 raw cofinal-stability refutation          VERIFIED
L-90603 positive-mixture Bohr theorem              VERIFIED WITH FIXES
L-90604 symmetrized Stirling/Hurwitz transfer      VERIFIED
R-90602 current finite real-zero finishes          VERIFIED AS REFUTED
L-90602 fixed-compact 1/N asymptotic               VERIFIED WITH FIXES
X-90601 / X-90602                                  EMPIRICAL ONLY
Riemann Hypothesis                                 UNPROVED
```

No load-bearing gap was found in the selected-prime → Steinhaus → polygon → Kronecker → Hurwitz argument. The exact current finite Brownian producers do have unavoidable high-frequency off-line zeros for every sufficiently large truncation index.

Consequently, the following are **FALSE**, not merely open:

1. raw all-large-`N` half-plane stability;
2. raw stability on any unbounded cofinal sequence;
3. logarithmic Nörlund one-sided half-plane stability;
4. logarithmic Nörlund finite-real-zero stability after functional-equation symmetrization;
5. central-binomial Green/Robin finite-real-zero stability after symmetrization.

The theorem does not contradict local-uniform convergence to `xi`, fixed-height zero approximation, finite probability identities, the corrected one-fiber Robin theorem, or RH itself. It closes one proof architecture rather than settling the full problem.

## 1. Exact parent target

PR #343 reduces the raw route to the zero-free theorem

\[
\mathbb E[Q_N^z]\ne0,
\qquad \Re z>\frac14,
\]

for every sufficiently large `N`, or at least for an unbounded sequence of indices.

Using the exact Dirichlet/Hermite formula of `L-34003`, the non-elementary zero set is the zero set of

\[
H_N(z)=\sum_{n=1}^N C_{N,n}n^{-2z}(z+\alpha_{N,n}),
\]

where

\[
C_{N,n}=4\frac{(N!)^4}{(N-n)!^2(N+n)!^2}>0.
\]

Thus one high-frequency zero of `H_N` with `Re z>1/4` contradicts stability for that `N`. A theorem producing such zeros for every sufficiently large `N` refutes all possible cofinal stable subsequences.

## 2. Review of `L-90601`: raw high-frequency theorem

### 2.1 Decomposition at large vertical height

The proof writes

\[
H_N(z)=zF_N(z)+G_N(z),
\]

with

\[
F_N(z)=\sum_{n=1}^N C_{N,n}n^{-2z},
\qquad
G_N(z)=\sum_{n=1}^N C_{N,n}\alpha_{N,n}n^{-2z}.
\]

For fixed `N` and vertical shifts `t_j→∞`, division by `z+it_j` removes the lower-order `G_N` contribution uniformly on compact sets. Therefore it is enough to construct one twisted vertical limit of `F_N` with a zero at a prescribed real point

\[
\frac14<\sigma<\frac12.
\]

**Verdict:** exact and correctly normalized.

### 2.2 Selected-prime coefficient estimates

Choose

\[
\mathcal P_N=\{p\text{ prime}:2\sqrt N\le p\le3\sqrt N\}.
\]

The exact ratio

\[
\frac{C_{N,k+1}}{C_{N,k}}
=
\left(\frac{N-k}{N+k+1}\right)^2
\]

implies the lower bound

\[
C_{N,p}\ge4e^{-20}
\]

for all sufficiently large `N` and every selected prime `p`.

For `m≥2` with `mp≤N`, the same ratio gives

\[
\frac{C_{N,mp}}{C_{N,p}}
\le e^{-5(m^2-1)}.
\]

The constants are deliberately crude but valid. The second estimate gives the uniformly summable multiple tail

\[
\eta_\sigma
=
\sum_{m=2}^{\infty}e^{-5(m^2-1)}m^{-2\sigma}<10^{-6}.
\]

**Verdict:** verified. No finite computation is load bearing.

### 2.3 Independence and composite bookkeeping

No integer `n≤N` is divisible by two selected primes because the product of two selected primes is at least `4N>N`. Also, if `n=pm≤N` with selected `p`, then `m` contains no selected prime.

Hence the support splits exactly into:

1. integers divisible by no selected prime;
2. one disjoint fiber for each selected prime.

There is no hidden overlap or double assignment of composites.

**Verdict:** verified.

### 2.4 Steinhaus residual estimate

At `Re z=σ`, set

\[
a_n=C_{N,n}n^{-2\sigma}.
\]

Randomize the primes outside `P_N` by independent Haar phases and extend completely multiplicatively. Distinct integers give distinct exponent vectors, so Steinhaus orthogonality yields

\[
\mathbb E|R|^2
=
\sum_{n\text{ avoiding }\mathcal P_N}a_n^2
\le16\sum_{n=1}^{\infty}n^{-4\sigma}
=16\zeta(4\sigma).
\]

The lower boundary `σ>1/4` is exactly what makes the background square summable. Therefore one deterministic twist satisfies

\[
|R|\le4\sqrt{\zeta(4\sigma)}.
\]

**Verdict:** verified. Composite dependence has not been mistaken for probabilistic independence.

### 2.5 Available selected-prime phase mass

For a selected prime, define the complete fiber

\[
B_p=\sum_{m\le N/p}a_{pm}\omega(m).
\]

The multiple-tail estimate gives

\[
|B_p-a_p|\le\eta_\sigma a_p.
\]

By the prime number theorem,

\[
\#\mathcal P_N\gg\frac{\sqrt N}{\log N},
\]

and therefore

\[
\sum_{p\in\mathcal P_N}|B_p|
\gg_\sigma
\frac{N^{1/2-\sigma}}{\log N}
\longrightarrow\infty.
\]

The upper boundary `σ<1/2` is exactly what makes the selected phase mass diverge. Meanwhile

\[
\frac{\max_p|B_p|}{\sum_p|B_p|}\to0.
\]

Thus the full interval

\[
\frac14<\sigma<\frac12
\]

arises from two complementary requirements:

```text
σ>1/4  → bounded square-summable background;
σ<1/2  → diverging independent selected-prime phase mass.
```

**Verdict:** verified.

### 2.6 Polygon closure

For large `N`, the selected lengths satisfy

\[
2\max_p|B_p|<\sum_p|B_p|
\]

and the total selected length exceeds `|R|`. The elementary polygon theorem therefore permits phases `u_p` such that

\[
\sum_{p\in\mathcal P_N}u_pB_p=-R.
\]

Extending the twist by `χ(p)=u_p` gives an exact torus zero

\[
F_{N,\chi}(\sigma)=0.
\]

**Verdict:** verified. Exact cancellation is obtained; no approximate zero is being promoted.

### 2.7 Kronecker approximation

The numbers `log p`, for the finitely many primes `p≤N`, are linearly independent over `Q`: a rational relation would exponentiate to a multiplicative relation among distinct primes.

Kronecker therefore provides arbitrarily large `t_j` such that

\[
p^{-2it_j}\to\chi(p)
\]

simultaneously for every relevant prime. Hence

\[
F_N(z+it_j)\to F_{N,\chi}(z)
\]

locally uniformly.

**Verdict:** verified. The factor `2` in the vertical phase does not change density of the one-parameter orbit.

### 2.8 Hurwitz/Rouché transfer

Define

\[
\mathcal H_j(z)=\frac{H_N(z+it_j)}{z+it_j}.
\]

Since the sum is finite and

\[
\frac{z+it_j+\alpha_{N,n}}{z+it_j}\to1
\]

uniformly on compact sets,

\[
\mathcal H_j(z)\to F_{N,\chi}(z)
\]

locally uniformly. The limit is not identically zero and its zero at `σ` is isolated. Hurwitz, or Rouché on a zero-isolating circle, gives actual zeros

\[
z_j=w_j+it_j
\]

of `H_N`, with

\[
w_j\to\sigma,
\qquad
|\Im z_j|\to\infty.
\]

**Verdict:** verified.

### 2.9 Quantifier order

The theorem proves

\[
\forall\sigma\in(1/4,1/2)\;
\exists N_0(\sigma)\;
\forall N\ge N_0(\sigma)\;
\exists\text{ infinitely many violating zeros}.
\]

Taking one fixed value, such as `σ=3/8`, proves that every sufficiently large `N` fails the proposed half-plane stability. Therefore no unbounded stable subsequence exists.

**Verdict for `L-90601` and `R-90601`: VERIFIED.**

## 3. Review of `L-90603`: positive cutoff mixtures

For a positive cutoff mixture,

\[
D_{\lambda,N}(s)
=sB_{\lambda,N}(s)+A_{\lambda,N}(s),
\]

where

\[
B_{\lambda,N}(s)
=
\sum_{n=1}^N b_{N,n}n^{-s},
\qquad
b_{N,n}
=
\frac12\sum_{K=n}^N\lambda_{N,K}C_{K,n}.
\]

Assume

\[
\sum_{N/2\le K\le N}\lambda_{N,K}
\ge\frac{c_0}{\log N}.
\]

At a fixed `1/2<β<1`, the background now satisfies

\[
\mathbb E|R|^2\le4\zeta(2\beta),
\]

while the selected-prime phase mass obeys

\[
\sum_{p\in\mathcal P_N}|B_p|
\gg_{\beta,c_0}
\frac{N^{(1-\beta)/2}}{(\log N)^2}
\to\infty.
\]

The same polygon, Kronecker and Hurwitz argument gives infinitely many one-sided zeros with real parts tending to `β`.

Both repository mixtures satisfy the top-half hypothesis:

```text
logarithmic Nörlund:      λ_(N,K)=1/(K H_N);
central-binomial Green:   λ_(N,K)=ω_K/Σ_(J≤N)ω_J.
```

**Verdict:** the theorem is correct under its stated top-half-mass hypothesis.

### Required fixes

1. Under only `λ_(N,K)≥0` and `Σ_K λ_(N,K)=1`, the general coefficient statement should be
   \[
   b_{N,n}\ge0,
   \]
   not `b_(N,n)>0` for every `n`. Strict positivity is present on the selected-prime block because the top-half-mass condition supplies weight at `K≥p`.
2. The phrase `positive finite cutoff averaging as cure FALSE` is too broad. The proof refutes the two repository mixtures and every positive mixture satisfying the displayed top-half-mass condition; it does not refute every conceivable positive weighting scheme.

These are scope/editorial fixes and do not affect the conclusion for the current producers.

**Verdict for `L-90603`: VERIFIED WITH FIXES.**

## 4. Review of `L-90604`: symmetrization

Write

\[
m_N(s)=A(s)D_N(s),
\qquad
A(s)=\pi^{-s/2}\Gamma(1+s/2),
\]

and

\[
\mathcal X_N(s)=m_N(s)+m_N(1-s).
\]

Near a vertical translate `s=w+it_j`, normalize by

\[
\mathcal Y_j(w)
=
\frac{\mathcal X_N(w+it_j)}{it_jA(w+it_j)}.
\]

The one-sided term converges locally uniformly to the twisted polynomial `B_(N,χ)(w)`. On a compact set contained in `Re w>1/2`, uniform Stirling gives

\[
\left|
\frac{A(1-w-it_j)}{A(w+it_j)}
\right|
\ll_K
|t_j|^{1/2-\Re w}
\to0.
\]

Because `D_N(s)=sB_N(s)+A_N(s)` with finite Dirichlet polynomials, the reflected Dirichlet factor divided by `it_j` remains bounded. Hence

\[
\mathcal Y_j(w)\to B_{N,\chi}(w)
\]

locally uniformly. Hurwitz transfers the torus zero to an actual zero of the exact symmetrization with real part tending to every prescribed `β∈(1/2,1)`.

**Verdict:** verified. Functional-equation symmetry does not cure the high-frequency finite defect.

## 5. Review of `L-90602`: fixed-height salvage

The compact asymptotic

\[
m_N(s)
=
2\xi(s)
-
\frac{2s}{\pi N}\xi(s-2)
+
O_K(N^{-2})
\]

follows from the independent tail decomposition `S_∞=S_N+R_N`, the estimates

\[
\mathbb E R_N=\frac2N+O(N^{-2}),
\qquad
\mathbb E R_N^2=O(N^{-2}),
\]

and a Taylor expansion with uniformly controlled negative moments on each fixed compact set.

At a fixed simple zero `ρ` of `xi`, the analytic implicit-function/Rouché expansion yields

\[
s_N
=
\rho
+
\frac{\rho\xi(\rho-2)}{\pi\xi'(\rho)}\frac1N
+
O_\rho(N^{-2}).
\]

This is fully compatible with `L-90601`: compact-height zeros converge well while different spurious zeros escape to high imaginary height.

### Required qualification

The continuum integral

\[
\int_0^\infty
 e^{-2x^2}x^{-2z}
 \left(z-\frac12+2x^2\right)dx
\]

is directly convergent initially for `Re z<1/2`. Its zero identity then extends meromorphically/analytically by the gamma recurrence. The initial domain and continuation should be stated.

**Verdict for `L-90602`: VERIFIED WITH FIXES.**

## 6. Stale sentence to repair

`R-90601` says that the symmetrized Brownian/Robin programme is unaffected. That sentence was accurate at the earlier raw-only head, but it is stale at current head `0ed0e7d...` because `L-90603`, `L-90604` and `R-90602` now refute the two current symmetrized finite producers.

Recommended replacement:

```text
not addressed by L-90601 alone;
subsequently addressed for the current Nörlund and Green mixtures by
L-90603/L-90604 and R-90602.
```

## 7. Computation boundary

No large experiment package was rerun. The retained scripts correctly describe themselves as finite algebra and numerical diagnostics only.

The retained evidence includes:

```text
X-90601:
  3,160 exact coefficient-ratio checks;
  multiple-tail constant;
  numerical roots for N=63 and N=60;
  continuum-cancellation regression.

X-90602:
  exact weight normalization and top-half mass checks;
  exact leading-coefficient construction;
  finite multiple-ratio diagnostics.
```

The analytic refutation rests on the written PNT/Steinhaus/polygon/Kronecker/Hurwitz proof, not the finite roots.

## 8. Meaning for the full problem

### 8.1 What is closed negatively

The raw Brownian proof DAG formerly ended with

```text
finite gamma sum
→ Dirichlet-average factorization
→ explicit Hermite numerator H_N
→ global cofinal half-plane zero-freeness
→ local convergence/Rouché
→ RH.
```

The global finite zero-free arrow is now false.

The current logarithmic Nörlund and central-binomial Green/Robin finite-real-zero finishes are also false. No canonical-system or Hermite–Biehler representation can prove global real-rootedness for those exact finite functions because the functions themselves possess infinitely many off-line zeros.

### 8.2 What survives exactly

Retain:

- Brownian/gamma probability representation;
- finite gamma and Dirichlet-average algebra;
- explicit Hermite divided differences;
- positive occupation identities;
- corrected one-fiber Robin classification;
- exact functional equation;
- local-uniform convergence to `xi`;
- fixed-zero `1/N` displacement;
- bounded-height reconnaissance as reconnaissance.

### 8.3 Why there is no contradiction with compact convergence

Local-uniform convergence controls every fixed compact set. It gives no information about zeros whose heights tend to infinity while `N` is fixed.

Thus all of the following can hold simultaneously:

```text
finite scans through a large but fixed height pass;
every fixed xi zero is approximated at rate 1/N;
the approximant satisfies an exact functional equation;
individual favorable Robin fibers are self-adjoint;
the complete finite approximant has infinitely many much higher off-line zeros.
```

### 8.4 Brownian routes that remain logically live

1. **Height-dependent truncation.** Choose `N=N(T)` and prove the required property only below height `T`, then use a diagonal argument as `T→∞`.
2. **Producer redesign.** Change the finite coefficient architecture so that no large family of almost-isolated independent prime phases can create a Bohr-torus zero.
3. **Direct infinite canonical system.** Construct the limiting canonical system or Hermite–Biehler object for `xi` directly rather than through globally stable finite Dirichlet-polynomial approximants.

PR #376 does not settle any of these three alternatives.

### 8.5 Relationship to RH

This is a strong negative result about one proof architecture. It is not evidence that RH is false, and it neither proves nor disproves RH.

Its principal scientific value is route selection: it prevents further work on an impossible all-large/cofinal finite-stability theorem and redirects Brownian work toward height-dependent, redesigned, or direct-infinite constructions.

## 9. Recommended repository dispositions

```text
finite gamma / Dirichlet / Hermite algebra             VERIFIED
small-N zero-free results                              VERIFIED
local-uniform convergence and fixed-zero displacement  VERIFIED
raw global all-large/cofinal stability                 FALSE
logarithmic Nörlund one-sided stability                 FALSE
current Nörlund finite-real-zero finish                 FALSE
current Green/Robin finite-real-zero finish             FALSE
height-dependent Brownian theorem                       OPEN
redesigned finite producer                              OPEN
direct infinite canonical system                        OPEN
Riemann Hypothesis                                      UNPROVED
```

Recommended integration actions:

1. integrate `L-90601`, `R-90601`, `L-90603`, `L-90604` and `R-90602` with the fixes listed above;
2. change the raw Brownian route DAG from an open zero-free theorem to a verified no-go;
3. remove the exact current finite Nörlund and Green/Robin real-zero producers from the live proof frontier;
4. preserve all finite algebra and compact-height results;
5. rewrite the Brownian research frontier around height-dependent truncation, producer redesign and direct infinite canonical systems;
6. keep RH status explicitly unproved and undisproved.
