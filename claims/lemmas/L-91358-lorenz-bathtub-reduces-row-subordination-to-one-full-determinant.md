# L-91358 — The Lorenz bathtub principle reduces literal row subordination to one full determinant

Claim ID: `L-91358`  
Status: **PROVED EXACT ORDERED-MEASURE REDUCTION THEOREM**  
Created: 2026-08-13  
Depends on: `L-91348`; elementary bathtub/rearrangement principle  
RH status: **unproved**

## 1. Ordered score and row measures

Let `D` be a totally ordered finite or countable source space.  Let `E` and `O`
be finite positive measures on `D`, interpreted as the even capacity and odd
demand in **score-mass units**.

Write

\[
 E_S=E(D),
 \qquad
 O_S=O(D),
 \qquad
 0<O_S\le E_S.
\tag{L-91358.1}
\]

Let

\[
 q:D\to\mathbb R_{\ge0}
\]

be nonincreasing.  The corresponding row masses are

\[
 E_R=\int q\,dE,
 \qquad
 O_R=\int q\,dO.
\tag{L-91358.2}

For the `P_61` causal packet one has

\[
 q(d)=\frac{K_R^{(j)}(d)}{K_S(d)}.
\]

## 2. Leftmost Lorenz submeasure

Let `U<=E` be the leftmost submeasure of total mass `O_S`: it contains all of
`E` below one cutoff, possibly a fractional atom at the cutoff, and no mass
above it.  This is exactly the score-Lorenz removal used in `L-91348`.

The bathtub principle states that among all submeasures `V<=E` with

\[
 V(D)=O_S,
\]

the leftmost submeasure maximizes every nonincreasing payoff:

\[
 \boxed{
 \int q\,dU
 \ge
 \int q\,dV.
 }
\tag{L-91358.3}

In particular, taking the proportional submeasure

\[
 V=\frac{O_S}{E_S}E
\]

gives

\[
 \boxed{
 \frac1{O_S}\int q\,dU
 \ge
 \frac{E_R}{E_S}.
 }
\tag{L-91358.4}

## 3. One full determinant is sufficient

Assume the single full-packet determinant inequality

\[
 \boxed{
 E_RO_S-E_SO_R\ge0.
 }
\tag{L-91358.5
}

Equivalently,

\[
 \frac{E_R}{E_S}\ge\frac{O_R}{O_S}.
\]

Combining with (L-91358.4),

\[
 \frac1{O_S}\int q\,dU
 \ge\frac{O_R}{O_S},
\]

and therefore

\[
 \boxed{
 \int q\,dU\ge O_R.
 }
\tag{L-91358.6
}

Let

\[
 \nu=E-U\ge0
\]

be the Lorenz residual.  Then

\[
\begin{aligned}
 \int q\,d\nu
 &=E_R-\int q\,dU\\
 &\le E_R-O_R.
\end{aligned}
\]

Hence

\[
 \boxed{
 \text{residual positive row}
 \le
 \text{signed arithmetic row}.
 }
\tag{L-91358.7
}

This is the exact row-subordination orientation required by literal row-packet
typing.

## 4. Continuous and fractional-cutoff versions

The proof uses only order, positivity and finite mass.  It applies unchanged to:

```text
continuous source measures;
countable source measures;
fractional cutoff atoms;
measure-valued endpoint packets;
all component rows simultaneously whenever each q_j is nonincreasing.
```

No Hall edge construction is needed after the Lorenz submeasure is defined.

## 5. `P_61` specialization

For a causal packet at parameters

\[
 p\ge67,
 \qquad1\le y\le67,
 \qquad2\le j\le66,
\]

put

\[
 K_R^{(j)}(d)
 =d^{-1/2}
 \left[Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)\right]
\tag{L-91358.8}

and let `K_S(d)` be the causal endpoint-score atom.  Let `E` and `O` carry masses
`K_S(d)` on even and odd `P_61` divisors.

Then literal row subordination follows from precisely:

1. **causal profile monotonicity**
   \[
   d_1\le d_2
   \Longrightarrow
   \frac{K_R^{(j)}(d_1)}{K_S(d_1)}
   \ge
   \frac{K_R^{(j)}(d_2)}{K_S(d_2)};
   \tag{L-91358.9}
   \]
2. **one full determinant**
   \[
   \left(\sum_{\mu(e)=1}K_R^{(j)}(e)\right)
   \left(\sum_{\mu(o)=-1}K_S(o)\right)
   \ge
   \left(\sum_{\mu(e)=1}K_S(e)\right)
   \left(\sum_{\mu(o)=-1}K_R^{(j)}(o)\right).
   \tag{L-91358.10}
   \]

Thus the earlier family of cutoff-prefix row determinants is sufficient but not
necessary.  The cutoff bound of `L-91357` remains useful for direct certificates,
but the bathtub reduction replaces all of those prefix signs by two structured
global statements.

## 6. Proof boundary

```text
leftmost-submeasure bathtub principle             EXACT
one full determinant -> row subordination         EXACT
fractional/measure-valued extension                EXACT
P_61 causal row/score profile monotonicity         OPEN / FINITE-ANALYTIC
P_61 full even/odd determinant                     OPEN / FINITE-ANALYTIC
literal row-packet typing after those two gates    IMMEDIATE
Riemann Hypothesis                                 UNPROVEN
```
