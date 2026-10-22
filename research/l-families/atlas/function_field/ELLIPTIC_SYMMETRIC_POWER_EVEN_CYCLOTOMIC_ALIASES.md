# Even-cyclotomic aliases of complete symmetric-power spectra

## Result in one paragraph

Let \(N=2M\ge4\), let \(\zeta\) be a primitive \(N\)-th root of unity,
and let \(a\) be a unit modulo \(N\). Put

\[
 E_m=\{m-2j\bmod N:0\le j\le m\}
\]

with multiplicity, and write

\[
 m+1=kM+s,\qquad 0\le s<M.
\]

This packet proves the complete stabilizer classification

\[
 \operatorname{Stab}_{U(N)}(E_m)=
 \begin{cases}
 U(N),&s\in\{0,1,M-1\},\\
 \{a\in U(N):a\equiv\pm1\pmod M\},
   &2\le s\le M-2,\ m\text{ even},\\
 \{\pm1\pmod N\},
   &2\le s\le M-2,\ m\text{ odd}.
 \end{cases}
\]

When \(4\mid N\), the extra two generic lifts at even \(m\) are precisely
the central-sign mates \(g\mapsto-g\); they are not new nonsign aliases.
On the three all-unit edge residues there are genuine nonsign primitive
aliases exactly when \(N\notin\{4,6,8,12\}\). The first case is
\(N=10,m=3\). All statements concern complete eigenvalue multisets and
complete local factors, not merely one character value.

This is an exact local representation-theory result. It constructs no
curve, motive, global Euler product, or compatible family.

## 1. Setup and the two locked predecessors

For the determinant-one class

\[
 g_a=\operatorname{diag}(\zeta^a,\zeta^{-a}),
\]

the complete spectrum and factor of its \(m\)-th symmetric power are

\[
 S_m(\zeta^a)=
 \{\zeta^{a(m-2j)}:0\le j\le m\},
\]

and

\[
 F_m(\zeta^a;T)=
 \prod_{j=0}^{m}\bigl(1-\zeta^{a(m-2j)}T\bigr).
\]

Thus equality is exactly equality, with multiplicity, of \(E_m\) and
\(aE_m\).

This packet binds:

- the odd-order cyclotomic packet, payload
  b783dc120095c5256cacc2eaa79f3f152883f9b33b4074a18b123489f81bc6ff;
- the rational full-factor/sign packet, payload
  f1a7f183ee16c98c8f633e9b5ffa5f1bb76c0521cd596d5be71840a35711d983.

The odd-order proof uses that \(2\) is invertible at the root order and
does not cover the parity-coset geometry here. The sign packet explains
the central kernel over rational fixed-determinant classes. Neither locked
payload is used as the proof below; the locks establish provenance and a
precise boundary with the preceding results.

## 2. Complete cycles and the exact affine interval

The sequence

\[
 m,m-2,m-4,\ldots\pmod{2M}
\]

has exact period \(M\). One period is every residue congruent to \(m\)
modulo \(2\), once. Consequently, the first \(kM\) terms give \(k\)
copies of the full parity coset, and only

\[
 R_s=\{m-2j\bmod 2M:0\le j<s\}
\]

can break unit symmetry. Every unit modulo \(2M\) is odd, hence preserves
both parity cosets and their uniform multiplicities.

Index the residual atoms by

\[
 I_s=\{0,1,\ldots,s-1\}\subset\mathbb Z/M\mathbb Z,
\qquad e_j=m-2j.
\]

For a unit \(a\), the index \(j'\) of the transformed exponent satisfies

\[
 m-2j'\equiv a(m-2j)\pmod{2M}.
\]

Dividing the even difference by \(2\) gives the exact induced affine map

\[
 A_a(j)=
 aj-\frac{(a-1)m}{2}\pmod M.
\]

The numerator is even because \(a\) is odd. Therefore

\[
 aE_m=E_m
 \quad\Longleftrightarrow\quad
 A_a(I_s)=I_s,
\]

with multiplicity. This formulation works for both exponent parities and
does not pretend that the odd-parity torsor has a universally fixed center.

## 3. Interior intervals force signs modulo \(M\)

For the cyclic interval \(I_s\), define

\[
 C_s(d)=\#\bigl(I_s\cap(I_s+d)\bigr).
\]

For \(1\le d<M\), direct interval overlap gives

\[
 C_s(d)=\max(0,s-d)+\max(0,s-(M-d)).
\]

If \(2\le s\le M-2\), then

\[
 C_s(d)=s-1
 \quad\Longleftrightarrow\quad
 d\equiv\pm1\pmod M.
\]

All other nonzero displacements have correlation at most \(s-2\).
An affine map of slope \(a\) sends the adjacent displacement \(1\) to
\(a\), while translation does not affect autocorrelation. Hence
\(A_a(I_s)=I_s\) forces

\[
 a\equiv\pm1\pmod M.
\]

Conversely, the relevant lifts of both signs act as the identity or
reversal of \(I_s\), except for the central-sign lift at odd \(m\), which
is separated in the next section.

## 4. Lift audit and the central sign

### 4.1 \(M\) odd

Reduction \(U(2M)\to U(M)\) is an isomorphism. Of the two lifts of a
residue modulo \(M\), exactly one is odd. The lifts of
\(\pm1\pmod M\) are therefore exactly

\[
 \pm1\pmod{2M}.
\]

The positive lift fixes every index. For the negative lift, the affine
formula and \(m\equiv s-1\pmod M\) give

\[
 A_{-1}(j)=s-1-j,
\]

which reverses \(I_s\). Thus both signs genuinely stabilize the interval.

### 4.2 \(M\) even

Both lifts of a unit modulo \(M\) are odd. The four lifts of the two signs
are

\[
 1,\quad -1,\quad M+1,\quad M-1\pmod{2M},
\]

apart from the coincidence \(M+1=-1\) at \(N=4\). The second lift differs
from the first by \(M\), and

\[
 \zeta^{a+M}=-\zeta^a.
\]

It is exactly multiplication of the base \(SL_2\) class by the central
element \(-I\). Functoriality gives

\[
 \operatorname{Sym}^m(-g)=(-1)^m\operatorname{Sym}^m(g).
\]

For even \(m\), the central sign is in the representation kernel. In the
affine formula the two lifts induce the same map modulo \(M\), because
\(Mm/2\) is divisible by \(M\). Thus all four lifts stabilize \(I_s\).
They consist only of inversion and central sign, so the extra two do not
give a new nonsign alias.

For odd \(m\), the lift \(a\mapsto a+M\) adds \(M/2\) to the affine map:

\[
 A_{a+M}(j)=A_a(j)+\frac M2\pmod M.
\]

A nonempty proper consecutive interval is not invariant under translation
by \(M/2\). The shift partitions the group into two-point orbits; an
invariant indicator would have equal values on the two halves, whereas a
proper initial interval has a boundary pair with unequal values. The
producer and independent tests check this elementary lemma at every even
\(M\le32\).

Therefore the central lifts are excluded in every odd-\(m\) interior case,
leaving only

\[
 a\equiv\pm1\pmod{2M}.
\]

When \(M\) is even and \(m\) is odd, \(m+1=kM+s\) forces \(s\) even.
The apparent edges \(s=1\) and \(s=M-1\) cannot occur in this parity;
there is no conflict with the edge statement below.

## 5. The three all-unit edges

The interval argument deliberately excluded three lengths, which are best
checked directly from the affine map.

For \(s=0\), \(I_s\) is empty.

For \(s=1\), one has \(m=kM\), and

\[
 A_a(0)=-\frac{(a-1)kM}{2}\equiv0\pmod M
\]

because \(a-1\) is even. Thus the singleton is fixed by every unit.

For \(s=M-1\), the interval is all of
\(\mathbb Z/M\mathbb Z\) except the index \(-1\). Here
\(m=(k+1)M-2\), so

\[
 A_a(-1)+1
 =-\frac{(a-1)(m+2)}2
 =-\frac{(a-1)(k+1)M}{2}
 \equiv0\pmod M.
\]

Every unit fixes the omitted point and hence its complement. Combining
these edge computations with the interior and lift arguments proves

\[
 \boxed{
 \operatorname{Stab}_{U(2M)}(E_m)=
 \begin{cases}
 U(2M),&s\in\{0,1,M-1\},\\
 \{a\in U(2M):a\equiv\pm1\pmod M\},&
 2\le s\le M-2,\ m\text{ even},\\
 \{\pm1\pmod{2M}\},&
 2\le s\le M-2,\ m\text{ odd}.
 \end{cases}}
\]

Composite \(M\) and \(N\) are included; neither primality nor
squarefreeness is used.

## 6. Closed factors on the edges

One full parity cycle has factor

\[
 C_m(T)=1-(-1)^mT^M.
\]

The even parity coset is the set of all \(M\)-th roots, while the odd
parity coset is the set of all roots of \(X^M+1\). With
\(m+1=kM+s\), the edge formulas are

\[
 s=0:\qquad F_m(T)=C_m(T)^k,
\]

\[
 s=1:\qquad
 F_m(T)=C_m(T)^k\bigl(1-(-1)^kT\bigr),
\]

and

\[
 s=M-1:\qquad
 F_m(T)=
 \frac{C_m(T)^{k+1}}{1-(-1)^{k+1}T}.
\]

For the last identity, augment the \(M-1\) residual atoms to a full parity
cycle. The missing exponent is

\[
 m-2(M-1)=(k-1)M,
\]

whose eigenvalue is \((-1)^{k-1}=(-1)^{k+1}\). Writing \(k+1\), rather
than \(k-1\), avoids a negative exponent in the first case \(k=0\). The
quotient is an exact integer polynomial.

For a common fixed-determinant lift with eigenvalues
\(\rho\zeta^a,\rho\zeta^{-a}\) and \(\rho^2=q\), every symmetric-power
atom acquires the common scalar \(\rho^m\). Substitute \(\rho^mT\) for
\(T\) in the formulas. Replacing \(\rho\) by \(-\rho\) is the separately
audited central-sign operation; it is not silently included at odd \(m\).

The producer locks all three formulas at orders
\(4,6,8,10,12,16,18,20\), using exact integer polynomial
multiplication and division.

## 7. Genuine nonsign primitive collapse

There are

\[
 \frac{\varphi(N)}2
\]

primitive determinant-one trace classes because inversion identifies
\(a\) with \(-a\).

If \(M\) is odd, the negative of a primitive \(N\)-th root has order \(M\),
not \(N\). Central sign leaves the primitive-\(N\) stratum, so an all-unit
edge has a genuine nonsign collision exactly when

\[
 \varphi(N)>2.
\]

If \(M\) is even, central sign remains in the primitive-\(N\) stratum.
For \(N>4\), quotienting by inversion and central sign leaves

\[
 \frac{\varphi(N)}4
\]

classes. An edge has a genuinely nonsign collision exactly when

\[
 \varphi(N)>4.
\]

For completeness, the standard elementary classification is
\(\varphi(n)\le4\) exactly for
\(n\in\{1,2,3,4,5,6,8,10,12\}\). In the present parity split it can be
seen directly as follows. If \(M\) is odd,
\(\varphi(2M)\le2\) leaves only \(N=6\): a prime \(p\ge5\) would make
\(p-1\mid\varphi(N)\), and the remaining powers of \(2\) and \(3\) give
the familiar list \(\varphi(n)\le2\) only for
\(n\in\{1,2,3,4,6\}\).

If \(4\mid N\) and \(\varphi(N)\le4\), an odd prime divisor can only be
\(3\) or \(5\). A factor \(5\) together with \(4\) already forces
\(\varphi(N)\ge\varphi(20)=8\). A factor \(3\) forces \(12\mid N\);
increasing either the \(2\)-adic or \(3\)-adic exponent then raises the
totient to at least \(8\), leaving \(N=12\). With no odd prime,
\(N=2^r\) and \(2^{r-1}\le4\), leaving \(N=4,8\). Hence the exact
nongenuine list is

\[
 N\in\{4,6,8,12\}.
\]

Thus \(N=10\) is the first genuine even-order example. Here \(M=5\), and
at \(m=M-2=3\),

\[
 F_3(T)=\frac{1+T^5}{1+T}
 =1-T+T^2-T^3+T^4.
\]

The two primitive trace classes modulo inversion share this complete
factor and are not related by a central sign inside primitive order \(10\).

## 8. Corner moduli

At \(N=4\), \(M=2\), every possible \(s\) is \(0\) or \(1\), both edges,
and \(U(4)=\{\pm1\}\). The central lift \(M+1\) already equals \(-1\).

At \(N=6\), \(M=3\), every possible \(s\) is \(0,1\), or \(2=M-1\).
Again all cases are edges, but \(U(6)=\{\pm1\}\), so no second primitive
class is present.

At \(N=8\) and \(N=12\), two primitive trace classes exist but form one
central-sign orbit. Their generic even-power equality is the kernel of
\(\operatorname{Sym}^{2r}\). At the available odd all-cycle edge, the
factor is invariant under spectral negation. Either way the pair remains
a sign pair, not a genuinely nonsign collision.

## 9. Bounded replay and resource discipline

The theorem is proved by the cycle, affine-interval, autocorrelation, and
lift arguments. The stored regression is a falsification net, not the
basis of the universal claim. It checks every even order \(4\le N\le64\),
every unit, and all \(0\le m<2N\). It also checks every interior interval
length and displacement, every available half-period shift, the exact
primitive class counts, and 24 named edge factors.

The canonical JSON records the exact work ledger under an exclusive cap of
150,000 units. There are zero floats, random samples, symbolic packages,
field enumerations, curve enumerations, polynomial-model enumerations, and
trace-range enumerations.

Replay with:

    python research/l-families/atlas/function_field/elliptic_symmetric_power_even_cyclotomic_aliases.py --check
    python -O research/l-families/atlas/function_field/elliptic_symmetric_power_even_cyclotomic_aliases.py --check
    python -m unittest tests.test_elliptic_symmetric_power_even_cyclotomic_aliases
    python -O -m unittest tests.test_elliptic_symmetric_power_even_cyclotomic_aliases

## 10. Scope firewall and next questions

This packet does **not** claim:

- that equality of one symmetric-power character implies equality of the
  complete factor;
- that these cyclotomic classes occur as Frobenius classes of elliptic
  curves over rational finite fields;
- that one local class supplies a motive, compatible system, automorphic
  family, or global Euler product;
- a rational fixed-determinant nonsign counterexample;
- literature priority or novelty;
- any consequence for analytic continuation, zero-free regions, RH, GRH,
  or zero statistics.

The next problems are simultaneous aliases across several representations,
Galois-orbit constraints in nontrivial coefficient fields, cross-prime
compatibility, and analogous central-kernel effects for other functorial
\(L\)-function detectors.
