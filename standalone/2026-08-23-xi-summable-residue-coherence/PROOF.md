# Summable residue coherence in the high Xi derivative tail

## 1. Setting

Use the positive Fourier representation

\[
\Xi(z)=2\int_0^\infty\Phi(u)\cos(zu)\,du
\]

and moments

\[
M_j=\int_0^\infty u^j\Phi(u)\,du.
\]

For `m>=1`, define

\[
\kappa_m^2={M_{m+1}\over M_{m-1}},
\qquad
\Delta_m=\Xi^{(m+1)}+\kappa_m^2\Xi^{(m-1)}.
\]

Under the tilted probability

\[
d\nu_{m-1}(u)=M_{m-1}^{-1}u^{m-1}\Phi(u)du,
\]

`kappa_m^2=E U^2`.

## 2. Exact centering

For the one-sided Fourier companion,

\[
\mathscr D_m(z)
=i^{m-1}M_{m-1}E[(\kappa_m^2-U^2)e^{izU}].
\]

Because `E(kappa_m^2-U^2)=0`,

\[
\mathscr D_m(z)
=i^{m-1}M_{m-1}
E[(\kappa_m^2-U^2)(e^{izU}-e^{iz\mu})],
\]

where `mu=EU`. Reflection recovers `Delta_m`.

For real `x`,

\[
|\Delta_m(x)|
\le2M_{m-1}|x|
E[|U^2-\kappa_m^2||U-\mu|].
\]

Write `V=U-mu`, `sigma^2=EV^2`. Then

\[
U^2-\kappa_m^2=2\mu V+(V^2-\sigma^2).
\]

The Laplace concentration already used for the high-derivative cosine theorem
gives

\[
\mu\asymp\log m,
\quad
\sigma^2\ll{\log m\over m},
\quad
E|V|^3\ll\left({\log m\over m}\right)^{3/2}.
\]

Therefore

\[
E[|U^2-\kappa_m^2||V|]
\ll {\log^2m\over m}
\asymp {\kappa_m^2\over m}.
\]

Since `M_(m-1)kappa_m^2=M_(m+1)`,

\[
|\Delta_m(x)|\ll M_{m+1}|x|/m.
\]

## 3. Residue carrier

Let `c` be a real zero of `Xi^(m)` in a fixed window. Uniform sine/cosine
localization gives

\[
|\Xi^{(m+1)}(c)|\gg M_{m+1}.
\]

The recurrence gives

\[
{\Xi^{(m-1)}(c)\over\Xi^{(m+1)}(c)}
=-\kappa_m^{-2}
+\kappa_m^{-2}{\Delta_m(c)\over\Xi^{(m+1)}(c)}.
\]

Thus

\[
\rho_{m,c}
=-{M_{m-1}\over M_{m+1}}(1+O_T(m^{-1})).
\]

## 4. Coherence squares the error

Normalize the residues as `rho_(m,c)=-a_m x_c`, where
`a_m=M_(m-1)/M_(m+1)` and `x_c=1+O_T(m^-1)`. Then

\[
C_m(T)
={\bigl(\sum x_c\bigr)^2\over R_m(T)\sum x_c^2}.
\]

The deficit is the normalized variance of the `x_c`. Hence

\[
1-C_m(T)=O_T(m^{-2}).
\]

The series of multiplicative coherence deficits converges, and

\[
\prod_{m=M}^N(2C_m(T)-1)
\ge\exp(-O_T(1/M)).
\]

## 5. Second-level debt

At a real zero `d` of `Xi^(m+1)`,

\[
\kappa_m^2\Xi^{(m-1)}(d)=\Delta_m(d),
\]

so

\[
|\Xi^{(m-1)}(d)|\ll M_{m-1}T/m.
\]

The two neighboring model derivatives are bounded below:

\[
|\Xi^{(m)}(d)|\gg M_m,
\qquad
|\Xi^{(m+2)}(d)|\gg M_{m+2}.
\]

Therefore

\[
\left|
{\Xi^{(m-1)}(d)^2\over
 \Xi^{(m)}(d)\Xi^{(m+2)}(d)}
\right|
\ll_T{1\over m^2}{M_{m-1}^2\over M_mM_{m+2}}.
\]

Moment log convexity converts this to

\[
O_T(a_m^2/m^2).
\]

After summing, the PR #723 cross-residue debt is an `O_T(m^-2)` fraction of
the real residue second moment.

## 6. Boundary

This proves that the high-order **multiplicative coherence channel** is summable. The additive endpoint term in the one-step count theorem is not summed; it remains on the exact endpoint/winding ledger. The result does not control the finite derivative prefix, that boundary charge as height grows, or RH.
