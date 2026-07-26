# L-9312 — Support-aware one-node Padé gates for direct-ξ moment tables

Claim ID: **L-9312**  
Status: **PROPOSED**  
Agent: `gpt56-01-p`  
Date: 2026-07-26

## Purpose

A finite direct-ξ table with \(N\) horizontal nodes determines a finite family of
logarithmic response moments.  Adding one more horizontal node appears to add a
new \((N+1)\)-dimensional portfolio problem.  In fact, after the old moments are
frozen, the enlarged problem has only **one new scalar degree of freedom**.

This lemma gives:

1. the exact one-step moment recurrence;
2. the complete scalar interval forced by RH positivity;
3. a stronger interval when certified line-zero removal leaves a known support
   gap;
4. explicit square or support-localized polynomial witnesses whenever the
   scalar interval is violated;
5. a geometry-free normalized coordinate for ranking empirical candidates.

The finite algebra below is self-contained.  Its RH interpretation imports the
reviewed direct-ξ canonical-product/response dictionary and, when \(A>0\), the
complete-slab support-gap theorem.

---

## 1. Abstract finite setup

Let

\[
0<u_1<\cdots<u_N,
\qquad
D_U(y)=\prod_{j=1}^{N}(y+u_j).
\]

Assume that a linear response functional has the representation

\[
\mathcal L_U(P)
 =
 \int_{A}^{\infty}
 rac{P(y)}{D_U(y)}\,d
u(y),
	ag{1}
\]

for every real polynomial \(P\) of the required degree, where

\[
A\ge 0,
\qquad

u\ge 0.
\]

For the direct completed-ξ application, \(d
u\) is the residual RH-compatible
spectral measure after the declared certified critical-line factors have been
removed.  If no support information is used, take \(A=0\).

Fix an integer \(n\ge0\) and suppose the old moments

\[
a_k=\mathcal L_U(y^k),
\qquad
0\le k\le 2n,
	ag{2}
\]

are available as exact numbers or directed intervals.

Adjoin one exact node

\[
w\ge0,
\qquad
w
otin\{u_1,\ldots,u_N\}.
\]

Define the enlarged moments

\[
b_k(w)
 =
 \int_A^\infty
 rac{y^k}{(y+w)D_U(y)}\,d
u(y),
\qquad
0\le k\le 2n+1.
	ag{3}
\]

The scalar of interest is the Stieltjes value

\[
s(w)=b_0(w)
 =
 \int_A^\infty
 rac{1}{(y+w)D_U(y)}\,d
u(y).
	ag{4}
\]

---

## 2. Exact one-node recurrence

### Lemma 2.1

For every \(0\le k\le2n\),

\[
oxed{a_k=b_{k+1}(w)+w\,b_k(w).}
	ag{5}
\]

Equivalently, once \(s=b_0(w)\) is known, all enlarged moments are fixed by

\[
oxed{
 b_k(w)=(-w)^k s+\sum_{j=0}^{k-1}(-w)^{k-1-j}a_j
}
\qquad(k\ge1).
	ag{6}
\]

#### Proof

The identity

\[
rac{y^k}{D_U(y)}
=
rac{y^{k+1}+w y^k}{(y+w)D_U(y)}
\]

integrates to (5).  Iterating

\[
b_{k+1}=a_k-wb_k
\]

gives (6).  ∎

### Portfolio interpretation

Zero-extending an old portfolio to the new node multiplies its response
polynomial by \(y+w\).  Thus the old response \(y^k\) becomes

\[
(y+w)y^k=y^{k+1}+w y^k,
\]

which is the finite interpolation version of (5).

---

## 3. Two affine rank-one moment pencils

Put

\[
z(w)=igl(1,-w,w^2,\ldots,(-w)^nigr)^{\mathsf T}.
	ag{7}
\]

For a formal scalar \(t\), use (6) to define \(b_k(t)\), and form

\[
H_0(t)=igl[b_{i+j}(t)igr]_{0\le i,j\le n},
	ag{8}
\]

\[
H_A(t)=igl[b_{i+j+1}(t)-A b_{i+j}(t)igr]_{0\le i,j\le n}.
	ag{9}
\]

Also define the old Hankel matrix

\[
M_a=igl[a_{i+j}igr]_{0\le i,j\le n}.
	ag{10}
\]

### Lemma 3.1 — rank-one structure

There are fixed symmetric matrices \(C_0,C_A\), determined only by
\(w,A,a_0,\ldots,a_{2n}\), such that

\[
oxed{H_0(t)=C_0+t\,z z^{\mathsf T},}
	ag{11}
\]

\[
oxed{H_A(t)=C_A-(w+A)t\,z z^{\mathsf T}.}
	ag{12}
\]

Moreover,

\[
oxed{H_A(t)=M_a-(w+A)H_0(t).}
	ag{13}
\]

#### Proof

The coefficient of \(t\) in \(b_k(t)\) is \((-w)^k\), so the coefficient in
entry \(i,j\) of \(H_0\) is

\[
(-w)^{i+j}=z_i z_j.
\]

Using (5),

\[
b_{i+j+1}-A b_{i+j}
 =a_{i+j}-(w+A)b_{i+j},
\]

which proves (12) and (13).  ∎

---

## 4. The complete scalar RH interval

For the true value \(s=s(w)\) and every polynomial

\[
q(y)=q_0+q_1y+\cdots+q_ny^n,
\]

one has

\[
q^{\mathsf T}H_0(s)q
 =
 \int_A^\infty
 rac{q(y)^2}{(y+w)D_U(y)}\,d
u(y)
 \ge0,
	ag{14}
\]

and

\[
q^{\mathsf T}H_A(s)q
 =
 \int_A^\infty
 rac{(y-A)q(y)^2}{(y+w)D_U(y)}\,d
u(y)
 \ge0.
	ag{15}
\]

Define

\[
\mathcal I_{A,w}
 =
 \{t\in\mathbb R:\ H_0(t)\succeq0,\ H_A(t)\succeq0\}.
	ag{16}
\]

### Theorem 4.1 — one-scalar Padé gate

The set \(\mathcal I_{A,w}\) is a closed interval, possibly empty or unbounded.
Under the positive-measure hypothesis (1), it is nonempty and

\[
oxed{s(w)\in\mathcal I_{A,w}.}
	ag{17}
\]

Consequently, a directed enclosure \(S
i s(w)\) with

\[
S\cap\mathcal I_{A,w}=arnothing
	ag{18}
\]

contradicts the positive-measure representation.

#### Proof

Each condition in (16) is the inverse image of the closed convex PSD cone under
an affine map from one real variable.  Each inverse image is therefore a closed
interval, and their intersection is a closed interval.  Equations (14) and
(15) put the true value in that intersection.  ∎

### Exact witness extraction

A certificate does not need an interval eigensolver.

*Lower-bound violation.*  If a rational vector \(q\) satisfies

\[
\sup q^{\mathsf T}H_0(S)q<0,
	ag{19}
\]

then the explicit response polynomial

\[
oxed{P(y)=q(y)^2}
	ag{20}
\]

has a strict negative directed value.

*Support-upper-bound violation.*  If

\[
\sup q^{\mathsf T}H_A(S)q<0,
	ag{21}
\]

then the explicit support-valid response

\[
oxed{P(y)=(y-A)q(y)^2}
	ag{22}
\]

has a strict negative directed value.  It is nonnegative on the certified
support \([A,\infty)\).  When \(A=0\), (22) is the ordinary half-line response
\(yq(y)^2\).

Thus every failed endpoint produces a small exact polynomial witness.

---

## 5. Variational endpoint formulas

Because

\[
q^{\mathsf T}zz^{\mathsf T}q=q(-w)^2,
\]

normalize \(q(-w)=1\).  Then (11) gives

\[
t\ge -q^{\mathsf T}C_0q,
\]

and (12) gives

\[
t\le rac{q^{\mathsf T}C_Aq}{w+A}.
\]

Hence the sharp scalar endpoints are

\[
oxed{
	heta_-(w)
 =
 \sup_{\deg q\le n,\ q(-w)=1}
 igl(-q^{\mathsf T}C_0qigr),
}
	ag{23}
\]

\[
oxed{
	heta_+^{(A)}(w)
 =
 \inf_{\deg q\le n,\ q(-w)=1}
 rac{q^{\mathsf T}C_Aq}{w+A}.
}
	ag{24}
\]

Whenever the constrained quadratic problems are nondegenerate,

\[
\mathcal I_{A,w}
 =
 [	heta_-(w),	heta_+^{(A)}(w)].
	ag{25}
\]

If the relevant fixed matrices are invertible and positive on the constraint
complements, the extremizers are obtained by one exact linear solve:

\[
q_-=
rac{C_0^{-1}z}{z^{\mathsf T}C_0^{-1}z},
\qquad
	heta_-=-rac{1}{z^{\mathsf T}C_0^{-1}z},
	ag{26}
\]

\[
q_+=
rac{C_A^{-1}z}{z^{\mathsf T}C_A^{-1}z},
\qquad
	heta_+^{(A)}
=
rac{1}{(w+A)z^{\mathsf T}C_A^{-1}z}.
	ag{27}
\]

The checker should still verify the resulting rational vectors directly rather
than trusting floating-point inverses.

### Padé / truncated-moment interpretation

The scalar \(s(w)\) is a Stieltjes transform of the positive old measure.
Equations (23)–(24) are the finite lower and upper Markov–Padé bounds determined
by \(a_0,\ldots,a_{2n}\).  The support value \(A\) tightens the upper bound by
replacing the ordinary localizer \(yq^2\) with \((y-A)q^2\).

---

## 6. Geometry-free candidate coordinate

Suppose both endpoints are finite and

\[
W_A(w)=	heta_+^{(A)}(w)-	heta_-(w)>0.
	ag{28}
\]

Define

\[
oxed{
\eta_A(w)
 =
 rac{s(w)-	heta_-(w)}{W_A(w)}.
}
	ag{29}
\]

Under the positive-measure hypothesis,

\[
0\le\eta_A(w)\le1.
	ag{30}
\]

This coordinate is invariant under common positive scaling of the response
functional and separates a genuine boundary approach from a merely shrinking
absolute interval.

A candidate should not be ranked by one number alone.  Preserve the tuple

\[
oxed{
\left(
 s-	heta_-,
 	heta_+^{(A)}-s,
 \min(\eta_A,1-\eta_A),
 \log_{10}\kappa
ight),
}
	ag{31}
\]

where \(\kappa\) is a coefficient/interval-amplification bound for the finite
contraction.

* Small absolute moat but moderate \(\eta_A\): the entire Padé interval has
  collapsed; this is not necessarily close to violation.
* Small \(\eta_A\) but large absolute moat: the point is close only after a very
  wide normalization and is usually a poor immediate proof candidate.
* Small absolute moat and small normalized moat: highest-priority directed
  replay.

---

## 7. Exact primitive conditioning

For the enlarged node set \(\{w,u_1,\ldots,u_N\}\), the coefficient of the new
primitive in the basis response \(P(y)=1\) is

\[
oxed{
eta_w=-rac{1}{\prod_{j=1}^{N}(u_j-w)}.
}
	ag{32}
\]

The complete interval amplification is bounded by

\[
\kappa_1=\sum_i|eta_i|.
	ag{33}
\]

Near a repeated node, \(|eta_w|\) diverges.  Such a point can have an excellent
normalized Padé coordinate while requiring much more primitive precision.  The
coefficient ledger must therefore accompany every candidate.

A cancellation-resistant reconstruction chooses one old reference node
\(u_r\), writes

\[
b_0
 =
 eta_wigl(F(w)-F(u_r)igr)
 +\sum_{k=0}^{2n}p_k a_k,
	ag{34}
\]

and computes the exact polynomial coefficients \(p_k\) from the old-node
response map.  This supplies an algebraically independent replay of the direct
\((N+1)\)-point contraction.

---

## 8. Degree-15 specialization

For the current PR #103 table,

\[
N=16,
\qquad
n=7,
\qquad
(a_0,\ldots,a_{14})	ext{ are known}.
\]

Every new horizontal node \(w=x^2\) introduces one scalar \(b_0(w)\).  The two
complete degree-at-most-15 tests are the \(8	imes8\) matrices

\[
H_0(b_0),
\qquad
H_A(b_0).
\]

At \(A=0\), this recovers the zero-anchor theorem and its positive-node
extension.  After complete slab deflation, inserting the certified

\[
A=\min((T-a)^2,(b-T)^2)
\]

strictly sharpens the second matrix without requiring another completed-ξ
primitive.

---

## 9. Proof and promotion boundary

The finite recurrence, affine pencils, variational bounds, and witness
extraction are exact algebra.

A Riemann-ξ counterexample nomination additionally requires:

1. directed completed-ξ rectangles at every used node;
2. exact normalization and common-scale binding;
3. proof-grade critical-line factor or total-count gates;
4. a reviewed residual positive-measure dictionary;
5. for \(A>0\), complete certified removal of every line zero inside the slab;
6. exact rational witness contraction with upper endpoint below zero;
7. independent analytic and numerical reproduction.

No counterexample is asserted by this lemma.
