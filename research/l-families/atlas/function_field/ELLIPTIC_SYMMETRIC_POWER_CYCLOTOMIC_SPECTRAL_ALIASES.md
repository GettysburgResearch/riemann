# Cyclotomic aliases of complete elliptic symmetric-power spectra

## Result in one paragraph

Let an \(SL_2\) semisimple class have eigenvalues \(z,z^{-1}\), and let
\(\zeta\) be a primitive root of odd order \(N\).  This packet proves the
exact all-\(N\), all-\(m\) classification

\[
 \operatorname{Spec}\!\left(\operatorname{Sym}^m
   \operatorname{diag}(\zeta,\zeta^{-1})\right)
 =
 \operatorname{Spec}\!\left(\operatorname{Sym}^m
   \operatorname{diag}(\zeta^a,\zeta^{-a})\right)
\]

for \(\gcd(a,N)=1\): equality holds exactly when

\[
 a\equiv \pm1\pmod N
 \qquad\text{or}\qquad
 m\equiv -2,-1,0\pmod N.
\]

The first alternative is the original semisimple conjugacy class.  The
second collapses all primitive classes and, for odd N at least 5, gives
genuine non-sign aliases.  (At N=3 there is only one primitive class modulo
inversion.)
In particular, orders \(5,7,9,11\) explain complete-factor aliases at
\(m=3,5,7,9\).  These examples have algebraic irrational traces.  A separate
quotient-group argument proves that for rational \(x,y,q\), with fixed
\(q\ne0\), equality of complete symmetric-power factors for \(m\ge1\)
forces \(x=\pm y\).  Thus the cyclotomic examples do not contradict rational
trace recovery.

This is a local representation-theoretic packet.  It enumerates no field,
curve, or polynomial model and constructs no global Euler product.

## 1. Complete spectra, not one character value

For

\[
 g_z=\operatorname{diag}(z,z^{-1}),
\]

the complete symmetric-power eigenvalue multiset is

\[
 S_m(z)=
 \left\{z^{m-2j}:0\le j\le m\right\},
\]

with multiplicity.  Its factor is

\[
 F_m(z;T)=
 \prod_{j=0}^{m}\left(1-z^{m-2j}T\right).
\]

The upstream packet
`elliptic_symmetric_power_trace_aliasing.json` studies only

\[
 \tau_m(z+z^{-1})=\sum_{\lambda\in S_m(z)}\lambda.
\]

Equality of that one sum need not imply equality of \(S_m\) or \(F_m\).
This packet binds the upstream payload for provenance and then uses none of
its finite histograms.

## 2. Exact odd-order stabilizer theorem

Fix a primitive \(N\)-th root \(\zeta\), where \(N\ge3\) is odd, and a unit
\(a\) modulo \(N\).  Equality of spectra is equality of the exponent
multisets

\[
 E_{m,N}=
 \left\{m-2j\bmod N:0\le j\le m\right\}
\]

and \(aE_{m,N}\).

Write

\[
 m+1=kN+s,\qquad 0\le s<N.
\]

Because the step \(-2\) is a unit modulo odd \(N\), the first \(kN\) terms
give \(k\) copies of every residue.  The nonuniform remainder is

\[
 R_s=
 \left\{s-1-2j\bmod N:0\le j<s\right\}.
\]

Multiplication by \(2^{-1}\) turns \(R_s\) into a cyclic interval of length
\(s\).  Therefore the problem is the multiplicative stabilizer of one
centered cyclic interval.

### 2.1 The interior cases

For the standard cyclic interval \(I_s=\{0,\ldots,s-1\}\), put

\[
 C_s(d)=\#\bigl(I_s\cap(I_s+d)\bigr).
\]

For \(1\le d\le N-1\), direct interval overlap gives

\[
 C_s(d)=
 \max(0,s-d)+\max(0,s-(N-d)).
\]

If \(2\le s\le N-2\), then

\[
 C_s(d)=s-1
 \quad\Longleftrightarrow\quad
 d\equiv\pm1\pmod N,
\]

and every other nonzero displacement has correlation at most \(s-2\).
Autocorrelation is unchanged by translating or scaling an interval.  If
\(aR_s=R_s\), multiplication by \(a\) sends the displacement \(1\) to the
displacement \(a\), so

\[
 C_s(a)=C_s(1)=s-1.
\]

The unique-maximum statement forces \(a\equiv\pm1\pmod N\).

### 2.2 All three edge cases

No endpoint is hidden in the preceding proof:

- \(s=0\), equivalently \(m\equiv-1\pmod N\): the remainder is empty.
- \(s=1\), equivalently \(m\equiv0\pmod N\): the remainder is \(\{0\}\).
- \(s=N-1\), equivalently \(m\equiv-2\pmod N\): the remainder is every
  nonzero residue.

Every unit preserves each of these three sets.  Combining the interior and
edge cases proves

\[
 \boxed{
 S_m(\zeta)=S_m(\zeta^a)
 \iff
 a\equiv\pm1\pmod N
 \ \text{or}\
 m\equiv-2,-1,0\pmod N.}
\]

The statement includes composite odd \(N\); primality was not used.

## 3. The three adjacent universal factors

For any primitive \(\zeta\) of odd order \(N\),

\[
 \prod_{r=0}^{N-1}(1-\zeta^rT)=1-T^N.
\]

The exponent multiplicities at the first three exceptional powers are
especially transparent.

### 3.1 Power \(m=N-2\)

The exponents are every nonzero residue once, so

\[
 S_{N-2}(\zeta)=\{\zeta,\zeta^2,\ldots,\zeta^{N-1}\}
\]

and

\[
 F_{N-2}(\zeta;T)
 =
 \frac{1-T^N}{1-T}
 =
 1+T+\cdots+T^{N-1}.
\]

### 3.2 Power \(m=N-1\)

Every residue occurs once:

\[
 F_{N-1}(\zeta;T)=1-T^N.
\]

### 3.3 Power \(m=N\)

Every residue occurs once and residue \(0\) occurs one additional time:

\[
 F_N(\zeta;T)=(1-T)(1-T^N).
\]

These are complete factors, not merely equal first coefficients.

### 3.4 Scalar prefactors and lift signs

The displayed formulas are for determinant-one classes.  For a fixed
determinant \(q\), choose one common scalar lift \(\rho\) with
\(\rho^2=q\), and compare the classes with eigenvalues

\[
 \rho\zeta^a,\qquad \rho\zeta^{-a}.
\]

Every eigenvalue in \(\operatorname{Sym}^m\) has the same additional scalar
\(\rho^m\).  Hence the exact fixed-determinant formula is obtained by
replacing \(T\) with \(\rho^mT\), and the factors remain identical for all
primitive powers \(a\) using that same lift.

This qualification matters.  Replacing \(\rho\) by \(-\rho\) multiplies the
complete \(\operatorname{Sym}^m\) spectrum by \((-1)^m\).  Since \(N-1\) is
even, the positive and negative lifts give the same \(m=N-1\) factor.
Since \(N-2\) and \(N\) are odd, the negative lift instead sends \(F(T)\) to
\(F(-T)\).  It is not silently included in those two alias statements.

More generally, if \(m=kN-2,kN-1,kN\), the normalized factors are

\[
 \frac{(1-T^N)^k}{1-T},
 \qquad
 (1-T^N)^k,
 \qquad
 (1-T^N)^k(1-T),
\]

respectively, with the natural interpretation \(k\ge1\) in the first two
formulas.

## 4. Orders 5, 7, 9, and 11

At \(m=N-2\), all primitive classes modulo inversion share
\((1-T^N)/(1-T)\).  Their base traces

\[
 x_a=\zeta^a+\zeta^{-a}
\]

are roots of the following irreducible polynomials.

| \(N\) | \(m=N-2\) | primitive classes modulo inversion | minimal polynomial |
|---:|---:|---:|---|
| 5 | 3 | 2 | \(X^2+X-1\) |
| 7 | 5 | 3 | \(X^3+X^2-2X-1\) |
| 9 | 7 | 3 | \(X^3-3X+1\) |
| 11 | 9 | 5 | \(X^5+X^4-4X^3-3X^2+3X+1\) |

The generator certifies these without a symbolic package.  Define

\[
 C_0(X)=2,\qquad C_1(X)=X,\qquad
 C_n(X)=XC_{n-1}(X)-C_{n-2}(X).
\]

Then \(C_n(z+z^{-1})=z^n+z^{-n}\).  Exact integer polynomial arithmetic
checks

\[
 C_N(X)-2=(X-2)M_N(X)^2
\]

for \(N=5,7,11\), and

\[
 C_9(X)-2=(X-2)(X+1)^2M_9(X)^2.
\]

For each displayed \(M_N\), every possible monic factor of degree at most
half its degree is exhausted modulo \(2\); none divides.  Gauss's lemma then
gives irreducibility over the rationals.

The aliases are not sign pairs.  Equality of traces for determinant-one
semisimple classes identifies \(z\) with \(z^{-1}\).  Equality with a
negative trace would identify an odd-order root with the negative of an
odd-order root, which has even order.  That is impossible.

## 5. Rational fixed-determinant recovery

The cyclotomic aliases disappear when both base traces and the common
determinant are rational.

Let

\[
 P_x(U)=U^2-xU+q,\qquad
 P_y(U)=U^2-yU+q,
\]

where \(x,y,q\in\mathbb Q\), \(q\ne0\), and take semisimple roots
\(\alpha,\beta\) and \(\gamma,\delta\).  For \(m\ge1\), set

\[
 A_x=
 \left\{\alpha^{m-j}\beta^j:0\le j\le m\right\}.
\]

The quotient group intrinsic to this multiset is

\[
 \Gamma(A_x)=
 \left\langle u/v:u,v\in A_x\right\rangle
 =
 \left\langle\alpha/\beta\right\rangle.
\]

All quotients are powers of \(\alpha/\beta\), while the adjacent \(j=0,1\)
terms exhibit the generator itself.  This remains true for \(m=1\) and for
repeated eigenvalues.  Equality of complete factors gives equality of the
root multisets and therefore equality of these quotient groups.

Write \(r_x=\alpha/\beta\).  If the common group is infinite, its only
generators are mutual inverses.  Therefore

\[
 r_y=r_x^{\pm1}.
\]

Since

\[
 r_x+r_x^{-1}=\frac{x^2}{q}-2,
\]

we obtain \(x^2=y^2\).

If the group is finite, \(r_x\) is a root of unity and
\(r_x+r_x^{-1}\) is a rational algebraic integer in the real interval
\([-2,2]\).  It is therefore one of

\[
 -2,-1,0,1,2.
\]

The corresponding eigenratio orders and trace squares are

| order of \(r_x\) | \(r_x+r_x^{-1}\) | \(x^2/q\) |
|---:|---:|---:|
| 1 | 2 | 4 |
| 2 | -2 | 0 |
| 3 | -1 | 1 |
| 4 | 0 | 2 |
| 6 | 1 | 3 |

The quotient group fixes its order, so the table again gives
\(x^2=y^2\).  Over \(\mathbb Q\),

\[
 \boxed{x=\pm y.}
\]

For orders \(5,7,9,11\), the primitive trace square is not rational; hence
no choice of fixed rational \(q\) can turn these examples into two rational
base traces.  This is the precise boundary between the algebraic
cyclotomic aliases and the rational recovery theorem.

## 6. Bounded replay and resource discipline

The theorem is not inferred from a search.  The stored replay nevertheless
checks every unit and two full \(m\)-periods for every odd
\(3\le N\le51\), and independently checks the cyclic-interval
autocorrelation formula at every admissible length and displacement.

- 37,508 unit-stabilizer candidates;
- 20,800 autocorrelation comparisons;
- 18 named cyclotomic/factor/source certificates;
- 58,326 total accounted units under an exclusive cap of 100,000;
- zero field, curve, or polynomial-model enumerations;
- zero random samples, floats, or symbolic packages.

Replay with:

```powershell
python research/l-families/atlas/function_field/elliptic_symmetric_power_cyclotomic_spectral_aliases.py --check
python -O research/l-families/atlas/function_field/elliptic_symmetric_power_cyclotomic_spectral_aliases.py --check
python -m unittest tests.test_elliptic_symmetric_power_cyclotomic_spectral_aliases
python -O -m unittest tests.test_elliptic_symmetric_power_cyclotomic_spectral_aliases
```

## 7. Firewalls and next questions

This packet does **not** claim:

- that a scalar \(\tau_m\) collision is a complete-factor collision;
- that the algebraic traces above occur as rational elliptic traces;
- that one local compact conjugacy class supplies a curve, motive,
  compatible Euler product, monodromy group, or automorphic family;
- a closed classification for even root order;
- literature priority or novelty;
- any implication for analytic continuation, a zero-free region, RH, or
  GRH.

The immediate extensions are an exact affine-coset classification for even
root order, arithmetic realization over nontrivial coefficient fields, and
cross-prime compatibility constraints capable of distinguishing a local
cyclotomic coincidence from a genuine family of \(L\)-functions.
