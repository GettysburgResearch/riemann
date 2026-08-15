# L-91361 — Multiplicative source children embed by same-index scaling in every physical row and column

Claim ID: `L-91361`  
Status: **PROVED EXACT SOURCE/ROW/CAPACITY FUNCTOR THEOREM**  
Created: 2026-08-13  
Depends on: retained component row `L-91112.25--26`; linear ordinary/radix-four response and score maps  
Corrects: the affine-child instruction in historical `L-91404/T-91403`  
RH status: **unproved**

## 1. One multiplicative source child

Let `m>=1`, let `Y=X/m`, and let a positive source packet at endpoint `Y` have source coefficients `nu(n)>=0`.  Its canonical component row is

\[
 R_Y^\nu(j)
 =\sum_n\nu(n)n^{-1/2}Q_{Y/n}(j).
\tag{L-91361.1}
\]

In the parent arithmetic source, the same packet occurs on the multiplied source nodes `mn` with coefficient `m^{-1/2}nu(n)`.  Its parent row contribution is therefore

\[
\begin{aligned}
 R_{X,m}^\nu(j)
 &=\sum_n\nu(n)(mn)^{-1/2}Q_{X/(mn)}(j)\\
 &=m^{-1/2}\sum_n\nu(n)n^{-1/2}Q_{Y/n}(j).
\end{aligned}
\]

Hence

\[
\boxed{
 R_{X,m}^\nu=m^{-1/2}R_Y^\nu
}
\tag{L-91361.2
}

coefficientwise in the **same row index** `j`.

No map of the form

\[
 j\mapsto m(j+1)-1
\]

occurs.

## 2. Arbitrary feasible child packings

Let `d_Y(j)>=0` be any feasible packing for the typed child packet at endpoint `Y`.  Define its parent placement by

\[
\boxed{
 \iota_m d_Y(j)=m^{-1/2}d_Y(j).
}
\tag{L-91361.3
}

The row indices are unchanged.  Every linear physical functional therefore scales by the same coefficient.  In particular, for each integer ordinary column `q`,

\[
\boxed{
 C_{\iota_m d_Y}(q)=m^{-1/2}C_{d_Y}(q),
}
\tag{L-91361.4
}

and for the radix-four detail,

\[
\boxed{
 \mathcal D_4C_{\iota_m d_Y}(q)
 =m^{-1/2}\mathcal D_4C_{d_Y}(q).
}
\tag{L-91361.5
}

The literal component entropy also scales exactly:

\[
\boxed{
 \mathcal S(\iota_m d_Y)=m^{-1/2}\mathcal S(d_Y).
}
\tag{L-91361.6
}

Thus feasibility and score are transported without fractional columns, unmatched affine fibers, or entropy amplification assumptions.

## 3. Source-disjoint packet sums

Suppose an exact positive source decomposition has the form

\[
\boxed{
 P_X=F_X+\sum_bm_b^{-1/2}P_{Y_b}^{(b)},
 \qquad Y_b=X/m_b,
}
\tag{L-91361.7
}

where every source atom occurs once.  Applying the component-row map gives the exact row identity

\[
\boxed{
 R_X(P_X)=R_X(F_X)+
 \sum_bm_b^{-1/2}R_{Y_b}(P_{Y_b}^{(b)}).
}
\tag{L-91361.8
}

Let `d_F` be feasible for the current packet and let `d_b` be arbitrary feasible rows for the actual child packets.  Then

\[
\boxed{
 d_X=d_F+\sum_bm_b^{-1/2}d_b
}
\tag{L-91361.9
}

is nonnegative.  Since every target/capacity coordinate is linear and the source decomposition is exact, the child target shares and their row responses are scaled by the same coefficients.  Therefore `d_X` consumes the parent target exactly once and is feasible in every ordinary and radix-four physical column.

The score identity is

\[
\boxed{
 \mathcal S(d_X)
 =\mathcal S(d_F)+
  \sum_bm_b^{-1/2}\mathcal S(d_b).
}
\tag{L-91361.10
}

## 4. Application to a finite-prime stopping line

In the paired least-prime expansion, a stopped child labelled by a finite product `m` has endpoint `X/m` and source coefficient `m^{-1/2}`.  Equation (L-91361.2) is exactly the row covariance of that source identity.

Consequently a finite-block decomposition such as

\[
 P_X=F_{61,X}+
 \sum_{d\mid P_{61}}
 \sum_{p\ge67}(dp)^{-1/2}P_{X/(dp)}^{(d,p)}
\tag{L-91361.11
}

may recurse on the actual paired children with their same row indices.  The affine Pascal lift previously inserted into this interface is unnecessary and, by `R-91558`, unsafe in signed detail columns.

## 5. Relationship with nested component embedding

`L-91559` proves a second valid same-index construction: when one canonical packet at a smaller endpoint is a subpacket of a larger-endpoint canonical packet, the positive difference `Q_X-Q_Y` pays the current row and an arbitrary child packing replaces `Q_Y` by the identity map.

The present theorem concerns a different but compatible situation: multiplicative source dilation already contributes the scaled child row itself to the parent source identity.  No endpoint-difference row is required.

Both theorems have the same physical lesson:

```text
row indices are physical coordinates;
child replacement is by identity/same-index scaling;
affine row-index dilation is not a radix-four functor.
```

## 6. Proof boundary

```text
multiplicative source-to-row covariance            EXACT
same-index arbitrary child placement               EXACT
ordinary/radix-four response scaling               EXACT
literal entropy scaling                            EXACT
source-disjoint child sum uses target once         EXACT
historical affine-child joint                      REMOVED / REFUTED
complete finite-forcing producer                   SEPARATE
packet-envelope recurrence                         AVAILABLE
Riemann Hypothesis                                 UNPROVEN
```
