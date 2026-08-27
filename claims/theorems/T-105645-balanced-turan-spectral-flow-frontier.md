# T-105645 — Balanced Turán spectral flow joins the pointwise and endpoint programmes

Claim ID: `T-105645`  
Status: **MAJOR EXACT TWO-RUNG SYNTHESIS; SIGNED PHYSICAL ESTIMATE OPEN**  
Created: 2026-08-25  
Depends on: `T-105640`; `L-105643`; sibling `L-106400--L-106431`  
RH status: **unproved**

## 1. The parent and derivative atoms are one divisor

For a real entire `F`, define

\[
\mathcal L_F=F'^2-FF''.
\]

The exact identity

\[
\boxed{
{\mathcal L_F\over FF'}
=\partial_z\log{F\over F'}
}
\tag{T-105645.1}
\]

assigns residue `+m` to a parent zero of multiplicity `m` and residue `-n` to
a noncommon derivative zero of multiplicity `n`.

The height all-pass

\[
\mathcal R_{F,H}(x)
={F(x+iH)F'(x-iH)
 \over F(x-iH)F'(x+iH)}
\]

has degree

\[
\boxed{
\deg\mathcal R_{F,H}
=N_{F'}(H)-N_F(H),
}
\tag{T-105645.2}
\]

and continuous phase velocity

\[
\boxed{
\partial_H\arg\mathcal R_{F,H}(x)
=2\operatorname{Re}
{\mathcal L_F(x+iH)
 \over F(x+iH)F'(x+iH)}.
}
\tag{T-105645.3}
\]

Thus a parent Clark atom and a derivative anti-inner factor are not independent
debts.  They are opposite atoms of one signed Turán spectral flow.

## 2. First-contact source/index split

At one simple derivative crossing of depth `delta`, the exact adaptive-band law
is

\[
\boxed{
\begin{aligned}
\text{source-visible charge}
 &=|A(b)|^2(1-e^{-2\delta L}),\\
\text{signed endpoint charge}
 &=|A(b)|^2e^{-2\delta L}.
\end{aligned}
}
\tag{T-105645.4}
\]

A parent crossing has the same model-space law with the opposite divisor sign
inside `mathcal R_(F,H)`.  The complete parent-minus-derivative index is
therefore conserved while charge moves between:

```text
continuous actual Turan source;
finite source bank;
microscopic endpoint collar;
distributional zero-crossing atoms.
```

## 3. Revised physical target

The former separate gates

```text
PARENTATOM105640;
MICROCOLLAR105640;
ENDIDX105630;
raw shell-energy transfer;
```

are replaced, at the exact algebraic level, by one balanced statement:

```text
BSTF105645 — balanced signed Turan flow

On a cofinal family of regular Xi rectangles and adaptive source bands,
control the signed height integral of

  2 Re[(Xi'^2-Xi Xi'')/(Xi Xi')]

plus the exact source-band / endpoint-complement spectral-flow atoms, so that
its parent-minus-derivative index has no adverse uncompensated unit.
```

The numerator is the already-proved actual positive exterior-square source.
The denominator and all-pass phase remain physical and signed.  No frozen
carrier, surrogate numerator, absolute model-space coverage, or raw negative
Hardy energy appears in `BSTF105645`.

## 4. Interaction with reverse Rolle

Along a derivative ladder, the two-rung height indices telescope.  A terminal
fixed-width derivative with no off-line zeros leaves only:

```text
base parent index;
signed Turan flow across the intervening rungs;
one cofinal endpoint/common-zero ledger.
```

Consequently a sufficiently strong `BSTF105645`, together with the reviewed
terminal moving-saddle theorem, would close the low-order reverse-Rolle descent.
The exact quantitative threshold depends on whether the consumer is:

```text
pointwise:       zero adverse unit, yielding RH;
trace/topology:  total adverse charge below two, emptying a conjugate shell;
proportion:      the fixed signed-tail allowance of the endpoint programme.
```

## 5. What is now proved and what is not

```text
actual Xi Turan Fourier source positive             PROVED UNCONDITIONALLY
parent/derivative divisor identity                  PROVED EXACT
height all-pass parent-minus-derivative index       PROVED EXACT
continuous Turan phase generator                    PROVED EXACT
first-crossing source/index conservation            PROVED EXACT
fixed-band source-only descent                      REFUTED
BSTF105645 signed physical estimate                 OPEN / RH-BEARING
POINTID105630                                       OPEN / RH-BEARING
fixed-width moving-saddle endpoint                  PROPOSED / REVIEW
Riemann Hypothesis                                  UNPROVEN
```

## 6. Scope

This theorem reorganizes the remaining proof but does not estimate the signed
physical quotient.  A positive Fourier numerator does not control the phase of
`Xi Xi'`; the existing positive-source countermodels remain binding.  Multiple
crossings require the full confluent model-space matrix rather than scalar
addition.  RH remains unproved.
