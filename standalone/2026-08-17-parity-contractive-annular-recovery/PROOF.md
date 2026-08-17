# Recovery publication: parity-contractive annular factor-67 successor

This is a fresh deterministic recovery publication. It is **not claimed to be byte-identical** to the unavailable earlier packet whose links failed.

The mathematical change relative to PR #556 is structural. PR #561's parity cocycle is treated as binding. Rather than attempting to orient each terminal leaf positively, the successor uses PR #559's positive `5:3` base dictionary to define an unsigned source mass, proves a complete `P_61` signed-bias interval, recombines all low-scale children before observation, and retains high-scale odd-history children with their negative sign. The factor-67 child mass bound then gives a strict `1/960` hereditary margin.

```text
parity cocycle                         binding
5:3 base dictionary                   exact positive
complete P61 scalar bias              candidate certificate
low-child recombination               exact
high-child unsigned mass              <1/8
parity contraction margin             1/960
scalar annular positivity             candidate complete
Mellin numerator noncancellation      exact
RH                                    proposed / unestablished
```

# R-97100 — Parity-blind terminal substitution is forbidden

For paired positive sources `S(E,O)=(O,E)` and signed observation

\[
\mathcal O(E,O)=R(E)-R(O),
\]

a rough history of length `h` contributes

\[
\mathcal O(S^hP)=(-1)^h\mathcal O(P).
\]

Therefore a canonical terminal realization cannot be installed on an odd-history leaf without reversing its signed datum. This packet does not use parity-blind terminal substitution, fixed-product three-knot packets, or an all-integer rough reservoir. The replacement is quantitative: the odd-history contribution is retained with its negative sign and bounded by a strict hereditary contraction.

# L-97100 — Positive 5:3 scalar source and complete P61 bias certificate

Put

\[
\mathcal A_X=5[c_X(2)-c_{X/4}(2)]+3[c_X(3)-c_{X/4}(3)].
\]

The unsieved scalar dictionary is

\[
q_\star(2)=15,\quad q_\star(3)=6,\quad q_\star(4)=3,
\quad q_\star(m)=6\ (m\ge5),
\]

and is coefficientwise positive. Define

\[
H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
\qquad
A_\star(x)=\sum_{m\ge2}\frac{q_\star(m)}{\sqrt m}H_x(m).
\]

For `P=P_61`, define

\[
F(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_\star(x/d),
\qquad
M(x)=\sum_{d\mid P}\frac1{\sqrt d}A_\star(x/d).
\]

The controlling finite/directed certificate asserts

\[
0\le F(x)\le M(x)\qquad(1\le x<67),
\]

and

\[
\boxed{\frac1{40}M(x)\le F(x)\le\frac18M(x)\qquad(x\ge67).}
\]

Every `d|P_61` color is kept inside the grouped finite-Euler packet until this scalar observation is applied. This certificate is the first hostile reconstruction target; the lightweight replay checks only its contract and downstream rational algebra.

# L-97101 — Exact low-child recombination and parity-covariant current bounds

For a rough prime `p>=67`, put `r=p^{-1/2}` and `y=x/p`. Rough placement exchanges parity channels. The positive nondivisible current is

\[
C_{x,p}=P_x-rSA_pP_y.
\]

Its unsigned mass and signed scalar are

\[
m(C_{x,p})=M(x)-rM(y),
\qquad
f(C_{x,p})=F(x)+rF(y).
\]

When `x,y>=67`, write

\[
a=F(x)/M(x),\quad b=F(y)/M(y),\quad q=rM(y)/M(x).
\]

Then

\[
\frac{f(C_{x,p})}{m(C_{x,p})}=\frac{a+qb}{1-q}.
\]

Using `1/40<=a,b<=1/8` and `0<=q<1/8` gives

\[
\boxed{
\frac1{40}m(C_{x,p})\le f(C_{x,p})\le\frac9{56}m(C_{x,p})<\frac16m(C_{x,p}).
}
\]

For `\lambda_i=r_is_{i-1}` and `\alpha_i=r_i\lambda_i`, a child with scale below `67` is never observed separately. Its current and final child recombine before signed observation:

\[
\boxed{
\lambda_i(P_x-r_iSA_{p_i}P_{x/p_i})+
\alpha_iSA_{p_i}P_{x/p_i}=\lambda_iP_x.
}
\]

Thus outer parity never requires a reversed terminal Hall realization.

# L-97102 — Strict parity-contractive factor-67 induction

Let `H_x` be the total unsigned mass of recursive children whose scale remains at least `67`. The exact factor-67 coefficients and monotonicity of the positive source mass give

\[
H_x<\frac18M(x).
\]

The complete current satisfies

\[
\frac1{40}(M(x)-H_x)\le f(C_x)\le\frac16(M(x)-H_x).
\]

Every recursive child is parity-swapped. Assuming inductively

\[
0\le f(P_y)\le\frac16m(P_y),
\]

the exact parent identity is

\[
f(P_x)=f(C_x)-\sum_i\alpha_if(P_{x/p_i}).
\]

Consequently

\[
\begin{aligned}
f(P_x)
&\ge\frac1{40}(M(x)-H_x)-\frac16H_x\\
&>\frac7{320}M(x)-\frac1{48}M(x)
=\boxed{\frac1{960}M(x)>0}.
\end{aligned}
\]

The upper bound `f(P_x)<=M(x)/6` follows from the current upper bound and subtraction of nonnegative recursive terms. Rank decreases by a factor at least `67`, while all low children are recombined exactly, so the induction is finite. Therefore

\[
\boxed{\mathcal A_X\ge0\qquad(X\ge1).}
\]

# T-97101 — Parity-contractive annular Mellin–Landau RH candidate

The Mellin transform is

\[
\int_1^\infty\mathcal A_X X^{-s-1}\,dX
=(1-4^{-s})\left[
\frac6{s^2}-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}
\right],
\qquad z=s+\frac12.
\]

The factor `1-4^{-s}` has no zero in `Re s>0`. The finite numerator vanishes only when `2^{-z}=1` or `2^{-z}=2`, which force `Re z=0` or `Re z=-1`; neither can cancel a nontrivial zero in `0<Re z<1`.

Landau's real-abscissa theorem applied to the proposed nonnegative scalar kernel gives the proposed conclusion `RH`.

**Scientific status:** candidate complete unconditional RH proof proposal; independent reconstruction of the complete `P_61` bias certificate and imported Mellin–Landau hypotheses is required. RH is not treated as established by publication.
