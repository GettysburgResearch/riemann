# Canonical cusp endpoints: all six native weight classes

Status: PROPOSED SOURCE-SPECIFIC THEOREM; independent frozen-SHA review required.
Exactly five new files; no EP, UQ, CZ or CF source is edited.
This extends EP's effective and asymptotic conclusions to EVERY even integer
weight k>=65536. It is not an optimal-onset, simplicity, uniqueness, global-zero
classification, new-automorphic-family, or zeta/RH claim.

The complete EP source at 27496745df9dd49fcde17699d333a54cf8620772 and complete
CF family at b69c854d9e3dd1db7b82d95fe6f032fe47d5306b are pinned as ten literal
Git blobs. EP supplies the already written analytic endpoint argument;
this note verifies the genuinely new uniform modular hypotheses, rather than
treating the residue-class extension as automatic.

## 1. The actual source and theorem

Use CF's canonical decomposition
\[
 k=12d+r,\quad r\in\{0,4,6,8,10,14\},\quad
 M_r=E_4^aE_6^b,\qquad r=4a+6b,\quad0\le a\le2,\ 0\le b\le1.
                                                               \tag{AW1}
\]
The respective (a,b) pairs are (0,0),(1,0),(0,1),(2,0),(1,1),(2,1).
For k congruent to 2 modulo12, r is FOURTEEN, not two, and
d=(k-14)/12=dim S_k. Every even k>=65536 belongs to exactly one class and d>=2.

Let q=exp(2*pi*i*z), ell(f)=[q]f, W=ker ell, and take the ACTUAL CF g_1,
\[
 h_k=\Delta E_4^{\,3d-3+a}E_6^b,\qquad\ell(h_k)=1.        \tag{AW2}
\]
This is not generally Miller f_1 or f_d. Retain the original Petersson
G(f)=integral_F y^(k-2)|f|^2 dx dy, completed period I(s), restriction I_W,
and canonical quotient Q_k=det I/det I_W. Set G_h=G(h_k)>0.

**Effective theorem.** For every even k>=65536, every nonzero f in W,
and every real s in [1-18/k,1),
\[
 I_s(f,f)/G(f)\le-k/144+60<0,\qquad
 I_{1-18/k}(h_k,h_k)/G_h\ge {773k\over72000}-{2019\over100}>0.
                                                               \tag{AW3}
\]
Therefore Q_k has an uncancelled odd-order real-zero pair in (1-18/k,1)
and (0,18/k). I_W has no real zeros on either interval; at such a quotient
zero the full period matrix has corank one and its nullvector has nonzero ell.

The first covered weights by class are:

| r | a | b | first k>=65536 | d |
|---|---|---|---|---|
| 0 | 0 | 0 | 65544 | 5462 |
| 4 | 1 | 0 | 65536 | 5461 |
| 6 | 0 | 1 | 65538 | 5461 |
| 8 | 2 | 0 | 65540 | 5461 |
| 10 | 1 | 1 | 65542 | 5461 |
| 14 | 2 | 1 | 65546 | 5461 |

65536 is a SUFFICIENT threshold, not the first true zero onset.
Nothing here certifies 6144 for the canonical quotient.

**Uniform asymptotic theorem.** Fix a compact real interval J contained
in (0,24), c in J, L_k=log(k/(4*pi)), B_0=(gamma-log(4*pi))/2, and
Lambda(u)=pi^(-u/2)Gamma(u/2)zeta(u). Uniformly over ALL six classes,
\[
\begin{split}
 {Q_k(1-c/k)\over G_h}
 ={}&k\left({1\over24}-{1\over2c}\right)
 -\left({c\over24}+{1\over2}\right)L_k\\
 &+B_0-{1\over24}-{c\Lambda'(2)\over2\pi}
 +O_J(\log^2 k/k).                                      \tag{AW4}
\end{split}
\]
For each sufficiently large even k an uncancelled real-zero pair exists with
\[
 1-s_k={12\over k}+{288\log k+O(1)\over k^2}.             \tag{AW5}
\]
Writing C_12=B_0-1/24-6Lambda'(2)/pi, the more precise version is
\[
 k(1-s_k)=12+{288L_k-288C_{12}\over k}
                         +O(\log^2 k/k^2).             \tag{AW6}
\]
Every real-zero sequence whose c=k(1-s) stays in a fixed compact subset of
(0,24) obeys AW6. There is NO residue-dependent constant in this expansion.
The error constants and sufficiently-large thresholds can be chosen jointly
for the six classes, but are NOT explicitly certified equal to65536.
No uniqueness, simplicity or control of sequences escaping c->0 or c->24
is inferred from this asymptotic statement.

## 2. The extra E6 bound on the whole fundamental domain

Put rho=|q|=exp(-2*pi*y). EP/CZ give rho<1/100 on F,
|Delta|<1, |E4|<4, and |E4-1|<=480rho. The only added primitive is E6.

For each positive integer n,
\[
 \sigma_5(n)=n^5\sum_{e\mid n}e^{-5}
 \le\zeta(5)n^5<\tfrac54 n^5,
\]
because sum_(e>=2)e^(-5)<integral_1^infinity t^(-5)dt=1/4.
Repeated application of rho*d/drho to (1-rho)^(-1) gives exactly
\[
 {\sum_{n\ge1}n^5\rho^n\over\rho}
 =S_5(\rho)={1+26\rho+66\rho^2+26\rho^3+\rho^4\over(1-\rho)^6}.
                                                               \tag{AW7}
\]
The power series has positive coefficients, so S_5 is increasing on [0,1).
Exactly S_5(1/100)=422208670000/313826716467, and
5*422208670000<8*313826716467. Thus S_5(1/100)<8/5 applies throughout
0<=rho<=1/100. It can also be verified by cross-multiplication of the displayed
integer polynomials. Using E6=1-504 sum sigma_5(n)q^n gives
\[
 |E_6-1|\le504\cdot\tfrac54\cdot\tfrac85\,\rho=1008\rho,
 \qquad |E_6|<1+1008/100={277\over25}<16.                 \tag{AW8}
\]
These are simultaneous bounds for all x, not imaginary-axis estimates.
There is no assumption that E6 has no zeros on the low part of F.

## 3. Same low-mass and high-mass hypotheses, with exact exponent accounting

Let p=3d-3+a. The source weight identity gives
2p=k/2-6-3b<=k/2. On all of F,
\[
 |h_k|^2\le4^{2p}16^{2b}
       =2^{\,4p+8b}=2^{\,k-12+2b}\le2^k.                \tag{AW9}
\]
Here Delta's modulus was bounded by1. The E6 factor cannot be discarded,
but its exact extra exponent is harmless because b is0 or1.

For the high part let Y=log k, so rho<=k^(-6) using pi>3.
The squared Delta product contributes an error48rho/(1-rho).
The 2p copies of E4 contribute at most480(2p)rho<=240k rho.
The 2b copies of E6 contribute at most1008(2b)rho<=2016rho. Hence set
\[
 u={48\rho\over1-\rho}+240k\rho+2016\rho
 \le(240k+2065)\rho\le289k\rho\le289k^{-5}.               \tag{AW10}
\]
The first bound uses48/(1-rho)<49. The second uses2065<=49k,
which certainly holds for every k>=65536.

Bernoulli's product lower bound and log(1+t)<=t now give
\[
 1-u\le|h_k/q|^2\le e^u\le(1-u)^{-1}.                    \tag{AW11}
\]
For the lower bound, the three factors are bounded below by
1-48rho/(1-rho), 1-240k rho and 1-2016rho, respectively.
They are nonnegative because u<1/1000 at the high cutoff; their product
is at least1-u. Thus no zero-free assumption about E4 or E6 away from this
high region has entered the argument.

Define M_k(beta) and A_k(beta) exactly as EP14, now with the witness AW2.
The proof of EP16--EP17 uses only AW9, AW11, the actual weight k and the
same full cusp rectangle. It therefore proves, for EVERY even k>=65536,
\[
 {998\over1000}\le {M_k(\beta)\over A_k(\beta)}
 \le{1003\over1000}\quad(0\le\beta\le1).                 \tag{AW12}
\]
To make the transfer explicit: the low integrals are <=(2log k)^k and
(log k)^k; both divided by A_k(beta) are below
3^16 k^2(96log k/k)^k<1/1000 by EP16's ALL-integer monotonicity proof.
Above the cutoff AW10 supplies the same u<1/1000. Neither step required
k to be divisible by12, so even weights in the other five classes meet
exactly the same numerical bounds.

## 4. Effective native noncancellation across all classes

EP8's Parseval/integration-by-parts proof concerns ANY weight-k cusp form
with its first N-1 coefficients zero. It applies to all of the actual W
with N=2 in every residue class. EP11--EP12's completed-zeta bounds
|Lambda(1-2epsilon)+1/(2epsilon)|<=19 and
|Lambda(2-2epsilon)-pi/6|<=48epsilon are independent of the modular witness.
Thus the entire EP13 proof, including its explicit error60, applies verbatim
at 0<epsilon<=18/k and yields the first bound in AW3.

For the witness, AW12 allows the same Gamma probability Jensen lower bound
as EP18; EP8 with N=1 and concavity give the same actual-Petersson upper bound:
\[
 {M_k(1-18/k)\over G_h}\ge{49\over50}{k\over4\pi},
 \qquad {M_k(18/k)\over G_h}\le{101\over100}.              \tag{AW13}
\]
The constants C>=19pi/120, D>=-k/36-19 with D<0, and |R|<1 in the unchanged
Eisenstein expansion then prove EP20's SAME positive reserve, the second
bound in AW3. This is a uniform all-weight estimate, not period sampling.

In the actual adapted basis (h_k,f_2,...,f_d), the first coefficient is1
and W is unchanged. Its block D=I_W is negative definite, so the Schur
identity gives Q_k=I(h_k,h_k)-b^tD^(-1)b>=I(h_k,h_k)>0 at1-18/k.
CF4's unchanged positive endpoint residue gives Q_k(s)<0 as real s->1-.
Denominator nonvanishing along the interval makes the sign-change zero
genuine and uncancelled; analytic real zeros force an odd-order choice.
The block rank argument gives corank one and ell nonzero on its nullvector.
Entrywise CF reflection transfers denominator nonvanishing and the same
zero order to the reflected interval. No indefinite minimization claim is used.

## 5. Complex high-cusp control and the actual Schur correction

For any fixed integer A>0, now cut at Y=A log k. Product telescoping gives
control of the COMPLEX ratio, not just its modulus:
\[
 |h_k/q-1|\le e^v-1,\qquad
 v={24\rho\over1-\rho}+480p\rho+1008b\rho
 \le(120k+1033)\rho=O(k\rho).                            \tag{AW14}
\]
Indeed apply |product(1+z_i)-1|<=exp(sum|z_i|)-1 to the24 Delta copies,
p E4 copies and b E6 copies, then pass to the convergent infinite product.
For small v, e^v-1<=2v. The bound is uniform in all six (a,b), in x,
and in y>=Y. Thus delta_Y=sup|h_k/q-1|=O(k exp(-2*pi*Y)),
with a residue-independent implicit constant.

For each fixed J compactly contained in (0,24), the full W coercivity
EP21 remains uniform in the six classes because it uses only the weight
and Fourier gap. On the high rectangle q is exactly orthogonal in x to
every f in W for every weight depending only on y. Therefore EP23--EP24
apply with AW14:
\[
 {|I_{1-c/k}(h_k,f)|\over\sqrt{G_hG(f)}}
 \ll_{J,A}k^{3-2\pi A}
 +kY\sqrt{\,O_A(k^2(8\pi eA\log k/k)^k)}.                \tag{AW15}
\]
Here the harmless O(exp(-2*pi*Y)) Fourier-remainder term is absorbed by
the first bound for k>=1. The bound holds uniformly over ALL f in W,
not just its displayed basis. Given fixed M, choose fixed A>(M+3)/6.
This gives O_(J,M)(k^(-M)) with no dimension or residue factor.

Consequently the actual inverse-form estimate EP25 proves
\[
 0\le Q_k(1-c/k)-I_{1-c/k}(h_k,h_k)
       \ll_{J,M}k^{-2M-1}G_h.                            \tag{AW16}
\]
No free coefficients, changed norm, generic replacement flag, or unproved
small Schur correction is being substituted.

## 6. Why neither leading nor constant location depends on the residue

AW9 and AW14 also upgrade AW12, for each fixed N, to
M_k(beta)=A_k(beta)(1+O_N(k^(-N))) uniformly0<=beta<=1 and over all six classes,
by taking A sufficiently large. The integrated nonconstant Eisenstein term
is O_N(k^(-N))G_h by the same high/low split.

The resulting scalar comparison is the SAME A_k(beta)=
Gamma(k-1+beta)/(4pi)^(k-1+beta). There is no r-dependent shift in its exponent:
the period uses y^(k-2) and the q-leading coefficient of every h_k is1.
EP26's shrinking-interval digamma proof therefore gives uniformly
\[
 {M_k(c/k)\over G_h}=1+{cL_k\over k}+O_J(\log^2 k/k^2),
\]
\[
 {M_k(1-c/k)\over G_h}
 ={k-1-cL_k\over4\pi}+O_J(\log^2 k/k).                   \tag{AW17}
\]
Multiplying by the unchanged C,D Laurent expansions in EP27 and using
AW16 proves AW4, including its constant term, with no residue correction.

For clarity, existence and localization follow without a derivative estimate:
1/24-1/(2c) has opposite signs on either side of12 and derivative1/288 there.
Uniform AW4 and W nonvanishing give a real sign-change zero in any fixed
small c interval around12 for sufficiently large k. At every such zero,
first c=12+O(log k/k); substitution back into AW4 gives AW6 and hence AW5.
If a zero sequence stays in any compact subset of(0,24), the same leading
equation first forces c->12. The finite number of residue choices, together
with the uniform envelopes already proved, permits common constants and
thresholds. It does not turn these non-effective remainders into the explicit
K threshold or prove uniqueness/simplicity.

## 7. Finite replay and boundaries

The producer replays AW7 by an exact differential recurrence, checks its
rational endpoint bound and all six exponent/onset ledgers, and constructs
native q-prefixes of Delta^j E4^(3(d-j)+a)E6^b. Small controls in every class
are compared with authenticated CF primitives; independent test recurrences
also cover the six first effective weights. It replays EP's unchanged
integer/Gamma-Jensen reserve ledger and symbolic12/288 location coefficients.
No Gamma, zeta, E6, logarithm, period, eigenvalue or zero is sampled numerically.

Arithmetic is MIXED with CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL,
without rounding. Strict bool/int separation, 4096-bit arithmetic outputs,
128-bit radial rational inputs, q order<=8, control weight<=2^20,
2,000,000 charged local units, separately capped authenticated-source work,
and 2,000,000-byte/20,000-node JSON caps fail closed. These machine caps do
not bound the written all-weight theorem. All ten source blobs, four artifact
seals, typed reconstruction and canonical payload digest are enforced.

The ring, dimension and Eisenstein definitions are the classical CF1 inputs,
not new modular families. Euler summation, Gamma/Jensen and special-function
references remain those explicitly proved/cited in frozen EP. This extension
adds only the source-specific E6 envelope and uniform six-class verification;
there is no claim of new abstract zero or asymptotic theory, exhaustive novelty,
RH positivity, an optimal threshold, or a global divisor classification.

Release requires named tests and producer --check in normal and -O Python,
both emission modes in both modes, Ruff, full authoring-base diff checks and
fresh exact-SHA replay. Independent proof review remains necessary.
