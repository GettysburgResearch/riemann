# T-107200 — Xi growing-window entry and the exact Cauchy-defect frontier

Claim ID: `T-107200`  
Status: **UNCONDITIONAL HIGH-DERIVATIVE ENTRY AND EXACT LOW-ORDER REDUCTION; \(90\%\) OPEN**  
Created: 2026-08-30  
Depends on: `L-107100--L-107102`, `L-107200--L-107202`,
`R-107200`  
RH status: **unproved**

## 1. Closed high-derivative target

`L-107202` proves the saddle estimate requested by `T-107110`.  There are
absolute constants \(c,m_0>0\) such that every \(m\ge m_0\) satisfies

\[
\boxed{
\Xi^{(m)}(z)=0,\quad
|\Re z|\le c\sqrt{\frac m{\log m}},
\quad
|\Im z|\le\frac12
\Longrightarrow
z\in\mathbb R
\text{ and the zero is simple}.
}
\tag{T-107200.1}
\]

Thus the growing-window high-derivative entry is unconditional.

## 2. Exact low-order quantity

For \(F_k=\Xi^{(k)}\), define

\[
r_k=\frac{F_{k+1}}{F_k},
\qquad
Q_k=-r_k',
\]

and

\[
\mathscr C_{k,\varepsilon}(T)
=
\frac1\pi
\int_T^{2T}
\frac{\varepsilon(Q_k)_-}{r_k^2+\varepsilon^2}\,dt.
\tag{T-107200.2}
\]

With multiplicity, common-zero and endpoint events collected in the exact
regularization ledger \(\mathscr M_5(T)\),

\[
\boxed{
R_0(T,2T)
=
R_5(T,2T)
-
2\sum_{k=0}^{4}
 \lim_{\varepsilon\downarrow0}\mathscr C_{k,\varepsilon}(T)
-
\mathscr M_5(T)
+
O(1).
}
\tag{T-107200.3}
\]

This is an equality, not a positive transport majorant.  Each integral
counts only the upward logarithmic-derivative crossings that destroy a
Rolle return.

## 3. The \(90\%\) gate

Assume the source-locked fifth-derivative input

\[
R_5(T,2T)
\ge
\left(\frac{997}{1000}-o(1)\right)N(T,2T).
\]

Then the Xi-specific theorem

\[
\boxed{
\limsup_{T\to\infty}
\frac{
2\sum_{k=0}^{4}
 \lim_{\varepsilon\downarrow0}\mathscr C_{k,\varepsilon}(T)
+\mathscr M_5(T)}
{N(T,2T)}
<
\frac{97}{1000}
}
\tag{T-107200.4}
\]

implies

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>
\frac9{10}.
}
\tag{T-107200.5}
\]

Name (T-107200.4) `XISCREEN107200`.

A finite-screening variant follows from `L-107200.7`: it is enough to prove
uniform critical-corridor transversality and the corresponding bound for a
declared \(\varepsilon_T\).

## 4. Why this is narrower than the former transport gates

The Cauchy layer:

- includes multiplicity and orientation exactly;
- is invariant under the natural simultaneous spatial/screening dilation;
- vanishes on ordinary downward Rolle extrema;
- does not pay favorable Hardy-space escape, omitted numerator subfactors or
  normal-equation error;
- uses the nonreal-pair curvature source from `L-107101` without replacing
  it by unscreened \(L^1\) mass.

The remaining input is nevertheless genuinely Xi-specific.  The dilation
firewall `R-107200` and the counterfamilies already present on PRs #731 and
#767 show that positive Fourier source and high-derivative real-rootedness
alone do not imply `XISCREEN107200`.

## Exact status

```text
multiplicity-sensitive real cascade                PROVED EXACT
Cauchy-screened continuous defect measure          PROVED EXACT
logarithmic curvature derivative flux              PROVED EXACT
Xi positive-frequency saddle concentration         PROVED
growing critical-strip high-derivative entry       PROVED
XISCREEN107200                                      OPEN / 90%-BEARING
more than 90 percent                               UNPROVED
density one / RH                                   UNPROVED
```
