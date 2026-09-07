# Genus-two high-weight channel probe (DRAFT)

This note records a bounded attack on the unresolved second moment of

\[
F_D=\frac{q a_D^2-b_D^2}{q^2}
\]

over monic squarefree quintics. It separates exact representation algebra,
finite exact controls, and conjectural continuation. The replay is
`genus2_high_weight_channel_probe.py`; its frozen output is
`genus2_high_weight_channel_probe.json`.

The principal outcome is an exact triangularization of the three missing raw
moments. The proposed rational formulas remain conjectures: the symbolic audit
also shows exactly why the first one does not follow by a cheap cancellation.

## 1. Exact character coordinates

Put

\[
t=\operatorname{Tr}(U),\qquad e=e_2(U),qquad U\in USp(4).
\]

The family normalization is

\[
t^2=\frac{a_D^2}{q},\qquad e=\frac{b_D}{q}.
\]

An independent Kostant-character construction, checked coefficientwise as a
two-variable Laurent polynomial, gives

\[
\boxed{\chi_{0,3}=e^3-e^2-2et^2-e+3t^2},
\]

\[
\boxed{
\chi_{2,2}=-e^3+e^2t^2+e^2-et^2+e-t^4+2t^2-1
},
\]

and

\[
\boxed{
\chi_{0,4}=e^4-e^3-3e^2t^2-2e^2+6et^2+e+t^4-4t^2+1
}.
\]

Their dimensions at the identity are respectively `30`, `81`, and `55`.
The middle character has the useful exact factorization

\[
\boxed{
\chi_{2,2}=\big((1-e)^2-t^2\big)\big(t^2-e-1\big).
}
\]

This factorization is pointwise representation algebra. It does not impose a
sign on its family average.

## 2. The triangular raw-moment basis

The original honest obstruction is

\[
H=\chi_{0,4}+\chi_{2,2}+2\chi_{0,3}.
\]

The following three character packets instead align one-for-one with the
three unknown raw moments.

First,

\[
\boxed{R_3=\chi_{0,3}=e^3-e^2-2et^2-e+3t^2}.
\]

All terms except `e^3=b_D^3/q^3` already have proved family means.

Second, the cubic terms cancel in

\[
\boxed{
R_{22}=\chi_{0,3}+\chi_{2,2}
=e^2t^2-3et^2-t^4+5t^2-1.
}
\]

All terms except `e^2t^2=a_D^2b_D^2/q^3` already have proved means.

Finally, add twice this packet to `H`:

\[
\boxed{
\begin{aligned}
R_4
&=H+2R_{22}\\
&=\chi_{0,4}+3\chi_{2,2}+4\chi_{0,3}\\
&=e^4-5et^2-2t^4+14t^2-3e^2-2.
\end{aligned}}
\]

All terms except `e^4=b_D^4/q^4` already have proved means.

Thus the open arithmetic can be organized as the triangular chain

```text
R3   <-> b_D^3
R22  <-> a_D^2 b_D^2
R4   <-> b_D^4
```

This is exact for every family member and every odd prime power. It is a
change of basis, not an evaluation of the three averages.

## 3. Exact finite controls

The frozen aggregate sums at the three already explored fields are

| `q` | `sum b^3` | `sum a^2 b^2` | `sum b^4` |
|---:|---:|---:|---:|
| 3 | 8,256 | 8,352 | 45,552 |
| 5 | 788,080 | 857,040 | 8,278,480 |
| 7 | 14,205,744 | 16,117,248 | 221,057,088 |

These are now supplied by the independently replayable bounded enumeration in
`balanced_control_family_scan.py`.  That producer reconstructs every member's
`(a_D,b_D)` pair, hashes the complete coefficient ledger, and source-locks its
tests and arithmetic dependencies.  This packet reads the resulting fixture,
refuses any sentinel or channel mismatch, and does not enumerate a field.
The provenance dependency is one-way from that scan to this analysis.

Substitution into the exact character polynomials gives

| `q` | `mean chi_(0,3)` | `mean chi_(2,2)` | `mean chi_(0,4)` |
|---:|---:|---:|---:|
| 3 | `74/3^6` | `37/3^6` | `-19/3^7` |
| 5 | `614/5^6` | `213/5^6` | `-51/5^7` |
| 7 | `2386/7^6` | `621/7^6` | `-99/7^7` |

The three channels reconstruct the previously frozen values of `mean(H)`.
The raw `B4-2q*M22` combination independently reconstructs the frozen second
moment. Those checks make the new coordinates internally consistent, but
they do not add a fourth field or turn three values into a theorem.

## 4. Sparse candidate and its consequence

The channel rows match the strikingly sparse continuation

\[
\boxed{
\begin{aligned}
\langle\chi_{0,3}\rangle_q
&\stackrel{?}=\frac{q^4-2q-1}{q^6},\\
\langle\chi_{2,2}\rangle_q
&\stackrel{?}=\frac{2q^3-q^2-2q-2}{q^6},\\
\langle\chi_{0,4}\rangle_q
&\stackrel{?}=-\frac{2q^2+1}{q^7}.
\end{aligned}}
\]

There is a useful denominator-free normalization of exactly the same
candidate.  For a weight-`w` affine-invariant character, set

\[
T_\lambda(q)=
\frac{q^{w/2}}{q(q-1)}
\sum_{D\in\mathcal H_5(q)}\chi_\lambda(D).
\]

Since `|AGL_1(F_q)|=q(q-1)` and
`|H_5(q)|=q^4(q-1)`, the three proposed formulas are equivalent to

\[
\boxed{
T_{0,3}=q^4-2q-1,\qquad
T_{2,2}=2q^3-q^2-2q-2,\qquad
T_{0,4}=-(2q^2+1).
}
\]

This packages the arithmetic target in the form expected of a compactly
supported cohomological trace.  Interpreting the affine quotient as the
precise marked-Weierstrass local-system stack still requires checking the
central hyperelliptic-involution convention; that geometric identification
is a handoff, not a result proved by this packet.

Question marks are essential. If these formulas hold, the corresponding raw
moments are

\[
\mathbb E[b_D^3]
\stackrel{?}=
\frac{4q^6-9q^5+7q^4+8q^3-12q^2-9q-1}{q^3},
\]

\[
\mathbb E[a_D^2b_D^2]
\stackrel{?}=
\frac{(q+1)(5q^5-19q^4+29q^3-5q^2-21q-3)}{q^3},
\]

and

\[
\mathbb E[b_D^4]
\stackrel{?}=
\frac{10q^7-29q^6+21q^5+44q^4-47q^3-56q^2-10q-1}{q^3}.
\]

They would imply

\[
\boxed{
\langle H\rangle_q
\stackrel{?}=
\frac2{q^2}+\frac2{q^3}-\frac1{q^4}
-\frac8{q^5}-\frac4{q^6}-\frac1{q^7}
}
\]

and hence

\[
q^2\langle H\rangle_q\longrightarrow 2.
\]

This structured candidate would replace the earlier weak `9/4` nomination,
not refute a theorem: both constants currently rest on the same three fields.
It also predicts the complete second moment

\[
\boxed{
\mathbb E[F_D^2]
\stackrel{?}=
3-\frac8q+\frac6{q^2}+\frac8{q^3}-\frac9{q^4}
-\frac{19}{q^5}-\frac4{q^6}-\frac1{q^7}.
}
\]

## 5. Why the cubic channel is not yet proved

Expanding `b_D^3` introduces three ordered monic-quadratic slots. The bounded
factor-signature generator finds exactly 23 signatures:

| odd-radical degree | signature count |
|---:|---:|
| 0 | 4 |
| 2 | 10 |
| 4 | 5 |
| 6 | 4 |

The four generic degree-six types have leading mixture

\[
(1,3,3,1)/8.
\]

For a degree-six odd radical, write

\[
L_r(u)=(1-u)(1+p_1u+p_2u^2+qp_1u^3+q^2u^4).
\]

If the radical has `l` linear and `k` irreducible-quadratic primes, its
squarefree-sieve contribution has coefficients

\[
[p_1]S_5=-q^2+\binom{l+1}{2}+k,
\qquad [p_2]S_5=q-l.
\]

For the four generic types `(l,k)=(6,0),(4,1),(2,2),(0,3)`, these are

```text
p1: 21-q^2, 11-q^2, 5-q^2, 3-q^2
p2: q-6,    q-4,    q-2,   q
```

None vanishes identically. Therefore the sparse `chi_(0,3)` formula cannot be
proved by signature-level cancellation. One must evaluate genuine averages
of `p1`, `p2`, and the deletion-character factors across the 23 strata.

This is a useful negative result: it prevents the polynomial-looking finite
values from being mislabeled as elementary bookkeeping.

## 6. Three precise next lemmas

1. `B3-PRIMITIVE-TRACE-AVERAGE`: evaluate the marked `p1,p2` averages across
   the 23 cubic signatures. This decides `mean(chi_(0,3))`.

2. `M22-TRIANGULAR-TRACE-AVERAGE`: evaluate the existing 20 `M22`
   signatures after projecting to `R22`. This decides
   `mean(chi_(0,3)+chi_(2,2))` without carrying the cubic moment.

3. `B4-TRIANGULAR-TRACE-AVERAGE`: project the 54 `B4` signatures to `R4`.
   Once the first two lemmas are known, this decides `chi_(0,4)` and the full
   second moment.

A cohomological route is also plausible. Bergström proves polynomial
equivariant counts for pointed hyperelliptic moduli through weight seven in
odd characteristic, which is directly suggestive for the two weight-six
channels ([arXiv:math/0611813](https://arxiv.org/abs/math/0611813)). A proof
still has to identify our monic odd-quintic measure with the correct
stack-weighted marked-Weierstrass count; that comparison has not been made
here. The weight-eight `chi_(0,4)` channel also lies beyond that paper's stated
weight-seven range. Rubinstein and Wu study the identical squarefree monic
hyperelliptic ensemble and emphasize exact versus guessed moment formulas
([arXiv:1407.1018](https://arxiv.org/abs/1407.1018)), but their central-value
moments do not by themselves prove the coefficient formulas above.

## 7. Firewalls

- The three character identities and triangularization are exact.
- The 23-signature census and noncancellation statement are exact.
- The three sparse rational functions are conjectures matching only
  `q=3,5,7`.
- The three separate high raw sums are frozen controls from an independently
  replayable, content-hash-locked enumeration artifact.
- Only `q=5` samples the `chi_q(-1)=+1` branch, so no reciprocity branch is
  fitted or excluded.
- No field beyond the frozen three is enumerated by the replay.
- No effective equidistribution, number-field transfer, RH, or GRH claim is
  made.
