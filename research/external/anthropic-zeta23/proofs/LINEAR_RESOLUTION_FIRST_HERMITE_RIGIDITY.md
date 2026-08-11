# Linear-resolution density-one positivity and a deterministic prime-resonance certificate

**Status:** `PROPOSED COMPLETE LARGE-VALUE / INVERSE THEOREM — INDEPENDENT REVIEW REQUIRED`  
**Date:** 2026-08-11  
**RH status:** **unproved**  
**Depends on:** PR #379's exact first-Hermite prime formula; PR #385's pointwise `4 log log` wedge; PR #390's prime-block moment theorem; Montgomery--Vaughan mean values in the form used upstream by Zeta23.

This note sharpens PR #390 in two directions.

First, the Gaussian prime polynomial may be truncated at `exp(a q)` for any fixed `a>2`, rather than the deliberately wasteful `exp(8q)`. Fixed moments then prove simultaneous density-one positivity for every integer heat resolution up to a **fixed positive fraction of `log T`**. For every prescribed power saving in `log T`, the fraction may be chosen explicitly.

Second, any remaining negative centre has a deterministic inverse description. It forces one common half-plane alignment among at least

\[
  \gg \frac{(\log T)^2}{q}
\]

prime-power coordinates and therefore among at least

\[
  \gg \frac{(\log T)^2}{q^2}
\]

distinct primes. At the terminal scale \(q\asymp\log\log T\), one exceptional carrier must coordinate at least

\[
  \gg \frac{(\log T)^2}{(\log\log T)^2}
\]

distinct prime phases.

The result still does **not** remove one exceptional point. It changes the final pointwise problem from an unspecified large value into a high-codimension, many-prime resonance problem.

## 1. First-Hermite polynomial and the negative threshold

For \(q\ge1\), put

\[
 h_q(u)=\left(1-\frac{u^2}{2q}\right)e^{-u^2/(4q)}
\tag{LR.1}
\]

and

\[
 b_q(n)=\frac{\Lambda(n)}{\sqrt n}h_q(\log n),
 \qquad
 S_q(t)=\sum_{n\ge2}b_q(n)n^{it}.
\tag{LR.2}
\]

PR #379 gives

\[
 \mathcal M(q,t)
 =
 \mathcal P_{\rm pole}(q,t)
 +\mathcal G(q,t)
 -\frac{1}{2\sqrt\pi q^{3/2}}\Re S_q(t).
\tag{LR.3}
\]

On \(t\in[T,2T]\), write

\[
 L=\log T.
\tag{LR.4}
\]

The Stirling lower bound used on PRs #384--#390 gives, uniformly in the present ranges,

\[
 \mathcal G(q,t)\ge\frac{cL-C}{q^{3/2}},
\tag{LR.5}
\]

while the pole term is negligible at high carrier. Therefore there are absolute \(c_0>0\) and \(T_0\) such that

\[
 \boxed{
 \mathcal M(q,t)<0
 \Longrightarrow
 |S_q(t)|\ge c_0L
 }
\tag{LR.6}
\]

for \(T\ge T_0\) and \(q\ge1\) in every range used below.

The coefficient energy is, by PR #390,

\[
 \boxed{
 V(q):=\sum_{n\ge2}|b_q(n)|^2=q+O(\sqrt q).
 }
\tag{LR.7}
\]

## 2. Adaptive Gaussian truncation

Fix once and for all

\[
 a>2
\tag{LR.8}
\]

and truncate at

\[
 N_{a,q}=e^{aq},
 \qquad
 S_{q,a}(t)=\sum_{n\le N_{a,q}}b_q(n)n^{it}.
\tag{LR.9}
\]

### Lemma 2.1 (adaptive tail)

For \(q\ge1\),

\[
 \boxed{
 \sup_{t\in\mathbb R}|S_q(t)-S_{q,a}(t)|
 \ll_a
 q^3e^{-c_aq},
 \qquad
 c_a=\frac{a(a-2)}4.
 }
\tag{LR.10}
\]

### Proof

Use \(\Lambda(n)\le\log n\) and

\[
 |h_q(u)|
 \le
 \left(1+\frac{u^2}{2q}\right)e^{-u^2/(4q)}.
\tag{LR.11}
\]

The all-integer envelope is bounded by a first term plus

\[
 \int_{aq}^{\infty}
 u\left(1+\frac{u^2}{2q}\right)
 e^{u/2-u^2/(4q)}\,du.
\tag{LR.12}
\]

Complete the square:

\[
 \frac u2-\frac{u^2}{4q}
 =
 \frac q4-\frac{(u-q)^2}{4q}.
\tag{LR.13}
\]

At \(u=aq\), this equals

\[
 -\frac{a(a-2)}4q=-c_aq.
\tag{LR.14}
\]

Since the exponent is decreasing throughout \(u\ge aq\), one integration against the Gaussian tail gives (LR.10), with the harmless polynomial \(q^3\). \(\square\)

Thus, once \(T\) is large, the tail is \(o(L)\) uniformly for every \(1\le q\le cL\), with any fixed \(c>0\). In particular (LR.6) implies

\[
 \mathcal M(q,t)<0
 \Longrightarrow
 |S_{q,a}(t)|\ge \frac{c_0}{2}L
\tag{LR.15}
\]

through all ranges below.

## 3. Growing moments with the shorter cutoff

PR #390 proves the prime-block torus moment bound

\[
 \int_{\mathbb T^\infty}|S_q(\boldsymbol\omega)|^{2k}
 d\boldsymbol\omega
 \le [Ck(q+k)]^k.
\tag{LR.16}
\]

Raise \(S_{q,a}\) to the \(k\)-th power:

\[
 S_{q,a}(t)^k
 =
 \sum_{m\le e^{akq}}c_{q,a,k}(m)m^{it}.
\tag{LR.17}
\]

Unique factorisation identifies

\[
 \sum_m|c_{q,a,k}(m)|^2
\tag{LR.18}
\]

with the corresponding torus moment. Montgomery--Vaughan then gives the following.

### Lemma 3.1 (adaptive growing-moment transfer)

If

\[
 akq\le \frac12L,
\tag{LR.19}
\]

then

\[
 \boxed{
 \int_T^{2T}|S_{q,a}(t)|^{2k}\,dt
 \ll
 T[Ck(q+k)]^k.
 }
\tag{LR.20}
\]

The implied constant is absolute once \(a\) is fixed.

Combining (LR.15), (LR.20), and Markov gives

\[
 \boxed{
 \frac{|E_q(T)|}{T}
 \ll
 \left[
 \frac{Ck(q+k)}{L^2}
 \right]^k,
 \qquad
 E_q(T):=\{t\in[T,2T]:\mathcal M(q,t)<0\},
 }
\tag{LR.21}
\]

for every integer \(k\ge1\) satisfying (LR.19).

## 4. A sharper one-resolution estimate

Choose a sufficiently small \(\kappa=\kappa(a)>0\) and put

\[
 k=
 \left\lfloor
 \frac{\kappa L}{q+1}
 \right\rfloor.
\tag{LR.22}
\]

For \(2\le q\le c_a' L\), with \(c_a'>0\) sufficiently small, (LR.19) holds.

If \(q\le\sqrt L\), then

\[
 \frac{Ck(q+k)}{L^2}
 \ll_a \frac1{(q+1)^2}.
\tag{LR.23}
\]

If \(q\ge\sqrt L\), then

\[
 \frac{Ck(q+k)}{L^2}
 \ll_a \frac1L.
\tag{LR.24}
\]

Hence:

### Theorem 4.1 (refined exceptional-set exponent)

For some \(c,C>0\), depending only on the fixed cutoff parameter \(a>2\),

\[
 \boxed{
 \frac{|E_q(T)|}{T}
 \le
 C\exp\left[
 -c\frac{L}{q+1}
 \log\!\left(2+\min(q,\sqrt L)\right)
 \right]
 }
\tag{LR.25}
\]

uniformly for

\[
 2\le q\le cL.
\tag{LR.26}
\]

This adds the logarithmic factor discarded in the deliberately simpler statement of PR #390. For example, if

\[
 q\le L^{1-\varepsilon},
\tag{LR.27}
\]

then

\[
 \frac{|E_q(T)|}{T}
 \le
 \exp[-c_\varepsilon L^\varepsilon\log L].
\tag{LR.28}
\]

## 5. Simultaneous positivity to a positive fraction of \(\log T\)

Fix an integer

\[
 K\ge3.
\tag{LR.29}
\]

Let

\[
 Q_{a,K}(T)
 =
 \left\lfloor\frac{L}{4aK}\right\rfloor.
\tag{LR.30}
\]

For every \(q\le Q_{a,K}(T)\), the fixed choice \(k=K\) satisfies (LR.19). Summing (LR.21),

\[
\begin{aligned}
 \frac1T
 \left|
 \bigcup_{1\le q\le Q_{a,K}(T)}E_q(T)
 \right|
 &\ll_{a,K}
 \frac1{L^{2K}}
 \sum_{q\le Q_{a,K}(T)}(q+K)^K\\
 &\ll_{a,K}
 L^{1-K}.
\end{aligned}
\tag{LR.31}
\]

Therefore:

### Theorem 5.1 (linear-resolution density-one positivity)

For every integer \(K\ge3\),

\[
 \boxed{
 \left|
 \left\{
 t\in[T,2T]:
 \exists q\in\mathbb N,\ 
 1\le q\le\frac{\log T}{4aK},\
 \mathcal M(q,t)<0
 \right\}
 \right|
 \ll_{a,K}
 T(\log T)^{1-K}.
 }
\tag{LR.32}
\]

Equivalently, for every \(A>0\), there is an explicit \(c_A>0\) such that

\[
 \boxed{
 \left|
 \left\{
 t\in[T,2T]:
 \exists q\in\mathbb N,\ 
 1\le q\le c_A\log T,\
 \mathcal M(q,t)<0
 \right\}
 \right|
 \ll_A
 \frac{T}{(\log T)^A}.
 }
\tag{LR.33}
\]

For instance, with \(a=3\) one may take

\[
 c_A=\frac1{12(\lceil A\rceil+2)}.
\tag{LR.34}
\]

This is a genuine increase from PR #390's simultaneous range \((\log T)^{1-\varepsilon}\): the heat resolution now reaches a fixed positive fraction of \(\log T\), at the price that the fraction depends on the requested logarithmic saving.

### Corollary 5.2 (finite logarithmic measure)

Choose \(A>2\), and define

\[
 \mathcal E_A
 =
 \left\{
 t\ge T_0:
 \exists q\in\mathbb N,\ 
 1\le q\le c_A\log t,\
 \mathcal M(q,t)<0
 \right\}.
\tag{LR.35}
\]

Then

\[
 \boxed{
 \int_{\mathcal E_A}\frac{dt}{t}<\infty.
 }
\tag{LR.36}
\]

Indeed, sum (LR.33) over dyadic carrier blocks.

## 6. Deterministic inverse theorem: many prime powers must align

The measure theorem still permits isolated points. We now record exactly what one such point entails.

Assume \(t\in[T,2T]\), \(q\le cL\), and

\[
 \mathcal M(q,t)<0.
\tag{LR.37}
\]

For \(T\) large, (LR.15) gives

\[
 |S_{q,a}(t)|\ge H,
 \qquad
 H=\frac{c_0}{2}L.
\tag{LR.38}
\]

Choose \(\theta\) so that

\[
 e^{-i\theta}S_{q,a}(t)=|S_{q,a}(t)|.
\tag{LR.39}
\]

For \(n\le e^{aq}\), put

\[
 r_n
 =
 \left[
 \Re\left(
 e^{-i\theta}b_q(n)n^{it}
 \right)
 \right]_+.
\tag{LR.40}
\]

Then

\[
 \sum_nr_n\ge H.
\tag{LR.41}
\]

Choose a subset \(J\) of minimum cardinality such that

\[
 \sum_{n\in J}r_n\ge \frac H2.
\tag{LR.42}
\]

Since \(r_n\le|b_q(n)|\), Cauchy--Schwarz and (LR.7) give

\[
 \frac H2
 \le
 \sum_{n\in J}|b_q(n)|
 \le
 |J|^{1/2}
 \left(\sum_n|b_q(n)|^2\right)^{1/2}
 \ll
 |J|^{1/2}q^{1/2}.
\tag{LR.43}
\]

Therefore:

### Theorem 6.1 (prime-power resonance codimension)

Every negative centre in the stated range forces a common half-plane alignment of at least

\[
 \boxed{
 |J|\gg\frac{L^2}{q}
 }
\tag{LR.44}
\]

prime-power coordinates.

Every \(n\in J\) is a prime power \(p^r\le e^{aq}\). For one fixed prime,

\[
 r\le\frac{aq}{\log2}.
\tag{LR.45}
\]

Consequently the underlying distinct-prime set

\[
 \mathcal P_J=\{p:\ p^r\in J\text{ for some }r\}
\tag{LR.46}
\]

satisfies

\[
 \boxed{
 |\mathcal P_J|
 \gg_a
 \frac{L^2}{q^2}.
 }
\tag{LR.47}
\]

All selected prime-power contributions lie in the same open half-plane after the single rotation \(e^{-i\theta}\).

At the terminal first-Hermite scale

\[
 q\asymp\log\log T,
\tag{LR.48}
\]

this becomes

\[
 \boxed{
 |\mathcal P_J|
 \gg
 \frac{(\log T)^2}{(\log\log T)^2}.
 }
\tag{LR.49}
\]

Thus one hypothetical pointwise violation is not a one-prime or finite-prime accident. It is a coherent resonance involving an unbounded, quantitatively huge set of distinct prime phases.

## 7. Exact remaining pointwise gate

The present continuation proves:

```text
all but O_A(T/log^A T) carrier points:
    positivity simultaneously for q <= c_A log T;

one negative carrier:
    at least c log^2 T/q prime-power coordinates aligned;
    at least c log^2 T/q^2 distinct primes aligned.
```

What it does not prove is that the actual prime-log flow

\[
 t\longmapsto(p^{it})_p
\tag{LR.50}
\]

cannot hit this high-codimension resonance set at one exceptional carrier.

The remaining inverse gate can now be stated sharply:

> **Zeta-carrier prime-resonance exclusion.**  
> Prove that no ordinate capable of supporting a terminal off-line zeta pair can simultaneously place
> \[
> \gg \frac{(\log T)^2}{q^2}
> \]
> distinct prime blocks in the common half-plane configuration forced by Theorem 6.1, at the corresponding first-Hermite resolution \(q\).

A generic metric, moment, or density theorem cannot establish this. PR #390's support-length firewall remains: one isolated pair contributes only \(o(T)\) throughout the available moment budget. A conclusion-producing proof must use information specific to a zeta-zero carrier, or a new deterministic theorem for the prime-log flow.

## 8. Proof boundary

Proposed complete here, pending independent review:

```text
adaptive cutoff exp(a q), every fixed a>2
tail O_a(q^3 exp[-a(a-2)q/4])
growing moments under a k q <= (1/2)log T
refined exceptional exponent
simultaneous density-one positivity to c_A log T
arbitrary logarithmic-power exceptional saving
finite logarithmic measure
prime-power resonance codimension
distinct-prime resonance codimension
```

Still open:

```text
deterministic exclusion of one resonance carrier
pointwise first-Hermite positivity
arithmetic corrected-kernel floor
Riemann Hypothesis
```
