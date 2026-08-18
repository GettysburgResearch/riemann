# L-97610 — Repaired complete P61 bias for the 5:3 annular scalar

Status: **PROVED DIRECTED/ANALYTIC**
RH: not assumed.

Let

\[
q_\star(2)=15,
\quad q_\star(3)=6,
\quad q_\star(4)=3,
\quad q_\star(m)=6\ (m\ge5),
\]

\[
H_x(n)=\min(\log4,\log(x/n))_+,
\qquad
A_\star(x)=\sum_{m\ge2}\frac{q_\star(m)}{\sqrt m}H_x(m),
\]

and, for `P=P_61`,

\[
F(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_\star(x/d),
\qquad
M(x)=\sum_{d\mid P}\frac1{\sqrt d}A_\star(x/d).
\]

Then

\[
0\le F(x)\le M(x)\qquad(1\le x<67),
\]

and

\[
\boxed{\frac1{42}M(x)\le F(x)\le\frac18M(x)\qquad(x\ge67).}
\]

The stronger lower constant `1/40` in PR #565 is false. At `x=184`,

```text
40F-M < -18.1144,
42F-M >  3.2727.
```

The proof checks every real activation cell through `10^6` with 256-bit outward MPFR intervals. The tail uses the Euler-ramp expansion with remainder `<5Y^(-3/2)`. This reconstruction corrects the rational log/sqrt helpers so the quotient is divided outward before the monotone function, and computes coverage/tail penalties by outward interval operations.

This theorem is a finite-`P_61` scalar theorem. It does not prove the completed rough-history common-source inequality.
