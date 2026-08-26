# R-105500 — The QPTI semiprime main does not transfer to the balanced F1 source

Claim ID: `R-105500`

Status: **BINDING SOURCE-DISAMBIGUATION FIREWALL**

Created: 2026-08-27

Depends on: PR #730 `L-105462`, `T-105490`; corrected PR #719
`L-103120--L-103121`, `R-103121`, `T-103130`; native Vaughan identity
`L-100311`

RH status: **not assumed; RH remains unproved**

Corrected PR #719 proves a power-sized negative semiprime main for the
completed harmonic Euler–Beta source.  That result invalidates the former
`QPTI103112` producer and every implication which silently identifies it with
the balanced Boolean/F1 source.  It does **not**, by itself, prove that the
cutoff-dependent balanced source on PR #730 has the same main.

This distinction is load-bearing.

## 1. The refuted harmonic completion

The literal QPTI source of `L-103120` has physical atoms

\[
N=pq\,c^2
\]

with coefficient

\[
\frac{\mu(c)}
{\binom{\omega(c)+2}{2}\sqrt{pq}\,c}.
\tag{R-105500.1}
\]

After the root and first-chaos core rows are removed, `R-103121` proves

\[
\boxed{
H_{\rm EB}(X)
=
-C_0\sqrt X\frac{\log\log X}{\log X}(1+o(1)),
\qquad C_0>0.
}
\tag{R-105500.2}
\]

Hence `QPTI103112` and `EBD103120` are false as stated, and the former
completed-source chain

```text
QPTI103112 <=> BCI102990 <=> HMO102940
```

is withdrawn.

## 2. The balanced F1 source has a different core coefficient

The configuration square of `L-105462` is built from the balanced Boolean
coefficient

\[
b_U=a_U*a_U*\mu,
\qquad
a_U=\varepsilon-\mu_U*\mathbf1,
\tag{R-105500.3}
\]

not from the fixed harmonic coefficient \(\mu\).  Its equal-pair physical
atom has the same *shape* \(pq\,c^2\), but coefficient

\[
\frac{b_U(c)}
{\binom{\omega(c)+2}{2}\sqrt{pq}\,c}.
\tag{R-105500.4}
\]

Shape equality is not source equality.

`L-105501` proves

\[
b_U=a_U*\nu_U,
\qquad
\nu_U=\bigl(\mu(n)\mathbf1_{n>U}\bigr),
\tag{R-105500.5}
\]

and both factors vanish on \(n\le U\).  Consequently

\[
\boxed{b_U(c)=0\qquad(c\le U^2).}
\tag{R-105500.6}
\]

The fixed-core density responsible for (R-105500.2) is therefore absent from
every cofinal balanced block.  The proof of `R-103121` cannot be copied with
\(\mu(c)\) silently replaced by \(b_U(c)\).

## 3. Exact disposition

The semiprime audit proves:

```text
harmonic Euler–Beta completion QPTI103112          REFUTED;
EBD103120                                           REFUTED;
QPTI/BCI/HMO completed-source equivalence           WITHDRAWN;
any PR #730 arrow relying only on that equivalence  WITHDRAWN.
```

It does **not** prove:

```text
the balanced b_U F1 current has the same semiprime main;
the generic cell/Gram identities are false;
the cutoff-dependent balanced Hodge gate is false.
```

Those statements remain separate mathematical questions.

## 4. Required source-safe repair

A conclusion-facing route must now be proved directly from the native
ordinary-Möbius scalar, without using the refuted harmonic completion as an
intermediate source.  `L-105501--L-105504` do this:

```text
native Möbius wavelet
  = integrable Type-I row
    + exact balanced tail-pair row;

balanced tail-pair row
  = differential cross-Hodge mismatch of two long native fields.
```

This yields the independent RH-equivalent frontier `T-105500`.
