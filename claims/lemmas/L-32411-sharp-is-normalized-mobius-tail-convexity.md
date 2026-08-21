# L-32411 — SHARP is normalized Möbius-tail convexity

Claim ID: `L-32411`  
Title: The square-root hinge average-row coefficient is exactly a second difference of one normalized tail of the multiples-Mobius state  
Status: **PROPOSED COMPLETE EXACT REDUCTION — CONVEXITY OPEN / RH-BEARING**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #329 `L-32303`; finite multiples-Mobius inversion  
Scope: exact reformulation of SHARP; no claim of the missing convexity

## 1. Hinge and multiples-Mobius state

Fix an integer endpoint `T>=3` and put

\[
 h_T(q)=q^{-1/2}-T^{-1/2},
 \qquad1\le q\le T.
\tag{L-32411.1}
\]

Define its finite multiples-Mobius inverse

\[
\boxed{
 u_T(m)=
 \sum_{k\le T/m}\mu(k)h_T(mk).
}
\tag{L-32411.2}
\]

Then ordinary finite Mobius inversion on multiples gives

\[
\boxed{
 h_T(q)=\sum_{m:\,q\mid m}u_T(m).
}
\tag{L-32411.3}

For later computation, if

\[
 M(x)=\sum_{k\le x}\mu(k),
 \qquad
 A(x)=\sum_{k\le x}{\mu(k)\over\sqrt k},
\]

then exactly

\[
\boxed{
 u_T(m)
 ={1\over\sqrt m}A(\lfloor T/m\rfloor)
 -{1\over\sqrt T}M(\lfloor T/m\rfloor).
}
\tag{L-32411.4}

No triangular matrix appears in this formula.

## 2. Tail state

Define

\[
\boxed{
 S_T(j)=\sum_{m=j}^{T}u_T(m),
 \qquad1\le j\le T+1,
}
\tag{L-32411.5}

with `S_T(T+1)=0`. Then

\[
 u_T(j)=S_T(j)-S_T(j+1).
\tag{L-32411.6}

The exact adjoint formula on PR #329 is

\[
 c_T(j)=
 { (j+1)[j u_T(j)-(j-2)u_T(j+1)]
   +2S_T(j+2)
  \over j(j-1)}.
\tag{L-32411.7}

## 3. Exact cancellation to a second difference

Substitute (L-32411.6) into (L-32411.7). The numerator becomes

\[
\begin{aligned}
&j(j+1)S_T(j)
-2(j^2-1)S_T(j+1)
+j(j-1)S_T(j+2).
\end{aligned}
\]

Factoring `j(j^2-1)` gives

\[
\boxed{
 c_T(j)
 =(j+1)
 \left[
 {S_T(j)\over j-1}
 -2{S_T(j+1)\over j}
 +{S_T(j+2)\over j+1}
 \right].
}
\tag{L-32411.8}

Define the normalized tail

\[
\boxed{
 V_T(j)={S_T(j)\over j-1},
 \qquad j\ge2.
}
\tag{L-32411.9}

Then the complete square-root hinge inverse is simply

\[
\boxed{
 c_T(j)=(j+1)\,[V_T(j)-2V_T(j+1)+V_T(j+2)].
}
\tag{L-32411.10}

Therefore

\[
\boxed{
 \mathrm{SHARP}
 \iff
 V_T(j)-2V_T(j+1)+V_T(j+2)\ge0
 \quad(2\le j<T).
}
\tag{L-32411.11}

In words: **SHARP is exactly discrete convexity of one normalized Mobius-tail sequence.**

## 4. Low-row RH scalar in tail coordinates

The row-two and row-three compression of `T-32403` also simplifies. From (L-32411.8),

\[
 c_T(2)=3\left[S_T(2)-S_T(3)+{S_T(4)\over3}\right],
\]

\[
 c_T(3)=4\left[{S_T(3)\over2}-{2S_T(4)\over3}+{S_T(5)\over4}\right].
\]

Hence

\[
\boxed{
 5c_T(2)+3c_T(3)
 =3[5S_T(2)-3S_T(3)-S_T(4)+S_T(5)].
}
\tag{L-32411.12}

Using `S(j)=u(j)+S(j+1)` repeatedly gives the equivalent four-coordinate form

\[
\boxed{
 5c_T(2)+3c_T(3)
 =3[5u_T(2)+2u_T(3)+u_T(4)+2S_T(5)].
}
\tag{L-32411.13}

Using the full-tail identity

\[
 S_T(1)=h_T(1)=1-T^{-1/2},
\]

this reduces further to

\[
\boxed{
 5c_T(2)+3c_T(3)
 =3[2h_T(1)-2u_T(1)+3u_T(2)-u_T(4)].
}
\tag{L-32411.14}

Thus the RH-equivalent low-row sign requires only the multiples-Mobius states at scales `1,2,4` after the exact total-tail cancellation.

## 5. Why tail positivity alone is not being assumed

A tempting sufficient route would be to prove both

```text
S_T(j)>=0;
V_T is convex.
```

Large directed reconnaissance supports these inequalities, but neither is promoted here.

There is a structural reason for caution. For a geometric endpoint hinge

\[
 g_{T,x}(q)=x^q-x^T,
 \qquad0<x<1,
\]

the infinite-endpoint tail formally approaches the Lambert series

\[
\boxed{
 H_j(x)=\sum_{d\ge1}\mu(d){x^{jd}\over1-x^d}.
}
\tag{L-32411.15}

Its Mellin transform after `x=e^{-t}` contains

\[
 {1\over\zeta(s)}
 \sum_{k\ge j}k^{-s}.
\]

Thus a cofinal one-sign theorem for these tails is itself reciprocal-zeta sensitive. The exact tail reformulation is useful because it localizes the arithmetic obstruction; it does not turn it into a generic complete-monotonicity theorem.

This also explains why the componentwise Bernstein/Stieltjes shortcut was correctly refuted in `R-32403`.

## 6. Computational consequence

Equations (L-32411.4)--(L-32411.10) reduce an endpoint check to:

1. one Mobius prefix array `M(K)`;
2. one weighted prefix array `A(K)`;
3. one `O(T)` evaluation of `u_T(m)`;
4. one reverse cumulative sum for `S_T`;
5. second differences of `V_T`.

No triangular backward solve is required. Directed certification of SHARP can therefore be performed in linear time after the sieve.

## 7. Proof boundary

Closed exactly:

- the multiples-Mobius formula for the square-root hinge;
- the tail-state representation;
- the cancellation of the full adjoint formula to one second difference;
- equivalence of SHARP with normalized-tail convexity;
- the low-row RH scalar in four tail/Mobius coordinates;
- the Lambert-series firewall against treating tail positivity as generic.

Open:

- convexity of `V_T` for every endpoint;
- the low-row eventual sign;
- SHARP;
- RH.
