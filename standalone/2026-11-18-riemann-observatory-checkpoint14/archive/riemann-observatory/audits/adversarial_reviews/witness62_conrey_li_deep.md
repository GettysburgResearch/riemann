# Conrey–Li's de Branges positivity counterexamples

I read all ten pages of arXiv:math/9812166v1, including both proofs in §2, the four counterexamples in §3, the Sarnak remark in §4, and the Mathematica appendix. This is a whole-preprint reading with a focused reconstruction of the counterexamples. Journal metadata is available for the same work. The published typeset text was outside the passage comparison. [Primary preprint](https://arxiv.org/pdf/math/9812166v1) [Journal metadata](https://doi.org/10.1155/S1073792800000489)

## Entire-function shift form

In Theorem 1, \(E\) is entire with no real zeros, \(|E(\bar z)|<|E(z)|\) in the upper half-plane, \(E^\#(z)=\epsilon E(z-i)\) with \(|\epsilon|=1\), and \(|E(x+iy)|\) strictly increasing for \(y>0\) at every real \(x\). The kernel is
\[
K_E(w,z)=\frac{E(z)\overline{E(w)}-E^\#(z)E(\bar w)}{2\pi i(\bar w-z)},\qquad E^\#(z)=\overline{E(\bar z)}.
\]
The assumed form is \(\Re\langle F,F(\cdot+i)\rangle\ge0\) on the domain where both entire functions belong to \(\mathcal H(E)\). The proof uses (2.3) to place the zero kernel in that domain. Cauchy–Schwarz for the symmetrized semidefinite form then gives the zero location \(\Im w=-1/2\) and the necessary sign
\[
\Re K_E(w,w+i)=\Re\frac{\overline{E'(w)}E(w+i)}{2\pi i}\ge0.
\]

Use \(E(z)=X(1-iz)\), with \(X(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\) or \(X(s)=(4/\pi)^{s/2}\Gamma((s+1)/2)L(s,\chi_4)\). Here \(\chi_4\) is the real primitive odd character modulo four. The functional equations give the vertical shift identity for \(E^\#\). The real symmetry and the pairing in the reported zero products, together with \(0<\Re\rho<1\), give the stated Hermite–Biehler and monotonicity conditions. One can reflect \(E\) to the product evaluated at \(iz\) when verifying the inequalities for absolute values. Comparing at \(y\) and \(-y\) gives factors \((\Re\rho\pm y)^2+(\Im\rho-x)^2\) after reindexing conjugate zeros. Fixed positive \(y\) gives the strict inequality by one strictly greater factor and nondecreasing remaining ratios, with upper-half-plane nonvanishing from the zero-free region. The same factor comparison for \(0<y_1<y_2\) gives monotonicity.

For a certified critical-line zero \(\rho=\tfrac12+it\), set \(w=i(\rho-1)=-t-i/2\). We have \(E'(w)=-iX'(\rho)\) and \(E(w+i)=X(\rho+1)\). Since \(X\) is real-valued on the critical line, \(X'(\rho)\) is purely imaginary. Consequently the real kernel sign is \(-\Re[X'(\rho)X(\rho+1)]/(2\pi)\). Conrey and Li evaluate the numerator in their §3.1 (3.2) and §3.2 following (3.7). We independently find opposite endpoint signs for the real critical-line values on each of these exact rational intervals of half-width \(10^{-20}\). Realness gives a zero by continuity. The interval derivative product strictly excludes zero throughout its corresponding box, so no zero index or numerical uniqueness assumption is needed. For \(\chi_4\), the root number in the real functional equation is \(+1\), as also follows by evaluating it at \(1/2\), where the alternating series for \(L(1/2,\chi_4)\) is strictly positive.

| Function | Center of zero interval | Certified open enclosure for \(-\Re[X'(\rho)X(\rho+1)]\) |
|---|---:|---:|
| \(\zeta\) | \(111.029535543169674524656\) | \((-5.390,-5.388)\cdot 10^{-69}\) |
| \(L(\cdot,\chi_4)\) | \(67.6369208635460683980549\) | \((-2.311,-2.309)\cdot 10^{-45}\) |

At an actual zero in each interval, \(K_E(w,\cdot)\) and its positive \(i\)-shift belong to \(\mathcal H(E)\) by (2.3), and the real form at that vector equals the negative kernel sign. This gives an explicit domain-level failure for both spaces.

## Reciprocal-function kernel shift

Theorem 2 takes \(W\) analytic and zero-free in the upper half-plane and assumes a linear \(T:\mathcal F(W)\to\mathcal F(W)\) with \(TK_W(w,\cdot)=K_W(w+i,\cdot)\) for every \(\Im w>0\), where \(K_W(w,z)=W(z)\overline{W(w)}/[2\pi i(\bar w-z)]\). Its numerical-range hypothesis is \(\Re\langle F,TF\rangle\ge0\) for all \(F\). Under the hypothesis, the symmetrized kernel is positive semidefinite. Normalizing it by \(W+W(\cdot+i)\) gives the shifted Hardy kernel multiplied by \(1-B(z)\overline{B(w)}\), where \(B=(W-W(\cdot+i))/(W+W(\cdot+i))\). Kernel vectors restricted to \(\Im w>0\) span densely in the Hardy space on \(\Im z>-1/2\) by the identity theorem. The kernel contraction extends there, and its adjoint supplies the contractive analytic multiplier \(B\) there. The Cayley transform gives the claimed nonnegative real part of \(W(z)/W(z+i)\). Also \(W(z+i)\) is analytic there by the original domain of \(W\), so this gives the claimed analytic extension of \(W\).

For \(W(z)=1/X(1-iz)\), both \(W(w)\) and \(W(w+i)\) are nonzero at the tested \(w\). With \(w=-t+i\eta\) and \(s=1+\eta+it\), the kernel quotient is \(W(w)/W(w+i)=X(s+1)/X(s)\). The printed numerical examples evaluate \(q=X(s)/X(s+1)\). They give the same sign since \(\Re(1/q)=\Re(q)/|q|^2\). The two exact \(t\) values are 282 and \(8714.2=43571/5\), from §3.1 (3.4) and the example after §3.2 (3.8).

| Function | \(\eta\) | Certified open enclosure for \(\Re q\) |
|---|---:|---:|
| \(\zeta\) | \(0\) | \((-0.000131958,-0.000131956)\) |
| \(\zeta\) | \(10^{-6}\) | \((-0.000131764,-0.000131763)\) |
| \(L(\cdot,\chi_4)\) | \(0\) | \((-0.000422341,-0.000422340)\) |
| \(L(\cdot,\chi_4)\) | \(10^{-6}\) | \((-0.000422314,-0.000422313)\) |

The strictly interior \(\eta=10^{-6}\) cases give an immediate negative value of the numerical-range form on a single kernel, since
\[
\Re\langle K_W(w,\cdot),TK_W(w,\cdot)\rangle
=\frac{|W(w+i)|^2}{2\pi(2\Im w+1)}\Re\frac{W(w)}{W(w+i)}.
\]
Only the prescribed action on kernel vectors enters this failure. Conrey and Li introduced the numerical examples. Their §4 also credits Peter Sarnak with a nonnumerical argument using values of \(\log\zeta\) and gives the analogous attribution for Dirichlet functions. The finite certificates here do not use those logarithmic branches or density results.

## Reproduction and scope

The certificates use python-flint 0.9.0 at 256 bits. Real positive bases use the real logarithm in the completed functions. The Hurwitz expression for the Dirichlet case follows from \(L(s,\chi_4)=4^{-s}(\zeta(s,1/4)-\zeta(s,3/4))\), initially for \(\Re s>1\) and then by continuation. Thus \(X\) employs \((4\pi)^{-s/2}\) with the Hurwitz difference. The code uses exact rational input points and ball evaluation of gamma, zeta, and Hurwitz zeta. First Taylor coefficients of complex ball series give the derivative enclosure uniformly in the input box. The replay record contains the full balls tested for strict sign. These computations rely on the ball-arithmetic implementation in FLINT rather than a proof-assistant kernel. Both model obstructions are unconditional and concern the specified shifts.

From the repository root, create an isolated environment and replay the pinned package. The audit used the existing interpreter at `/tmp/witness62-conrey/bin/python`.

```sh
python -m venv /tmp/witness62-conrey
/tmp/witness62-conrey/bin/python -m pip install python-flint==0.9.0
/tmp/witness62-conrey/bin/python experiments/code/witness62_conrey_li_deep.py
```

The final command reproduces the JSON on standard output. [Replay script](../../experiments/code/witness62_conrey_li_deep.py) [Ball enclosures](../../experiments/results/witness62_conrey_li_deep.json)
