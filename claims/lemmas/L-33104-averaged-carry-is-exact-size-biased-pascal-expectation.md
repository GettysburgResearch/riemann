# L-33104 — The averaged carry row is exactly a size-biased Pascal expectation

Claim ID: `L-33104`  
Title: The classical averaged carry coefficient is exactly the expectation of the atomized carry indicator under the finite `Beta(2,1)` Pascal split law  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Issue: #331  
Dependencies: PR #247 `L-23808`; `L-33102`  
Scope: exact finite carry/probability identification; no RH conclusion

## 1. Atomized and averaged carry rows

For integers `0<=j<=n` and `q>=2`, put

\[
\chi_{n,j}(q)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor
\in\{0,1\}.
\]

The standard row-averaged carry coefficient is

\[
\beta_{nq}=\frac1{n+1}\sum_{j=0}^n\chi_{n,j}(q).
\tag{L-33104.1}
\]

Equivalently, writing `n=aq+r`, `0<=r<q`, direct counting gives

\[
\beta_{nq}=\frac{a(q-1-r)}{n+1}.
\]

## 2. Exact size-biased split law

Define

\[
\pi_n(j)=\frac{2j}{n(n+1)},
\qquad 0\le j\le n.
\tag{L-33104.2}
\]

The weights are nonnegative and

\[
\sum_{j=0}^n\pi_n(j)=1.
\]

They are exactly the finite `Beta(2,1)` law of `L-33102`: choose a split uniformly and then follow a size-biased child.

The carry row is symmetric,

\[
\chi_{n,j}(q)=\chi_{n,n-j}(q).
\tag{L-33104.3}
\]

Hence

\[
\begin{aligned}
\sum_{j=0}^n j\chi_{n,j}(q)
&=\frac12\sum_{j=0}^n[j+(n-j)]\chi_{n,j}(q)\\
&=\frac n2\sum_{j=0}^n\chi_{n,j}(q).
\end{aligned}
\]

Multiplying by `2/[n(n+1)]` gives the exact identity

\[
\boxed{
\beta_{nq}
=\sum_{j=0}^n\pi_n(j)\chi_{n,j}(q).
}
\tag{L-33104.4}
\]

Thus the finite averaged carry matrix is already the atomized carry matrix averaged under the exact finite size-biased Pascal law. No limiting argument is required.

## 3. Continuum counterpart

For the atomized continuum carry indicator of PR #247,

\[
C(x,u)=\lfloor x\rfloor-\lfloor ux\rfloor-\lfloor(1-u)x\rfloor,
\]

one has `C(x,u)=C(x,1-u)`. Therefore

\[
\begin{aligned}
\int_0^1 2u C(x,u)\,du
&=\int_0^1 2(1-u)C(x,u)\,du\\
&=\int_0^1C(x,u)\,du.
\end{aligned}
\]

PR #247 identifies the last integral with the continuum carry kernel `K(x)`. Hence

\[
\boxed{
K(x)=\int_0^1 2u\,C(x,u)\,du.
}
\tag{L-33104.5}
\]

The same `Beta(2,1)` law therefore represents the carry average at finite and continuum scale.

## 4. Finite logarithmic-loss state

Under `pi_n`, put `V_n=J/n` on `J>=1`. For every bounded function `f`,

\[
\mathbb E f(V_n)=\sum_{j=1}^n\frac{2j}{n(n+1)}f(j/n).
\]

As `n->infinity` these Riemann sums converge to

\[
\int_0^1 2u f(u)\,du,
\]

so `V_n` converges to `Beta(2,1)`. In particular the two-step logarithmic state used in `L-33101/L-33102` is the scaling limit of two exact finite atomized-carry split coordinates, while (L-33104.4) says each one-step carry column already averages against that same law.

## 5. Consequence for the Martingale Pascal Lift

The remaining finite lift cannot be dismissed as a mismatch between the continuum probability law and the discrete carry matrix. The probability measure is literally a row measure of that matrix.

A production MPL may therefore work at the atomized split level:

```text
size-biased Pascal split law pi_n
-> exact atomized carry expectation beta_nq
-> two-step Pascal logarithmic state
-> centered carry/Gamma martingale
-> Pascal four-cycle recombination
-> optimized capacity debt.
```

What remains nontrivial is the martingale/cycle realization and the critical square-root source pairing. This lemma does not claim either is automatic.

## 6. Proof boundary

Established exactly:

1. the size-biased probability weights `pi_n`;
2. the finite identity `beta=E_pi chi` for every carry column;
3. the continuum identity `K=int 2u C du`;
4. convergence of the finite split state to the `Beta(2,1)` state.

Open:

1. a finite martingale coupling compatible with all carry columns simultaneously;
2. a subpower Cycle-Debt theorem;
3. RH.
