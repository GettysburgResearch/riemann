# T-102740 — Two SHARP rays cross the signed compact filter exactly

Claim ID: `T-102740`  
Status: **MAJOR UNCONDITIONAL FILTER-TRANSPORT ADVANCE; RH UNPROVED**  
Created: 2026-08-22  
Base: PR #719  
RH status: **unproved**

The signed dyadic filter

\[
P_2=(I-\sqrt2S_2)(I-S_2)^2
\]

does not preserve an arbitrary positive scalar or matrix cone.  That general
firewall remains binding.

`L-102725--L-102727` nevertheless prove that two fixed activation-zero SHARP
rays survive the filter on the literal native source.

## 1. Positive filtered carriers

For

\[
z=-1,\qquad z=-\frac12,
\]

the carriers

\[
K_z=P_2|4\sqrt y-3+z|^2\mathbf1_{y\ge1}
\]

are pointwise nonnegative.  Their exact piecewise formulas and derivative
signs are given in `L-102725`.

## 2. Global native prime budgets

The complete labelled child budgets, including the second `67` label, satisfy

\[
\sup_y\mathfrak b_{-1}(y)<0.874777,
\]

\[
\sup_y\mathfrak b_{-1/2}(y)<0.941359.
\]

The proof combines an analytic prime tail with exact finite cell certificates.
Adjacent-level greatest-owner pairing therefore gives

\[
\sum_n\frac{\beta(n)}{\sqrt n}K_z(X/n)\ge0
\]

for both rays and every scale.

## 3. Tangent transport through the filter

The completion tangent is a positive combination of multiplicative shifts of
the same native source.  Hence

\[
P_2Q_{\tau,-1}\ge0,
\qquad
P_2Q_{\tau,-1/2}\ge0.
\]

After the positive primitive `J` and the exact quadratic-boundary identity,
these become

\[
\boxed{P_2Q_\tau-5G_\tau\ge0,}
\]

and

\[
\boxed{P_2Q_\tau-4G_\tau-\frac34P_2a_\tau\ge0.}
\]

Thus the programme has crossed the signed compact filter on two nontrivial,
fixed, source-faithful rays.  This is strictly stronger than unfiltered SHARP
positivity and strictly weaker than full filtered Lorentz-cone transport.

## 4. Remaining exact gate

`R-102721` gives an exact algebraic fixture showing that the two inequalities
alone do not force

\[
5P_2a_\tau-G_\tau\ge0.
\]

The remaining theorem may now be stated more narrowly:

```text
FLC102740:
  supply one carrier-recombined lower control for the filtered wavelet current,
  compatible with the two proved upper rays and the single source-owned
  S-lemma slack.
```

Equivalently, prove that the missing lower direction is supplied by the
polarized cross-owner current or the centered completion envelope without
introducing a second reserve.

The conclusion chain remains

\[
\mathrm{FLC}_{102740}
\Longrightarrow
\mathrm{AR\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
\]

```text
filtered carrier z=-1                    PROVED POSITIVE
filtered carrier z=-1/2                  PROVED POSITIVE
complete labelled prime budgets          PROVED <1
native filtered observations             PROVED NONNEGATIVE
tangent filtered observations            PROVED NONNEGATIVE
two exact compact-current inequalities   PROVED
full filtered Lorentz cone                OPEN
FLC102740                                 OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
