# T-107200 Xi Cauchy-layer and saddle execution — five-minute handoff

Status: **new exact reverse–Rolle defect measure and unconditional growing-window Xi derivative entry; fixed-low-order \(90\%\) estimate open**

Base:

```text
PR #767
research/gpt56-pro/107100-xi-reverse-rolle-execution
cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57
```

Read in order:

1. `claims/lemmas/L-107200-cauchy-layer-represents-reverse-rolle-defect.md`
2. `claims/lemmas/L-107201-logarithmic-curvature-transport-under-differentiation.md`
3. `claims/lemmas/L-107202-xi-positive-frequency-saddle-concentration.md`
4. `claims/theorems/T-107200-xi-growing-window-entry-and-cauchy-defect-frontier.md`
5. `claims/refutations/R-107200-unscreened-curvature-mass-is-not-a-count.md`
6. `experiments/X-107200-xi-cauchy-saddle/README.md`

## Exact new real/complex bridge

For \(r=f'/f\), \(Q_f=-r'\), and a regular compact interval \(I\), define

\[
\mathcal C_{\varepsilon,I}(f)
=
\frac1\pi
\int_{I\setminus Z(f)}
\frac{\varepsilon (r')_+}{r^2+\varepsilon^2}\,dx
=
\frac1\pi
\int
\frac{\varepsilon (Q_f)_-}{r^2+\varepsilon^2}\,dx.
\]

If a nonshared zero of \(f'\) has multiplicity \(m_c\), then

\[
\mathfrak R_I(f)
=
\sum_c(m_c-1)
+
2\lim_{\varepsilon\downarrow0}\mathcal C_{\varepsilon,I}(f).
\]

Thus the exact multiplicity-sensitive reverse–Rolle defect of PR #767 is a
Cauchy-screened negative-curvature measure. No externally chosen depth or
separation threshold is needed.

## Unconditional Xi saddle entry

Let

\[
d\nu_m(u)
=
\frac{u^m\Phi_\Xi(u)\,du}
     {\int_0^\infty u^m\Phi_\Xi(u)\,du},
\qquad u>0.
\]

Using the literal standard Xi kernel and its first-theta-orbit bounds, the
packet proves a unique saddle \(w_m\) and natural width \(a_m\) with

\[
w_m=\tfrac12\log\frac{m}{\log m}+O(1),
\qquad
a_m^2\asymp\frac{\log m}{m},
\]

and the uniform concentration

\[
\nu_m(|u-w_m|>A a_m)\le C e^{-cA^2}.
\]

Combined with `L-107102`, every sufficiently high derivative
\(\Xi^{(m)}\) has only simple real zeros in

\[
|\Re z|\le c\sqrt{\frac m{\log m}},
\qquad
|\Im z|\le\frac12.
\]

This closes `XISADDLE107110`.

## Honest \(90\%\) frontier

For the five adjacent rungs \(F_k=\Xi^{(k)}\), put

\[
\mathcal E_5(T)
=
\sum_{k=0}^{4}
\lim_{\varepsilon\downarrow0}
\mathcal C_{\varepsilon,[T,2T]}(F_k),
\]

with the declared multiplicity, common-zero and endpoint ledger
\(\mathcal M_5(T)\). Then exactly

\[
R_0(T,2T)
=
R_5(T,2T)
-
2\mathcal E_5(T)
-
\mathcal M_5(T)
+
O(1).
\]

Hence the pinned \(R_5/N>997/1000-o(1)\) input would yield \(>90\%\) from

\[
\limsup
\frac{2\mathcal E_5+\mathcal M_5}{N}
<
\frac{97}{1000}.
\]

The packet does **not** prove that Xi-specific screened-curvature estimate.

```text
Cauchy-layer defect identity                    PROVED EXACT
derivative curvature-flux identity              PROVED EXACT
Xi growing-window saddle concentration          PROVED ANALYTICALLY
XISADDLE107110                                   CLOSED
fixed-low-order screened-curvature estimate     OPEN
more than 90 percent                            UNPROVED
density one / RH                                UNPROVED
```
