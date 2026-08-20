# T-100103 — Exact hostile disposition of DCE100100 and QPET100101

Claim ID: `T-100103`  
Status: **UNCONDITIONAL AUDIT THEOREM; RH UNPROVED**  
Created: 2026-08-20  
Depends on: `L-100101`; `L-100103--L-100104`; `R-100103`  
RH status: **unproved**

The two producer gates proposed in `T-100100--T-100101` have different final
dispositions.

## I. DCE100100

At every future-prime edge,

\[
C_p(Y)=C_{p^+}(Y)-p^{-1/2}C_{p^+}(Y/p).
\]

Therefore

\[
\boxed{
\mathrm{DCE}_{p,Y}
\iff C_p(Y)\ge0.
}
\tag{T-100103.1}

The proposed low-prime maximum principle is exactly the collection of signs it
was intended to produce. Moreover every fixed tail has the same
reciprocal-zeta poles up to a finite zero-free Euler factor, so eventual
nonnegativity of even one fixed tail is already conclusion-bearing.

Thus `DCE100100` is not proved by the terminal corridor or by the one-prime
kernel Harnack inequality. It remains a stronger pointwise sign formulation of
the critical arithmetic obstruction.

## II. QPET100101

For every fixed `k>=2`, the proved corridor implies

\[
\boxed{
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}\ge A_k^*.
}
\tag{T-100103.2}

The definition of `QPET100101` asks for the strict opposite inequality for one
`k`. Hence

\[
\boxed{
\mathrm{QPET100101}\text{ is false as stated}.
}
\tag{T-100103.3}

The residue-amplification theorem does not change this result. Inside the
positive corridor, the Euler-level upper bound forces the other poles and
contour terms to cancel any amplified selected residue at the same scale.

## III. Correct conclusion graph

```text
critical-carrier terminal corridor        PROVED
DCE edge = predecessor sign               PROVED
DCE100100                                 OPEN / CONCLUSION-BEARING

finite-completion positive corridor        PROVED
finite pole preservation/amplification     PROVED
QPET100101 strict-liminf gate              REFUTED
one-pole UPE dominance in corridor         REFUTED

Riemann Hypothesis                         UNPROVED
```

The finite-completion work remains a valid unconditional positivity corridor
and a useful spectral stress test, but it is not a second closure route in the
form stated. The viable arithmetic frontier is the critical source itself:
actual-prime activation/cross-core cancellation, or a genuinely noncircular
average estimate for its negative mass.

No theorem in this packet proves RH.
