# T-21706 — Corrected Brownian cardinal global criterion

Claim ID: `T-21706`  
Title: A global canonical-system or aggregate Hermite–Biehler theorem for the corrected Brownian length mixture would imply RH  
Status: **EXACT CONDITIONAL CRITERION — NO UNPROVED STEP ASSIGNED TO REVIEWERS**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #296 finite Nörlund convergence; `R-21703`, `L-21709`, `R-21704`, `L-21710`  
RH status: **unproved**

## 1. Correct finite approximants

Retain the finite logarithmic Nörlund approximants of PR #296:

\[
X_N(s)=\overline m_N(s)+\overline m_N(1-s).
\]

They satisfy the exact functional equation

\[
X_N(s)=X_N(1-s)
\]

and converge locally uniformly to `4xi(s)` in the closed critical strip at the stated logarithmic rate.

Put

\[
F_N(z)=X_N\left(\frac12+z\right).
\tag{T-21706.1}
\]

Then `F_N` is a real even entire function.

## 2. Correct cardinal representation

Let `overline T_N` be the positive tail of the finite Nörlund law in the normalization of PR #296. `R-21703` gives

\[
\boxed{
F_N(z)
=\frac12\int_{-\infty}^{\infty}
 e^{\ell/4}\overline T_N(e^\ell)
\Phi_\ell(z)d\ell,
}
\tag{T-21706.2}

where

\[
\Phi_\ell(z)
=\cosh\frac{\ell z}{2}
+2z\sinh\frac{\ell z}{2}.
\tag{T-21706.3}

The published `cosh+sinh/ell` fiber is withdrawn.

## 3. Local spectral information is insufficient

`L-21709` proves:

```text
ell>0   -> Phi_ell has only imaginary zeros;
ell<0   -> Phi_ell has exactly one real pair;
ell=0   -> Phi_ell=1.
```

`R-21703` proves that the finite tail necessarily has a dominant negative-length sector at sufficiently large reflected length, so pointwise reflected-tail domination is impossible.

Even after deleting every negative length, `R-21704` gives the exact counterexample

\[
\Phi_0+\frac1{10}\Phi_8,
\]

which has an off-axis zero by the first Newton coefficient inequality. Thus one-fiber self-adjointness and positivity of the length measure do not close the finite theorem.

## 4. Correct global theorem

Define **Brownian Aggregate Canonical Stability (`BACS`)** as either of the following equivalent production statements for an unbounded sequence `N_j`:

1. construct one regular or singular canonical system whose de Branges real part is `F_(N_j)`; or
2. construct an entire function `E_(N_j)` satisfying the Hermite–Biehler inequality
   \[
   |E_{N_j}(z)|>|E_{N_j}^{\#}(z)|
   \qquad(\operatorname{Im}z>0),
   \]
   and
   \[
   F_{N_j}(z)=\frac{E_{N_j}(z)+E_{N_j}^{\#}(z)}2;
   \]
3. equivalently, prove every Jensen polynomial of the even coefficient sequence of `F_(N_j)` is hyperbolic, with a uniform genus/order ledger sufficient for passage to the entire function.

The production object must concern the aggregate mixture itself. A direct integral of the one-fiber Robin problems is not accepted, because positive superposition is not real-rooted.

Under BACS, every zero of `F_(N_j)` lies on the imaginary axis. In the `s` variable every zero of `X_(N_j)` lies on `Re(s)=1/2`.

## 5. Conditional deduction to RH

Local uniform convergence

\[
X_{N_j}(s)\longrightarrow4\xi(s)
\]

and Hurwitz's theorem imply that every zero of `xi` in the open strip is a limit of zeros of `X_(N_j)`. Under BACS these approximating zeros lie on the critical line. Hence

\[
\boxed{
\mathrm{BACS}\Longrightarrow\mathrm{RH}.
}
\tag{T-21706.4}

This implication is complete conditionally.

## 6. Finite firewalls

Before a claimed BACS proof is accepted, it must reproduce:

```text
centered evenness of the corrected fiber;
the unique real pair for each negative length;
failure of finite reflected-tail domination;
R-21704 positive-fiber-cone counterexample;
all length-moment Newton/Jensen inequalities of L-21710;
the raw-truncation off-line mutation already recorded on PR #296.
```

## 7. Why this is not a completed proof

No aggregate canonical system, Hermite–Biehler function, or all-order Jensen hierarchy is constructed here. The theorem is retained as a precise global criterion, not as a task assigned to reviewers.

The present branch's completed contribution is the correction and refutation of the local Robin route. RH remains unproved.

## 8. Exact status

```text
finite Brownian/gamma/Norlund algebra       RETAINED
published cardinal Robin formula            FALSE
correct cardinal fiber                      PROVED
one-fiber Robin classification              PROVED
finite reflected-tail domination            FALSE
positive-fiber mixture closure              FALSE
aggregate BACS theorem                      OPEN / RH-BEARING
BACS -> RH                                  COMPLETE CONDITIONAL
Riemann Hypothesis                          UNPROVEN
```