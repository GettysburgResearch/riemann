# L-34001 — The true Q=4 physical current is exactly the carry row of the source current

Claim ID: `L-34001`  
Title: The corrected Q=4 centered-prefix physical current is the ordinary binary carry transform of `q_4=b_4*Lambda_4`, with no extra source convolution or floor transform  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 corrected coefficient `c_4=e_4*Lambda_4`; PR #337 source current `q_4=b_4*Lambda_4`; `1*b_4=e_4`  
Scope: exact integer physical/carry identification; no sign, norm, recurrence, or RH conclusion

## 1. Q=4 source identities

Retain

\[
 q_4=b_4*\Lambda_4,
 \qquad
 \mathbf 1*b_4=e_4,
 \qquad
 c_4=e_4*\Lambda_4.
\]

Associativity gives the exact coefficient identity

\[
\boxed{
 \mathbf 1*q_4
 = (\mathbf1*b_4)*\Lambda_4
 =e_4*\Lambda_4
 =c_4.
}
\tag{L-34001.1}
\]

This is a Dirichlet-convolution identity. It must not be confused with ordinary prefix summation of `q_4`.

## 2. Ordinary prefix of `c_4` is the floor transform of `q_4`

Put

\[
 G_4(N)=\sum_{m\le N}c_4(m),
 \qquad N\ge0,
\]

with `G_4(0)=0`. By (L-34001.1),

\[
\begin{aligned}
 G_4(N)
 &=\sum_{m\le N}\sum_{d\mid m}q_4(d)\\
 &=\sum_{d\le N}q_4(d)
   \left\lfloor\frac Nd\right\rfloor.
\end{aligned}
\]

Hence

\[
\boxed{
G_4(N)=\sum_{d\le N}q_4(d)\lfloor N/d\rfloor.
}
\tag{L-34001.2}
\]

No approximation, PNT input, or cutoff convention enters.

## 3. Exact physical current = exact carry current

For an integer split

\[
 n=j+k,
 \qquad 0\le j\le n,
\]

the correctly typed Q=4 physical current of PR #325/#337 is

\[
 Q_4^{\rm phys}(n,j)
 =G_4(n)-G_4(j)-G_4(k).
\]

Insert (L-34001.2). Since

\[
 \chi_{n,d}(j)
 =\left\lfloor\frac nd\right\rfloor
 -\left\lfloor\frac jd\right\rfloor
 -\left\lfloor\frac kd\right\rfloor,
\]

one obtains

\[
\boxed{
 Q_4^{\rm phys}(n,j)
 =\sum_{d\le n}q_4(d)\chi_{n,d}(j).
}
\tag{L-34001.3}
\]

Thus, in the notation of PR #337 `L-32711`,

\[
\boxed{Q_4^{\rm phys}(n,j)=Q_e=\mathcal L_e(q_4).}
\tag{L-34001.4}
\]

This identifies two quantities which had previously been carried in parallel notation.

## 4. Consequences for existing Q=4 theorems

Equation (L-34001.4) means that all rowwise statements already proved for the source current `Q_e` apply to the true integer physical current without any new transference constant. In particular the source-curvature coordinate

\[
 \mathcal A_e
 =R_4(n,j)+Q_e^2-Y_eT_e
\]

of `L-32711` may be written exactly as

\[
\boxed{
 \mathcal A_e
 =R_4(n,j)+|Q_4^{\rm phys}(n,j)|^2-Y_eT_e.
}
\tag{L-34001.5}
\]

Likewise the product-source curvature on an unaugmented integer binary row is

\[
\boxed{
 2\left(|Q_4^{\rm phys}(n,j)|^2+Y_eT_e\right).
}
\tag{L-34001.6}
\]

The continuous carry-position cells require the explicit endpoint augmentation of PR #326 `L-32412`; (L-34001.3) is the exact interior binary-row identity.

## 5. Scope firewall

This lemma does **not** say

```text
c_4 is the carry coefficient.
```

That statement is false and was corrected on PR #325/#337. The correct chain is

```text
source current q_4
   -- Dirichlet convolution by 1 --> c_4
   -- ordinary prefix --> G_4
   -- additive prefix defect --> Q_4^phys

which equals

q_4
   -- one binary carry transform --> Q_4^phys.
```

There is exactly one floor/carry transform, not two.

## 6. Proof boundary

Closed exactly:

1. `1*q_4=c_4`;
2. prefix/floor identity (L-34001.2);
3. physical-current/carry-row equality (L-34001.3);
4. identification with the source-curvature row coordinate of `L-32711`.

Open:

1. a proof-closing quantitative estimate for the current;
2. the global reflected/scattering recurrence;
3. RH.
