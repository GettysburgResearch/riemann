# O-15403 — After terminal closure, the balanced sector retains the full Möbius exponent

Observation ID: `O-15403`  
Title: The fixed-logarithm Heath–Brown Möbius slice cannot be hidden in the exponentially small terminal family  
Status: **EXACT CONSEQUENCE OF THE PACKET DECODER PLUS TERMINAL CLOSURE**  
Review base: PR #165 at `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0`  
Dependencies: PR #158 `L-15159/T-15123/R-15114`; `L-15449`; corrected terminal partition `L-15451`  
Scope: sharpens the location of the remaining RH-bearing arithmetic theorem

## 1. Exact Möbius slice

PR #158 proves that the signed Heath–Brown coefficient before the logarithmic factor reconstructs `mu` coefficientwise through the full finite endpoint. Fixing the logarithmic variable at a positive integer `q_0` leaves exactly

\[
\mu(m)\log q_0.
\]

For `q_0=2`, the corresponding compact-window signal is a fixed translate and nonzero scalar multiple of the Möbius safe signal.

Its cumulative energy has exact rightmost-zero exponent. In particular,

\[
E_{\mu,H}(J)=e^{o(J)}
\]

at the critical safe-window scale is RH-equivalent.

## 2. Finite packetization cannot erase that exponent

For fixed identity order `K`, decompose the fixed-`q_0` slice into the finite destination family. Write the block Hilbert vectors as

\[
h_{\mu,q_0}(J)
=h_{\mathrm{term}}(J)
+\sum_{\tau\in\mathfrak B_K}h_\tau(J),
\]

where `mathfrak B_K` is the balanced destination set after corrected terminal closure.

By the triangle inequality,

\[
\sum_{\tau\in\mathfrak B_K}\|h_\tau(J)\|
\ge
\bigl(\|h_{\mu,q_0}(J)\|-\|h_{\mathrm{term}}(J)\|\bigr)_+.
\]

Therefore at least one balanced packet satisfies

\[
\boxed{
\max_{\tau\in\mathfrak B_K}E_{K,\tau}(J)
\ge
{\left(
\sqrt{E_{\mu,q_0}(J)}-
\sqrt{E_{\mathrm{term}}(J)}
\right)_+^2
\over |\mathfrak B_K|^2}.}
\tag{O-15403.1}
\]

This is simply finite-dimensional Hilbert-space geometry; no number-theoretic estimate is used.

## 3. Terminal energy is exponentially negligible

`L-15449` plus the corrected full-tuple partition `L-15451` gives, for any fixed `eta<1/2`,

\[
E_{\mathrm{term}}(J)
\le
\exp\left[-(1-2\eta-o_K(1))J\right].
\]

At the convenient choice `eta=1/4`,

\[
E_{\mathrm{term}}(J)
\le e^{-(1/2-o_K(1))J}.
\]

Thus the terminal family has strictly negative exponential rate and cannot carry any positive rightmost-zero exponent.

Combining this with (O-15403.1) shows that the maximum balanced-packet energy has the same upper exponential obstruction as the Möbius slice whenever that obstruction is positive.

## 4. Consequence for BTP(K)

The balanced packet theorem is therefore not merely the last remaining bookkeeping estimate. At least one balanced destination contains the full RH-bearing Möbius mode after terminal rows are removed.

A proof of BTP(K) must consequently establish genuine arithmetic cancellation strong enough to imply subexponential Möbius safe energy. High identity order, finite packetization, divisor counting, or a generic operator norm cannot by themselves make every balanced packet easier.

The sharp production target is:

```text
trace the fixed q_0=2 Möbius slice through the deterministic balanced partition;
identify its exact signed normal Gram;
prove a strict lower-scale recurrence for that source-specific packet;
verify that the recurrence survives the first-cell fixed-ratio Mertens mutation.
```

If that packet cannot be contracted, the global BTP(K) programme cannot close.

## 5. Why standard tensor splitting is insufficient

Suppose a balanced convolution is split into factor logarithmic scales

\[
\alpha J,\qquad\beta J,
\qquad\alpha+\beta\approx1.
\]

A naive tensor estimate of the form

\[
E_{\rm parent}(J)
\lesssim e^{o(J)}E_1(\alpha J)E_2(\beta J)
\]

has total tensor exponent

\[
\kappa=\alpha+\beta=1,
\]

not a strict contraction `kappa<1`. Thus physical factor splitting alone does not prove BTP(K). A successful argument needs an actual arithmetic saving, a fractional-energy exponent, or an exact positive term moved to the opposite side of a source identity.

## 6. Correct frontier

After the terminal repair, the durable frontier is

\[
\boxed{
\text{signed source-specific balanced contraction}
\Longleftrightarrow
\text{the remaining RH-bearing arithmetic step in this architecture}.}
\]

This does not make BTP(K) impossible. It identifies where a genuine breakthrough must occur and provides a mandatory scalar audit for every proposed contraction.
