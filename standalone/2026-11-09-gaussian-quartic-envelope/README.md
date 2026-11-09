# Gaussian quartic arena: the reflection exists, but the window is empty

**Status:** exploratory envelope check with a negative outcome for one proposed route. Nothing here proves or improves a zero-free region. RH remains unproved.

**Scope:** the route "amplify the Gaussian Möbius sum with quartic twists, apply row Poisson, reflect, apply a large sieve", tested in the two architectures of the OpenAI quasi-RH papers (mean square, and the three-scale probe).

**Sources and dependencies:**

- [riemann#1019](https://github.com/GettysburgResearch/riemann/pull/1019) at `3bcc1daaeb51c71cb2785b9744cde0d641f68f4c`: `QUARTIC_PHYSICAL_ORIENTATION.md`, `PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md` (its (Q1)–(Q12)), and the imported [riemann#1016](https://github.com/GettysburgResearch/riemann/pull/1016) notes `CORRECTED_QUARTIC_CODEC.md` and `DIRECT_PRINCIPAL_TARGET.md`.
- de Faveri, *Optimal large sieve for fixed order characters*, [arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), Theorem 1.1. Statement read from the arXiv page on 9 November 2026; proof not checked.
- David–Dunn–Hamieh–Lin, [arXiv:2306.11875v4](https://arxiv.org/abs/2306.11875v4), only through the equations quoted in PR 1019. Not re-read here.
- OpenAI, *The Quasi-Riemann Hypothesis* (5 October 2026, the 11/12 paper) and *A Zero-Free Half-Plane ℜs > 7/8* (30 September 2026). Outline and Part I bookkeeping read; proofs not checked.

**What was actually run:** `python3 verify.py`, also under `-O`, with identical output saved in `RESULTS.json`. Part A is exact integer arithmetic in $\mathbb Z[i][\zeta_N]$; Part B is exact rational exponent arithmetic. No analytic continuation, functional equation, sieve inequality or zero-free statement is verified by the script.

**Smallest remaining gap:** statement (L) in section 6.

## Summary

The route in one line: *over $\mathbb Z[i]$, amplify Möbius with quartic twists (rows $p^4$), row Poisson, reflect with the quartic Gauss-sum functional equation, large sieve.* It looked attractive because fourth powers are denser than sixth powers, so the dial would read $1/2+3a/8$ in place of the Eisenstein $1/2+5a/12$.

1. **The functional equation is not the missing piece.** [PR 1019][pr1019] already supplies it: the Poisson-dual column is the Kubota series with numerator $k^3$ (its (Q2)), with conductor $N(k)^3$ (its (Q8)).
2. **That conductor is the obstruction.** Reflection shortens a column sum of length $D$ only on rows $N(k)\le D^{2/3}$. A fourth-power amplifier is nontrivial only when rows $N(k)>D^{2/3}$ are present. The two ranges do not meet.
3. **Outside the reflection range only a sieve is left, and a sieve cannot help.** de Faveri's bound after row Poisson returns exactly the trivial bound for the principal sum for every $H\le D$, and worse for $H>D$.
4. **The three-scale architecture gives the same answer.** Over all scale choices the best abscissa is exactly 1.
5. **One inequality separates the arenas.** With amplifier order $m$ and dual degree $d$, a window exists only if $(m-2)/(m-1)<2/d$. The Eisenstein sextic arena has $4/5<1$. The Gaussian quartic arena has $2/3=2/3$: zero margin before real sieve losses, and closed after them.

## 1. Setting and the quartic dial

$F=\mathbb Q(i)$; $c$ is primary, $c\equiv1\pmod{(1+i)^3}$; $\chi_c(x)=(x/c)_4$; $g_4(r,c)=\sum_{x\bmod c}\chi_c(x)e(\operatorname{Tr}(rx/c))$; $\gamma(c)=g_4(1,c)/\sqrt{Nc}$; $\alpha(c)=c/|c|$. These are the conventions of [PR 1016][pr1016] and [PR 1019][pr1019]. $A\preccurlyeq B$ means $A\ll_\epsilon D^\epsilon B$.

For a fixed finite-order Hecke character $\nu$ and smooth annular $W$,

$$M_u(D)=\sum_n\mu(n)\nu(n)\chi_n(u)(Nn)^{-1/2}W(Nn/D),\qquad |M_u(D)|^2\ll D\ \text{trivially}.$$

Since $\chi_n(p^4)=\mathbf 1_{p\nmid n}$, rows $u=p^4$ are copies of $M_1$. The argument of `DIRECT_PRINCIPAL_TARGET.md` with sixth powers replaced by fourth powers (not re-proved here) gives: if

$$\sum_{0<Nu\le H}|M_u(D)|^2\preccurlyeq H\qquad(H\ge D^a) \tag{R4}$$

then $|M_1(D)|^2\preccurlyeq H^{3/4}$ and $\zeta_F$, hence $\zeta$, has no zeros in $\Re s>1/2+3a/8$. This is nontrivial exactly for $a<4/3$.

## 2. What [PR 1019][pr1019] already established

Row Poisson on a coprime pair turns the column $\mu(c)\chi_c(u)$ into $\alpha(c)^{\mp1}\gamma(c)\chi_c(k)$ up to fixed ray phases (`QUARTIC_PHYSICAL_ORIENTATION.md`, (O4)–(O6)). The character of $k$ is $\chi_c$, not $\overline{\chi_c}$, so the column is $g_4(k^3,c)/\sqrt{Nc}$ and not the native $g_4(k,c)/\sqrt{Nc}$. Write

$$S_k(Y)=\sum_{c}\gamma(c)\alpha(c)^{\mp1}\xi(c)\chi_c(k)(Nc)^{-1/2}U(Nc/Y).$$

`PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md` then records that the local factor at $p\mid k$ is $1-\alpha(p)^{\mp4}(Np)^{1-4s}$ (Q2), that the reflection has conductor factor $N(k^3)^\delta$ and three gamma quotients (Q8), and a Mellin-line bound whose exponent after the Poisson prefactor is $17/12$ for $a\le1$ (Q12), against a target of $a$. This note explains why that negative result is structural and extends it to the whole amplifier range $a<4/3$.

## 3. Mean-square architecture

Three inputs, all schematic in the sense of the OpenAI outline (coprime pairs only, smooth weights separated):

$$\sum_{0<Nu\le H}|M_u(D)|^2\preccurlyeq H+\frac HD\sum_{0<Nk\preccurlyeq D^2/H}|S_k(D)|^2 \tag{P}$$

$$\sum_{Nk\asymp K}|S_k(Y)|^2\preccurlyeq K+Y+K^{3/4}Y^{1/2}+K^{1/2}Y^{3/4} \tag{S}$$

$$|M_1(D)|^2\preccurlyeq H^{-1/4}\sum_{0<Nu\le H}|M_u(D)|^2 \tag{A}$$

(P) has the form of (2.8) in the 11/12 paper. (S) is de Faveri's Theorem 1.1 for $n=4$, which is (Q4) of [PR 1019][pr1019], applied directly to the annular sum. It is stated for fourth-power-free rows; a general row $k=wv^4$ carries the character of $w$, and grouping rows by $w$ changes no exponent below. (A) is the fourth-power amplifier.

Put $H=D^a$ and $\sum_u|M_u(D)|^2\preccurlyeq D^{E(a)}$. The best case, allowing a lossless reflection wherever it shortens the sum, is:

| Range of $a$ | $E(a)$ | Exponent of $\lvert M_1\rvert^2$ | Tools |
|---|---|---|---|
| $0\le a\le1$ | $1+a/4$ | $1$ | (P), (S) |
| $1\le a\le4/3$ | $3/4+a/2$ | $3/4+a/4$ | (P), (S) |
| $4/3\le a\le15/11$ | $15/4-7a/4$ | $15/4-2a$ | (P), reflection, (S) |
| $a\ge15/11$ | $a$ | $3a/4$ | (P), reflection, (S) |

The trivial exponent is 1. The third column never goes below 1, and equals 1 exactly on $0\le a\le1$. (R4) is reached only from $a=15/11$, and from $a=3/2$ without reflection; the amplifier needs $a<4/3$.

Two remarks.

- **The first row is forced.** $(H/D)(D^2/H)^{3/4}D^{1/2}=DH^{1/4}$ is the trivial bound for the $H^{1/4}$ fourth-power rows. An inequality valid for every coefficient vector must allow coefficients identically one, for which those rows have no cancellation. So no general sieve, before or after Poisson, in any arena, can bound the principal sum nontrivially. The gain has to come from reflection.
- **Against (Q12).** Applying (S) directly gives exponent $5/4$ at $a=1$ where the Mellin-line method of [PR 1019][pr1019] gives $17/12$. Both are above the target 1.

## 4. Why reflection cannot help: degree three

Row $k$ has conductor $N(k)^3$, so $S_k(D)$ reflects to length $N(k)^3/D$. That is at most $D$ only when $N(k)\le D^{2/3}$. The rows present after Poisson run up to $D^2/H$, and the amplifier is nontrivial only when $H<D^{4/3}$, that is $D^2/H>D^{2/3}$. On every row that matters, reflection lengthens the sum.

Even the ideal reflected sieve $K+Y$ does not change this: (R4) then starts at exactly $a=4/3$, where the amplifier exponent is exactly 1 (`B2` in the results).

In the Eisenstein arena both things go the other way. The conductor is $N(h)^2$ (dual range $N(h)^2/X$ in (2.13) of the 11/12 paper), so reflection shortens every row up to $D$; and the reflected twist $\chi_h^3$ is quadratic, where the sieve is $K+Y$ with no extra term. The same calculator returns $5/6$ at $a=1$, which is the published $11/12$.

The source of the difference is the Gauss sums. In the Eisenstein arena $\mu$ times the sextic Gauss sum is a cubic Gauss sum, up to a quadratic Gauss sum and unit factors (the identity before (2.7) in the 11/12 paper). So the dual columns are cubic Gauss sums, which are theta coefficients of degree two, and the sextic twist is not a power of the cubic symbol, so reflection changes it. In the Gaussian arena the dual columns are quartic Gauss sums, of degree three, and the twist $\chi_c(k)=\overline{\chi_c(k^3)}$ is only a change of numerator. The reflected family is the same family.

## 5. Three-scale architecture

This is a transplant of the Part I bookkeeping of the 7/8 paper (probe $I_\eta(X,Y,Z)$, sections 6–11), not of its proofs. Put $X=Z^{l_x}$, $Y=Z^{l_y}$, $q=l_x+l_y$; the rows have norm about $XY$, the completed Gauss index is at scale $Z$, and the dual rows run up to $Z/X$. Here $m$ is the amplifier order, 6 or 4.

- **Signal:** $X^{1/2-1/m}Z^{\beta_*-1+1/m}$, from the pole at $z=1/m$ of the sum over $m$-th powers (it is $\zeta_F(6z)$ in (7.5)).
- **LOW:** $|I|\preccurlyeq(XY)^{-1/2}\big((XY+Y^2)/Y\big)^{1/2}Z^{e_B(q)/2}$, as in (6.2) and Lemma 6.2, where $Z^{e_B(q)}$ bounds the mean square of the Gauss rows.
- **HIGH:** for every bin $\delta\le2\beta_*-1$, $\ (1+\delta)(1-l_y)/2+(1-l_x)\big(R(\delta)+\delta/2-1/m\big)<\beta_*$, with the row count $R(\delta)$ derived from the sieve as in Proposition 9.2. The HIGH column below is the least $\beta_*$ for which this holds.

| Arena | Best abscissa over all scales | Where | LOW | HIGH |
|---|---|---|---|---|
| Eisenstein sextic (control) | $11/12$ | $l_x=l_y=1/2$ | $11/12$ | $5/6$ |
| Gaussian quartic | $1$ | $l_x=l_y=1/2$ | $1$ | $3/4$ |

The control reproduces Part I. In the quartic arena HIGH is comfortable and LOW is the binding side, for the same reason as in section 3: at balanced scales the Gauss rows have conductor $Z^3$ and length $Z$, and (S) gives $Z^{5/4}$ where $Z$ is needed. LOW below 1 needs $q<2/3$ and HIGH below 1 needs $q>2/3$; the script checks both implications at every point of the scale grid.

## 6. What would reopen the route

For some $2/3<\kappa<2$ and some $\eta>0$,

$$\sum_{0<Nk\le D^\kappa}|S_k(D)|^2\ll D^{3\kappa/4+1/2-\eta}. \tag{L}$$

- For $\kappa\ge1$ this is any power saving over (S) for this one coefficient vector. For $\kappa<1$ it also has to recover the gap $(1-\kappa)/4$.
- De Faveri's introduction cites matching lower bounds for $n=4$ (with Dunn and Hoffstein; read from the arXiv page, not checked). If so, (L) cannot come from a sieve. It has to use the Gauss vector.
- Run (P) backwards and (L) says that the principal sum has a power saving and the other rows are no worse. So (L) is a restatement of the goal, not a reduction of it. What is missing is an independent handle on $S_k(D)$ when $D$ is below the square root of the conductor $N(k)^3$.

## 7. A test for other arenas

An amplifier of order $m$ needs rows above $D^{(m-2)/(m-1)}$. Reflection of a dual family of degree $d$ needs rows below $D^{2/d}$. A window requires

$$\frac{m-2}{m-1}<\frac2d.$$

| Arena | $m$ | $d$ | Amplifier needs $K>$ | Reflection needs $K\le$ | Verdict |
|---|---|---|---|---|---|
| sextic over $\mathbb Q(\omega)$ | 6 | 2 | $D^{4/5}$ | $D$ | open |
| quartic over $\mathbb Q(i)$ | 4 | 3 | $D^{2/3}$ | $D^{2/3}$ | zero margin |
| order 10 over $\mathbb Q(\zeta_5)$ | 10 | 4 | $D^{8/9}$ | $D^{1/2}$ | closed |

The first two rows rest on the cited sources. The third assumes that order-$2\ell$ twists dualize to $\ell$-th order Gauss sums of degree $\ell-1$; that is a heuristic extrapolation and was not checked.

## 8. Finite identities checked exactly

All in $\mathbb Z[i][\zeta_N]$ with integer arithmetic, with negative controls (wrong sign and wrong conjugate are rejected).

| Check | Statement | Instances |
|---|---|---|
| A1 | $g_4(c)^2=\mu(c)\,c\sqrt{Nc}$, and $\mu(c)g_4(c)\sqrt{Nc}=c\,\overline{g_4(c)}$ | 12 moduli, split, inert and composite |
| A2 | $g_4(k,c)=\overline{\chi_c(k)}g_4(1,c)$, $\ g_4(k^3,c)=\chi_c(k)g_4(1,c)$; they differ iff $\chi_c(k)^2=-1$ | 62 pairs, 43 differ |
| A3 | $g_4(mp^3,p^j)=0,0,0,-N(p)^3,0$ for $j=1,\dots,5$ | 2 primes, 3 multipliers |
| A4 | twisted multiplicativity and quartic reciprocity | 7 pairs |
| A5 | the row Poisson coefficient of a coprime pair, and $\mu(c)g_4(k,c)\sqrt{Nc}=c\,\overline{g_4(k^3,c)}$ | 11 |
| A6 | $g_4(k^3,p^jc')$ for $p\mid k$: zero for $j=1,2,3$, and $-N(p)^3g_4(k^3,c')$ for $j=4$ | 2 cofactors |

A1 is the codec of [PR 1016][pr1016], A2 and A5 the orientation of [PR 1019][pr1019], A3 and A6 the local factor in (Q2). These confirm conventions on small moduli. They are not new.

## 9. Limits

- The table in section 3 is a best-case envelope. It grants a lossless reflection and ignores common-divisor strata, fourth-power completion and bad primes. Those can only make the true bounds worse, so the negative conclusion does not depend on them. The positive entries ($15/11$, $3/2$) are not claimed as theorems.
- The obstruction is for this toolset: row Poisson, the quartic reflection, and inequalities valid for arbitrary coefficients. It is not a theorem that the Gaussian arena cannot work.
- (S) and the conductor exponent are imported. If either is misquoted the tables change; the script takes them as inputs.
- The three-scale computation was matched to the 7/8 paper only at the numbers it prints: the low exponent $1/4$ of Proposition 6.3, the row count $R(\delta)$ of Proposition 9.2, and the high exponent at $d=1/2$ in (10.12).

[pr1019]: https://github.com/GettysburgResearch/riemann/pull/1019
[pr1016]: https://github.com/GettysburgResearch/riemann/pull/1016
