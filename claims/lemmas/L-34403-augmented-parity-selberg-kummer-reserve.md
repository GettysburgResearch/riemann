# L-34403 — Augmenting one missing unit can only increase the parity-paired Selberg–Kummer reserve

Claim ID: `L-34403`  
Title: The one-step augmented carry rows arising at real physical positions inherit at least the ordinary parity-paired reserve, so the cofinal parity Selberg–Kummer theorem extends to the complete continuous carry field  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #337 `L-32704`; PR #341 `L-34001`; endpoint Selberg identity  
Scope: deterministic generalized-prime/Selberg carry reserve on ordinary and augmented rows; no source-current upper estimate or RH conclusion

## 1. Augmented carry rows

Let

\[
n=j+k+1,
\qquad j,k\ge0,
\]

and define for every `d>=2`

\[
\boxed{
\chi^*_{n,d}(j,k)
=\left\lfloor{n\over d}\right\rfloor
 -\left\lfloor{j\over d}\right\rfloor
 -\left\lfloor{k\over d}\right\rfloor.
}
\tag{L-34403.1}
\]

This is the three-child carry for the partition

\[
n=j+k+1,
\]

because `floor(1/d)=0` for `d>=2`.

Put

\[
m=k+1.
\]

The ordinary binary split `n=j+m` has carry

\[
\chi_{n,d}(j)
=\left\lfloor{n\over d}\right\rfloor
 -\left\lfloor{j\over d}\right\rfloor
 -\left\lfloor{m\over d}\right\rfloor.
\]

Since

\[
\left\lfloor{m\over d}\right\rfloor
-\left\lfloor{m-1\over d}\right\rfloor
=\mathbf1_{d\mid m},
\]

one has the exact augmentation identity

\[
\boxed{
\chi^*_{n,d}(j,k)
=\chi_{n,d}(j)+\mathbf1_{d\mid m}.
}
\tag{L-34403.2}

No estimate enters this formula.

## 2. Parity-paired current and forcing

Retain PR #337's two generalized-prime systems

\[
\Lambda_+,
\qquad
\Lambda_-=\chi_2\Lambda_+,
\qquad
\chi_2(d)=(-1)^{v_2(d)},
\]

and

\[
C_\pm=\Lambda_\pm\log+\Lambda_\pm*\Lambda_\pm.
\]

For an ordinary row define

\[
P_\pm=\sum_{d\le n}\Lambda_\pm(d)\chi_{n,d}(j),
\qquad
S_\pm=\sum_{d\le n}C_\pm(d)\chi_{n,d}(j).
\tag{L-34403.3}
\]

For the augmented row define `P_+^*,P_-^*,S_+^*,S_-^*` by replacing `chi` with `chi*`.

Also put the endpoint divisor sums

\[
H_\pm(m)=\sum_{d\mid m}\Lambda_\pm(d),
\qquad
K_\pm(m)=\sum_{d\mid m}C_\pm(d).
\tag{L-34403.4}
\]

Equation (L-34403.2) gives exactly

\[
\boxed{
P_\pm^*=P_\pm+H_\pm(m),
\qquad
S_\pm^*=S_\pm+K_\pm(m).
}
\tag{L-34403.5}

## 3. Endpoint Selberg equality

For an ordinary endpoint split `(m,1)`,

\[
\chi_{m,d}(1)=\mathbf1_{d\mid m}
\qquad(d\ge2).
\]

The generalized Selberg endpoint identity used in PR #337 therefore gives, separately in the two parity systems,

\[
\boxed{
K_+(m)=H_+(m)^2,
\qquad
K_-(m)=H_-(m)^2.
}
\tag{L-34403.6}

This is an exact coefficient identity, not an inequality.

## 4. Reserve increment

Define

\[
\mathcal R=P_+^2+P_-^2-S_+-S_-,
\]

and

\[
\mathcal R^*=(P_+^*)^2+(P_-^*)^2-S_+^*-S_-^*.
\]

Using (L-34403.5)--(L-34403.6), the endpoint squares cancel identically:

\[
\boxed{
\mathcal R^*-\mathcal R
=2\left[P_+H_+(m)+P_-H_-(m)\right].
}
\tag{L-34403.7}

It remains only to sign this cross term.

## 5. Parity orthogonalization signs the cross term

Use PR #337's decomposition

\[
P_+=A+R,
\qquad
P_-=A-R,
\tag{L-34403.8}
\]

where

\[
A=O+E\ge0,
\qquad R\ge0
\]

are respectively the odd-prime-plus-even-dyadic current and the odd-dyadic current.

Apply the same decomposition to the endpoint divisor sums:

\[
H_+(m)=B+C,
\qquad
H_-(m)=B-C,
\tag{L-34403.9}
\]

where `B,C>=0`: `B` is the endpoint odd-prime plus even-two-adic generalized-prime mass and `C` is the endpoint odd-two-adic mass.

Therefore

\[
\begin{aligned}
P_+H_+ +P_-H_-
&=(A+R)(B+C)+(A-R)(B-C)\\
&=2AB+2RC\\
&\ge0.
\end{aligned}
\tag{L-34403.10}
\]

Substitution into (L-34403.7) proves

\[
\boxed{
\mathcal R^*\ge\mathcal R.
}
\tag{L-34403.11}

Thus inserting the missing unit child can only **increase** the complete parity-paired Selberg–Kummer reserve.

## 6. Continuous physical carry positions

PR #341 `L-34001` uses

\[
\mathcal C(X/d,\theta)
=\left\lfloor{X\over d}\right\rfloor
 -\left\lfloor{\theta X\over d}\right\rfloor
 -\left\lfloor{(1-\theta)X\over d}\right\rfloor.
\]

Let

\[
n=\lfloor X\rfloor,
\quad
j=\lfloor\theta X\rfloor,
\quad
k=\lfloor(1-\theta)X\rfloor.
\]

Because the two child arguments sum to `X`, exactly one of the following holds:

```text
j+k=n     ordinary binary row;

j+k=n-1   augmented row of Section 1.
```

Moreover for every integer `d`,

\[
\left\lfloor{X\over d}\right\rfloor=\left\lfloor{n\over d}\right\rfloor,
\]

and likewise for the two children. Hence the entire real physical carry field is literally one of these two finite row types.

PR #337 `L-32704` proves cofinally

\[
\mathcal R\ge0
\]

for every ordinary row. Equation (L-34403.11) therefore yields

\[
\boxed{
P_+^*(X,\theta)^2+P_-^*(X,\theta)^2
\ge
S_+^*(X,\theta)+S_-^*(X,\theta)
}
\tag{L-34403.12}

for every sufficiently large real `X` and every `0<=theta<=1`, including every one-step augmented cell.

## 7. What this closes

The parity-paired Selberg–Kummer reserve no longer has an integer-row versus real-physical-position gap. The exact physical/carry placement of PR #341 may use the cofinal parity reserve on the complete continuous carry-position field without an unproved interpolation or collar sign.

This theorem does **not** turn the deterministic generalized-prime reserve into an upper bound for the source-convolved RH-sensitive current. That independent-frequency/no-double-spend composition remains the conclusion-producing step.

## 8. Proof boundary

Closed exactly:

1. augmented carry = ordinary carry + one endpoint divisor column;
2. endpoint generalized Selberg equality;
3. exact reserve increment formula;
4. nonnegative parity-orthogonalized cross term;
5. augmented reserve dominates ordinary reserve;
6. extension of PR #337's cofinal row theorem to all real physical carry positions.

Still open:

1. source-convolved independent-frequency current upper estimate;
2. coefficient-one neutral recurrence;
3. RH.
