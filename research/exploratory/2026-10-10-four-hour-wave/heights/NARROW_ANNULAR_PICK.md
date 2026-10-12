# Narrow annuli and a polynomial maximum certify global finite Pick orders

Status: proposed theorem under explicit published and classical inputs;
independent review required. RH remains unproved. The reviewed order-twelve
packet is preserved separately in [ANNULAR_GLOBAL_PICK.md](ANNULAR_GLOBAL_PICK.md).

## 1. Quantitative result

Use the complete xi squared-pole source and the arbitrary-node moment
congruence (1)--(5) of `ANNULAR_GLOBAL_PICK.md`. Import the same published
verified critical-line height `H=3*10^12`, Trudgian argument estimate, and
classical Hadamard and zero-count identities. Suppose all horizontal zero
depths satisfy `a<=A<=1/2`.

For an even integer `8<=n<=350`, the following sufficient inequality gives
global positivity for every Pick packet of at most `n` positive nodes:

\[
 \boxed{204800 A^2 n^8/H^2<1.}
 \tag{N1}
\]

The few elementary auxiliary inequalities used below all hold throughout
`8<=n<=350` at the specified `H`, and are checked exactly in the replay.
Consequently:

* The **classical critical strip**, `A=1/2`, certifies **global order 320**,
  with sufficient ratio `34359738368/54931640625<2/3`.
* An independently accepted uniform **quasi-RH strip**, `A=3/8`, certifies
  **global order 350**, with sufficient ratio `0.720600125<3/4`.
  This second statement explicitly depends on accepting that imported strip
  theorem; the first does not.

Distinct-node packets are positive definite; repeated-node packets are
positive semidefinite. Nodes may be arbitrarily close, arbitrarily large, or
at arbitrarily different scales. The result does not assert all orders.

## 2. Annular moment test without a Vandermonde condition number

Partition the complete high-height source into annuli

\[
 (L,rL],\qquad r=1+1/n,
 \quad L=H r^k,\quad k=0,1,2,\ldots.
 \tag{N2}
\]

Fix any `n` distinct positive nodes. As in the earlier congruence put
`rho_i=x_i^2/L^2`, `D=prod(1+rho_i)`, and

\[
 \phi(z)=D/\prod_i(\rho_i+z).
\]

For an annular pole write

\[
 z=s/L^2=v+i\delta,\quad
 v=(b^2-a^2)/L^2,\quad \delta=2ab/L^2.
\]

The normalized source moments are `sum w phi(z) z^j`.
Their two Hankel blocks have size `n/2`, with quadratic forms

\[
 \sum_\alpha w_\alpha\psi_k(z_\alpha)P(z_\alpha)^2,
 \qquad \psi_k(z)=z^k\phi(z),\quad k=0,1,
 \tag{N3}
\]

where `P` is any nonzero real polynomial of degree at most `n/2-1`.
The sums are real after conjugate grouping. Positivity of (N3) for every
such `P` proves positive definiteness of both moment blocks and hence of the
Pick packet. This quadratic-form test avoids conditioning a monomial frame.

Set

\[
 J=[1-A^2/L^2,r^2],\quad h=|J|/2\ge1/n,
 \quad M=\max_{v\in J}|P(v)|>0.
\]

Use the classical Markov inequality, after scaling `J` to `[-1,1]`, in the
iterated form

\[
 \max_J|P^{(j)}|\le(d^2/h)^j M,
 \qquad d=n/2.
 \tag{N4}
\]

It applies also when the actual polynomial degree is smaller than `d`.
Writing `D_P=d^2/h<=n^3/4`, the finite Taylor series yields, on every vertical
segment above `J`,

\[
 |P^{(j)}(v+iy)|\le D_P^j e^{D_P|y|}M.
 \tag{N5}
\]

Here `|delta|<=3A/L<=3/(2L)` and
`D_P|delta|<=3n^3/(8L)<1/2`; since `exp(1/2)<2`, we obtain

\[
 |P|\le2M,\quad |P'|\le(n^3/2)M,
 \quad |P''|\le(n^6/8)M.
 \tag{N6}
\]

This is a finite-degree polynomial bound. It makes no assumption about a
complex maximum principle for the complete xi function.

## 3. Uniform control of the rational weight on vertical segments

For `L>=H` and `n<=350`,

\[
 v\ge1023/1024,\qquad v\le(1+1/n)^2\le81/64.
\]

Since the denominators increase in absolute value on vertical segments,

\[
 |\phi(v+iy)|\le\phi(v)
 \le(1024/1023)^n<2.
\]

Also `|v+iy|<3`, so `|psi_k|<=6`. Logarithmic differentiation, using
`|rho_i+z|>=|z|`, gives the deliberately rounded bounds

\[
 |\psi_k'|\le12n,\qquad |\psi_k''|\le24n^2,
 \qquad k=0,1.
 \tag{N7}
\]

For example the unrounded bounds are
`6(n+1)(1024/1023)` and
`6(n+1)(n+2)(1024/1023)^2`, which are below those in (N7) for `n>=8`.

For real projected `v`,

\[
 \phi(v)\ge r^{-2n}>1/8,
 \qquad \psi_k(v)>1/16.
 \tag{N8}
\]

Indeed `(1+1/n)^n<e<11/4`, whose square is below `8`, and
`v>=1023/1024` handles `k=1`. These bounds are uniform over all node scales.

## 4. Conjugate-pair error as a polynomial quadratic form

Put `f(z)=psi_k(z)P(z)^2`. From (N6)--(N7),

\[
 |f''|\le
 (96n^2+48n^4+6n^6)M^2<7n^6M^2
 \qquad(n\ge8).
 \tag{N9}
\]

The four terms are respectively `psi'' P^2`, `4 psi' P P'`,
`2 psi (P')^2`, and `2 psi P P''`.
Conjugation cancels the linear term. Taylor's integral remainder therefore
bounds the deviation from the positive real-projection contribution by

\[
 \boxed{|\Re f(v+i\delta)-f(v)|
 \le32 A^2 n^6 M^2/L^2.}
 \tag{N10}
\]

This follows from `delta^2<=9A^2/L^2` and
`(7/2)*9<32`. It is a bound per unit squared-pole weight, including both
members of a conjugate pair with their actual multiplicities.

## 5. A maximum supplies a source reserve without zero-spacing assumptions

At a point where `|P|=M`, one of the two directions inside `J` has length
at least `h`. The Markov derivative bound gives a one-sided real interval
`I` of length

\[
 \ell=h/(2d^2)\ge2/n^3
\]

on which `|P|>=M/2`.
To ensure every zero in a height band has its real projection in `I`, choose
its squared-height interval inside

\[
 [\inf I+A^2/L^2,\sup I].
\]

This interval lies in `[1,r^2]`. Since `A^2/L^2<1/n^3`, the corresponding
interval of height ratios has length at least

\[
 \frac{\ell-A^2/L^2}{2r}>1/(3n^3).
\]

It therefore contains an open height band of width `L/(4n^3)` inside
`(L,rL)`. Every critical or off-line zero in that band has its real projected
`v` in `I`. This construction is allowed to depend on `P`; the source count
lower bound holds for every such band.

The source-qualified argument/theta estimate in section 7 of the earlier
packet gives

\[
 N_+(\beta L)-N_+(\alpha L)
 >\left(\frac{25L}{896n^3}-1\right)\log L
 >\frac{L\log L}{100n^3},
 \tag{N11}
\]

whenever `beta-alpha=1/(4n^3)` and `1<=alpha<beta<=2`.
The sufficient scalar condition is
`H*(25/896-1/100)>n^3`, verified even at `n=350`.
As before, inward nonzero endpoints followed by one-sided limits give the
open-band bound with all multiplicities.

The band has squared-pole weight more than `L log L/(50n^3)`. Equations
(N8) and `P^2>=M^2/4` give the lower real-projection reserve

\[
 \boxed{\sum w\psi_k(v)P(v)^2
 > L\log L\,M^2/(3200n^3).}
 \tag{N12}
\]

All other projected contributions are nonnegative.

## 6. The narrow annular count completes domination

The same argument/theta count, now in the upper direction, gives

\[
 W((L,rL])=2[N_+(rL)-N_+(L)]<2L\log L/n.
 \tag{N13}
\]

For detail, the main term increment is below `L log L/(6n)` because
`pi>3` and `r<2pi`. The two endpoint errors sum to less than `log L`.
The condition `L>6n/5` makes their sum below `L log L/n`.
One-sided limits again handle endpoints, and assign the upper endpoint to
this annulus consistently.

Multiplying (N10) by (N13) and comparing with (N12) bounds the relative
error by

\[
 \boxed{\text{relative error}\le204800 A^2 n^8/L^2.}
 \tag{N14}
\]

Under (N1) every annulus in (N2) has both Hankel quadratic forms strictly
positive for every nonzero `P`. Its Pick packet is therefore positive
definite at every set of `n` distinct positive nodes. Summing the complete
annuli and the verified low critical source proves section 1. Absolute
source convergence justifies the sum; at least one annulus already supplies
strict positivity. Smaller packets and repeated nodes follow as in the
order-twelve packet.

## 7. Scope and relation to the recent strip theorem

This theorem only uses the complete xi source, classical or improved
horizontal strip, complete local zero counts, and the published verified
critical range. It does not use positivity of every individual off-line
quartet: those sources remain indefinite at sufficiently high order.
The many projected source locations in each annulus supply the reserve.

The narrow-band argument proves a finite quantitative hierarchy. Its bound
has `n^8`, so increasing the order eventually exhausts the known verified
height. The claim does not become all-order positivity or RH by taking a
limit in `n` at fixed `H`.

The imported `A=3/8` hypothesis is the symmetric consequence, using the
functional equation, of a uniform zero-free half-plane `Re(s)>7/8`.
The exact version and provenance of that new theorem belong to the wave's
literature audit. This file treats it as an explicit additional input and
keeps the classical `A=1/2` order-320 conclusion independent of it.

[verify_narrow_annular.py](verify_narrow_annular.py) records all exact scalar
inequalities, several rational complex polynomial controls, and the input
proof hashes. It does not replay Markov's theorem, Trudgian's published
argument estimate, the complete Hadamard product, or the verified height.
