# L-103104 — The half-completed near-collision has one Möbius owner after gcd grouping

**Status:** PROVED EXACT SOURCE REDUCTION.

Expand

\[
h_U(m)=\sum_{\substack{d\mid m\\d>U}}\mu(d)\eta(m/d).
\]

Substitution into the off-diagonal form of `L-103102` gives a finite sum over tail divisors `d,e>U` and positive renewal indices. Since `mu(d)mu(e)` vanishes unless both are squarefree, write

\[
d=ga,\qquad e=gb,\qquad (a,b)=1,
\qquad \mu^2(gab)=1.
\]

Then

\[
\boxed{\mu(d)\mu(e)=\mu(a)\mu(b)=\mu(ab).}
\tag{L-103104.1}
\]

The common gcd `g` is sign-free. All half-divisor coefficients `eta` are nonnegative. Choosing the unique largest prime `p=P^+(ab)` and writing `ab=pc` gives

\[
\boxed{\mu(ab)=-\mu(c).}
\tag{L-103104.2}
\]

Hence the terminal near-collision packet has exactly:

```text
one sign-free gcd core g;
one unique largest prime p;
one remaining cofactor sign mu(c);
positive half-divisor renewal weights;
one explicit signed ratio-local kernel R(log(m/n)).
```

This is the ratio-geometry analogue of the single-wing owner reduction in PR #696. It aligns `HCNC103100` with the live largest-prime and phase-owner machinery without replacing the signed autocorrelation by an unsigned large sieve.
