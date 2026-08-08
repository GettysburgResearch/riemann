# L-33802 — Positive Q=4 Jordan deformation and exact product-source curvature

Claim ID: `L-33802`  
Title: The Q=4 Euler–Blaschke Dirichlet system has a coefficientwise-positive full Jordan deformation, and the remaining reflected product-source block is exactly the second deformation curvature of one physical energy  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/PLANCHEREL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 Q=4 definitions; PR #337 `L-32710`; elementary local Euler algebra  
Scope: positive all-order source and exact resummation/placement of the product-source block; no sign for that curvature, no recurrence, no RH conclusion

## 1. Q=4 Dirichlet system

Retain

\[
 B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)},
 \qquad
 A_4(s)=B_4(s)^{-1}.
\]

For real `tau>=0` define the full Jordan deformation

\[
\boxed{
 J_{4,\tau}(s)
 =\frac{A_4(s-\tau)}{A_4(s)}
 =\sum_{n\ge1}\frac{J_{4,\tau}(n)}{n^s}.
}
\tag{L-33802.1}
\]

At `tau=0`, `J_(4,0)=epsilon`.

Coefficientwise differentiation at zero gives

\[
\boxed{
 \partial_\tau J_{4,\tau}|_{0}=\Lambda_4,
 \qquad
 \partial_\tau^2 J_{4,\tau}|_{0}=C_4,
}
\tag{L-33802.2}
\]

because `J_(4,tau)=b_4*(a_4 n^tau)` and the first two logarithmic derivatives are exactly the generalized-prime and Selberg sequences.

## 2. Odd-prime Euler factors are positive

For an odd prime `p`, put

\[
 z=p^{-s},
 \qquad
 a=p^\tau\ge1.
\]

The local factor is

\[
 \frac{1-z}{1-az}
 =1+\frac{(a-1)z}{1-az}.
\]

Hence

\[
\boxed{
 J_{4,\tau}(p^k)
 =(p^\tau-1)p^{\tau(k-1)}\ge0,
 \qquad k\ge1.
}
\tag{L-33802.3}
\]

## 3. Exact prime-two factor

Write

\[
 z=2^{-s},
 \qquad a=2^\tau\ge1.
\]

Since the Q=4 inverse has local generating function

\[
 A_{4,2}(z)
 =\sum_{r\ge0}4^{\lfloor r/2\rfloor}z^r
 =\frac{1+z}{1-4z^2},
\]

the local Jordan ratio is

\[
\boxed{
 R_a(z)
 =\frac{A_{4,2}(az)}{A_{4,2}(z)}
 =\frac{(1+az)(1-4z^2)}{(1+z)(1-4a^2z^2)}.
}
\tag{L-33802.4}
\]

Write

\[
 R_a(z)=\sum_{r\ge0}j_r(a)z^r.
\]

Then `j_0(a)=1`, and direct partial fractions or coefficient comparison gives

\[
\boxed{j_1(a)=a-1,}
\tag{L-33802.5}
\]

and for every `m>=0`,

\[
\boxed{
 j_{2m+1}(a)
 =(a-1)
 \frac{
  4^{m+1}a^{2m}(a^2-1)+3
 }{4a^2-1}
 \ge0.
}
\tag{L-33802.6}
\]

For every `m>=1`,

\[
\boxed{
 j_{2m}(a)
 =(a-1)
 \frac{
 4^m a^{2m}(4a^2+3a-1)-3a
 }{a(4a^2-1)}
 \ge0.
}
\tag{L-33802.7}
\]

The signs are immediate for `a>=1`: denominators are positive; the odd numerator is at least three; and in the even numerator

\[
4^m a^{2m}(4a^2+3a-1)
\ge4a^2\cdot6>3a.
\]

Thus the complete prime-two local factor has nonnegative coefficients.

## 4. Complete coefficientwise positivity

The deformation is multiplicative. Equations (L-33802.3) and (L-33802.5)--(L-33802.7) therefore give

\[
\boxed{
 J_{4,\tau}(n)\ge0
 \qquad(n\ge1,\ \tau\ge0).
}
\tag{L-33802.8}
\]

For `tau>0` every coefficient allowed by the local Euler factors is strictly positive.

This is the Q=4 analogue of the positive Jordan deformations on the parity-Euler and ordinary-zeta branches, but it is now tied to the Euler–Blaschke source which is all-pass at the critical line and already carries the live source/reserve package.

## 5. Source-convolved deformation

Define

\[
\boxed{
 K_{4,\tau}=b_4*J_{4,\tau},
}
\tag{L-33802.9}
\]

so its Dirichlet multiplier is

\[
 K_{4,\tau}(s)=B_4(s)J_{4,\tau}(s).
\]

From (L-33802.2),

\[
\boxed{
 K_{4,0}=b_4,
 \qquad
 K'_{4,0}=q_4=b_4*\Lambda_4,
 \qquad
 K''_{4,0}=t_4=b_4*C_4.
}
\tag{L-33802.10}
\]

Thus the bare source, RH-sensitive first current, and higher Selberg current are the first three jets of one explicit deformation, rather than unrelated fields.

## 6. Physical deformation energy

Use the atomized carry-window physical localization and bilinear form of PR #337 `L-32710`. For any multiplier `F`, write `P_F` for its localized physical field and

\[
 \mathfrak B_J(F,G)
 =\langle \mathcal P_F,\mathcal P_G\rangle_{J,I}.
\]

Define

\[
\boxed{
 \mathscr E_{4,J}(\tau)
 =\mathfrak B_J(K_{4,\tau},K_{4,\tau})
 =\|\mathcal P_{K_{4,\tau}}\|_{J,I}^2.
}
\tag{L-33802.11}
\]

For each fixed finite/regularized block, coefficientwise differentiation and Plancherel give

\[
\boxed{
 \mathscr E'_{4,J}(0)
 =2\operatorname{Re}\mathfrak B_J(q_4,b_4),
}
\tag{L-33802.12}
\]

and

\[
\boxed{
 \mathscr E''_{4,J}(0)
 =2\mathfrak B_J(q_4,q_4)
 +2\operatorname{Re}\mathfrak B_J(t_4,b_4).
}
\tag{L-33802.13}
\]

## 7. The product-source block is exactly this curvature

PR #337 `L-32710` writes the localized source-convolved reflected Selberg identity as

\[
 \mathfrak P_J
 -2\operatorname{Re}\mathfrak B_J(B_4C_4,B_4)
 =2\mathfrak B_J(B_4L_4,B_4L_4).
\]

But

\[
 B_4L_4=q_4,
 \qquad
 B_4C_4=t_4.
\]

Comparing with (L-33802.13) gives the exact resummation

\[
\boxed{
 \mathfrak P_J
 =\mathscr E''_{4,J}(0).
}
\tag{L-33802.14}
\]

Therefore the formerly opaque **product-source block** is precisely the second deformation curvature of one physical Q=4 Jordan energy.

This is an exact independent-frequency statement. No diagonal-frequency collapse and no rowwise replacement occurs.

## 8. Finite physical coefficient form

Because

\[
 \mathbf1*b_4=e_4,
\]

atomized carry localization of `K_(4,tau)` has the interval-kernel coefficient sequence

\[
\boxed{
 c_{4,\tau}=e_4*J_{4,\tau}.
}
\tag{L-33802.15}
\]

Thus the whole curvature can also be replayed from one explicit finite coefficient family. Its first jets are

\[
 c_{4,0}=e_4,
 \qquad
 c'_{4,0}=e_4*\Lambda_4=c_4,
 \qquad
 c''_{4,0}=e_4*C_4.
\]

This gives a direct finite artifact target for future exact curvature experiments or symbolic factorization.

## 9. What this changes — and what it does not

Before this lemma the remaining reflected accounting contained three separately named objects:

```text
product-source block;
RH-sensitive current square;
higher-current x bare-source cross term.
```

Equations (L-33802.10)--(L-33802.14) show that all three are the second-order jets of one source-complete deformation.

A future completion may therefore attack one scalar/Hilbert curvature theorem for `mathscr E_(4,J)(tau)` rather than separately place infinitely many logarithmic-current terms.

However, coefficientwise positivity of `J_(4,tau)` does **not** imply convexity of `mathscr E_(4,J)(tau)`. The inverse source `b_4` remains signed and the RH-sensitive denominator remains in the deformed field. No sign of (L-33802.14) is asserted here.

In particular this lemma does not convert the positive Jordan source into an RH proof by itself.

## 10. Proof boundary

Closed exactly, subject to review:

1. positive odd-prime local deformation;
2. explicit nonnegative prime-two deformation coefficients;
3. complete coefficientwise positivity of `J_(4,tau)`;
4. recovery of `Lambda_4,C_4` as its first two jets;
5. source-convolved jet identities `b_4,q_4,t_4`;
6. exact physical-energy differentiation;
7. product-source block = second Q=4 Jordan energy curvature;
8. finite interval-kernel coefficient family `e_4*J_(4,tau)`.

Open:

1. a sign or source-bound upper theorem for the curvature `mathscr E''_(4,J)(0)`;
2. no-double-spend use of the cofinal row reserve;
3. coefficient-one neutral recurrence;
4. RH.
