# A positive self-adjoint realization for rational Bessel boundary conditions

Status: proposed component theorem, with a complete form construction and proof. It is a sufficient gate for a specified class of finite Bessel combinations; no application to every theta approximant, no RH proof, and no new zero-free boundary is asserted.

Scope: real polynomial combinations of a modified Bessel function and its radial derivative at a fixed a>0. This supplements the theta agent's finite-polynomial calculations. Classical Sturm–Liouville/closed-form construction is used explicitly below.

## 1. Source and notation

For E in C define the even-in-order, entire-in-E solution

\[
 y_E(u)=K_{i\sqrt E}(ae^u),\qquad u\ge0,
\]

where the square root is immaterial because \(K_\nu=K_{-\nu}\). It solves

\[
 -y_E''+a^2e^{2u}y_E=Ey_E
\tag{1}
\]

and decays at infinity. Its boundary derivative is
\(y_E'(0)=aK_{i\sqrt E}'(a)\). Standard Bessel identities and the decaying asymptotic are recorded at [DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9), [10.25.3](https://dlmf.nist.gov/10.25.E3), and [10.29](https://dlmf.nist.gov/10.29). The integral representation also proves that the solution is entire in E; it is not identically zero for any E, by its large-u asymptotic.

Let A,B be real polynomials, not both zero, and put

\[
 F(E)=A(E)y_E(0)+B(E)y_E'(0).
\]

The original z-plane transform is F((z/2)^2). Hence all of its zeros are real precisely when all zeros of F lie in \([0,\infty)\).

Factor out the real polynomial gcd d of A and B, writing A=dA_0, B=dB_0. Any root of d is automatically a root of F. Therefore a necessary preliminary gate is that every root of d lie in \([0,\infty)\). A common factor cannot be ignored when claiming all-real z zeros.

Suppose B_0 is not identically zero and the reduced rational boundary function has the representation

\[
 r(E)=-\frac{A_0(E)}{B_0(E)}
 =h-bE+\sum_{j=1}^m\frac{\gamma_j}{E-\lambda_j},
\tag{2}
\]

with h real, b>=0, distinct \(\lambda_j>0\), and \(\gamma_j>0\). The case m=0 is allowed. This is a rational anti-Herglotz function: it maps the upper half-plane into the lower closed half-plane. The representation itself, including positive residues and absence of a higher-degree polynomial part, is a substantive gate to verify for an actual finite Bessel approximant.

Define

\[
 m_a(0)=\frac{y_0'(0)}{y_0(0)}
 =-a\frac{K_1(a)}{K_0(a)}<0,
 \qquad r(0)=h-\sum_j\frac{\gamma_j}{\lambda_j}.
\tag{3}
\]

## 2. All-zero theorem, with a sharp form threshold

**Theorem.** Assume (2). The reduced function
\(F_0(E)=A_0(E)y_E(0)+B_0(E)y_E'(0)\) has all its zeros in \([0,\infty)\) if and only if

\[
 r(0)\ge m_a(0).
\tag{4}
\]

If the inequality is strict, all reduced zeros are positive. At equality, E=0 is a reduced zero and every other reduced zero is positive. Consequently, if all roots of d are nonnegative and (4) holds, every zero of F((z/2)^2) is real. The simpler condition r(0)>=0 is sufficient because m_a(0)<0.

The necessity assertion here is within the rational class (2), not among arbitrary rational boundary functions. Failing (2) does not by itself prove that the corresponding Bessel sum has nonreal zeros.

### Hilbert space and closed form

If b>0, use

\[
 \mathcal H_b=L^2(0,\infty)\oplus\mathbb C\oplus\mathbb C^m,
 \quad
 \|(y,\eta,x)\|^2=\|y\|_2^2+b|\eta|^2+\sum_j|x_j|^2.
\]

The form domain imposes \(\eta=y(0)\) and consists of

\[
 y\in H^1(0,\infty),\quad
 \int_0^\infty a^2e^{2u}|y(u)|^2du<\infty,
 \quad x\in\mathbb C^m.
\]

For b=0, omit the independent boundary coordinate and use the same y,x domain in \(L^2\oplus\mathbb C^m\). Define

\[
 \mathfrak q[y,x]=
 \int_0^\infty(|y'|^2+a^2e^{2u}|y|^2)du
 +h|y(0)|^2+\sum_j\lambda_j|x_j|^2
 +2\sum_j\sqrt{\gamma_j}\Re(y(0)\overline{x_j}).
\tag{5}
\]

This domain is dense. When b>0, vectors supported only in the boundary coordinate can be approximated in the ambient norm by narrow H^1 functions with prescribed trace. The usual trace estimate
\(|y(0)|^2\le\varepsilon\|y'\|_2^2+\varepsilon^{-1}\|y\|_2^2\)
shows that the trace and finite-coordinate coupling terms are infinitesimally form-bounded with respect to the positive bulk plus finite-coordinate norm. Thus (5) is a closed, lower-semibounded form and defines a self-adjoint operator. Its resolvent is compact: the confining potential makes the bulk form embedding compact by Rellich on finite intervals and a uniformly small L² tail; the remaining coordinates are finite dimensional.

### Eigenvalue equations and the sign of the boundary mass

Variation in the oscillator coordinates gives

\[
 (\lambda_j-E)x_j=-\sqrt{\gamma_j}\,y(0).
\]

Integration by parts in the bulk gives (1) and the boundary equation

\[
 y'(0)=h y(0)+\sum_j\sqrt{\gamma_j}x_j-bE y(0).
\tag{6}
\]

The minus sign before bE is forced by the positive boundary mass; it is not optional. Away from the poles, substituting
\(x_j=\sqrt{\gamma_j}y(0)/(E-\lambda_j)\)
into (6) gives exactly \(y'(0)=r(E)y(0)\).

Every decaying solution of (1) is a scalar multiple of y_E. The unique decaying branch is square integrable, and every operator eigenfunction uses that branch. It follows that, away from the poles, zeros of F_0 are precisely the eigenvalues of this self-adjoint operator.

At a pole E=lambda_j, coprimality ensures A_0(lambda_j) is nonzero. Thus F_0(lambda_j)=0 exactly when y_(lambda_j)(0)=0. The same condition gives an eigenvector: put the other oscillators equal to zero and take \(x_j=y_{\lambda_j}'(0)/\sqrt{\gamma_j}\). The derivative cannot also vanish, by uniqueness for the second-order ODE. Conversely the oscillator equation at this pole forces y(0)=0, so this accounts for every pole-case eigenvalue. Distinct poles prevent nonzero oscillator-only dark eigenvectors. Thus the zero/eigenvalue identification is complete, including poles.

### Positivity by a zero-energy ground state

Put \(w(u)=K_0(ae^u)>0\). It solves \(-w''+a^2e^{2u}w=0\). The ground-state identity, first for a core and then by closure, is

\[
 \int_0^\infty(|y'|^2+a^2e^{2u}|y|^2)du
 =\int_0^\infty w^2\left|\left(\frac yw\right)'\right|^2du
 -m_a(0)|y(0)|^2.
\]

Completing the oscillator squares gives

\[
 \mathfrak q[y,x]=
 \int_0^\infty w^2\left|\left(\frac yw\right)'\right|^2du
 +[r(0)-m_a(0)]|y(0)|^2
 +\sum_j\lambda_j
 \left|x_j+\frac{\sqrt{\gamma_j}}{\lambda_j}y(0)\right|^2.
\tag{7}
\]

Hence (4) makes the operator nonnegative, proving the all-zero assertion by the exact identification above. If (4) is strict, equality in (7) forces y=0 and x=0. Compact resolvent then puts the spectrum strictly above zero. At equality, the nonzero vector y=w, \(x_j=-\sqrt{\gamma_j}w(0)/\lambda_j\), is a zero eigenvector. If r(0)<m_a(0), that same vector has negative form value. The min–max principle and compact resolvent supply a negative eigenvalue, hence a negative-E zero of F_0 and a nonreal z zero. This proves necessity and all assertions of the theorem.

## 3. Common factors, zero poles and degenerate boundary cases

**Common factors.** Always extract d before testing r. Its roots multiply the Bessel transform regardless of the boundary realization. A negative root of d gives imaginary z zeros, and a nonreal root gives nonreal z zeros. Nonnegative roots, including zero, are harmless for the all-real assertion. Coprimality is also what makes the pole-case argument complete.

**A genuine pole at zero is different from a common zero.** Suppose the reduced r has an additional term gamma_0/E with gamma_0>0, and all its other poles satisfy (2). Its self-adjoint realization has an oscillator of energy zero coupled to y(0). It cannot be nonnegative, whatever the finite value of h and the positive boundary mass b. Take y=epsilon*w, set the zero oscillator to a fixed negative real value, and choose the positive oscillators to complete their squares. The coupling is a strictly negative term of order epsilon, while all other form terms are order epsilon². Thus the form has a negative direction and hence a negative eigenvalue. Since this negative eigenvalue is not a pole, it is a negative-E zero of F_0. A genuine positive-residue pole at zero therefore obstructs all-real z zeros in this class. If numerator and denominator cancel at zero, reduce first; there is then no zero pole.

**B identically zero.** After removing the polynomial factor, the reduced equation is y_E(0)=0. It is the Dirichlet half-line problem, whose eigenvalues are positive because the bulk potential is at least a². The roots of the removed polynomial remain a separate gate.

**A identically zero.** After removing the polynomial factor, the reduced equation is y_E'(0)=0. This is the Neumann problem and likewise has positive eigenvalues. It is also covered by m=0,h=b=0, because 0>m_a(0).

## 4. A local gate when the global rational realization fails

The global representation (2) is sufficient but can be unnecessarily strong for an approximation scheme. Let R>0 and retain the reduced coprime A_0,B_0, with B_0 not identically zero. Set \(D_R=\{E:|E|\le R^2/4\}\), and define r=-A_0/B_0 where finite. Suppose:

1. Every root of the removed common factor d in D_R is nonnegative real.
2. For every nonreal E in D_R at which r is finite,
   \(\Im r(E)/\Im E\le0\).
3. For every real \(E\in[-R^2/4,0)\) at which r is finite,
   \(r(E)\ne m_a(E)\), where \(m_a(E)=y_E'(0)/y_E(0)\).

**Local zero theorem.** These three conditions imply that every zero of F((z/2)^2) in \(|z|\le R\) is real. No decomposition of r into globally positive residues, no global self-adjoint realization, and no restriction on zeros outside that disk is required.

**Proof.** The decaying ODE solution satisfies the Lagrange identity

\[
 \frac{\Im m_a(E)}{\Im E}
 =\frac{\int_0^\infty|y_E(u)|^2du}{|y_E(0)|^2}>0
 \qquad(\Im E\ne0).
\tag{8}
\]

Here y_E(0) cannot vanish for nonreal E because that would give a nonreal eigenvalue of the ordinary self-adjoint Dirichlet half-line operator. A reduced zero with B_0(E) nonzero would require m_a(E)=r(E), contradicting condition 2. If B_0(E)=0, coprimality makes A_0(E) nonzero, and the reduced zero condition would require y_E(0)=0, again impossible for nonreal E. Thus no reduced nonreal-E zero exists in D_R.

For E<0, \(y_E(0)=K_{\sqrt{-E}}(a)>0\), so a pole of r is not a reduced zero. At regular points, condition 3 excludes the equation m_a(E)=r(E). Condition 1 handles the removed factors. All remaining zeros in D_R have E>=0, giving real z. This proves the assertion.

There is a convenient sufficient replacement for condition 3. If r has no poles on \([-R^2/4,0]\), condition 2 implies \(r'(E)\le0\) on the real interior, by taking the limit from the upper half-plane. If also

\[
 r(0)\ge m_a(0),
\]

then for E<0,

\[
 r(E)\ge r(0)\ge m_a(0)>m_a(E).
\]

The last strict inequality follows from the real version of (8), \(m_a'(E)=\int y_E^2/y_E(0)^2>0\), below the first Dirichlet eigenvalue. Hence condition 3 follows. The endpoint E=0 can be a zero without violating all-real z zeros.

### Cofinal local zero exclusion is enough

Suppose entire functions \(\mathcal F_j(z)\), each arising from a specified Bessel combination, converge locally uniformly to a nonzero entire target \(\mathcal F\). Suppose radii R_j tend to infinity and every zero of \(\mathcal F_j\) in \(|z|\le R_j\) is real, as can be established by the local gate. Then every zero of \(\mathcal F\) is real.

Indeed, a hypothetical nonreal target zero has a small closed disk around it avoiding the real axis and with a zero-free boundary. For all sufficiently large j this disk lies inside \(|z|\le R_j\), and Rouché's theorem forces a zero of \(\mathcal F_j\) there, a contradiction. More generally it suffices that the local approximant zeros obey \(|\Im z|\le\epsilon_j\) with \(\epsilon_j\to0\). An approximate sign condition on r must still supply the quantitative margin needed to prove such a strip bound; it cannot simply be substituted for condition 2.

This is a concrete repair path when a finite approximant fails the global positive-residue test only at remote energies. The local rational sign inequalities and locally uniform convergence still have to be established for the actual unbounded sequence. The argument does not turn failure of a sufficient global gate into success of the local one.

## 5. What this does and does not close

The theorem converts a verified rational boundary decomposition into an all-zero statement for a specified finite Bessel combination, including negative-energy exclusion and the sometimes-missed common factors. Positive coefficients in a Bessel mixture do not automatically give the residue and pole signs in (2). The theta approximants must pass those exact polynomial gates at unbounded degree before this construction can support a cofinal argument. No such all-degree verification is proved here.
