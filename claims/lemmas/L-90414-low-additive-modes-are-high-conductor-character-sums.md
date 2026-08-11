# L-90414 — The remaining low additive modes are high-conductor Dirichlet-character prime sums

Claim ID: `L-90414`  
Title: Every low residue in the compact-Q4 major arc has an exact Dirichlet-character expansion with conductor at least the square-root scale  
Status: **PROPOSED COMPLETE EXACT HYBRID REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90412`; elementary finite character orthogonality  
Scope: exact decomposition only; no character-sum estimate, PIG, or RH conclusion

## 1. Scale-four prime exponential sums

Assume \(4\mid N\). For an integer \(a\), define

\[
P(X,a)
=
\sum_{m<X}\Lambda(m)
\sin\frac{2\pi am}{X}.
\tag{L-90414.1}
\]

The innovation sine coordinate of `L-90412` is exactly

\[
\boxed{
S_a(N)
=
P(N,a)-4P(N/4,a)
+
3(\log4)
\sum_{\substack{r\ge1\\4^r<N}}
\sin\frac{2\pi a4^r}{N}.
}
\tag{L-90414.2}
\]

Thus the only nonlocal arithmetic is a scale-four difference of ordinary
prime exponential sums; the four-adic correction is explicit and logarithmic.

## 2. Exact character expansion at one rational frequency

Put

\[
g=(a,X),\qquad q=X/g,\qquad b=a/g,
\]

so that \((b,q)=1\) and \(e(am/X)=e(bm/q)\), where
\(e(t)=e^{2\pi it}\).

For a Dirichlet character modulo \(q\), write

\[
\psi(Y,\chi)=\sum_{m<Y}\Lambda(m)\chi(m)
\]

and

\[
\tau(\overline\chi)
=
\sum_{r\bmod q}\overline{\chi(r)}e(r/q).
\]

Character orthogonality on the unit group gives, for every \((m,q)=1\),

\[
e(bm/q)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\chi(b)\tau(\overline\chi)\chi(m).
\tag{L-90414.3}
\]

Since a von Mangoldt coefficient with \((m,q)>1\) is a prime power of a
prime dividing \(q\), one obtains the exact identity

\[
\boxed{
\begin{aligned}
\sum_{m<Y}\Lambda(m)e(am/X)
={}&
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\chi(b)\tau(\overline\chi)\psi(Y,\chi)\\
&+
\sum_{p\mid q}
\sum_{\substack{k\ge1\\p^k<Y}}
(\log p)e(bp^k/q).
\end{aligned}
}
\tag{L-90414.4}
\]

The second line is a completely explicit local-conductor correction and obeys

\[
\boxed{
|R_q(Y,b)|
\le \omega(q)\log Y
\le \frac{\log(2q)\log Y}{\log2}.
}
\tag{L-90414.5}
\]

Taking imaginary parts yields \(P(X,a)\).

## 3. Conductors in the PIG major arc

For

\[
1\le a<\sqrt N,
\]

the reduced modulus in the first term of (L-90414.2) satisfies

\[
\boxed{
q=\frac{N}{(a,N)}
\ge\frac Na
>\sqrt N.
}
\tag{L-90414.6}
\]

For the quarter-scale term,

\[
q'
=
\frac{N/4}{(a,N/4)}
\ge
\frac{N}{4a}
>
\frac{\sqrt N}{4}.
\tag{L-90414.7}
\]

Therefore every nonzero additive mode left open by `L-90412` is an exact
linear combination of prime sums twisted by characters of conductor at least
the square-root scale, plus an explicit polylogarithmic correction.

## 4. Consequence

This identifies the nonzero major modes with a specific hybrid frontier:

```text
prime-sum length       asymptotic to N;
character modulus      between sqrt(N) and N;
number of periods      at most sqrt(N);
weight in PIG          inverse-square in the additive frequency.
```

The decomposition connects the Q4 PIG obstruction to the growing-conductor
Dirichlet-L direction of the imported Claude programme. A positive proportion
of critical zeros for those \(L\)-functions is not by itself enough to bound
\(\psi(Y,\chi)\) at the square-root scale. A successful continuation needs a
hybrid mean-square statement strong enough for the weighted family in
(L-90414.2)--(L-90414.4), or a new finite-compression statistic that avoids
estimating each character sum separately.

No such estimate is claimed here.
