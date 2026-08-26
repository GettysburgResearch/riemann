# Native \(q\)-adic wavelet zero stratum

**Status:** exact endpoint-three theorem for every nonsquare odd prime power,
plus source-locked \(q=3,5,7\) orbit tomography. No new finite field or family
member was enumerated.

**Scope convention:** throughout the all-\(q\) theorem, \(q=p^e\) is an odd
prime power that is not a square as an integer, equivalently \(e\) is odd.
The Frobenius coefficients \(a_D,b_D\) are integers.

## 1. Result

Let

\[
 P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
 \qquad
 \frac1{P_D(u)}=\sum_{n\geq0}r_D(n)u^n,
\]

and use the native wavelet from the predecessor packet:

\[
 W_D(N)=\bigl(r_D(N)-r_D(N-1)\bigr)
       +\sqrt q\bigl(-r_D(N-1)+r_D(N-2)\bigr).
\]

Also put

\[
                       K_D=qa_D^2-b_D^2.
\]

Then, for every nonsquare odd prime power \(q\) and every monic squarefree
quintic member \(D\),

\[
\boxed{
 W_D(3)=0
 \quad\Longleftrightarrow\quad
 K_D=0
 \quad\Longleftrightarrow\quad
 (a_D,b_D)=(0,0).}
\tag{1}
\]

This is a memberwise algebraic equivalence. It is not an asymptotic or a
three-field interpolation.

## 2. Endpoint-three algebra

Coefficient comparison in \(P_D(u)^{-1}\) gives

\[
 r_D(1)=-a_D,
 \qquad
 r_D(2)=a_D^2-b_D,
 \qquad
 r_D(3)=-a_D(a_D^2-2b_D+q).
\tag{2}
\]

Writing \(a=a_D\) and \(b=b_D\), the two coordinates of \(W_D(3)\) are

\[
\begin{aligned}
 R&=r_D(3)-r_D(2)=-a^3-a^2+2ab-aq+b,\\
 S&=-r_D(2)+r_D(1)=b-a^2-a.
\end{aligned}
\tag{3}
\]

Because \(q\) is not a square, \(1\) and \(\sqrt q\) are linearly
independent over \(\mathbf Q\). Hence \(W_D(3)=R+S\sqrt q=0\) if and only if
\(R=S=0\). The equation \(S=0\) gives

\[
                            b=a^2+a.
\tag{4}
\]

After this substitution, the rational coordinate becomes

\[
                       R=a\bigl((a+1)^2-q\bigr).
\tag{5}
\]

The second factor cannot vanish because \((a+1)^2=q\) would make \(q\) an
integer square. Thus \(a=0\), and then (4) gives \(b=0\). The converse is
immediate from (2) and (3).

Independently,

\[
 K_D=0\quad\Longleftrightarrow\quad b^2=qa^2.
\]

If \(a\ne0\), this would make \(q=(b/a)^2\) a rational square. A positive
integer that is a rational square is an integer square, again contradicting
the scope assumption. Therefore \(a=b=0\). This proves both equivalences in
(1). The producer separately certifies every polynomial identity in
(2)--(5) by exact sparse-polynomial arithmetic.

## 3. Spectral classification of the stratum

On the zero stratum,

\[
 P_D(u)=1+q^2u^4,
 \qquad
 F_D(x)=x^4P_D(1/x)=x^4+q^2.
\tag{6}
\]

Every root of \(F_D\) is \(\sqrt q\,\zeta\), where \(\zeta^4=-1\). Thus all
normalized Frobenius eigenvalues are roots of unity, so the genus-two
Jacobian is supersingular.

The polynomial \(x^4+q^2\) is irreducible over \(\mathbf Q\) for odd \(q\).
It has no rational linear factor. Any rational quadratic factorization must
have the form

\[
 (x^2+cx+d)(x^2-cx+e).
\]

Coefficient comparison gives

\[
 c(e-d)=0,
 \qquad
 d+e-c^2=0,
 \qquad
 de=q^2.
\]

If \(c=0\), then \(e=-d\), forcing \(-d^2=q^2\), which is impossible over
\(\mathbf Q\). Otherwise \(d=e=\pm q\), and the only positive possibility
forces \(c^2=2q\). But \(v_2(2q)=1\), whereas every rational square has even
\(2\)-adic valuation. Hence no factorization exists. Irreducibility of the
rational Frobenius polynomial rules out a nontrivial
\(\mathbf F_q\)-isogeny factor, so the Jacobian is \(\mathbf F_q\)-simple.

This classification is conditional only on membership in the zero stratum;
it does not assert that such a member exists for every \(q\).

## 4. Every native endpoint on the stratum

Equation (6) gives the complete reciprocal series

\[
 \frac1{1+q^2u^4}
   =\sum_{m\geq0}(-q^2)^m u^{4m}.
\]

Therefore

\[
 r_D(4m)=(-q^2)^m,
 \qquad
 r_D(n)=0\quad(4\nmid n).
\tag{7}
\]

Substitution into the native wavelet shows, with the predecessor's
negative-index convention, that for every \(N\geq0\),

\[
\boxed{W_D(N)=0\quad\Longleftrightarrow\quad N\equiv3\pmod4.}
\tag{8}
\]

In the other three residue classes, respectively, at least one of
\(r_D(N),r_D(N-1),r_D(N-2)\) is the nonzero term from (7).

## 5. Frozen arithmetic authentication

The producer reads only the 251 atoms of the source-locked joint
\((a_D,b_D)\) histograms. It does not read or reconstruct individual
quintics. Three independent predecessor views agree:

- the native-wavelet fixture supplies the \(W_D(3)\) and \(W_D(7)\) zero
  counts;
- the balanced-control histogram supplies the exact \((a_D,b_D)\) atoms;
- the affine-orbit fixture supplies the \(K_D=0\) member and orbit counts.

Their common member counts are:

| \(q\) | \(W_3=0\) | \(K_D=0\) | \((a_D,b_D)=(0,0)\) | \(W_7=0\) |
|---:|---:|---:|---:|---:|
| 3 | 12 | 12 | 12 | 12 |
| 5 | 50 | 50 | 50 | 50 |
| 7 | 336 | 336 | 336 | 336 |

At endpoint seven, the producer also checks every histogram atom and finds
no off-stratum zero for these three fields. This last converse is **only** a
frozen \(q=3,5,7\) statement; equation (1), not the endpoint-seven converse,
is the all-\(q\) theorem.

## 6. Affine-orbit tomography

For the full \(AGL(1,\mathbf F_q)\) action, the zero strata decompose as:

| \(q\) | group order | zero-orbit types | stack mass |
|---:|---:|---|---:|
| 3 | 6 | 2 free orbits of size 6 | \(2\) |
| 5 | 20 | 2 free orbits of size 20; 2 size-5 orbits with stabilizer 4 | \(5/2\) |
| 7 | 42 | 8 free orbits of size 42 | \(8\) |

The mass is the exact quotient-stack groupoid cardinality

\[
 \frac{\#\{D:K_D=0\}}{|AGL(1,\mathbf F_q)|}
 =\sum_{\mathcal O}\frac1{|\operatorname{Stab}(\mathcal O)|}.
\]

These are authenticated finite facts, not values of a proposed all-\(q\)
count formula.

## 7. Provenance and resource boundary

The JSON fixture locks the committed native-wavelet note, producer, fixture,
and test; the balanced-control fixture and producer; and the affine-orbit
fixture and producer. It verifies both normalized file hashes and all
available canonical payload hashes before consuming data.

The replay uses:

- 251 frozen joint-histogram atoms, cap 4,096;
- 1,757 recurrence updates, cap 4,096;
- 502 exact wavelet-coordinate checks, cap 1,024;
- no floating point, field construction, curve construction, or member
  enumeration.

## 8. Claim boundary

- The endpoint-three converse requires nonsquare \(q\). At square prime
  powers, rational and radical coordinates can cancel without vanishing
  separately.
- Endpoint-seven off-stratum exclusion is proved here only for the frozen
  fields \(q=3,5,7\).
- The finite zero counts and stack masses are not an all-\(q\) count law.
- No RH, GRH, equidistribution, motive-identification, or novelty claim is
  made.

## 9. Replay

```text
python research/l-families/atlas/function_field/native_qadic_wavelet_zero_stratum.py --check
python -O research/l-families/atlas/function_field/native_qadic_wavelet_zero_stratum.py --check
python -m unittest tests.test_native_qadic_wavelet_zero_stratum
python -O -m unittest tests.test_native_qadic_wavelet_zero_stratum
```
