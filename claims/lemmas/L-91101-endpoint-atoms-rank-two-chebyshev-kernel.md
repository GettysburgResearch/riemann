# L-91101 — Endpoint atoms form a rank-two Chebyshev kernel

Claim ID: `L-91101` (provisional research range)  
Title: Deep endpoint rows have exact separation rank two; their endpoint/row kernel is strictly sign-regular, and every moment-neutral convex-order increment is a nonnegative sum of local martingale butterflies  
Status: **PROPOSED COMPLETE EXACT STRUCTURAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Frozen source: PR #352 head `906b5a477a1ed7c88a40db7569924f15f3d54b72`; PR #265 endpoint atoms  
Scope: exact endpoint-row structure and finite convex-order geometry; no feasibility theorem and no RH conclusion

## 1. Endpoint increments

Retain the parabolic seed
\[
 b_X(m)=2\sqrt m\left[
 \log\frac Xm-2\left(1-\sqrt{\frac mX}\right)
 \right]\mathbf 1_{m\le X}.
\]

For an integer endpoint \(T\ge3\), put
\[
 e_T(m)=b_T(m)-b_{T-1}(m).
\]
For every old node \(m\le T-1\),
\[
\boxed{
 e_T(m)=\alpha_T\sqrt m-\delta_Tm,
}
\tag{L-91101.1}
\]
where
\[
\boxed{
 \alpha_T=2\log\frac T{T-1}>0,
 \qquad
 \delta_T=4\left((T-1)^{-1/2}-T^{-1/2}\right)>0.
}
\tag{L-91101.2}
\]

Let
\[
 A_X(m)=\frac{b_X(m)}{m-1},
 \qquad
 d_X(n)=(n+1)\Delta^2A_X(n),
\]
with forward second difference
\[
 \Delta^2f(n)=f(n)-2f(n+1)+f(n+2),
\]
and define the positive endpoint row atom
\[
 a_T(n)=d_T(n)-d_{T-1}(n).
\]

For a deep row \(2\le n\le T-3\), all three entries in the second difference are old nodes, so (L-91101.1) gives
\[
\boxed{
 a_T(n)=\alpha_TU_n-\delta_TV_n
       =\alpha_TU_n(1-r_Ts_n),
}
\tag{L-91101.3}
\]
where
\[
 U_n=(n+1)\Delta^2\!\left(\frac{\sqrt n}{n-1}\right)>0,
\tag{L-91101.4}
\]
\[
 \boxed{
 V_n=(n+1)\Delta^2\!\left(\frac n{n-1}\right)
 =\frac2{n(n-1)}>0,
 }
\tag{L-91101.5}
\]
and
\[
 r_T=\frac{\delta_T}{\alpha_T},
 \qquad
 s_n=\frac{V_n}{U_n}.
\tag{L-91101.6}
\]

Thus the complete deep-interior endpoint matrix has separation rank two:
\[
\boxed{
 [a_T(n)]_{\rm deep}
 =
 [\alpha_T]\,[U_n]
 -
 [\delta_T]\,[V_n].
}
\tag{L-91101.7}
\]

The only failure of this rank-two law occurs in the moving endpoint collar
\[
 n\in\{T-2,T-1\}.
\]

## 2. The endpoint coordinate \(r_T\) decreases strictly

Using
\[
 \int_{T-1}^{T}x^{-3/2}\,dx
 =2\left((T-1)^{-1/2}-T^{-1/2}\right)
\]
and
\[
 \int_{T-1}^{T}x^{-1}\,dx
 =\log\frac T{T-1},
\]
one gets
\[
\boxed{
 r_T
 =
 \frac{\int_{T-1}^{T}x^{-3/2}\,dx}
      {\int_{T-1}^{T}x^{-1}\,dx}.
}
\tag{L-91101.8}
\]

Hence \(r_T\) is the \(x^{-1}dx\)-weighted mean of the strictly decreasing function \(x^{-1/2}\) on \([T-1,T]\). Therefore
\[
\boxed{
 T^{-1/2}<r_T<(T-1)^{-1/2},
 \qquad
 r_{T+1}<r_T.
}
\tag{L-91101.9}
\]

The endpoint index has therefore become a one-dimensional ordered state coordinate.

## 3. The row coordinate \(s_n\) decreases strictly

Put
\[
 f(x)=\frac{\sqrt x}{x-1},
 \qquad
 g(x)=\frac{x}{x-1}.
\]
Direct differentiation gives
\[
\boxed{
 \frac{f''(x)}{g''(x)}
 =
 R(x)
 :=
 \frac{3x^2+6x-1}{8x^{3/2}},
}
\tag{L-91101.10}
\]
and
\[
\boxed{
 R'(x)=\frac{3(x-1)^2}{16x^{5/2}}>0
 \qquad(x>1).
}
\tag{L-91101.11}
\]

The Peano formula for a forward second difference is
\[
 \Delta^2h(n)
 =
 \int_n^{n+2}h''(x)\tau_n(x)\,dx,
\tag{L-91101.12}
\]
where
\[
 \tau_n(x)=
 \begin{cases}
 x-n,&n\le x\le n+1,\\
 n+2-x,&n+1\le x\le n+2,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Consequently
\[
 \frac{U_n}{V_n}
 =
 \frac{\int R(x)g''(x)\tau_n(x)\,dx}
      {\int g''(x)\tau_n(x)\,dx}.
\tag{L-91101.13}
\]

Let \(\mu_n\) be the probability law obtained by normalizing
\[
 g''(x)\tau_n(x)\,dx.
\]
On the overlap \([n+1,n+2]\),
\[
 \frac{d\mu_{n+1}}{d\mu_n}(x)
 \quad\text{is proportional to}\quad
 \frac{x-n-1}{n+2-x},
\tag{L-91101.14}
\]
which increases strictly from \(0\) to \(+\infty\). Moreover \(\mu_n\) has its extra support on the left interval \([n,n+1]\), while \(\mu_{n+1}\) has its extra support on the right interval \([n+2,n+3]\). Thus \(\mu_{n+1}\) strictly dominates \(\mu_n\) in monotone-likelihood-ratio, hence first-order stochastic, order.

Since \(R\) is strictly increasing,
\[
 \frac{U_{n+1}}{V_{n+1}}
 >
 \frac{U_n}{V_n}.
\]
Equivalently,
\[
\boxed{
 s_{n+1}<s_n.
}
\tag{L-91101.15}
\]

## 4. Strict reverse total positivity of order two

Let
\[
 T_1<T_2,
 \qquad
 n_1<n_2\le T_1-3.
\]
Using (L-91101.3),
\[
\begin{aligned}
&\det
\begin{pmatrix}
a_{T_1}(n_1)&a_{T_1}(n_2)\\
a_{T_2}(n_1)&a_{T_2}(n_2)
\end{pmatrix}\\
&\quad=
\alpha_{T_1}\alpha_{T_2}U_{n_1}U_{n_2}
(r_{T_1}-r_{T_2})(s_{n_2}-s_{n_1}).
\end{aligned}
\tag{L-91101.16}
\]
By (L-91101.9) and (L-91101.15), the last two factors have opposite signs. Hence
\[
\boxed{
\det[a_{T_i}(n_j)]_{i,j=1}^{2}<0.
}
\tag{L-91101.17}
\]

Thus the deep endpoint-row matrix is a strict reverse-TP\(_2\), or sign-regular Chebyshev, kernel. This is not an asymptotic statement.

## 5. Two moments annihilate the complete inherited bulk

Let \(c_T\) be any finitely supported real endpoint perturbation, and put
\[
 P(c)=\sum_Tc_T\alpha_T,
 \qquad
 Q(c)=\sum_Tc_T\delta_T.
\tag{L-91101.18}
\]
If every active endpoint is at least \(T_0\), then for every \(n\le T_0-3\),
\[
\boxed{
 \sum_Tc_Ta_T(n)
 =
 U_n\,[P(c)-Q(c)s_n].
}
\tag{L-91101.19}
\]

Consequences:

1. If
   \[
   P(c)=Q(c)=0,
   \tag{L-91101.20}
   \]
   then the perturbation vanishes on every inherited deep row.

2. If \((P,Q)\ne(0,0)\), then the deep-row sign changes at most once, because \(s_n\) decreases strictly.

Thus arbitrary endpoint reweighting has a two-dimensional inherited bulk plus a moving finite collar. This is the exact finite analogue of a two-moment spline or martingale constraint.

## 6. Abstract adjacent-butterfly basis

Let
\[
 x_1<x_2<\cdots<x_N
\]
be arbitrary real nodes. For \(2\le i\le N-1\), define the adjacent martingale butterfly
\[
\boxed{
 \mathfrak b_i
 =
 \frac{x_{i+1}-x_i}{x_{i+1}-x_{i-1}}\delta_{x_{i-1}}
 -\delta_{x_i}
 +
 \frac{x_i-x_{i-1}}{x_{i+1}-x_{i-1}}\delta_{x_{i+1}}.
}
\tag{L-91101.21}
\]
It has total mass and first moment zero.

For a signed measure \(\eta\) on the nodes with
\[
 \eta(1)=\eta(x)=0,
\tag{L-91101.22}
\]
put
\[
 C_i(\eta)=\int(x-x_i)_+\,d\eta(x),
\tag{L-91101.23}
\]
and
\[
 \kappa_i
 =
 \frac{(x_i-x_{i-1})(x_{i+1}-x_i)}
      {x_{i+1}-x_{i-1}}>0.
\tag{L-91101.24}
\]

The hinge \((x-x_j)_+\) is affine on the support of \(\mathfrak b_i\) unless \(j=i\), while
\[
 C_i(\mathfrak b_i)=\kappa_i.
\]
Therefore
\[
\boxed{
 \eta
 =
 \sum_{i=2}^{N-1}
 \frac{C_i(\eta)}{\kappa_i}\,\mathfrak b_i.
}
\tag{L-91101.25}
\]

Moreover, affine terms disappear under (L-91101.22), and every convex function on the finite grid is an affine function plus a nonnegative combination of the grid hinges. Hence
\[
\boxed{
 \eta(\phi)\ge0\ \text{for every convex }\phi
 \iff
 C_i(\eta)\ge0\ \text{for every }i
 \iff
 \eta\in\operatorname{cone}\{\mathfrak b_2,\ldots,\mathfrak b_{N-1}\}.
}
\tag{L-91101.26}
\]

This is the finite one-dimensional convex-order cone, written in a basis diagonalized by call prices.

## 7. Endpoint interpretation

Use the ordered nodes \(r_T\). Since \(r_T\) decreases with \(T\), the adjacent butterfly centered at \(r_T\) is
\[
 \theta_T\delta_{r_{T-1}}
 -\delta_{r_T}
 +(1-\theta_T)\delta_{r_{T+1}},
\tag{L-91101.27}
\]
where
\[
 \theta_T
 =
 \frac{r_T-r_{T+1}}{r_{T-1}-r_{T+1}}.
\tag{L-91101.28}
\]

After converting measure mass back to endpoint-row coefficients, the corresponding endpoint perturbation is
\[
\boxed{
 \mathcal B_T
 =
 c_T^-a_{T-1}-a_T+c_T^+a_{T+1},
}
\tag{L-91101.29}
\]
with
\[
 c_T^-=\frac{\alpha_T\theta_T}{\alpha_{T-1}},
 \qquad
 c_T^+=\frac{\alpha_T(1-\theta_T)}{\alpha_{T+1}}.
\tag{L-91101.30}
\]

Equations (L-91101.20) hold exactly. Therefore
\[
\boxed{
 \mathcal B_T(n)=0
 \qquad(2\le n\le T-4).
}
\tag{L-91101.31}
\]
Since \(a_{T+1}\) vanishes at rows \(n\ge T+1\), every butterfly is supported on only four moving rows:
\[
\boxed{
 \operatorname{supp}\mathcal B_T
 \subseteq\{T-3,T-2,T-1,T\}.
}
\tag{L-91101.32}
\]

The endpoint scale is therefore a one-dimensional martingale state, and its elementary convex-order moves are compact four-row packets.

## 8. Proof boundary

Closed exactly, subject to review:

1. the rank-two deep-interior formula;
2. strict monotonicity of the endpoint and row state coordinates;
3. strict reverse-TP\(_2\) sign regularity;
4. exact two-moment cancellation and one-crossing law;
5. the abstract adjacent-butterfly basis for finite convex order;
6. the four-row support of endpoint martingale butterflies.

Still open:

1. a detail-feasible convex-order endpoint reweighting with controlled killing;
2. a finite shadow/left-curtain construction for the radix-four target;
3. the endpoint score theorem;
4. RH.
