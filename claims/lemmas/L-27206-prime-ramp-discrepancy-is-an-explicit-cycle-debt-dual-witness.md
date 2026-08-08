# L-27206 — The prime-ramp discrepancy is an explicit Cycle Debt dual witness

Claim ID: `L-27206`  
Title: The entropy-minus-all-integer carry potential yields two feasible bounded-superadditive dual certificates, so a false-RH scalar mode cannot disappear inside cycle optimization  
Status: **PROPOSED EXACT CONSEQUENCE OF `L-27203` AND `L-27205`**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27203`, `L-27205`  
Scope: source-firewall and quantitative duality; no RH assumption

## 1. Three node potentials

For `1<=n<=X`, define

\[
\mathcal L(n)=\log(n!),
\tag{L-27206.1}
\]

\[
\mathcal C(n)
=\sum_{q=2}^{n}\left\lfloor\frac nq\right\rfloor,
\tag{L-27206.2}
\]

and

\[
\mathcal G(n)
=\sum_{q=2}^{n}\frac1{\sqrt q}
 \left\lfloor\frac nq\right\rfloor.
\tag{L-27206.3}
\]

For an eta-balanced split `e=(n,j)`, with `k=n-j`, their split defects are

\[
\partial^*\mathcal L(e)
=\log\binom nj=:\ell_e,
\tag{L-27206.4}
\]

\[
\partial^*\mathcal C(e)
=\sum_{q=2}^{n}\chi_e(q)=:c_e,
\tag{L-27206.5}
\]

and

\[
\boxed{
\partial^*\mathcal G(e)
=\sum_{q=2}^{n}\frac{\chi_e(q)}{\sqrt q}
=\omega_e.}
\tag{L-27206.6}
\]

Put

\[
\mathcal H=\mathcal L-\mathcal C.
\tag{L-27206.7}
\]

Then

\[
\partial^*\mathcal H(e)=\ell_e-c_e.
\tag{L-27206.8}
\]

## 2. Feasible dual potentials

By `L-27203` and the capacity lower bound of `L-27205`, there is a constant
`A_eta>=1` such that

\[
|\partial^*\mathcal H(e)|
\le A_\eta\omega_e
\tag{L-27206.9}
\]

on every eta-balanced split.

Define

\[
\boxed{
F_\pm
=\frac12
\left(
\mathcal G\pm A_\eta^{-1}\mathcal H
\right).}
\tag{L-27206.10}
\]

Then

\[
\boxed{
0\le\partial^*F_\pm(e)\le\omega_e}
\tag{L-27206.11}
\]

for every allowed edge. Hence both `F_+` and `F_-` are feasible potentials in
the exact dual programme `L-27205.13`--`L-27205.14`.

## 3. Exact pairings with the Möbius target

Let `r_X=r^(w_X)` be the exact target divergence. Since pairing a node
potential with `r_X` equals pairing its split defect with any exact target flow,

\[
\boxed{
\langle r_X,\mathcal G\rangle
=K_X
:=\sum_{q=2}^{X}\frac{\log(X/q)}q.}
\tag{L-27206.12}
\]

Likewise,

\[
\boxed{
\langle r_X,\mathcal H\rangle
=P_X-W_X,}
\tag{L-27206.13}
\]

where

\[
P_X
=\sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a}
\]

is the complete prime-power ramp and

\[
W_X
=\sum_{q=2}^{X}q^{-1/2}\log(X/q)
\]

is the all-integer reference ramp.

## 4. Quantitative firewall

Apply the dual formula of `L-27205` to `F_+` and `F_-`. We obtain

\[
\mathfrak N_\eta(X)
\ge
\max\left(
0,
-\frac{K_X}{2}
+\frac{|P_X-W_X|}{2A_\eta}
\right).
\tag{L-27206.14}
\]

Equivalently,

\[
\boxed{
|P_X-W_X|
\le
A_\eta\bigl(K_X+2\mathfrak N_\eta(X)\bigr).}
\tag{L-27206.15}
\]

This is the optimized form of the primal entropy estimate in `L-27205`; the
same inequality is witnessed on the dual side by two explicit source
potentials.

## 5. Consequences

1. A subpower Cycle Debt theorem necessarily controls the actual coherent
   prime/Möbius scalar mode. It cannot succeed by sending that mode into an
   uncharged cycle direction.
2. Any polynomial-size prime-ramp discrepancy forces polynomial-size optimized
   debt along the same endpoints, up to the polylogarithmic baseline `K_X`.
3. The directed ternary mutation is not the only firewall. The exact scalar
   prime-ramp discrepancy is itself a legal dual mutation of every cycle
   certificate.
4. A numerical small-debt ladder which does not replay `F_+` and `F_-` has not
   authenticated the RH-bearing coordinate.

## 6. Proof boundary

This lemma proves an exact primal/dual compatibility and source firewall. It
does not bound `mathfrak N_eta(X)`, prove CDT, or prove RH.
