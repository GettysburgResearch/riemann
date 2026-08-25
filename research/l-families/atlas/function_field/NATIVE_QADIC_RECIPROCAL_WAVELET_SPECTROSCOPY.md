# Native \(q\)-adic reciprocal-wavelet spectroscopy

**Status:** exact operator/normalization theorem plus exact finite arithmetic
for the locked \(q=3,5,7\) genus-two families. This is a project-defined native
\(q\)-adic analogue, not a literal port of dyadic XD, HCNC, or BPOE.

**Exact sources:** the norm-lattice obstruction, the all-\(q\) low-weight
moment profile and affine twist law, and the complete frozen joint
\((a_D,b_D)\) distributions. All are source-locked.

**What was run:** 2,008 integer recurrence updates and 1,757
atom-endpoint evaluations on 251 already-frozen coefficient atoms. No field,
curve, quintic, zero, or Euler-product sweep was run.

**Smallest remaining gap:** compute one same-characteristic tower or prove a
new marked-stack trace theorem for the first unresolved symmetric-power
channel. The finite \(q=3,5,7\) values cannot be promoted by interpolation.

## 1. Choosing the native path explicitly

The literal canonical kernel is dyadic:

\[
          (I-\sqrt2S_2)(I-S_2)^2.
\]

For odd \(q\), multiplication by \(2\) is not a translation of the native
norm lattice \(q^{\mathbf Z}\). The preceding obstruction packet proved that
endpoint aliasing loses one cancellation moment, while retaining continuous
log phase produces a phase-resolved rather than degree-convolution operator.

Here we deliberately take the other admissible path:

\[
\boxed{\mathcal K_q=(I-\sqrt q\,S_q)(I-S_q)^2.}
\tag{1}
\]

This restores a native unit degree shift. It also changes the detector, so
the result below is always called a \(q\)-adic analogue, never XD.

## 2. Reciprocal source and exact normalization

For a squarefree quintic \(D\), write its genus-two numerator as

\[
 P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4
\]

and define the complete reciprocal sequence by

\[
             \frac1{P_D(u)}=\sum_{n\geq0}r_D(n)u^n.
\tag{2}
\]

Thus \(r_D(0)=1\), and coefficient comparison gives

\[
\begin{aligned}
r_D(n)={}&-a_Dr_D(n-1)-b_Dr_D(n-2)\\
         &-qa_Dr_D(n-3)-q^2r_D(n-4),
\end{aligned}
\tag{3}
\]

with negative-index terms zero. Put

\[
 M_D(N)=\sum_{0\leq n\leq N}r_D(n),
 \qquad
 (S_qM)(N)=M(N-1).
\]

We use the empty-sum extension \(M_D(N)=0\) for \(N<0\), consistently with
the negative-index convention for \(r_D\).

For \(N\geq2\), two telescoping differences turn (1) into

\[
\boxed{
 W_D(N)
 =r_D(N)-(1+\sqrt q)r_D(N-1)+\sqrt q\,r_D(N-2).}
\tag{4}
\]

The symbol of (1) has:

- a double zero at the constant mode \(S_q=1\);
- a zero at \(S_q=q^{-1/2}\), so it removes the pure carrier
  \(q^{N/2}\).

These are exact normalization statements before any arithmetic sign is
examined.

## 3. The representation-theoretic identity

Let \(U_D\in USp(4)\) be normalized Frobenius. Since

\[
 P_D(u)=\det(I-\sqrt q\,uU_D),
\]

the standard generating function for complete symmetric characters gives

\[
\boxed{
 \frac{r_D(n)}{q^{n/2}}=\chi_{(n,0)}(U_D).}
\tag{5}
\]

Equivalently, \(r_D(n)\) is the physical normalization of the character of
\(\operatorname{Sym}^n\) of the standard representation. For \(Sp(4)\), this
symmetric power is irreducible: it has highest weight \(n\omega_1\), and the
Weyl dimension

\[
 \dim V_{n\omega_1}=\frac{(n+1)(n+2)(n+3)}6
                   =\dim\operatorname{Sym}^n(\mathbf C^4)
\]

leaves no lower summand.

The full affine action on monic quintics,

\[
 D(T)\longmapsto \alpha^{-5}D(\alpha T+\beta),
 \qquad \alpha\in\mathbf F_q^\times,
\]

sends \(a_D\) to \(\chi(\alpha)a_D\) and fixes \(b_D\). Its square-multiplier
subgroup gives the marked-curve isomorphisms; a nonsquare multiplier is the
twist-pairing coset. Choosing such an \(\alpha\) therefore replaces \(P_D(u)\)
by \(P_D(-u)\). It follows exactly, for every odd prime power, that

\[
                 \mathbb E[r_D(2k+1)]=0.
\tag{6}
\]

If \(A_n(q)=\mathbb E[r_D(n)]\), equations (4) and (6) yield the adjacent
pair law

\[
\boxed{
\begin{aligned}
\mathbb E[W_D(2k)]
   &=A_{2k}(q)+\sqrt q\,A_{2k-2}(q),\\
\mathbb E[W_D(2k+1)]
   &=-(1+\sqrt q)A_{2k}(q).
\end{aligned}}
\tag{7}
\]

Thus an odd endpoint contains no new mean channel: it repeats the preceding
even symmetric-power trace with a fixed carrier factor.

For the marked-Weierstrass stack normalization already proved on the branch,
(5) gives the especially simple bridge

\[
\boxed{T_{(n,0)}(q)=q^3A_n(q)\qquad(n\text{ even}).}
\tag{8}
\]

The native wavelet is therefore a symmetric-power spectroscope. This is its
cleanest use in the atlas; it is not automatically a sign detector.

## 4. Proved low-weight calibration

The existing exact all-\(q\) character profile contains

\[
\mathbb E[\chi_{(2,0)}]=\frac1{q^3}-\frac1{q^4},
\qquad
\mathbb E[\chi_{(4,0)}]=-\frac3{q^5}.
\]

Equations (5) and (8) recover

\[
\boxed{T_{(2,0)}(q)=q-1,\qquad T_{(4,0)}(q)=-3.}
\tag{9}
\]

This is the normalization control: the reciprocal series, compact character,
and marked-stack conventions agree before any new finite observation is
interpreted.

## 5. Exact finite spectroscopy

Using only the complete frozen joint coefficient laws gives:

| channel | \(q=3\) | \(q=5\) | \(q=7\) | status |
|---|---:|---:|---:|---|
| \(T_{(2,0)}\) | 2 | 4 | 6 | all-\(q\) theorem \(q-1\) |
| \(T_{(4,0)}\) | -3 | -3 | -3 | all-\(q\) theorem \(-3\) |
| \(T_{(6,0)}\) | -4 | -4 | -4 | exact finite only |
| \(T_{(8,0)}\) | -21 | 199 | -1029 | exact finite only |

The constant weight-six row is tempting, but three characteristics leave the
exact ambiguity

\[
          (q-3)(q-5)(q-7)Q(q).
\]

It is not an all-\(q\) theorem. The weight-eight row is more visibly
arithmetic: it reverses sign at \(q=5\). This is precisely the kind of
channel for which a same-characteristic tower or a geometric trace formula
is needed.

In terms of reciprocal means:

| \(q\) | \(A_2\) | \(A_4\) | \(A_6\) | \(A_8\) |
|---:|---:|---:|---:|---:|
| 3 | \(2/27\) | \(-3/27\) | \(-4/27\) | \(-21/27\) |
| 5 | \(4/125\) | \(-3/125\) | \(-4/125\) | \(199/125\) |
| 7 | \(6/343\) | \(-3/343\) | \(-4/343\) | \(-1029/343\) |

The sharp change at \(A_8\) is not caused by a change in filter
normalization: equation (7) isolates it as the new representation channel.

## 6. Sign experiment

Every tested endpoint \(N=2,\ldots,8\) has both memberwise signs in every
locked field. Selected rows are:

| \(q\) | \(N\) | negative / zero / positive |
|---:|---:|---:|
| 3 | 2 | 66 / 3 / 93 |
| 3 | 8 | 81 / 0 / 81 |
| 5 | 2 | 1112 / 80 / 1308 |
| 5 | 8 | 1369 / 0 / 1131 |
| 7 | 2 | 6531 / 84 / 7791 |
| 7 | 8 | 7098 / 0 / 7308 |

Signs are evaluated exactly in \(\mathbf Q(\sqrt q)\): when the rational and
radical coordinates oppose, the producer compares \(R^2\) with \(qS^2\).
No floating-point square root enters.

This gives a clean negative conclusion:

\[
\boxed{\text{purity + native carrier cancellation does not force a
memberwise wavelet sign.}}
\tag{10}
\]

The family mean is useful as spectroscopy, but an RH-facing route would
still need the canonical source/owner geometry and an individualization
theorem.

## 7. Claim boundary and next experiment

This packet uses the complete global numerator \(P_D\) and its reciprocal
series. It does not reproduce:

- the literal dyadic scale geometry of XD;
- the oriented near-collision source of HCNC;
- the owner/cross-core physical-squareclass ledger;
- or a family-to-principal-member amplifier.

The most informative next step is not another three-field fit. It is one of:

1. prove \(T_{(6,0)}\) or \(T_{(8,0)}\) directly by character sums;
2. compute \(p,p^2,p^3\) for one channel and test a held-out recurrence;
3. reconcile the marked trace with a rigorously identified local system.

## 8. Replay

From the repository root:

    python -B research/l-families/atlas/function_field/native_qadic_reciprocal_wavelet_spectroscopy.py --check
    python -B -O research/l-families/atlas/function_field/native_qadic_reciprocal_wavelet_spectroscopy.py --check
    python -B -m unittest tests.test_native_qadic_reciprocal_wavelet_spectroscopy -v
    python -B -O -m unittest tests.test_native_qadic_reciprocal_wavelet_spectroscopy -v
