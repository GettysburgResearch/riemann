# The full direct majorant prevents gains from unequal lengths and hybrid numerator endpoints

**Status:** Proposed exact scalar theorem. Complete algebraic proof below; its identities and the finite witness cover are checked in `beyond_hybrid_barrier.py` using rational arithmetic.
**Scope:** The explicitly defined four-endpoint system below, with the existing count exponent and the full supplied direct majorant. Total length is free; either sign of the asymmetry is allowed; each class can independently select its best endpoint. The theorem does not bound actual character moments from below or assert that formal critical classes exist.
**Dependencies:** Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), Sections 14.1, 14.3, 14.8, 15.1, and 15.3; the exact four-witness certificate in `beyond_hybrid_barrier.md`.
**Relationship to the source:** Remark 14.13 excludes classwise mixing and unequal lengths from the stated refined optimality theorem. This note closes both possibilities for the concrete optimistic endpoint system written below. It does not assert optimality across unstated analytic estimates or arbitrary new contour constructions.

## 1. The enlarged estimate system

Write

\[
M=l_x+l_y,\qquad b=l_y-l_x,\qquad h=1-l_x+\ell,
\qquad l_x=(M-b)/2,\quad l_y=(M+b)/2.
\]

The full direct majorant in Liu's Section 15.1 requires

\[
B\ge B_{\rm low}:=\frac56+\frac{l_x}{6}-\frac\ell6+G+\frac K2,
\tag{1}
\]

where

\[
G=\max(0,b/12,b-l_y/2),
\]

\[
K=\max\left(0,\frac{1+3\ell-2M}{4},M+\ell-1,\frac{3\ell-1}{2}\right).
\tag{2}
\]

We allow the relaxed source domain \(M,l_y,\ell\ge0\). In particular, \(b\)
can be negative and \(l_x\) need not exceed \(\ell\). No balancing condition
\(M=1-\ell\) is imposed, and the algebra below does not impose \(\ell\le1/5\).

Retain the source's optimized count \(R=R_\kappa(\delta,x)\) from (14.3),
with \(\kappa_0\le\kappa\le1\), and put

\[
a=(1+\delta)/2,\qquad g=\delta x,\qquad
\mathcal R=(3R+1)/4,\qquad \theta=\frac{g}{6\kappa}.
\]

At the final row scale, grant each formal class the best of the following four
optimistic exponents:

\[
E_L=a-B-a l_y-\ell/2+\ell g+h(R+\delta/2-1/6),
\tag{3L}
\]

\[
E_R=a-B+(a-1)l_y-\ell/2+\ell g+h(R-1/6),
\tag{3R}
\]

\[
E_0=a-B-l_y/2-\ell/2+\ell g+h(\mathcal R-1/6),
\tag{3A}
\]

\[
E_\theta=E_0+\theta(h/2-l_y).
\tag{3B}
\]

The first two are the pointwise numerator's two contour duals. The last two are
the averaged numerator at shift zero and its full available prime capacity.
Every intermediate shift between these two averaged endpoints is affine in
the shift, so granting both endpoints is at least as strong. We also grant
full prime capacity independently of actual physical supply and omit all
positive contour, mesh, and local-factor losses. Such permissions enlarge the
scalar system; they do not claim that all four choices are analytically licensed
at every unequal length.

A successful uniform comparison in this enlarged system would require

\[
\min(E_L,E_R,E_0,E_\theta)\le0
\tag{4}
\]

for all formal controlled classes \(1/8\le\delta\le2B-1\), \(0\le x\le1/2\).

**Theorem.** Subject to (1)--(2), (4) is impossible if \(B<B_0\). It is also
impossible if \(B=B_0\) and \(\kappa>\kappa_0\). Here \(B_0=B_\flat\)
and \(\kappa_0=2B_0-1\) are the exact algebraic numbers in the companion
certificate. Thus varying the total length, changing the sign of the asymmetry,
and choosing independently among all four endpoints does not lower Liu's
boundary within this supplied estimate system.

This includes finite chains justified by prior bounds at least \(B_0\).
Starting strictly above \(B_0\) does not attain the endpoint in finitely many
steps. The existing limiting contradiction giving \(B_0\) remains unaffected.

## 2. The direct bound pays for every length change

First, the direct constraints imply the floor \(B\ge13/15\). This is the
short positive dual already recorded in Liu's Section 15.3 and in the earlier
repo direct-bound analysis. In detail, (1)--(2) imply

\[
L_0=\frac56+\frac M{12}-\frac\ell6,\quad
L_K=\frac13+\frac{7M}{12}+\frac\ell3,\quad
L_J=\frac{23}{24}-\frac M6+\frac{5\ell}{24}\quad\le B,
\]

and

\[
\frac{17}{30}L_0+\frac1{30}L_K+\frac25L_J=\frac{13}{15}.
\tag{5}
\]

The final row scale is positive throughout an attempted improvement: if
\(B\le B_0<7/8\), then \(L_K\le B\) and \(\ell\ge0\) imply
\(M<13/14\); since \(l_y\ge0\), this gives
\(h=1-l_x+\ell\ge1-M+\ell>1/14\).

Consequently all the companion witnesses, whose \(\delta<12/25\), lie in
the necessary controlled range because \(2B-1\ge11/15>12/25\).

Now set

\[
t=M-(1-\ell),\qquad \Delta=B_0-B,\qquad
\ell_0=4(11/12-B_0).
\]

Then \(K\ge\max(0,t)\), and \(G\ge\max(0,b/12)\). Rearranging (1)
gives the central resource inequality

\[
\boxed{\quad
\ell-\ell_0\ge4\Delta+\frac t3+2K+\frac{(-b)_+}{3}.
\quad}\tag{6}
\]

This keeps the direct price of shortening or lengthening the total range. It
also keeps the extra direct price that appears when \(b<0\).

## 3. Exact affine reduction of the four endpoints

Only classes with \(x=1/2\) and \(0<\delta<12/25\) are needed. For each
of the four endpoints \(j\), let \(E_j^\circ(b,\kappa)\) denote its value
at \(M=1-\ell_0\), \(\ell=\ell_0\), \(B=B_0\), with the same \(b\),
\(\kappa\), and class. Direct expansion gives

\[
E_j=E_j^\circ(b,\kappa)
       +A_j(\ell-\ell_0)+C_jt+\Delta.
\tag{7}
\]

The coefficients are as follows; \(R\) and \(\theta\) are the values at the
current class and \(\kappa\).

| Endpoint | \(A_j\) | \(C_j\) |
|---|---|---|
| \(L\) | \(-1/2+3R/2+3\delta/2\) | \(-1/6-(\delta+R)/2\) |
| \(R\) | \(-1/2+3R/2+\delta/4\) | \(-1/6-R/2+\delta/4\) |
| \(0\) | \(-1/8+9R/8+\delta/2\) | \(-7/24-3R/8\) |
| \(\theta\) | \(A_0+5\theta/4\) | \(C_0-3\theta/4\) |

In this table \(C_0\) denotes the third row's coefficient, not the earlier
balanced constant with that name.

Using only \(R\ge1-\delta\), \(\theta\ge0\), and
\(0\le\delta\le12/25\), one gets the strict sign bounds

| Endpoint | Lower bound on \(A_j\) | Lower bound on \(-C_j-A_j/3\) | Lower bound on \(C_j+7A_j/3\) |
|---|---:|---:|---:|
| \(L\) | \(1\) | \(1/3\) | \(5/3\) |
| \(R\) | \(2/5\) | \(13/75\) | \(47/75\) |
| \(0\) | \(7/10\) | \(19/75\) | \(86/75\) |
| \(\theta\) | \(7/10\) | \(19/75\) | \(86/75\) |

These inequalities have direct positive-coefficient proofs: substitute
\(R=1-\delta+\rho\) and \(\delta=12/25-u\), then subtract the stated
rational lower bound. Each resulting polynomial has nonnegative coefficients
in \(\rho,u,\theta\). The checker verifies these polynomial identities,
not samples of the variables.

Since \(A_j>0\), use (6) in (7). If \(t\le0\), use \(K\ge0\) and
\(C_j+A_j/3<0\); if \(t\ge0\), use \(K\ge t\) and
\(C_j+7A_j/3>0\). In either case,

\[
\boxed{\quad
E_j\ge E_j^\circ(b,\kappa)+(4A_j+1)\Delta
                 +A_j\frac{(-b)_+}{3}.
\quad}\tag{8}
\]

If \(t\ne0\), this inequality is strict. This is the balancing argument:
after the direct bound is paid, the changed total length cannot lower any of
the four relevant endpoint exponents at a witness class.

## 4. Nonnegative and negative asymmetry

For \(b\ge0\), the balanced values satisfy

\[
E_R^\circ-E_L^\circ=\frac\delta4(1+b-5\ell_0)>0,
\]

\[
E_0^\circ-E_\theta^\circ=\frac\theta4(1+b-5\ell_0)>0.
\tag{9}
\]

All the witnesses have \(\theta>0\). Thus the companion four-class cover
for \(E_L^\circ\) and \(E_\theta^\circ\) at \(\kappa_0\) also covers
the other two endpoints. These balanced exponents worsen as \(\kappa\)
increases, as proved in the companion note. At some witness class all four
are therefore nonnegative; they are all strictly positive if
\(\kappa>\kappa_0\). Equation (8) proves the theorem for \(b\ge0\).

For \(b<0\), let \(s_j=\partial_bE_j^\circ\). The extra term in (8)
gives

\[
E_j\ge E_j^\circ(0,\kappa)+(s_j-A_j/3)b+(4A_j+1)\Delta.
\tag{10}
\]

The four paid asymmetry slopes are

\[
s_L-A_L/3=-\frac16-\frac\delta2,
\qquad s_R-A_R/3=-\frac{1-\delta}{6},
\]

\[
s_0-A_0/3=-\frac{1+\delta}{6},
\qquad s_\theta-A_\theta/3=-\frac{1+\delta}{6}-\frac{2\theta}{3}.
\tag{11}
\]

All are negative. Hence \(b<0\) strictly increases the paid exponent. Choose
the single class \((\delta,x)=(\delta_0,1/2)\): at \(b=0\) and
\(\kappa=\kappa_0\), its averaged full-shift value is exactly zero and
all three other values are positive. Increasing \(\kappa\) only worsens
these balanced values. Equation (10) excludes every negative \(b\).

This finishes the proof, including free total length and either sign of the
asymmetry.

## 5. What has been certified and what remains outside the result

The standard-library checker certifies the algebraic number isolation,
critical-class identities, the exact four-witness sign cover, all four affine
reductions, their asymmetry and total-length slopes, and the twelve
positive-coefficient inequalities. Ordinary and optimized Python produce the
same receipt. No floating-point optimizer participates in acceptance.

The result is a barrier for the explicitly supplied bounds. It does not prove
that an arithmetic class with \(x=1/2\) exists, or that the actual numerator
and detector saturate separate moments. If a new theorem excludes those classes
or proves cancellation that changes their exponents, it changes an input and
is not ruled out.

The source-qualified intermediate-contour reduction already in PR #1005
reduces the stated block bounds to the relevant endpoint envelope in its
licensed range. The balanced hybrid theorem therefore includes that range.
The free-length theorem above is deliberately phrased for the four explicit
endpoints: it does not silently extend every analytic and Euler-factor
permission in the earlier intermediate-contour argument to arbitrary unequal
lengths.

This theorem identifies a substantive stopping point for parameter-only work.
Both potential omissions listed in Liu's refined optimality remark have now
been tested against the full direct price. Improving the numerical boundary
requires changing at least one of those supplied estimates or the source
geometry, rather than reassigning the same four endpoints to different classes.
