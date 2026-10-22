# L-32410 — Parity-corrected dyadic prime potential is globally superadditive

Claim ID: `L-32410`  
Title: Subtracting one odd-node logarithm from the dyadic prime floor potential leaves the central-binomial potential, whose split defect is nonnegative everywhere and only logarithmic in parent size  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32409`; Vandermonde's identity; central binomial bounds  
Scope: exact node-potential/carry-dual theorem; no RH conclusion

## 1. Exact floor potential of the dyadic prime source

Retain

\[
 \lambda^{(2)}=(\varepsilon-2\delta_2)*\Lambda.
\]

Its floor potential is

\[
 F_2(n)
 =\sum_{q\le n}\lambda^{(2)}(q)
   \left\lfloor{n\over q}\right\rfloor.
\tag{L-32410.1}
\]

Because `1*Lambda=log`,

\[
 \sum_q\Lambda(q)\left\lfloor{n\over q}\right\rfloor
 =\log(n!),
\]

and

\[
 \sum_q(\delta_2*\Lambda)(q)
 \left\lfloor{n\over q}\right\rfloor
 =\log\left(\left\lfloor{n\over2}\right\rfloor!\right).
\]

Hence

\[
\boxed{
 F_2(n)
 =\log(n!)-2\log\left(\left\lfloor{n\over2}\right\rfloor!\right).
}
\tag{L-32410.2}

In particular,

\[
\boxed{
 F_2(2m)=\log\binom{2m}{m},
}
\tag{L-32410.3}
\]

and

\[
\boxed{
 F_2(2m+1)
 =\log\left[(2m+1)\binom{2m}{m}\right].
}
\tag{L-32410.4}

This is the node-potential version of the parity sign table in `L-32409`.

## 2. One exact parity correction

Define

\[
\boxed{
 G(n)=F_2(n)-\mathbf1_{n\ {m odd}}\log n.
}
\tag{L-32410.5}

Then both parities collapse to one formula:

\[
\boxed{
 G(n)
 =\log\binom{2\lfloor n/2\rfloor}{\lfloor n/2\rfloor}.
}
\tag{L-32410.6}

Thus the entire negative even-parent/odd-child sector of `L-32409` is removed by one explicit boundary potential rather than by rowwise corrections.

## 3. Central binomial coefficients are supermultiplicative

Put

\[
 C_m=\binom{2m}{m},
 \qquad m\ge0.
\]

Vandermonde gives

\[
 \binom{2(a+b)}{a+b}
 =\sum_r\binom{2a}{r}\binom{2b}{a+b-r}
 \ge\binom{2a}{a}\binom{2b}{b}.
\]

Therefore

\[
\boxed{
 C_{a+b}\ge C_aC_b.
}
\tag{L-32410.7}

Also `C_m` is strictly increasing for `m>=0`.

## 4. Global superadditivity

Let `n=j+k` and put

\[
 M=\left\lfloor{n\over2}\right\rfloor,
 \quad
 A=\left\lfloor{j\over2}\right\rfloor,
 \quad
 B=\left\lfloor{k\over2}\right\rfloor.
\]

Always

\[
 M\ge A+B;
\]

indeed equality holds unless both children are odd, in which case `M=A+B+1`.

Using monotonicity and (L-32410.7),

\[
 C_M\ge C_{A+B}\ge C_AC_B.
\]

Taking logarithms gives

\[
\boxed{
 G(n)-G(j)-G(k)\ge0
 \qquad(n=j+k).
}
\tag{L-32410.8}

Thus `G` is a globally superadditive node potential on the complete split graph.

## 5. Logarithmic defect bound

The elementary central-binomial estimates

\[
 {4^m\over2m+1}\le C_m\le4^m
\tag{L-32410.9}
\]

follow because `C_m` is the largest coefficient in `(1+1)^(2m)`.

If `M=A+B`, then

\[
 {C_M\over C_AC_B}
 \le(2A+1)(2B+1).
\]

If `M=A+B+1`, the additional step satisfies `C_(M)<=4C_(M-1)`, so

\[
 {C_M\over C_AC_B}
 \le4(2A+1)(2B+1).
\]

Consequently every split obeys

\[
\boxed{
 0\le G(n)-G(j)-G(k)
 \le2\log(n+1)+\log4.
}
\tag{L-32410.10}

The source defect is logarithmic, not square-root size.

## 6. A genuine Cycle-Debt dual after fixed scaling

Fix a balanced split parameter `eta in (0,1/2)`. PR #272 gives a capacity lower bound

\[
 \omega_{n,j}\ge c_\eta\sqrt n
\]

on every allowed split.

By (L-32410.10), there exists a fixed constant `kappa_eta>0`, depending only on `eta`, such that for every allowed split

\[
\boxed{
 0\le
 \kappa_\eta[G(n)-G(j)-G(n-j)]
 \le\omega_{n,j}.
}
\tag{L-32410.11}

The finitely many small parents are absorbed into the choice of `kappa_eta`; for large `n`, `log n=o(sqrt n)`.

Thus `kappa_eta G` is an explicit feasible bounded-superadditive potential in the exact Cycle-Debt dual cone.

This is stronger than the rowwise sign classification of `L-32409`: the parity-corrected prime source now has one globally legal dual potential.

## 7. Exact increment/source form

The increments of `G` are especially sparse. For `m>=1`,

\[
 G(2m)-G(2m-1)
 =\log{\binom{2m}{m}\over\binom{2m-2}{m-1}}
 =\log\left(4-{2\over m}\right),
\tag{L-32410.12}
\]

whereas

\[
 G(2m+1)-G(2m)=0.
\tag{L-32410.13}

Hence if `b_G` is the unique divisor coefficient sequence of `G`,

\[
 b_G=\mu*a_G,
\]

with

\[
 a_G(2m)=\log(4-2/m)>0,
 \qquad a_G(2m+1)=0.
\tag{L-32410.14}

In the absolute-convergence half-plane its Dirichlet symbol is

\[
\boxed{
 B_G(s)
 ={2^{-s}\over\zeta(s)}
 \left[
 \log4\,\zeta(s)
 -\sum_{r\ge1}{\zeta(s+r)\over r2^r}
 \right].
}
\tag{L-32410.15}

The second form follows from

\[
 \log(4-2/m)
 =\log4-\sum_{r\ge1}{1\over r2^rm^r}.
\]

Thus the corrected potential remains reciprocal-zeta sensitive; superadditivity has not erased the arithmetic pole structure.

## 8. Proof boundary

Closed exactly:

- the dyadic prime floor potential;
- the parity correction to a central-binomial potential;
- global superadditivity by Vandermonde;
- a uniform logarithmic split-defect bound;
- fixed scaling into the Cycle-Debt dual cone;
- the exact sparse increment and Dirichlet-source formulas.

Open:

- a useful one-sided estimate for the pairing of `G` with the critical divergence;
- whether the positive-kernel form in (L-32410.14) yields a cofinal scalar estimate;
- Cycle Debt;
- RH.
