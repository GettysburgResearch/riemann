# R-23402 — A bounded terminal endpoint count does not prove the balanced Type-II contraction

Claim ID: `R-23402`  
Title: The reflected Selberg square is exact, but the proposed `C_*/K` terminal exponent leaves the declared balanced packet family untouched  
Status: **PROPOSED SCOPE CORRECTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Targets: PR #226 `L-9517/T-9509`  
Dependencies: PR #226 `L-9516`; PR #233 `L-23206/L-23207`; `T-23401`

## 1. Exact component retained

The reflected coefficient identity of `L-9516` is a genuine algebraic advance. Subtracting the two individual Selberg identities from the conjugate-product identity gives

\[
2\left|\frac{\zeta'}\zeta(\sigma+it)\right|^2
=\mathcal C_\times-\mathcal C_+-\mathcal C_-.
\]

After multiplication by a nonnegative safe-window weight, the left side is the required Hermitian vertical energy. This corrects the earlier analytic-square mismatch `H(z)^2` versus `|H(z)|^2`.

The present refutation does not challenge that identity.

## 2. The source reduction has three outputs

The corrected Type-I source theorem `L-23206` sends each exact row to one of:

1. a balanced Type-II destination;
2. a same-scale Type-I row of strictly lower complexity;
3. a terminal row with one unrestricted lattice variable.

It proves that the reduced Type-I graph is acyclic and that the terminal family is exponentially small by Euler cancellation.

It states explicitly that the balanced destinations are **not estimated**.

The separate interface `L-23207` defines their energies and labels the all-order recurrence `BTP(K)` as open.

## 3. The invalid elimination step

`L-9517` says that a finite induction “removes the first two classes” and leaves only the terminal rows. The induction removes only the second class: the same-scale reduced Type-I rows.

A balanced row has two complete factor groups satisfying

\[
e^{\delta J-O_K(1)}
\le a,b\le
 e^{(1-\delta)J+O_K(1)},
\]

while their product remains at the original output scale. Knowing that each **factor** is below `(1-delta)J` does not identify the packet energy with an already controlled one-variable lower-scale energy.

The missing map is precisely the signed normal-Gram or tensor contraction required in `L-23207.5/L-23207.6`.

Therefore

\[
\boxed{
\text{terminal endpoint counting}
\not\Longrightarrow
BTP(K).}
\tag{R-23402.1}

## 4. Why `C_*` does not repair the omission

Suppose every recombined terminal face truly has at most an absolute number `C_*` of free endpoint coordinates. Then the terminal family has exponent at most `C_*/K`, or, using `L-23205/L-23206`, in fact decays exponentially.

This says nothing about the balanced packet vector, which is the sole family left open after terminal closure. Its coefficients retain the full Möbius/binomial signs and its energy is at the original product scale.

`L-23404` sharpens the location of this obstruction: after all macroscopic free-variable rows are Euler-closed, the hard source is concentrated in the top identity orders. It does not disappear.

## 5. First-cell mutation is not supplied

`L-9517` further asserts that the terminal estimate becomes a high-order fixed-ratio Mertens bound under the `q_0=2` slice. But the exact Möbius decoder on PR #158 says only that the **complete signed packet** contains that slice. It does not identify the slice with the terminal subfamily.

The one-prime barrier `R-23401` shows why: the first shell cannot be canceled by a terminal one-variable parity pairing. Its sign reversal is balanced.

Accordingly, a valid first-cell mutation must pass through the balanced certificate itself and prove the shell-energy bound of `T-23401`. A terminal bound alone cannot yield it.

## 6. Corrected status of the reflected proposal

The valid chain is

```text
reflected Selberg Hermitian identity                 exact/proposed complete
corrected Type-I complexity reduction                proposed complete
terminal lattice Euler closure                       proposed complete
balanced Type-II packet theorem BTP(K)               open
first-cell shell-energy mutation                      open
RH                                                    unproved
```

The reflected identity is a valuable input to a future proof of `BTP(K)`. It is not, without the missing source-specific contraction, a completed proof of `BTP(K)`.

## 7. Required repair

A corrected full proposal must provide one of:

1. an explicit reflected Selberg equation for the **entire balanced packet vector**, including all cross terms, whose positive square dominates its normal Gram;
2. a signed common-cell dispersion theorem proving `L-23207.5`;
3. a tensor recurrence proving `L-23207.6` with `epsilon_K/(1-kappa_K)->0`;
4. a direct proof of the minimal shell energy `E_(2/3,log 2)(J)=exp(o(J))`.

Every repair must export the first-cell source map and pass `X-23401`.

## 8. Proof boundary

This file is a dependency and quantifier audit. It does not refute the reflected Selberg identity or the possibility that a future coupled packet equation proves `BTP(K)`. It rejects only the inference that terminal endpoint counting has already done so.
