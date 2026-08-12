# T-91501 — The prime Julia reserve absorbs the fixed-scale oscillatory long-jump channel

Claim ID: `T-91501`  
Status: **EXACT FIXED-SCALE OPERATOR DOMINATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91307`, `L-91502`, `T-91401`  
RH status: **unproved**

## 1. Two tail-Hankel channels

At the fixed safe scale

\[
a_0=4,
\qquad
\sigma_0=\frac92,
\]

let

\[
d\beta_4(u)
=4\sum_{n=p^k}\Lambda(n)n^{-9/2}
 \delta_{\log n}(du)
\]

be the ordinary-prime radial-score measure.  Its Hardy block is

\[
\mathsf H_{\beta_4}g(t)
=\int_{u>t}g(u-t)d\beta_4(u).
\]

After the plastic-cutoff normalization of `L-91502`, let

\[
d\lambda_4^-(u)=4u\,d\nu_{9/2}^-(u)
\]

be the complete negative oscillatory archimedean score measure, with Hardy
block `H_(lambda_4^-)`.

## 2. Uniform mass bounds

`L-91307` proves the exact rational estimate

\[
\boxed{
 m_4:=\beta_4((0,\infty))
 <\frac{85}{196}.
}
\tag{T-91501.1}
\]

`L-91502` proves

\[
\boxed{
 n_4:=\lambda_4^-((0,\infty))<\frac14.
}
\tag{T-91501.2}
\]

The tail-Hankel mass bound gives

\[
\mathsf H_{\beta_4}^*\mathsf H_{\beta_4}
\preceq m_4^2I,
\qquad
\mathsf H_{\lambda_4^-}^*\mathsf H_{\lambda_4^-}
\preceq n_4^2I.
\tag{T-91501.3}
\]

## 3. Prime Julia reserve

The explicit Julia dilation of `L-91307` is

\[
\|g\|^2
=\|\mathsf H_{\beta_4}g\|^2
 +\|D_0g\|^2+\|D_1g\|^2+\|D_2g\|^2.
\]

Define its positive defect operator

\[
\boxed{
\mathcal R_4^{\rm p}
:=I-\mathsf H_{\beta_4}^*\mathsf H_{\beta_4}
=D_0^*D_0+D_1^*D_1+D_2^*D_2.
}
\tag{T-91501.4}
\]

Then

\[
\mathcal R_4^{\rm p}
\succeq(1-m_4^2)I.
\tag{T-91501.5}
\]

## 4. Exact domination

The signed completed source carries the negative channel with coefficient four.
Combining (T-91501.1)--(T-91501.5),

\[
\begin{aligned}
\mathcal R_4^{\rm p}
-4\mathsf H_{\lambda_4^-}^*
  \mathsf H_{\lambda_4^-}
&\succeq
\left(1-m_4^2-4n_4^2\right)I\\
&\succ
\left[
1-\left(\frac{85}{196}\right)^2-\frac14
\right]I\\
&=
\boxed{
\frac{19751}{38416}I
}.
\end{aligned}
\tag{T-91501.6}
\]

Therefore

\[
\boxed{
\mathcal R_4^{\rm p}
\succeq
4\mathsf H_{\lambda_4^-}^*
 \mathsf H_{\lambda_4^-}
+rac{19751}{38416}I.
}
\tag{T-91501.7}
\]

The reserve is not close to saturation: more than one half of the ambient norm
remains after the complete oscillatory long-jump channel is paid.

## 5. Polarization and delays

Equation (T-91501.7) is an operator inequality, not a diagonal estimate.  It
therefore retains every cross term for any finite superposition of carrier
inputs.

If `g` is first passed through any common resident compressed-delay map, the
same inequality applies to the resulting vector.  Reflection gives the
anti-causal counterpart with the identical margin.  Thus the entire
infinite-dimensional oscillatory negative channel is closed simultaneously on
both Hardy orientations.

The theorem does not absorb the deterministic drift created by changing the
Lévy truncation to `kappa`, nor does it identify the finite bridge and
connection normalization.  Those finite ports must still be inserted in the
completed source lock.

## 6. Consequence for the fixed-scale programme

At `a=4`, the remaining signed-source problem is no longer an infinite
long-jump domination theorem.  It consists only of:

```text
the deterministic plastic-cutoff drift connection;
the finite bridge and gamma/pole placement;
the exact equality between the signed source form and the delayed screw/Weil Gram.
```

Once those finite/common-source identities are established, the negative
oscillatory channel is already paid with a strict uniform margin.

## 7. Exact boundary

```text
prime tail-Hankel Julia reserve                    EXACT
plastic-normalized negative tail-Hankel channel    EXACT
uniform domination with margin 19751/38416         EXACT
all carrier cross terms                            RETAINED
compressed-delay resident inputs                   RETAINED
opposite Hardy orientation                         RETAINED BY REFLECTION
deterministic drift/bridge source lock              OPEN
signed source = delayed screw Gram                  OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
