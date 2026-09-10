# Poincare-frame endpoint ladder — Part I: source frame, saturation, and exact centers

**Status:** proposed source-specific analytic theorem; independent proof review required.  
**Parent source:** PR #766 at `17c7624a0bd56c5356d00278b2a846d2efdbdccc`.  
**Repository effect:** proof/exposition only; no producer, fixture, or inherited certificate is modified.  
**RH/GRH:** RH and GRH remain unproved.

This packet replaces the growing Miller-echelon constants by the exact
source-normalized Poincare coefficient frame already constructed in PR #766.
The resulting theorem reaches the natural endpoint range

\[
\boxed{L(k)\log(k+2)=o(k)}
\tag{PF0}
\]

for the **existence and simplicity of every recentered determinant cluster**.
Strict zero--pole separation is a separate coupling question; it is treated
in Part II and in `CRITICAL_DIVISOR_RENEWAL_TRANSITION.md`.

---

## 1. Source objects

Retain the level-one cusp space `S_k`, Petersson form `G`, coefficient flag

\[
W_i=\{f:a_f(1)=\cdots=a_f(i-1)=0\},
\]

completed Eisenstein period `I(s)`, determinants

\[
D_i(s)=\det I(s)|_{W_i},
\qquad
Q_i(s)=D_i(s)/D_{i+1}(s),
\]

and endpoint coordinate

\[
c=k(1-s).
\]

Put

\[
A_n=A_n(k)=\frac{\Gamma(k-1)}{(4\pi n)^{k-1}}.
\tag{PF1}
\]

Let `P_n` be the ordinary holomorphic Poincare series reproducing the
`n`-th coefficient:

\[
G(P_n,f)=A_n a_f(n).
\tag{PF2}
\]

Set

\[
v_n=P_n/\sqrt{A_n}.
\]

For `1<=m,n<=M`, the exact Gram matrix is

\[
K^{(M)}_{mn}=G(v_m,v_n)
=\delta_{mn}
+2\pi i^k\sum_{q\ge1}\frac{S(m,n;q)}q
J_{k-1}\!\left(\frac{4\pi\sqrt{mn}}q\right).
\tag{PF3}
\]

This is the source-normalized coefficient kernel proved in the proper
Theta-source packet. No basis is chosen after observing the period.

---

## 2. Uniform Gram closeness up to twice the target depth

Let `L=L(k)` satisfy PF0 and put

\[
M=2L.
\]

For large `k`, `M<dim S_k` and `k>=96M`. The parent Petersson/Bessel estimate
gives

\[
\delta_{k,M}:=\|K^{(M)}-I\|_{op}
\le
4\pi M\frac{(2\pi M)^{k-1}}{(k-1)!}
\exp\!\left(\frac{4\pi^2M^2}{k}\right).
\tag{PF4}
\]

Stirling yields, uniformly under PF0,

\[
\delta_{k,M}
\le
\exp\!\left[-c k\log\frac{k}{C M}\right]
\tag{PF5}
\]

for absolute positive `c,C` and all sufficiently large `k`. In particular,
`delta_{k,M}` is smaller than every fixed negative power of `k` and `L`.

The full coefficient block is therefore independent, and

\[
\|(K^{(M)})^{-1}-I\|_{op}\le2\delta_{k,M}.
\tag{PF6}
\]

---

## 3. Exact Gram-dual coefficient lifts

For `1<=l<=M`, define

\[
w_l
=
\sqrt{A_l}\sum_{n=1}^{M}(K^{(M)})^{-1}_{nl}v_n.
\tag{PF7}
\]

Then, exactly,

\[
a_{w_l}(m)=\delta_{lm}
\qquad(1\le m\le M).
\tag{PF8}
\]

Indeed

\[
G(v_m,w_l)
=
\sqrt{A_l}\delta_{ml}
=
\sqrt{A_m}a_{w_l}(m).
\]

Moreover

\[
G(w_l,w_m)
=
\sqrt{A_lA_m}(K^{(M)})^{-1}_{lm},
\tag{PF9}
\]

so

\[
G(w_l)=A_l(1+O(\delta_{k,M})).
\tag{PF10}
\]

The vectors `w_l` are the unique minimum-Petersson-norm lifts of the first
`M` coefficient constraints. They satisfy the exact orthogonal decomposition

\[
S_k=\operatorname{span}\{w_1,\ldots,w_M\}
\mathbin{\perp_G}W_{M+1}.
\tag{PF11}
\]

Thus every elimination below is induced by the authenticated coefficient
source. It is not a free linear projector.

---

## 4. Energy saturation and complete tail control

Choose

\[
Y=\frac{k}{10000M}.
\tag{PF12}
\]

For large `k`, `Y>=1`, so the domain above `Y` is the full width-one cusp
rectangle. For every `l<=M`, the pure leading mode contributes

\[
A_l^{(Y)}
=
\int_Y^\infty y^{k-2}e^{-4\pi l y}\,dy
=A_l\bigl(1+O(e^{-c_1k})\bigr),
\tag{PF13}
\]

uniformly in `l`. This is an elementary lower-tail Chernoff estimate for a
Gamma variable, since `4 pi lY <=(4 pi/10000)k`.

On `y>=Y`, Fourier orthogonality and PF8 give

\[
\int_{y\ge Y}y^{k-2}|w_l|^2dxdy
=
A_l^{(Y)}
+
\sum_{n>M}|a_{w_l}(n)|^2A_n^{(Y)}.
\tag{PF14}
\]

Subtracting PF13--PF14 from PF10 proves the complete residual estimate

\[
\boxed{
\begin{aligned}
&\int_{\mathcal F,\,y<Y}y^{k-2}|w_l|^2dxdy\\
&\qquad+
\sum_{n>M}|a_{w_l}(n)|^2A_n^{(Y)}
\le
\varepsilon_{k,M}A_l,
\end{aligned}}
\tag{PF15}
\]

where

\[
\varepsilon_{k,M}
=C\delta_{k,M}+Ce^{-c_1k}.
\tag{PF16}
\]

The left side contains the whole low fundamental domain and the entire high
Fourier tail. No finite coefficient prefix is extrapolated.

A weighted version follows coefficientwise. Since every tail mode has
`n>=M+1`,

\[
\int_{y\ge Y}y\,y^{k-2}
\left|w_l-q^l\right|^2dxdy
\le
C\frac{k}{M}\varepsilon_{k,M}A_l.
\tag{PF17}
\]

The corresponding bounded-log and small complex-power moments cost only a
fixed polynomial in `k,M`; PF5 makes every such cost negligible.

---

## 5. Pure one-mode period matrix

Put `s=1-c/k`. For a pure Fourier mode `q^m`, the constant terms of the
completed Eisenstein series give the exact diagonal scalar

\[
T_m(c)
=
C(s)\frac{\Gamma(k-1+s)}{(4\pi m)^{k-1+s}}
+
D(s)\frac{\Gamma(k-s)}{(4\pi m)^{k-s}},
\tag{PF18}
\]

where

\[
C(s)=\Lambda(2s),\qquad D(s)=\Lambda(2s-1).
\]

For `l<m`, the nonconstant Fourier mode `h=m-l` gives the exact cross

\[
B_{lm}(c)
=
2h^{s-1/2}\sigma_{1-2s}(h)
\int_0^\infty
 y^{k-3/2}e^{-2\pi(l+m)y}
K_{s-1/2}(2\pi h y)\,dy.
\tag{PF19}
\]

On the real endpoint interval, `B_lm>0`. On a complex endpoint disc, put
`a=Re(c)/k`. The classical complex-order bound

\[
|K_{s-1/2}(x)|\le K_{\Re s-1/2}(x)\le K_{1/2}(x)
\]

gives

\[
\boxed{
\frac{|B_{lm}(c)|}{A_m}
\le
h^{-a}\sigma_{-1+2a}(h)
\le h^aS_h,
\qquad S_h=\sigma_{-1}(h).
}
\tag{PF20}
\]

Under PF0, `a log h=o(1)` uniformly for `h<=M`, so the last bound is
`(1+o(1))S_h`.

After symmetric source scaling,

\[
\frac{|B_{lm}|}{\sqrt{A_lA_m}}
\le
(1+o(1))S_{m-l}
\left(\frac lm\right)^{(k-1)/2}
\le
C(1+\log M)e^{-c k(m-l)/M}.
\tag{PF21}
\]

This exponential separation, not a growing cofactor estimate, controls the
finite endpoint matrix.

---

## 6. Approximation of the actual period entries

Let `H_lm(c)` be the period matrix on the exact source frame `w_1,...,w_M`
before eliminating `W_{M+1}`. For `|c|<=C_2L` and `|Im c|<=6`, PF15--PF17,
Fourier orthogonality, the parent absolute Eisenstein bound, and PF20 give

\[
H_{ll}(c)=T_l(c)+\rho_{k,M}A_l,
\tag{PF22}
\]

and, for `l!=m`,

\[
H_{lm}(c)=B_{lm}(c)+\rho_{k,M}\sqrt{A_lA_m},
\tag{PF23}
\]

where the notation means absolute errors bounded by the displayed scale and

\[
\rho_{k,M}\longrightarrow0
\tag{PF24}
\]

faster than every inverse power of `k` and `M`.

For completeness, the decomposition is as follows.

* On `y<Y`, `|E^*(z,1-c/k)|<=Ck`; PF15 pays both factors.
* On `y>=Y`, constant-term crosses between a pure mode and
  `W_{M+1}` vanish exactly.
* The nonconstant pure-to-deep term is bounded by the parent Fourier
  projection estimate, with first reserve mode `M+1`.
* Every remaining term contains at least one high Fourier tail and is paid
  by PF17 and weighted Cauchy--Schwarz.
* Replacing the truncated pure integrals by PF18--PF19 costs `O(e^{-c k})`.

The same estimates hold for one `c` derivative on a smaller fixed strip by
Cauchy's estimate. No numerical period evaluation enters.

---

## 7. Exact one-mode centers

### Lemma 7.1

Uniformly for `1<=m<=M`, the scalar `T_m(c)` has one simple real zero
`c_hat(k,m)` in the endpoint range, and

\[
\boxed{
\widehat c_{k,m}
=12m+
\frac{288m^2}{k}\log\frac{k}{4\pi m}
+O\!\left(
\frac{m^2}{k}
+
\frac{m^3\log^2(k/m+2)}{k^2}
\right).
}
\tag{PF25}
\]

Moreover

\[
\widehat c_{k,m+1}-\widehat c_{k,m}=12+o(1)
\tag{PF26}
\]

uniformly for `m<M`, and on every fixed disc
`|c-c_hat(k,m)|<=6`,

\[
\frac{T_m'(c)}{kA_m}
=
\frac1{2c^2}(1+o(1)),
\tag{PF27}
\]

\[
\left|\frac{T_m(c)}{kA_m}\right|
\asymp
\frac{|c-\widehat c_{k,m}|}{m^2}.
\tag{PF28}
\]

#### Proof

Use the Laurent expansions

\[
C(1-c/k)=\pi/6+O(m/k),
\qquad
D(1-c/k)=-k/(2c)+O(1),
\]

and uniform Gamma-ratio Stirling estimates in PF18. With
`L_m=log(k/(4 pi m))`, they give

\[
\frac{T_m(c)}{kA_m}
=
\frac1{24m}-\frac1{2c}
-\frac{L_m}{k}
+O\!\left(
\frac1k+\frac{m\log^2(k/m+2)}{k^2}
\right)
\tag{PF29}
\]

uniformly for `c=12m+O(m^2L_m/k+m^2/k+1)`. Differentiation gives PF27.
The implicit-function theorem yields PF25 and PF28.

The increment of the displayed main correction in PF25 is

\[
O\!\left(\frac{m\log(k/m+2)}k\right)=o(1)
\]

under PF0, and the remainder has the same property. This proves PF26. ∎

The absolute displacement `c_hat(k,m)-12m` need not tend to zero near the
largest PF0 depths. Recentring is therefore essential. The fixed center
`12m` is appropriate only in the smaller regime

\[
m^2\log(k/m+2)=o(k).
\tag{PF30}
\]

---

## 8. Disjoint recentered discs

Fix once and for all

\[
0<\Delta<5.
\tag{PF31}
\]

By PF26, the discs

\[
\Omega_{k,J}
=\{c:|c-\widehat c_{k,J}|<\Delta\},
\qquad 1\le J\le L(k),
\tag{PF32}
\]

are pairwise disjoint for sufficiently large `k`. On their boundaries,
PF28 gives

\[
|T_J(c)|\ge c_\Delta\frac{kA_J}{J^2},
\tag{PF33}
\]

and for `m!=J`, `m<=M`,

\[
|T_m(c)|
\ge
c_\Delta\frac{kA_m(1+|m-J|)}{L^2}.
\tag{PF34}
\]

Part II uses these exact centers, the far-deep coercivity, and the
exponentially separated finite matrix to count the actual determinant zeros.