# R-105350 — Bounded confluent order does not certify the boundary Loewner gate

Claim ID: `R-105350`  
Status: **PROVED EXACT ABSTRACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105329--L-105351`  
RH status: **not assumed**

## 1. A rational odd separator

On the interval `(-1,1)`, put

\[
\boxed{
H(z)={z\over4}
\left({1\over1+z}-1+{1\over1-z}\right).
}
\tag{R-105350.1}
\]

At the anchor zero this has the signed Hamburger representation

\[
H(z)=z\sum_{t\in\{-1,0,1\}}{w_t\over1-tz},
\qquad
(w_{-1},w_0,w_1)=\left({1\over4},-{1\over4},{1\over4}\right).
\tag{R-105350.2}
\]

Its moment sequence begins

\[
(m_0,m_1,m_2,m_3,m_4)
=\left({1\over4},0,{1\over2},0,{1\over2}\right).
\tag{R-105350.3}
\]

Therefore the first two confluent orders pass:

\[
\mathsf L_1=[1/4]\succ0,
\qquad
\mathsf L_2=
\begin{pmatrix}1/4&0\\0&1/2\end{pmatrix}\succ0.
\tag{R-105350.4}
\]

But

\[
\mathsf L_3=
\begin{pmatrix}
1/4&0&1/2\\
0&1/2&0\\
1/2&0&1/2
\end{pmatrix},
\qquad
\boxed{\det\mathsf L_3=-{1\over16}<0.}
\tag{R-105350.5}
\]

The polynomial witness `q(t)=1-t^2` isolates the negative atom:

\[
(1,0,-1)\mathsf L_3(1,0,-1)^T=-{1\over4}.
\tag{R-105350.6}
\]

## 2. A separated three-point failure

For the real packet

\[
X=\left(-{1\over2},{1\over4},{1\over2}\right),
\]

the Loewner matrix factors as

\[
\mathscr L_H(X)
=A^T\operatorname{diag}(1/4,-1/4,1/4)A,
\qquad
A_{t,x}={1\over1-tx}.
\tag{R-105350.7}
\]

Explicitly,

\[
\mathscr L_H(X)=
\begin{pmatrix}
31/36&67/180&5/12\\
67/180&319/900&11/20\\
5/12&11/20&31/36
\end{pmatrix}.
\tag{R-105350.8}
\]

Every diagonal entry and every two-point principal determinant is positive:

\[
{1\over6},\qquad {46\over81},\qquad {11\over4050},
\]

but

\[
\boxed{
\det\mathscr L_H(X)=-{16\over2025}<0.
}
\tag{R-105350.9}
\]

Thus even a packet whose one- and two-node restrictions all pass can contain a
three-node negative square.

## 3. Binding conclusion

```text
one anchor plus every confluent order          equivalent to all-packet BRP;
one anchor through any bounded order           insufficient in general;
packet positivity through any fixed small size insufficient abstractly.
```

The reduction `L-105350` is useful because it removes separated-node geometry,
not because it truncates the all-order burden. A valid Xi proof must obtain the
complete moment/Stieltjes theorem or a source-specific structural substitute.
