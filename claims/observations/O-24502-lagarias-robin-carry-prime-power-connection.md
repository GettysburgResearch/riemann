# O-24502 — Lagarias–Robin and carry share one prime-power geometry

Claim ID: `O-24502`  
Status: `EXACT CONNECTION / RESEARCH OBSERVATION`  
Scope: relation between the imported Lagarias criterion and PR #248  
Issue: #245

The Lagarias criterion and the parabolic carry program look different:

- Lagarias uses the multiplicative divisor sum `sigma(n)` and harmonic numbers;
- the carry route uses average logarithmic binomial coefficients and a prime-ramp LP.

They nevertheless share an exact prime-power linearization.

## 1. Exact prime-power expansion of the Robin functional

Write

\[
n=\prod_p p^{a_p}.
\]

Then

\[
\frac{\sigma(n)}n
=\prod_p\frac{1-p^{-(a_p+1)}}{1-p^{-1}}.
\]

Taking logarithms and expanding `-log(1-x)` gives the absolutely convergent identity

\[
\begin{aligned}
\log\frac{\sigma(n)}n
&=\sum_p\sum_{r\ge1}
 \frac{p^{-r}-p^{-(a_p+1)r}}r\\
&=\boxed{
\sum_{q=p^r}
\frac{\Lambda(q)}{\log q}\,
\frac{1-q^{-a_p}}q.}
\end{aligned}
\tag{O-24502.1}
\]

Thus the logarithmic divisor-sum extremal problem is a positive linear functional of the same prime-power von Mangoldt coordinates that appear in `L-24501`:

\[
J_X(b)=\sum_{q=p^r}\Lambda(q)v_q(b).
\]

The weights differ, but both routes preserve prime powers before any norm or absolute value.

## 2. Colossally-abundant exponent profile

Lagarias records the Alaoglu–Erdos description of a maximizing exponent profile. For generic `epsilon>0`, the exponent of a prime `p` in a maximizer of

\[
\frac{\sigma(n)}{n^{1+\varepsilon}}
\]

is

\[
\boxed{
a_p(\varepsilon)
=
\left\lfloor
\frac{\log(p^{1+\varepsilon}-1)-\log(p^\varepsilon-1)}{\log p}
\right\rfloor-1.}
\tag{O-24502.2}
\]

Consequently the dangerous Robin/Lagarias integers have consecutive-prime support and a smoothly decreasing prime-exponent profile.

## 3. Relevance to the carry route

Equation (O-24502.1) suggests three concrete interfaces.

1. **Prime-power-preserving consumer.** Any carry certificate that controls not only the single ramp weight `q^-1/2 log(X/q)` but a positive cone of prime-power weights can be tested directly against the Robin functional.
2. **Sparse extremal stress test.** Corrections in the carry LP should be projected onto exponent profiles (O-24502.2). A proposed contraction that loses coherent prime-power structure may fail first on these profiles.
3. **Alternative final exposition.** A completed carry proof can feed the square-screw/Landau consumer as currently planned; if a weight-transfer theorem from the ramp cone to (O-24502.1) is later proved, Lagarias supplies a second elementary final criterion.

No such weight-transfer theorem is claimed here. Lagarias does not by itself close PNC, and the imported criterion compresses rather than removes RH difficulty.

## 4. Important scope boundary

The word “elementary” in Lagarias describes the final inequality, not the proof of its equivalence: the source imports Robin's deep extremal divisor-sum theorems. This is analogous to the carry route, whose finite formulation is elementary while its global correction theorem carries the RH burden.
