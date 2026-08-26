# L-106112 — The principal atomic diagonal is paid and the equal-pair owner amplifier is one Wick square

Claim ID: `L-106112`  
Programme aliases: `LFAM1.PRINCIPAL_ATOMIC_DIAGONAL`, `LFAM2.OWNER_WICK_SQUARE`, `STRESS.SEMIPRIME_AMPLIFIER_FACTORIZATION`  
Status: **CORRECTED: PRINCIPAL ATOMIC BOUND PROVED; COMPLETE-FAMILY ATOMIC CLAIM RETRACTED BY `R-106131`; OWNER ALGEBRA RETAINED EXACT**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106110--L-106111`; parent `L-102746--L-102748`, `L-102962--L-102963`; `R-106131`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Expand the dual-amplified family in complete source atoms. One ordered
least-discrepancy interaction has literal coefficient

\[
z_\omega(t)
=
\frac{\gamma_\omega(t)}
{g^2cd\sqrt{PQ}},
\qquad
|\gamma_\omega(t)|\le X^{o(1)}.
\tag{L-106112.1}
\]

## Binding atomic correction

For an odd conductor `ell`, the total even-character weight is `ell-1`.
Therefore the atomic contribution to the complete moment `mathfrak M_DA` is

\[
\boxed{
g^2\ell(\ell-1)|z_\omega(t)|^2,
}
\tag{L-106112.2}
\]

not `g^2 ell |z_omega|^2`.

The latter scale is the principal/quadratic-root atomic channel only. Its
exact coefficient is

\[
g^2\ell\,c_\ell |z_\omega(t)|^2,
\qquad
c_\ell=\frac{\ell+1}{\ell-1}\le2.
\tag{L-106112.3}
\]

Since `ell<=c`,

\[
g^2\ell c_\ell |z_\omega(t)|^2
\ll
X^{o(1)}
\frac1{g^2cd^2PQ}.
\]

The finite source sums

\[
\sum_g\frac1{g^2}<\infty,
\qquad
\sum_c\frac1c\ll\log Y,
\qquad
\sum_d\frac1{d^2}<\infty,
\qquad
\sum_P\frac1P,\ \sum_Q\frac1Q
\ll(\log\log(3Y))^2
\]

and the compact Mellin kernel give

\[
\boxed{
\mathfrak M_{\rm DA}^{\rm principal\ atomic}(Y)=Y^{o(1)}.
}
\tag{L-106112.4}
\]

No bound for the complete uncentered nonprincipal atomic trace follows from
this calculation. Its omitted weight is

\[
\nu_\ell=\frac{\ell(\ell-3)}{\ell-1}.
\]

The exact full correction is `R-106131`; Wick normal ordering is `L-106131`.

## Equal-pair owner factorization

Fix one reduced core `d`, an allowed finite prime-label set `mathcal P`, a
complex character `chi`, and a Mellin parameter `s`. Put

\[
\mathcal P_{\chi,d}(s)
=
\sum_{\substack{p\in\mathcal P\\p\nmid d}}
\frac{\chi(p)}{p^s},
\qquad
\mathcal D_{\chi,d}(s)
=
\sum_{\substack{p\in\mathcal P\\p\nmid d}}
\frac{\chi(p)^2}{p^{2s}}.
\]

Then coefficientwise in the labelled prime algebra,

\[
\boxed{
\sum_{\substack{p<q\\p,q\in\mathcal P\\(pq,d)=1}}
\frac{\chi(pq)}{(pq)^s}
=
\frac12
\left[
\mathcal P_{\chi,d}(s)^2
-
\mathcal D_{\chi,d}(s)
\right].
}
\tag{L-106112.5}
\]

The canonical equal-pair Duhamel allocation factor is independent of the
selected unordered pair and multiplies both sides unchanged. Finite shell
projection is linear, and owner/core exclusions merely delete corresponding
prime terms.

The diagonal `mathcal D_(chi,d)` consists of repeated owner labels and
prime-square activity and remains in the inherited closed ledger. Hence the
nontrivial owner amplifier is

\[
\boxed{
\frac12\mathcal P_{\chi,d}(s)^2
}
\tag{L-106112.6}
\]

modulo that closed field.

## Correct scope

```text
principal atomic diagonal                         PROVED SUBPOWER
complete M_DA atomic diagonal                     NOT PROVED
owner Wick factorization                          PROVED EXACT
repeated-owner diagonal                           INHERITED CLOSED
uncentered nonprincipal family moment             OPEN / NOT A REQUIRED GATE
```

The preferred repaired family composition is `T-106140`.
