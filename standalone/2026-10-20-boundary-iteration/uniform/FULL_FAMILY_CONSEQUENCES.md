# Uniform reciprocals and shrinking angular sectors

20 October 2026. Status: proposed analytic consequences of the full-family
theorem in [ALL_UNITARY_REFINED_BOUNDARY.md](../global/ALL_UNITARY_REFINED_BOUNDARY.md).
All conclusions below retain that theorem's source dependencies. They
do not supply a new proof of its premise or lower its boundary.

## 1. Uniformity follows from the common boundary

Assume, over a fixed number field F, that every actual unitary Hecke
character has no zero on \(\Re s>\beta\), with \(1/2<\beta<1\).
Let \(\mathcal C(\chi,t)\) be the conductor in equation (2) of
[UNIFORM_INVERSE_AND_STRIPPING.md](UNIFORM_INVERSE_AND_STRIPPING.md).
Proposition 1 there gives, for every fixed positive gap \(\delta\),

\[
 (1/L_F)^{(j)}(\sigma+it,\chi)
 \ll_{F,\delta,\epsilon,j}\mathcal C(\chi,t)^\epsilon,
 \qquad \sigma\ge\beta+\delta,
\]

and

\[
 \sum_{N\mathfrak a\le x}\mu_F(\mathfrak a)\chi(\mathfrak a)
 \ll_{F,\epsilon}\mathcal C(\chi,0)^\epsilon x^{\beta+\epsilon}.
 \tag{1}
\]

These constants are uniform in the finite and archimedean conductors.
Uniform constants in the proof of the common boundary are not a
hypothesis: the Euler product and functional equation give the uniform
growth used by the complex-analysis argument. This does not make the
separate metaplectic transforms uniform in growing angular degree.

In the proposed full-family theorem one may take \(\beta=B_\flat\).
Thus (1) now includes the formerly omitted resonant unitary types.
The signed principal-factor threshold in Proposition 2 of the same note
is consequently \((3+B_\flat)/6\), approximately 0.645814441173327.
It remains a threshold for that operator, not a target zero-free bound.

## 2. A uniform prime-ideal estimate

Write \(\Lambda_F(\mathfrak a)\) for the ideal von Mangoldt function.
In the norm-twist convention \(L(s,N^{i\tau})=\zeta_F(s-i\tau)\),
put \(\delta_\chi=1\) if \(\chi=N^{i\tau}\) for some real \(\tau\),
and zero otherwise. Under the same premise,

\[
 \sum_{N\mathfrak a\le x}\Lambda_F(\mathfrak a)\chi(\mathfrak a)
 =\delta_\chi\frac{x^{1+i\tau}}{1+i\tau}
   +O_{F,\epsilon}\!\left(\mathcal C(\chi,0)^\epsilon
                             x^{\beta+\epsilon}\right).
 \tag{2}
\]

The pole term is omitted when \(\delta_\chi=0\). Additional fixed
Euler exclusions affect only the constants and their prime powers.

Here is the analytic step, to distinguish (2) from an unproved
uniform-zero-detector assertion. In the proof of Proposition 1, let
\(h_\chi\) be the logarithm of the pole-removed function. Cauchy's
formula applied to its bound (7) gives
\(h_\chi'(s)\ll\mathcal C(\chi,\Im s)^\epsilon\) on a smaller
fixed-gap half-plane. Therefore

\[
 -\frac{L_F'}{L_F}(s,\chi)
       -\frac{\delta_\chi}{s-1-i\tau}
 \ll_{F,\delta,\epsilon}\mathcal C(\chi,\Im s)^\epsilon.
 \tag{3}
\]

For a norm twist, the extra rational term after logarithmic
differentiation is \(-1/(s+1-i\tau)\), bounded in this half-plane.
For other characters it is absent.

Collecting ideals by rational norm bounds the Dirichlet coefficients
of \(-L'/L\) by \(d_{[F:\mathbb Q]}(m)\log m\), uniformly in
the character. Apply truncated Perron at
\(x_0=\lfloor x\rfloor+1/2\), and take height comparable to
\(x_0^2\mathcal C(\chi,0)^2\). This includes a possible translated
pole, since \(|\tau|\ll_F\mathcal C(\chi,0)\). Move to
\(\Re s=\beta+\epsilon/2\). There are no zeros in the rectangle;
the only residue is the displayed pole term. Equation (3), with its
arbitrary conductor exponent chosen sufficiently small, bounds the
vertical and horizontal integrals by the error in (2). The truncation
error is smaller by the coefficient bound and \(|x_0-m|\ge1/2\).
Replacing \(x_0\) by x in the main term costs at most a constant,
because its derivative has modulus one. This proves (2).

## 3. Eisenstein prime ideals in shrinking sectors

Let \(E=\mathbb Q(\omega)\), and omit the prime over 3. For each
ideal choose its unique primary generator c and set
\(\alpha(\mathfrak a)=c/|c|\). Write
\(\theta(\mathfrak a)=\arg\alpha(\mathfrak a)/(2\pi)\) in
\(\mathbb R/\mathbb Z\). For an arc I let \(|I|\) denote its
normalized length. The following estimate is uniform in every arc I:

\[
 \sum_{\substack{N\mathfrak p\le x\\
                  \theta(\mathfrak p)\in I}}
       \log N\mathfrak p
 = |I|x+O_{E,\epsilon}(x^{\beta+\epsilon}).
 \tag{4}
\]

To prove it, the k-th Fourier character is \(\alpha^k\), whose
finite conductor is bounded and whose archimedean conductor is
\(O((3+|k|)^2)\). For \(k\ne0\) it is not a norm character.
Equation (2) therefore bounds its prime-ideal sum by
\(x^{\beta+\epsilon}(3+|k|)^{2\epsilon}\). Removing higher
prime powers costs \(O_E(x^{1/2}\log^2 x)\), uniformly in k,
which fits the error since \(\beta>1/2\).

Apply the usual upper and lower trigonometric approximations to an
arc, of degree H. Their constant terms differ from \(|I|\) by
\(O(1/H)\), and their nonconstant coefficients are \(O(1/|k|)\).
The positive prime weights and (2) give an error

\[
 O\left(x/H+x^{\beta+\epsilon}H^{2\epsilon}\log(2H)\right).
\]

Take \(H=\lfloor x^{1-\beta}\rfloor\) and first choose the internal
epsilon small enough for the requested final error. This proves (4).
Partial summation gives the corresponding unweighted statement

\[
 \#\{\mathfrak p:N\mathfrak p\le x,
                    \theta(\mathfrak p)\in I\}
 =|I|\operatorname{Li}(x)+O_{E,\epsilon}(x^{\beta+\epsilon}).
 \tag{5}
\]

In particular the asymptotic is uniform on arcs of length at least
\(x^{\beta-1+\delta}\), for any fixed \(\delta>0\). With the proposed
full unitary boundary, this exponent is
\(B_\flat-1+\delta=-0.125113352960036\ldots+\delta\).
The former exception at the first angular harmonics could not simply
be omitted in this argument. The new full-family premise includes them.

This is an application of the proposed common boundary and classical
Fourier approximation. No priority claim is made, and no finite sector
experiment is offered as evidence for a global zero-free assertion.
