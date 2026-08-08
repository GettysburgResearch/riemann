# L-26215 — The strict digital source tail is Sobolev-small in the common carry metric

Claim ID: `L-26215`  
Title: The signed strict-delay tail of every annular bank observation inherits the explicit binary-digit `H^1 -> L^2` decay without source substitution  
Status: **PROPOSED COMPLETE ANALYTIC ADAPTER PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `L-26213`, `L-26214`; PR #236 `L-23016`; PR #268 `L-26802/L-26804`  
Scope: fixed compact smoothing or declared Sobolev source domain; no estimate for the finite current feature, commutator boundary, or RH

## 1. The digital tail operator

For

\[
c_2(n)=1-v_2(n),
\]

define

\[
\mathcal T_Y
=\sum_{n\ge Y}\frac{c_2(n)}{\sqrt n}\tau_{\log n}.
\]

PR #236 `L-23016` proves, for every causal source in the declared Sobolev domain,

\[
\boxed{
\|\mathcal T_Yf\|_2
\le
\varepsilon_Y
\left(\|f\|_2+\|f'\|_2\right),
}
\tag{L-26215.1}

where one explicit choice satisfies

\[
\boxed{
\varepsilon_Y
=O\!\left({\log Y\over\sqrt Y}\right).
}
\tag{L-26215.2}

The same estimate holds on cumulative finite horizons with the declared upper endpoint collar.

## 2. Tail observation of an annular source

Let `x` be any finite annular coefficient sequence and let

\[
Q_x=h_\omega*\alpha_x
\]

be the compact opposite-parity physical signal of `L-26213`.

The coefficient tail is

\[
x_Y^{\rm tail}=c_{\ge Y}*x.
\]

By the exact source intertwiner `L-26213`,

\[
\boxed{
Q_{x_Y^{\rm tail}}
=\mathcal T_YQ_x.
}
\tag{L-26215.3}

Therefore (L-26215.1) gives

\[
\boxed{
\|Q_{c_{\ge Y}*x}\|_2
\le
\varepsilon_Y\|Q_x\|_{H^1_*},
}
\tag{L-26215.4}

where

\[
\|Q_x\|_{H^1_*}=\|Q_x\|_2+\|Q_x'\|_2.
\]

For the critical parity-filtered windows, the same statement holds componentwise because the finite translation filters commute with the digital tail and with the physical derivative.

## 3. Exact transfer to the carry source tail

The carry split of `Q_(c_>=Y*x)` has coefficient source

\[
\omega_2*(c_{\ge Y}*x),
\]

which is exactly the tail `T_(Y,M)` of `L-26214` for the RH-sensitive annular coefficient.

By the common weighted isometry `L-26213`, its complete weighted carry vector `V_tail` satisfies

\[
\boxed{
\|V_{\rm tail}\|_{\mathscr H_w}
=\|Q_{c_{\ge Y}*x}\|_2.
}
\tag{L-26215.5}

Combining (L-26215.4) and (L-26215.5),

\[
\boxed{
\|V_{\rm tail}\|_{\mathscr H_w}
\le
\varepsilon_Y\|Q_x\|_{H^1_*},
\qquad
\varepsilon_Y=O((\log Y)/\sqrt Y).
}
\tag{L-26215.6}

No absolute value is taken on the Möbius source, and no pole-blind source replaces `x`.

## 4. Uniform absorption in the critical hyperbola bank

In `L-26211`, every current prefix has length at least `N`. Hence every individual strict-prefix tail obeys

\[
\|V_{\rm tail}\|_{\mathscr H_w}
\le
\varepsilon_N\|Q_x\|_{H^1_*}.
\]

The production ledger must still recombine repeated product destinations before summing the bank. But once the exact synthesis weights are assembled in the common metric, every residual tail column carries the same vanishing Sobolev factor `epsilon_N`.

Thus the tail is no longer an unquantified RH-bearing source. The only unsuppressed current-scale object in each observation is the finite three-scale generalized-prime feature of `L-26214`, together with the explicit pole-preserving boundary/commutator channel.

## 5. Consequence for the remaining theorem

The annular banked source theorem may now be stated without a generic lower-scale tail hypothesis. It remains to prove a complete signed estimate for

```text
finite three-scale generalized-prime current feature
+
pole-preserving commutator and endpoint collars
+
recombined bank synthesis,
```

while the strict digital tail is an absorbable `o(1)` Sobolev perturbation.

A valid proof must use the complete synthesis ledger; multiplying `epsilon_N` by a total-variation bound for all synthesis coefficients may erase its decay and is not justified by this lemma.

## 6. Proof boundary

Closed, subject to review:

- exact identification of the coefficient tail with the physical digital-tail operator;
- the explicit `O((log Y)/sqrt Y)` Sobolev bound;
- exact transfer to the common weighted carry norm;
- uniform vanishing factor for every prefix in the critical hyperbola bank.

Open:

- signed recombination of all bank tails without a total-variation loss;
- the finite current-feature/boundary reserve;
- the annular recurrence;
- RH.
