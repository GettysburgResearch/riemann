# R-103121 — The literal QPTI Euler–Beta field has a power-sized negative semiprime main

Claim ID: `R-103121`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC REFUTATION OF `EBD103120` AND THE LITERAL `QPTI103112` GATE**  
Created: 2026-08-26  
Supersedes: the disposition “QPTI not refuted” in `R-103120`; the open-gate status in `T-103120`  
Depends on: `L-103120`, `L-103121`, the classical squarefree-semiprime asymptotic, and the frozen subpower closed-ledger premise  
RH status: **not assumed; RH remains unproved**

The exact transform of `L-103120` exposes more than a nonzero owner mode.  Its
complete Möbius recombination has a strictly negative first global mode.  The
literal completed quarter-power gate is therefore false.

## 1. The declared live Euler–Beta current

After removing the root and first-chaos core layers, the current declared in
`L-103120` is

\[
\boxed{
 H_{\rm EB}(X)
 =\sum_{\substack{c\ {\rm squarefree}\\\omega(c)\ge2}}
 \frac{\mu(c)}{\binom{\omega(c)+2}{2}c}
 \sum_{\substack{p<q\\(pq,c)=1}}
 \frac1{\sqrt{pq}}
 K_L\!\left(\frac{X}{pqc^2}\right).
}
\tag{R-103121.1}
\]

This is exactly the source polynomial used in `R-103120.1`, now returned to
physical space.  Repeated owners `p=q` are absent.  The marked-67 duplication
and every finite exceptional set alter only lower-order terms.

## 2. Imported arithmetic input

We use the classical Landau theorem for squarefree semiprimes:

\[
 A_2(Z):=\#\{p<q:pq\le Z\}
 \sim Z\frac{\log\log Z}{\log Z}.
\tag{R-103121.2}
\]

This is the only imported asymptotic theorem.  Deleting any fixed finite set of
prime factors does not change its leading term.

Let `E` be a fixed finite prime set and let `K` be compactly supported and of
bounded variation on `[1,8]`.  Stieltjes partial summation applied to
(R-103121.2), uniformly on `Z/8<=t<=Z`, gives

\[
\boxed{
 \sum_{\substack{p<q\\p,q\notin E}}
 \frac1{\sqrt{pq}}K\!\left(\frac Z{pq}\right)
 =\widehat K(1/2)\sqrt Z\frac{\log\log Z}{\log Z}
 (1+o(1)).
}
\tag{R-103121.3}
\]

Indeed, the main integral is

\[
 \frac{\log\log Z}{\log Z}
 \int_{Z/8}^Zt^{-1/2}K(Z/t)\,dt
 =\widehat K(1/2)\sqrt Z\frac{\log\log Z}{\log Z}.
\]

The jumps of `K_L` at the dyadic boundaries are harmless because bounded
variation is sufficient.

## 3. Summation over the varying core

For fixed `c`, apply (R-103121.3) with `Z=X/c^2` and with the primes dividing
`c` excluded.  This gives

\[
 \frac1c
 \sum_{\substack{p<q\\(pq,c)=1}}
 \frac1{\sqrt{pq}}K_L\!\left(\frac{X/c^2}{pq}\right)
 =\frac{\widehat K_L(1/2)}{c^2}
 \sqrt X\frac{\log\log X}{\log X}(1+o_c(1)).
\tag{R-103121.4}
\]

The passage from fixed `c` to the complete core sum is legitimate.  To see
this without a hidden uniformity assumption, fix `0<eta<1/4` and split:

```text
c <= C;
C < c <= X^eta;
c > X^eta.
```

For the first range use (R-103121.4).  In the middle range, the standard upper
bound

\[
 A_2(Z)\ll Z\frac{\log\log(3Z)}{\log(3Z)}
\]

and the support of `K_L` give a majorant

\[
 \ll \sqrt X\frac{\log\log X}{\log X}
 \sum_{c>C}\frac1{c^2}.
\]

For `c>X^eta`, the trivial semiprime count gives

\[
 \ll \sqrt X\sum_{c>X^\eta}\frac1{c^2}
 =O(X^{1/2-\eta}).
\]

Let first `X` tend to infinity and then `C` tend to infinity.  Absolute
convergence of (L-103121.1) yields

\[
\boxed{
 H_{\rm EB}(X)
 =D_{\ge2}\widehat K_L(1/2)
 \sqrt X\frac{\log\log X}{\log X}(1+o(1)).
}
\tag{R-103121.5}
\]

By `L-103121`, the coefficient is strictly negative.  Therefore

\[
\boxed{
 H_{\rm EB}(X)
 =-C_0\sqrt X\frac{\log\log X}{\log X}(1+o(1)),
 \qquad
 C_0=D_{\ge2}(2-\sqrt2)^2\log2>0.
}
\tag{R-103121.6}
\]

## 4. Negative mass is power-sized

Regular variation makes (R-103121.6) uniform on one fixed dyadic ratio.
Consequently

\[
\boxed{
 \int_Y^{2Y}(H_{\rm EB}(X))_-\frac{dX}{X}
 =2(\sqrt2-1)C_0
 \sqrt Y\frac{\log\log Y}{\log Y}(1+o(1)).
}
\tag{R-103121.7}
\]

This is `Y^(1/2+o(1))`, not `Y^o(1)`.

If the inherited field `H_closed` has the asserted subpower logarithmic `L1`
cost, then

\[
 \int(H_{\rm EB}+H_{\rm closed})_-
 \ge \int(H_{\rm EB})_- -\int|H_{\rm closed}|,
\]

so it cannot cancel (R-103121.7).

## 5. Disposition

The following statements are now false as literally formulated:

```text
EBD103120 is an open potentially subpower estimate;
QPTI103112 for the complete Euler–Beta/quarter-power field is subpower;
EBD103120 <=> QPTI103112 <=> BCI102990 <=> HMO102940
  as a subpower-preserving completed-source transfer.
```

The exact finite Euler–Beta algebra of `L-103120.2--L-103120.7` is retained.
What fails is its promotion to a conclusion-bearing subpower current.

This refutation does **not** disprove RH.  It disproves a stronger producer
criterion.  It also does not refute the ordinary Möbius ratio-eight wavelet,
whose Mellin transform contains `1/zeta(s+1/2)` and therefore has no such
semiprime pole.  The repaired frontier is `T-103130`.
