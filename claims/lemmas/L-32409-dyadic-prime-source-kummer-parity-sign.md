# L-32409 — Dyadic prime-source Kummer defect has an exact parity sign

Claim ID: `L-32409`  
Title: The carry image of `(epsilon-2 delta_2)*Lambda` is positive on every odd parent and every even-even split, and negative only on even parents with two odd children  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: Kummer/Legendre valuation identity; Vandermonde's identity  
Scope: one split-row source theorem; no global prime Riesz sign or RH conclusion

## 1. The pole-cancelled prime source

Define

\[
\boxed{
 \lambda^{(2)}
 = (\varepsilon-2\delta_2)*\Lambda.
}
\tag{L-32409.1}
\]

Its Dirichlet series is

\[
 \sum_{n\ge1}{\lambda^{(2)}(n)\over n^s}
 = (1-2^{1-s})
 \left[-{\zeta'\over\zeta}(s)\right].
\tag{L-32409.2}
\]

This is exactly the arithmetic source of the dyadic prime criterion `T-32404`.

For a split `n=j+k`, put

\[
 \chi_{n,j}(q)
 =\left\lfloor{n\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{k\over q}\right\rfloor.
\]

Define its dyadic prime-source charge

\[
 \mathcal K_2(n,j)
 =\sum_q\lambda^{(2)}(q)\chi_{n,j}(q).
\tag{L-32409.3}
\]

## 2. Exact factorial formula

Kummer/Legendre gives

\[
 \sum_q\Lambda(q)\chi_{n,j}(q)
 =\log\binom nj.
\tag{L-32409.4}
\]

For the dilated source,

\[
\begin{aligned}
 \sum_q(\delta_2*\Lambda)(q)\chi_{n,j}(q)
 &=\sum_m\Lambda(m)\chi_{n,j}(2m)\\
 &=\log{\lfloor n/2\rfloor!\over
          \lfloor j/2\rfloor!\lfloor k/2\rfloor!}.
\end{aligned}
\tag{L-32409.5}
\]

The last identity is again Legendre, since

\[
 \left\lfloor{n\over2m}\right\rfloor
 =\left\lfloor{\lfloor n/2\rfloor\over m}\right\rfloor.
\]

Therefore

\[
\boxed{
 \mathcal K_2(n,j)
 =\log\binom nj
 -2\log{\lfloor n/2\rfloor!\over
          \lfloor j/2\rfloor!\lfloor k/2\rfloor!}.
}
\tag{L-32409.6}

Thus `exp(K_2)` is a rational factorial ratio and its sign can be decided exactly.

## 3. Even parent, even children: positive

Let

\[
 n=2m,
 \qquad j=2a,
 \qquad k=2b,
 \qquad a+b=m.
\]

Then

\[
\boxed{
 e^{\mathcal K_2(2m,2a)}
 ={\binom{2m}{2a}\over\binom ma^2}.
}
\tag{L-32409.7}

Vandermonde gives

\[
 \binom{2m}{2a}
 =\sum_r\binom mr\binom m{2a-r}
 \ge\binom ma^2.
\]

Hence

\[
\boxed{
 \mathcal K_2(2m,2a)\ge0,
}
\tag{L-32409.8}
\]

with strict inequality for every nontrivial even-even split.

## 4. Odd parent: positive

Let `n=2m+1`. By symmetry assume the even child is `j=2a`; then the other child is `2(m-a)+1`. Equation (L-32409.6) gives

\[
\boxed{
 e^{\mathcal K_2(2m+1,2a)}
 ={\binom{2m+1}{2a}\over\binom ma^2}.
}
\tag{L-32409.9}

Pascal and Vandermonde give

\[
 \binom{2m+1}{2a}
 \ge\binom{2m}{2a}
 \ge\binom ma^2.
\]

Therefore every nontrivial split of an odd parent has

\[
\boxed{
 \mathcal K_2(2m+1,j)>0.
}
\tag{L-32409.10}

## 5. Even parent, odd children: sharp negative theorem

Let

\[
 n=2m,
 \qquad j=2a+1,
 \qquad k=2b+1,
 \qquad a+b=m-1.
\]

Then

\[
\boxed{
 R_{m,a}:=e^{\mathcal K_2(2m,2a+1)}
 ={\binom{2m}{2a+1}
   \over
   m^2\binom{m-1}{a}^2}.
}
\tag{L-32409.11}

The ratio of consecutive terms is exact. Writing `b=m-1-a`,

\[
\boxed{
 {R_{m,a+1}\over R_{m,a}}
 ={(a+1)(2b+1)\over b(2a+3)}.
}
\tag{L-32409.12}

This ratio is at most one exactly when

\[
 a+1\le b.
\]

The sequence is symmetric under `a <-> b`; hence its maximum occurs at the two boundary values `a=0,m-1`. At the boundary,

\[
\boxed{
 R_{m,0}={2\over m}.
}
\tag{L-32409.13}

Consequently

\[
\boxed{
 R_{m,a}\le{2\over m}.
}
\tag{L-32409.14}

Thus:

- for `m=1` (`n=2`), the unique odd-odd split has positive charge `log 2`;
- for `m=2` (`n=4`), the two odd-odd endpoint-neighbor splits have zero charge;
- for every `m>=3` (`n>=6`), every odd-odd split has strictly negative charge.

More quantitatively,

\[
\boxed{
 \mathcal K_2(2m,2a+1)
 \le\log(2/m)<0
 \qquad(m\ge3).
}
\tag{L-32409.15}

## 6. Exact sign table

The complete nontrivial split geometry is therefore

```text
parent n odd:                  K_2 > 0;
parent n even, children even:  K_2 > 0;
parent n=2:                    K_2 > 0;
parent n=4, children odd:      K_2 = 0;
parent n>=6 even, children odd:K_2 < 0.
```

The entire negative source cone is one parity sector.

## 7. Connection to the dyadic prime RH criterion

For any exact signed carry flow `d` with load target `w`, finite interchange gives

\[
 \sum_q\lambda^{(2)}(q)w(q)
 =\sum_{(n,j)}d(n,j)\mathcal K_2(n,j).
\tag{L-32409.16}
\]

For the critical target, the left side is exactly `D_Lambda(X)` of `T-32404`.

Thus the prime criterion can be attacked entirely in finite fragmentation geometry:

```text
positive source charge:
    every odd parent and every even-even split;

negative source charge:
    only the even-parent / odd-odd sector.
```

A successful proof still has to show that the complete exact critical flow can pay that negative parity sector before any norm or absolute value is taken. This theorem does not assert such a global transference.

## 8. Proof boundary

Closed exactly:

- the factorial form of the pole-cancelled prime source;
- positive even-even charge;
- positive odd-parent charge;
- the sharp `2/m` upper bound for every odd-odd ratio;
- the complete parity sign classification.

Open:

- a source-complete parity transport or cycle identity which makes the total charge positive;
- eventual positivity of `D_Lambda`;
- RH.
