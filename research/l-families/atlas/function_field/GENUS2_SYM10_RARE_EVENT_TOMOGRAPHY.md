# Rare-event tomography for the genus-two \(\operatorname{Sym}^{10}\) channel

Status: **exact bounded tomography** of the source-locked complete
member-uniform \(q=3,5,7\) coefficient laws, together with exact compact
resonance formulas valid at every rank endpoint.  The finite rows are not an
all-\(q\) distribution theorem.

Scope: monic squarefree quintics and their reciprocal coefficient
\(r_D(10)=q^5\chi_{(10,0)}(U_D)\).  No polynomial, curve, finite field, root,
or cohomology group is enumerated by the replay.

What was actually run: 251 exact source atoms representing 17,068 complete
family members, one guarded length-ten integer recurrence per atom, an
independently derived 17-term sparse-polynomial equality check, and closed
compact-character algebra.

## 1. Why inspect the tails after proving the mean?

The all-field theorem determines

\[
 \sum_Dr_D(10)=q(q-1)T_{(10,0)}(q),
\]

but it does not say whether that signed total is a bulk effect or the residue
of a tiny exceptional stratum.  This matters because high-rank character
moments can be controlled by thin endpoint layers even when their weak bulk
law is stable.

For each complete finite family, define the tied outer absolute one-percent
tail by descending \(|r_D(10)|\) and including the largest threshold, with all
ties, whose retained mass is at least \(\lceil N/100\rceil\).

## 2. Exact finite tomography

| \(q\) | \(-/0/+\) members | tail threshold | tail members | tail share of \(L^1\) | tail share of \(L^2\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 57 / 18 / 87 | 401 | 6 | \(401/3958\) | \(160801/848976\) |
| 5 | 1125 / 50 / 1325 | 11928 | 36 | \(26046/205711\) | \(1281072/2879041\) |
| 7 | 7980 / 336 / 6090 | 50300 | 168 | \(73709/859163\) | \(5773597990/18244130049\) |

Thus these tied outer tails (which exceed one percent when the cutoff has
ties) carry about 19%, 44%, and 32% of the second moment in the three fields.
The first moment behaves very differently:

| \(q\) | full mean | tail mean | mean after deleting the tied tail | tail share of signed total |
|---:|---:|---:|---:|---:|
| 3 | \(638/27\) | 401 | \(237/26\) | \(401/638\) |
| 5 | \(18648/125\) | -175 | \(13545/88\) | \(-5/296\) |
| 7 | \(-100542/343\) | -1862 | \(-93094/339\) | \(3724/50271\) |

The \(q=3\) mean is tail-sensitive, the \(q=5\) tail almost cancels
internally, and the \(q=7\) mean remains of the same scale after trimming.
There is therefore no three-field rule that “the modular mean comes from the
outer one percent.”

## 3. Which exact strata carry the large \(L^2\) mass?

Put

\[
 \Delta=a_D^2-4b_D+8q.
\]

The integral split predicate is that \(\Delta\) is a nonnegative square with
the required parity; the repeated-factor locus is \(\Delta=0\).  Their exact
member counts and second-moment shares are:

| \(q\) | integral split members; \(L^2\) share | repeated members; \(L^2\) share |
|---:|---:|---:|
| 3 | 27; \(48907/424488\) | 0; 0 |
| 5 | 705; \(37053077/97887394\) | 15; \(2344977/8898854\) |
| 7 | 3570; \(2553482326/6081376683\) | 84; \(2573603650/18244130049\) |

At \(q=5\), all 15 repeated members lie in the tied tail.  At \(q=7\), 42
of 84 do.  No split member lies in the \(q=3\) tail.  A local factorization
predicate is therefore a strong finite correlate at two fields but not a
universal certificate of extremality.

The most coherent repeated row is

\[
 (a_D,b_D)=(0,2q),\qquad P_D(T)=(1+qT^2)^2.                  \tag{1}
\]

It occurs with 5 members at \(q=5\) and 42 at \(q=7\), lies entirely in the
outer tail, and contributes respectively
\(9765625/97887394\) and \(282475249/2027125561\) of the whole second
moment.  It is absent at \(q=3\).

## 4. Exact resonance ladders

The two central quadratic-square factors have generating functions

\[
 {1\over(1+qT^2)^2}
 =\sum_{n\ge0}(-1)^n(n+1)q^nT^{2n},
\qquad
 {1\over(1-qT^2)^2}
 =\sum_{n\ge0}(n+1)q^nT^{2n}.                                \tag{2}
\]

Hence

\[
 r_D(2n)=(-1)^n(n+1)q^n
 \quad\hbox{or}\quad
 r_D(2n)=(n+1)q^n.                                           \tag{3}
\]

At \(n=5\), these give the observed values \(-6q^5\) and \(+6q^5\).
They explain the \((0,\pm2q)\) atoms without fitting any finite histogram.

There is a much larger compact ceiling.  For every \(U\in\operatorname{USp}(4)\),

\[
 |\chi_{(10,0)}(U)|\le\dim\operatorname{Sym}^{10}(\mathbf C^4)
 =\binom{13}{3}=286,                                         \tag{4}
\]

with equality only at the scalar central classes \(U=\pm I\).  In
coefficient coordinates these would be

\[
 (a_D,b_D)=(\mp4\sqrt q,6q),
 \qquad P_D(T)=(1\mp\sqrt q\,T)^4.                           \tag{5}
\]

Thus the scalar equality rows have integral coefficient coordinates only on
square fields.  This identifies a potential square/nonsquare endpoint-access
bifurcation to test in a future source-complete extension-field census; it
does not assert that either scalar class is geometrically realized by a curve.

## 5. Exact zero rows

The \(r_D(10)=0\) atoms are

\[
\begin{array}{c|c}
q&(a_D,b_D;\text{ member count})\\ \hline
3&(-3,6;3),\ (0,0;12),\ (3,6;3),\\
5&(0,0;50),\\
7&(0,0;336).
\end{array}                                                    \tag{6}
\]

The nodal coefficient ghost \((0,0)\) explains all zeros at \(q=5,7\), but
not the two additional \(q=3\) atoms.  Those lie on the integral-trace
\(\operatorname{Sym}^3\) coefficient curve and are a small-field torsion
resonance, another warning that a zero character value need not identify a
generic geometric stratum.

## 6. Interpretation boundary

The exact finite conclusion is mixed and useful:

- thin strata can carry a highly disproportionate share of \(L^2\) energy;
- the signed first moment need not be tail-dominated;
- repeated and split factors are informative correlates, not memberwise
  certificates;
- square fields admit integral access to compact scalar endpoints that odd
  prime fields cannot reach.

Nothing here proves an asymptotic tail law, equidistribution, a monodromy or
endomorphism classification, a motive, a zero-density theorem, RH/GRH, or an
average-to-individual implication.

## Replay

```text
python -B research/l-families/atlas/function_field/genus2_sym10_rare_event_tomography.py --check
python -B -O research/l-families/atlas/function_field/genus2_sym10_rare_event_tomography.py --check
python -B -m unittest tests.test_genus2_sym10_rare_event_tomography
python -B -O -m unittest tests.test_genus2_sym10_rare_event_tomography
```
