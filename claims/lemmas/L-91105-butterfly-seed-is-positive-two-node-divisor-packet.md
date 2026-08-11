# L-91105 — Every endpoint butterfly is a positive two-node seed and a sparse three-integer divisor packet

Claim ID: `L-91105` (provisional research range)  
Title: The rank-two martingale butterfly cancels at seed level below its boundary and leaves exactly two positive adjacent seed atoms; its carry and radix-four detail responses are explicit divisor stencils on three consecutive integers, and arbitrary butterfly corrections admit an exact radix-four/Möbius/tail inversion  
Status: **PROPOSED COMPLETE EXACT SPARSE-FACTORISATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91101`; PR #352 `L-90027/L-90029`; ordinary multiples Möbius inversion  
Scope: exact finite seed, carry, divisor, and inversion algebra; positivity of the final endpoint weights and RH remain open

## 1. Seed-level butterfly

Retain
\[
 e_T(m)=b_T(m)-b_{T-1}(m)
\]
and the adjacent endpoint butterfly coefficients
\[
 c_T^-=rac{\alpha_T\theta_T}{\alpha_{T-1}},
 \qquad
 c_T^+=rac{\alpha_T(1-\theta_T)}{\alpha_{T+1}},
\]
where
\[
 \theta_T=rac{r_T-r_{T+1}}{r_{T-1}-r_{T+1}}.
\]

Define the corresponding seed packet
\[
\boxed{
 \mathcal P_T(m)
 =c_T^-e_{T-1}(m)-e_T(m)+c_T^+e_{T+1}(m).
}
\tag{L-91105.1}
\]

For every \(m\le T-2\), all three endpoint increments are in their old-node rank-two regime. The two moment identities defining the butterfly give
\[
 c_T^-\alpha_{T-1}-\alpha_T+c_T^+\alpha_{T+1}=0,
\]
\[
 c_T^-\delta_{T-1}-\delta_T+c_T^+\delta_{T+1}=0.
\]
Therefore
\[
\boxed{
 \mathcal P_T(m)=0
 \qquad(m\le T-2).
}
\tag{L-91105.2}

At \(m=T-1\), the actual entering endpoint value of \(e_{T-1}\) is zero. The virtual old-node value is
\[
 \alpha_{T-1}\sqrt{T-1}-\delta_{T-1}(T-1)
 =
 \alpha_{T-1}\sqrt{T-1}
 \left(1-r_{T-1}\sqrt{T-1}\right)<0,
\]
because `L-91101` gives
\[
 r_{T-1}>(T-1)^{-1/2}.
\]
Subtracting this missing virtual value from the exact moment cancellation gives
\[
\boxed{
 A_T:=\mathcal P_T(T-1)
 =c_T^-\alpha_{T-1}\sqrt{T-1}
 \left(r_{T-1}\sqrt{T-1}-1\right)>0.
}
\tag{L-91105.3}

At \(m=T\), only the entering old node of \(e_{T+1}\) survives. Hence
\[
\boxed{
 B_T:=\mathcal P_T(T)
 =c_T^+\alpha_{T+1}\sqrt T
 \left(1-r_{T+1}\sqrt T\right)>0,
}
\tag{L-91105.4}
\]
because
\[
 r_{T+1}<T^{-1/2}.
\]

All larger nodes vanish. Thus
\[
\boxed{
 \mathcal P_T=A_T\delta_{T-1}+B_T\delta_T,
 \qquad A_T,B_T>0.
}
\tag{L-91105.5}

This is stronger than the four-row support theorem for the row packet: the underlying seed packet is a positive measure on only two adjacent integers.

## 2. Direct positive score formula

Let
\[
 \ell_m=\log\frac m{m-1}.
\]
The endpoint entropy identity is
\[
 H_T=\sum_m e_T(m)\ell_m.
\]
Therefore the butterfly score gain of `L-91102` has the exact two-atom form
\[
\boxed{
 E_T
 =c_T^-H_{T-1}-H_T+c_T^+H_{T+1}
 =A_T\ell_{T-1}+B_T\ell_T>0.
}
\tag{L-91105.6}

Thus strict score improvement has a second proof requiring no global convexity argument: each butterfly creates two positive radical-switching atoms and the entropy increment is positive on both.

The convexity theorem remains valuable because it characterizes all nonnegative butterfly combinations and killed-shadow perturbations, not merely one local score.

## 3. Sparse ordinary carry response

For a finite seed \(F\), write
\[
 v_q(F)=\sum_{k\ge1}[F(kq)-F(kq+1)].
\]
Applying this to (L-91105.5) gives
\[
\boxed{
 v_q(\mathcal P_T)
 =B_T\mathbf1_{q\mid T}
 +(A_T-B_T)\mathbf1_{q\mid T-1}
 -A_T\mathbf1_{q\mid T-2}.
}
\tag{L-91105.7}

Hence one butterfly affects only divisor columns of the three consecutive integers
\[
 T-2,\ T-1,\ T.
\]
The dense positive endpoint matrix has collapsed to a sparse arithmetic stencil.

## 4. Sparse radix-four detail response

Define
\[
 h_q(n)=\mathbf1_{q\mid n}-2\mathbf1_{4q\mid n}
 \in\{-1,0,1\}.
\tag{L-91105.8}
\]

The radix-four detail response of one butterfly is
\[
 K_T(q)
 :=v_q(\mathcal P_T)-2v_{4q}(\mathcal P_T).
\]
By (L-91105.7),
\[
\boxed{
 K_T(q)
 =B_Th_q(T)
 +(A_T-B_T)h_q(T-1)
 -A_Th_q(T-2).
}
\tag{L-91105.9}

Thus every nonzero entry is caused by a divisor or quarter-divisor relation with one of three consecutive integers. No long dense kernel remains in butterfly coordinates.

## 5. Aggregate positive butterfly seed

Let \(\eta_T\ge0\) be finitely supported butterfly intensities and put
\[
 F(n)=\sum_T\eta_T\mathcal P_T(n).
\tag{L-91105.10}
\]
Using (L-91105.5),
\[
\boxed{
 F(n)=B_n\eta_n+A_{n+1}\eta_{n+1}\ge0.
}
\tag{L-91105.11}

So every nonnegative convex-order perturbation has an underlying coefficientwise positive seed, even though its row-coordinate packet has the alternating sign pattern forced by the Chebyshev system.

Define the adjacent seed difference
\[
\boxed{
 c(n)=F(n)-F(n+1).
}
\tag{L-91105.12}
Then
\[
\boxed{
 c(n)
 =B_n\eta_n
 +(A_{n+1}-B_{n+1})\eta_{n+1}
 -A_{n+2}\eta_{n+2}.
}
\tag{L-91105.13}

## 6. Divisor and radix-four factorization

Put
\[
 D_c(q)=\sum_{k\ge1}c(kq).
\tag{L-91105.14}
\]
Since \(c=F-SF\), ordinary carry switching gives
\[
 v_q(F)=D_c(q).
\tag{L-91105.15}

Consequently the aggregate detail response is
\[
\boxed{
 g(q):=\sum_T\eta_TK_T(q)
 =D_c(q)-2D_c(4q).
}
\tag{L-91105.16}

Equivalently,
\[
 g(q)=\sum_n c(n)h_q(n).
\tag{L-91105.17}

The complete map from butterfly intensities to detail columns factors as
\[
\boxed{
 \eta
 \xrightarrow{\text{positive adjacent two-node kernel}}
 F
 \xrightarrow{I-S}
 c
 \xrightarrow{\text{multiples sum}}
 D_c
 \xrightarrow{I-2S_4}
 g.
}
\tag{L-91105.18}

This is the exact finite algebra behind the shadow-packing route.

## 7. Exact double inversion

Conversely, let \(g(q)\) be any finitely supported desired detail correction.

First invert the radix-four renewal:
\[
\boxed{
 D_c(q)=\sum_{j\ge0}2^jg(4^jq).
}
\tag{L-91105.19}

Next invert the multiples transform by Möbius inversion:
\[
\boxed{
 c(n)=\sum_{k\ge1}\mu(k)D_c(kn).
}
\tag{L-91105.20}

Then recover the seed by a tail sum:
\[
\boxed{
 F(n)=\sum_{m\ge n}c(m).
}
\tag{L-91105.21}

Finally, the butterfly intensities, if they exist with the chosen terminal boundary, are recovered from the positive bidiagonal system
\[
\boxed{
 F(n)=B_n\eta_n+A_{n+1}\eta_{n+1}.
}
\tag{L-91105.22}

Thus the remaining feasibility question is no longer an opaque dense linear program. It is the positivity and endpoint-weight compatibility of one explicit sequence obtained by:

```text
radix-four renewal inversion;
multiples Möbius inversion;
one tail integral;
one positive bidiagonal deconvolution.
```

## 8. Exact equality seed for the critical target

Let
\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]
The unique zero-extended seed \(b_X^\star\) whose ordinary carry response is exactly \(w_X\) is obtained by
\[
\boxed{
 d_X^\star(m)
 =\sum_{k\le X/m}\mu(k)w_X(km),
}
\tag{L-91105.23}
\]
\[
\boxed{
 b_X^\star(n)=\sum_{m=n}^{X}d_X^\star(m).
}
\tag{L-91105.24}

Indeed, multiples Möbius inversion gives
\[
 \sum_{j\ge1}d_X^\star(jq)=w_X(q),
\]
and tail switching gives
\[
 v_q(b_X^\star)=w_X(q).
\]

Therefore the exact correction
\[
\boxed{
 F_X^\star=b_X^\star-b_X
}
\tag{L-91105.25}
has ordinary response \(w_X-v(b_X)\), and its radix-four response is precisely the target residual
\[
 \Omega_X-\sum_T\Xi_T.
\]

The shadow-packing problem can now be stated without an LP solver:

> Modify or partially realize the explicit equality correction \(F_X^\star\) by nonnegative two-node butterfly seeds, allowing only controlled initial killing, so that the induced endpoint weights stay nonnegative and the score loss is \(o(\log^2X)\) or nonpositive.

## 9. New connection with adjacent-dyadic Möbius flux

Equations (L-91105.19)--(L-91105.20) show that the factor-four endpoint packing and the compact Möbius-flux/CN3 programmes share the same hidden operators:

```text
critical radix-four renewal
+
multiples Möbius inversion
+
local adjacent difference.
```

The difference is the positive interface. Here the Möbius inversion is preceded and followed by positive finite transports: the positive target/endpoint details of PR #352 and the positive two-node butterfly seed of this theorem.

This supplies a concrete route for importing parity-breaking or adjacent-dyadic ideas without returning to a signed global Mertens estimate.

## 10. Proof boundary

Closed exactly, subject to review:

1. cancellation of every old seed node;
2. the positive two-node boundary seed;
3. the direct positive score formula;
4. the sparse three-integer divisor stencil;
5. the sparse radix-four divisor stencil;
6. positivity of every aggregate butterfly seed;
7. the divisor/radix-four factorization;
8. the exact double inversion;
9. the explicit critical equality seed.

Still open:

1. positivity of the reconstructed butterfly intensities after controlled boundary killing;
2. nonnegativity of the resulting endpoint weights;
3. a contractive recursive treatment of the remaining inner correction;
4. RH.
