# Exact row growth, conformal acceleration, and the unpaid source bound

Status: **PROPOSED proofs; not independently reviewed.** Local labels `BCG-1` through `BCG-5` belong only to this packet. No canonical theorem IDs are allocated. The implication to RH remains conditional on the source bound in section 8.

## 1. Source-defined moments and admissible products

First work with a nonconstant genus-zero product

$$F(u)=F(0)\prod_j(1+u/a_j),\qquad F(0)>0,$$

where the nonempty multiset is conjugation invariant, all multiplicities are positive integers, `Re(a_j)>0`, and `sum_j 1/|a_j|<infinity`. Finite products are allowed. No exponential prefactor is permitted. Fix `v>0`, put `h=F'/F`, and define, without supplying zeros as input,

$$m_n(v)=\frac{(-1)^n v^{n+1}}{n!}h^{(n)}(v),\qquad n\geq0.$$

The product gives the absolutely convergent identity

$$m_n=\sum_j k_j^{n+1},\qquad k_j=\frac{v}{v+a_j}.$$

Here `sum |k_j|=:C_v<infinity`, `|k_j|<1`, `|1-k_j|<1`, and `m_0>0` because every `Re(k_j)>0`. For an infinite multiset its only node accumulation point is zero. For each fixed polynomial define the linear functional `L_v(t^n)=m_n`. This is NOT presumed positive.

The Riemann specialization is

$$F(u)=\mathfrak X(u)=\xi\!\left(\frac12+\sqrt{u+\frac14}\right),\qquad
\xi(s)=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s).$$

The functional equation makes `F` entire of order at most `1/2`; its zero parameters are `a_rho=rho(1-rho)` for all upper-half-plane nontrivial zeros, with multiplicity. An off-line quartet contributes two conjugate parameters, not four. The classical genus-zero product and zero-count growth give the required summability. With `rho=1/2+delta+i*gamma`,

$$a_\rho=\gamma^2+\frac14-\delta^2-2i\delta\gamma.$$

Thus `Re(a_rho)>=gamma^2>0`, and all `a_rho` are positive real exactly when RH holds. These standard analytic inputs are also recorded in PR #790. They do not assume RH. That PR's coordinate `p_n^*` satisfies `m_n=p_{n+1}^*`.

## 2. Signed Bernstein rows and refinement: BCG-1

Define

$$H_{r,b}=\sum_{j=0}^b(-1)^j\binom bj m_{r+j},\qquad
b_{N,r}=\binom Nr H_{r,N-r},\quad 0\leq r\leq N,$$

$$V_N=\sum_{r=0}^N|b_{N,r}|,\qquad
D_N=\sum_{r=0}^N\max(0,-b_{N,r}).$$

All these numbers are real. Direct binomial expansion proves

$$b_{N,r}=\binom Nr\sum_j k_j^{r+1}(1-k_j)^{N-r},\qquad
\sum_r b_{N,r}=m_0,\qquad V_N=m_0+2D_N.$$

Degree elevation gives

$$b_{N,r}=\frac{N+1-r}{N+1}b_{N+1,r}
        +\frac{r+1}{N+1}b_{N+1,r+1}.$$

Taking absolute values and summing proves `V_N<=V_(N+1)`, hence `D_N<=D_(N+1)`. A negative row can never be followed by an entirely nonnegative row. These are linear-algebra identities, not a positivity theorem for the actual source.

## 3. Exact exponential variation rate: BCG-2

Set

$$M(v)=\sup_j\bigl(|k_j|+|1-k_j|\bigr)
     =\sup_j\frac{v+|a_j|}{|v+a_j|}.$$

**Theorem.** For every admissible product and every fixed `v>0`,

$$\boxed{\limsup_{N\to\infty}V_N(v)^{1/N}=M(v).}$$

Moreover `M=1` exactly when all parameters are positive real. If `M>1`, the same exponential rate holds for `1+D_N`.

**Upper bound.** The spectral row formula and the binomial theorem give

$$V_N\leq\sum_j |k_j|\bigl(|k_j|+|1-k_j|\bigr)^N\leq C_vM^N.$$

**Lower bound and cancellation audit.** If every parameter is positive real, every row is nonnegative and `V_N=m_0`, proving the result. Otherwise `M>1`; because the individual ratios tend to one along the infinite tail, their supremum is attained at a finite parameter `a_*`. Put `z_*=a_*/|a_*|`, which is on the unit circle and is not one. Define

$$B_N(z)=\sum_r b_{N,r}z^r=\sum_j k_j(1-k_j+k_jz)^N.$$

Then `|B_N(z_*)|<=V_N`, and

$$|1-k_*+k_*z_*|=\frac{v+|a_*|}{|v+a_*|}=M.$$

Writing `q_j=1-k_j+k_j*z_*`, the ordinary generating function is

$$\sum_{N\geq0}B_N(z_*)w^N=\sum_j\frac{k_j}{1-wq_j}.$$

It is analytic for `|w|<1/M`. At `w_*=1/q_*`, of modulus `1/M<1`, the right side has a genuine pole. Indeed, `q_j->1`; the summable tail is uniformly analytic in a neighborhood of `w_*`, which is not one. The map `k -> 1+(z_*-1)k` is injective. Only repeated copies of the same node can share the pole, and their residue is `-multiplicity*k_*/q_*`, not zero. No assumption about a unique dominant zero or absence of conjugate cancellations is made.

Consequently the Taylor radius is exactly `1/M`. Cauchy--Hadamard yields `limsup |B_N(z_*)|^(1/N)=M`, giving the lower bound. Finally subtracting the constant `m_0` from `V_N` does not alter a rate greater than one. This proves the theorem.

For the actual Riemann source, at ONE fixed `v>0`,

$$\mathrm{RH}\iff
\forall\epsilon>0\ \exists C_\epsilon<\infty\ \forall N\geq0:
V_N(v)\leq C_\epsilon e^{\epsilon N}.$$

This does not prove the bound. It states exactly what a proposed source estimate must achieve.

A useful source-side identity, initially near `w=0`, is

$$\boxed{\sum_{N\geq0}B_N(z)w^N=
\frac{v}{1-w}\,h\!\left(v\frac{1-wz}{1-w}\right).}$$

It follows by summing the geometric series or expanding the derivatives defining `m_n`.

## 4. Chebyshev comparison, not a claimed new criterion: BCG-3

Let `T_N` be the classical Chebyshev polynomial of the first kind and put

$$c_N(v)=L_v\!\left[T_N(2t-1)\right]
       =\sum_j k_jT_N(2k_j-1).$$

These are finite linear combinations of `m_0,...,m_N`. Write

$$\eta_j(v)=\frac{2\sqrt v\,|\operatorname{Im}\sqrt{a_j}|}{v+|a_j|},
\qquad R_j(v)=\sqrt{\frac{1+\eta_j(v)}{1-\eta_j(v)}},$$

where `sqrt(a_j)` has positive real part. Each `0<=eta_j<1`, and `R_j->1` in the tail. Define

$$\Gamma_C(v)=\limsup_{N\to\infty}\frac1N\log(1+|c_N(v)|).$$

**Theorem.**

$$\boxed{\Gamma_C(v)=\sup_j\operatorname{artanh}\eta_j(v),
\qquad \log M(v)=\log\cosh\Gamma_C(v).}$$

In particular RH is equivalent to subexponential growth of `c_N` at one fixed scale. Under RH the stronger bound `|c_N|<=m_0` holds at every degree.

**Proof.** Write `x_j=2k_j-1=(v-a_j)/(v+a_j)`. The roots of
`1-2*x_j*w+w^2=0` are reciprocal, and their larger modulus is `R_j`; this follows by factoring them as

$$\frac{\sqrt v+i\sqrt{a_j}}{\sqrt v-i\sqrt{a_j}}
\quad\hbox{and its reciprocal}.$$

The identity `T_N(x)=(r^N+r^(-N))/2`, with `r+r^(-1)=2x`, gives `|T_N(x_j)|<=R_j^N`. Hence `|c_N|<=C_v(sup R_j)^N`.

For the reverse rate use the classical generating function:

$$\begin{aligned}
\mathcal C_v(w)&=\sum_{N\geq0}c_N(v)w^N
 =\sum_j k_j\frac{1-x_jw}{1-2x_jw+w^2}\\
&=\boxed{\frac{m_0}{2}+
\frac{v(1-w)}{2(1+w)}
 h\!\left(v\left(\frac{1-w}{1+w}\right)^2\right).}
\end{aligned}$$

If a parameter is nonreal, the maximal `R_j>1` is attained. Its interior pole `w_*` is neither zero nor `+1` nor `-1`. A shared denominator pole determines `x_j=(w_*+w_*^(-1))/2` uniquely. The numerator there is `(1-w_*^2)/2`, not zero. Repeated parameters add rather than cancel. Since `x_j->-1`, the summable tail is uniformly analytic near that pole. Cauchy--Hadamard therefore proves the claimed rate. If all parameters are real, `x_j` is in `(-1,1)`, so `|c_N|<=sum k_j=m_0` and `Gamma_C=0`.

Finally, with `a=A+iB` and `R=|a|`,

$$|v+a|^2=(v+R)^2-4v(\operatorname{Im}\sqrt a)^2,$$

so `(v+R)/|v+a|=(1-eta^2)^(-1/2)=cosh(artanh eta)`. Taking suprema proves the comparison identity.

The noncancelling-pole/Chebyshev mechanism has close prior literature; see README. The exceptional reverse implication depends on the admissible logarithmic-derivative family. Arbitrary bounded signed moment sequences do not become positive by this argument.

## 5. Optimal scale and a verified-prefix allowance: BCG-4

For a fixed nonreal parameter `a`, both rates are maximized at `v=|a|`, since

$$\frac{2\sqrt v}{v+|a|}\leq\frac1{\sqrt{|a|}},$$

with equality exactly at that scale. If `theta=arg(a)`, the individual optimal rates are

$$\Gamma_{C,a}^{\rm opt}=\operatorname{artanh}\bigl(\sin(|\theta|/2)\bigr),
\qquad \log M_a^{\rm opt}=-\log\cos(\theta/2).$$

For `rho=1/2+delta+i*gamma`, fixed nonzero `delta`, and `gamma->infinity`, these are respectively asymptotic to

$$\frac{|\delta|}{\gamma}
\quad\hbox{and}\quad \frac{\delta^2}{2\gamma^2}.$$

At fixed `v`, the respective asymptotics are `2*sqrt(v)*|delta|/gamma^2` and `2*v*delta^2/gamma^4`. Chebyshev removes the quadratic loss in small displacement. This is an exponential-rate comparison, NOT a universal first-crossing bound: residues, other modes, and cancellation still affect finite detection. Changing `v` also changes the required source derivatives; optimal recentering is not a free operation on one finite jet.

Assume, as a separately imported premise `V_H`, that all zeros with `0<gamma<=H` are on the line, where `H>=1`. For the rest, `A=Re(a)>=gamma^2`, `|B|<=gamma`, and

$$|a|-A=\frac{B^2}{|a|+A}\leq\frac12.$$

Therefore

$$\boxed{\log M(v)\leq\frac12\log\left(1+\frac{v}{(v+H^2)^2}\right)
\leq\frac{v}{2(v+H^2)^2}\leq\frac1{8H^2}.}$$

Also `|Im sqrt(a)|<=1/2`, so

$$\boxed{\Gamma_C(v)\leq\operatorname{artanh}\frac{\sqrt v}{v+H^2}
\leq\operatorname{artanh}\frac1{2H}.}$$

The Platt--Trudgian result permits the imported choice `H=3*10^12`. It was not rerun here. These are arbitrarily long-degree estimates with a SMALL POSITIVE exponential allowance, not a zero allowance. A fixed verified height cannot be sent to infinity. Neither bound closes RH.

## 6. Sharp conditioning in raw derivative coordinates: BCG-5

Suppose the supplied primitive moments `m_0,...,m_N` have independent absolute errors bounded by `epsilon`.

For the Bernstein row map the exact operator norm from this error box to row `l^1` is

$$\boxed{\sup_{\|\delta m\|_\infty\leq\epsilon}
\sum_{r=0}^N|\delta b_{N,r}|=3^N\epsilon.}$$

The triangle inequality gives the upper bound `sum_r binom(N,r)*2^(N-r)*epsilon=3^N*epsilon`. It is attained by `delta m_j=(-1)^j*epsilon`, since then
`delta b_(N,r)=(-1)^r*binom(N,r)*2^(N-r)*epsilon`.

For the Chebyshev trace the corresponding sharp bound is

$$\boxed{\sup_{\|\delta m\|_\infty\leq\epsilon}|\delta c_N|
=T_N(3)\epsilon
=\frac{(3+2\sqrt2)^N+(3-2\sqrt2)^N}{2}\epsilon.}$$

Indeed `T_N(2t-1)` has all its roots in `(0,1)` and positive leading coefficient, so its monomial coefficients alternate. Their absolute sum is `|T_N(-3)|=T_N(3)`. Alternating primitive errors attain this sum. The displayed closed form follows from the Chebyshev recurrence.

Thus improved spectral sensitivity comes with WORSE raw-moment conditioning. Correlated intervals or a direct source-side algorithm can change the numerical error model, but no such improvement is assumed here. Floating-point signs at high mixed degree do not become certified merely by raising working precision without tracking this loss.

## 7. Exact hostile control inherited from PR #790

The polynomial

$$F_{\rm cf}(u)=(1+u)(1+4u/5+u^2/5)$$

has parameters `1,2+i,2-i`. Its heat density is
`exp(-t)+2*exp(-2t)*cos(t)>0`: use `cos(t)>=0` up to `pi/2`, and `exp(t)>2` thereafter. Consequently its logarithmic derivative is completely monotone at every order. At `v=1`, every `m_n>0`; alternatively, for powers of order at least two, the positive `2^(-n)` dominates the conjugate pair in modulus.

Nevertheless, exactly as recorded in PR #790,

$$H_{0,14}=-\frac{433316717939}{10^{15}}<0.$$

Its variation rate is `M=(1+sqrt(5))/sqrt(10)>1`, and BCG-3 supplies the faster Chebyshev rate. The checker independently reconstructs the inherited witness and tests both coordinate systems, including repeated conjugate parameters. This is a synthetic counterexample to an inference, not a counterexample to RH.

## 8. End-to-end closure attempt and exact stopping point

The proved chain is

```
literal theta/xi source -> derivatives m_n -> c_N or Bernstein rows
-> [UNPROVED: a subexponential source bound at one fixed v]
-> no interior generating-function poles -> all a_rho positive -> RH.
```

We tested three mechanisms for the missing bound.

**Positive heat.** PR #790 gives positivity of the actual heat density, hence positivity of every ordinary `m_n`. Section 7 shows that this entire layer does not imply the required growth bound. Taking absolute values inside the mixed transform discards precisely the needed cancellation.

**Finite zero prefix plus tail.** Section 5 pays explicit global upper rates, but they remain positive for every fixed `H`. Their smallness cannot replace the quantifier “for every epsilon>0.” No cofinal verification premise has been established.

**Direct arithmetic generating function.** For real `u>0`, let
`s=1/2+sqrt(u+1/4)>1`. Then, with all polar terms retained,

$$h(u)=\frac{1}{2s-1}\left[
\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)-\sum_{n\geq2}\frac{\Lambda(n)}{n^s}
\right].$$

Here `psi=Gamma'/Gamma`. The prime series is absolutely convergent in `Re(s)>1`, so this is a genuine local, zero-free-input representation of every finite jet at `v>0`. Insert it into the boxed source formula for `C_v(w)`. The Cayley map `t=(1-w)/(1+w)` sends the unit disk to `Re(t)>0`, and `u=v*t^2` to the slit plane. Near the disk boundary the corresponding `s` approaches the critical line. Absolute convergence of the prime series no longer supplies the required bound there. Analytic continuation of zeta alone does not make its logarithmic derivative pole-free. Assuming that denominator control would assume the desired conclusion.

The concrete next target is therefore to estimate the COMPLETED prime-plus-archimedean coefficients of this exact generating function, preserving their signs, so that for one fixed `v>0`

$$\forall\epsilon>0\ \exists C_\epsilon:\quad |c_N(v)|\leq C_\epsilon e^{\epsilon N}
\quad\text{for every }N.$$

A uniform bound or any polynomial bound would suffice. Neither is proved here. The present advance is a quantitative comparison and error analysis, not an independent arithmetic cancellation estimate.

## 9. Review and computation boundaries

The analytic proofs explicitly handle multiplicities, the infinite tail, exceptional points `w=+/-1`, fixed versus optimized scale, and limsup rather than an unjustified full limit. They require fresh independent review. The rational checker verifies only its stated finite fixtures and algebra; it cannot validate genus-zero theory, an infinite growth rate, the external zero census, or the missing source inequality. No formalization or existing theorem file has been altered.
