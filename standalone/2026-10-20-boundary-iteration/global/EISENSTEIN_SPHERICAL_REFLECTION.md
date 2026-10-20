# Spherical cubic reflection with all finite masks retained

Status: proposed source-dependent theorem; native extension of the pinned
completed-reflection proof to its missing spherical case.

Scope: the Eisenstein field \(E=\mathbb Q(\sqrt{-3})\), arbitrary fixed
finite-ray conductor, arbitrary moving sextic prime masks, and any fixed
number of selected prime lists. This proves the residue interface over
\(E\); it does not assert a full-conjecture result.

Exact sources:

* Ope26a, pinned commit
  1581d4cbdd69a0faf34b2089614fe2a814316a6a,
  preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
  SHA256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3.
  The load-bearing extract is Proposition prop:completed-reflection,
  its cusp construction, equations eq:reflection-local-fourier,
  eq:reflection-multiplier, and eq:reflection-additive-phase.
* Dunn--Radziwill, [v3, Section 5 and Appendix A](https://arxiv.org/html/2109.07463v3):
  (5.6), (5.7), (5.13)--(5.16). Only these unconditional theta formulas
  are imported. None of their GRH-dependent Type I estimates is used.

The notation \(q_x=N(x)\), \(\lambda=\sqrt{-3}\), \(\chi_p\), \(L\),
\(\mathfrak E\), \(c_F\), \(r\), \(c=c_Fr\), \(h_0\), \(\kappa_F\),
\(\sigma_p\), \(\epsilon_p\), \(B_p\), and \(d_H\) is exactly that of the
pinned proposition. All moving primes are prime to \(L\). In particular
\(\chi_p^0\) retains its zero on nonunits. The fixed family and \(L\) are
chosen before the moving primes.

## 1. Exact theorem

Let \(\Psi_0\) belong to the pinned proposition's finite family of
finite-ray characters, extended by zero off the \(\mathfrak E\)-units.
Put
\[
 \Psi(x)=\Psi_0(x)\prod_{p\in\mathcal P}\chi_p(x)^{j_p},
 \qquad 0\le j_p\le5.
\]
Define the spherical completed series
\[
 T_0(s,\Psi)=
 \sum_{n\ {\rm sf},\,b}
 \gamma_2(n)\Psi(nb^3)q_b^{1/2}(q_nq_b^3)^{-s},
 \tag{1.1}
\]
where \(n,b\) are primary and prime to \(\mathfrak E\), without a
coprimality restriction between them. It converges absolutely for
\(\Re s>1\). Both angular factors \(\bar\alpha\) in the pinned
proposition's product have been removed.

Then:

1. \(T_0\) continues meromorphically to \(\mathbb C\), with at most a
   simple pole at \(s=5/6\), and polynomial growth on fixed vertical strips
   away from that pole.
2. Its residue \(\mathcal R(\Psi)\) vanishes if any \(j_p\notin\{0,4\}\).
   When every digit is \(0\) or \(4\), writing
   \(r_4=\prod_{j_p=4}p\), one has
   \[
    |\mathcal R(\Psi)|
       \le C_L q_{r_4}^{-1/6}
            \prod_{p\in\mathcal P}(1-q_p^{-1})
       \le C_Lq_{r_4}^{-1/6}.                         \tag{1.2}
   \]
   The constant depends on the fixed finite data alone.
3. For a test \(V\) as in the pinned proposition, the completed sum is
   \[
   \begin{split}
    &\sum_{n\ {\rm sf},b}
     {\gamma_2(n)\Psi(nb^3)\over\sqrt{q_n}\,q_b}
     V(q_nq_b^3/X)\\
    &\quad=X^{1/3}\widehat V(1/3)\mathcal R(\Psi)
      +\sum_{\rm branches}\zeta_0
       \sum_{\mu\ne0}{d_H(\mu)\vartheta(\lambda^4\mu)\over\sqrt{q_\mu}}
       \prod_{p\ {\rm active}}B_p(\lambda^4\mu)
       V^\flat(q_\mu X/q_c^2).                         \tag{1.3}
   \end{split}
   \]
   The branch sets, \(B_p\), \(d_H\), and fixed sector characters are
   precisely those in the pinned proposition. The scalar is
   \[
    \zeta_0={1\over81}\widehat\phi(h_0)\bar\kappa_F
     \prod_{p\ {\rm inactive}}(1-q_p^{-1})
     \prod_{p\ {\rm active}}\chi_p(\sigma_p)^{-2}\omega_{p,j_p}.
                                                        \tag{1.4}
   \]
   Here
   \[
    V^\flat(x)={1\over2\pi i}\int_{(\sigma)}
       \widehat V(-t)
       {\Gamma(1/3+t)\Gamma(2/3+t)\over
        \Gamma(1/3-t)\Gamma(2/3-t)}
       (Kx)^{-t}\,dt,\qquad
       K={(2\pi)^4\over27},\quad \sigma\ge0.             \tag{1.5}
   \]
   For each fixed \(0<a_0<1/3\), all the pinned proposition's kernel,
   annular Fourier, and finite-seminorm estimates hold with small-argument
   power \(a_0\) in place of \(1/4\). In particular \(a_0=1/4\) is available.

Complex conjugation gives the companion theorem with allowed nonzero
digit \(2\) instead of \(4\), after conjugating the character convention
consistently. A fixed norm twist is handled by inserting \(x^{it}\) in the
test; its finite-seminorm cost is polynomial in \(1+|t|\).

## 2. Fixed finite conductor causes no residue gap

Use the fixed periodic function
\[
 \phi(x)=
 \begin{cases}
  \chi_x(\lambda)^2\Psi_0(x),
       &x\equiv1\pmod3,\ (x,\mathfrak E)=1,\\
  0,&\text{otherwise}.
 \end{cases}
\]
The supplementary law and finite-ray periodicity make it \(L\)-periodic.
The zero branch is evaluated before either character. In particular
\(\phi(0)=0\).

Use its complete finite Fourier expansion, together with the moving
prime expansions, to form the same translated theta sum
\[
 \mathcal F(z,v)=\sum_h C(h)\bar\theta(z+z_h,v),\quad
 C(h)=\widehat\phi(h_0)\prod_p C_{p,j_p}(h_p).
                                                        \tag{2.1}
\]
No unit-Fourier-support condition is imposed on \(h_0\). Thus a finite
character with arbitrarily deep conductor at \(3\), or at any other
fixed prime, is already covered. The pinned construction of the reduced
cusp \(z_h=a/c\) and \(g=GH\) is valid for every such \(h_0\).

Dunn--Radziwill (5.16) gives exactly
\[
 C_H(v)=
 \begin{cases}
  \sigma_\theta v^{2/3},&H=I\quad(F_1),\\
  0,&H\text{ in the other sectors }(F_{19},F_{10}),
 \end{cases}
 \qquad \sigma_\theta={3^{5/2}\over2}.                 \tag{2.2}
\]
There is no second power of \(v\). The pinned cusp construction identifies
the first case with \(3\mid c_F\), independently of all active \(h_p\).

At \(z=0\), the coordinate transformation in the pinned proof gives
\[
 \bar\theta(a/c,v)=
   \bar\kappa(G)\,
   \bar\theta\bigl(H(-\delta'/c,1/(q_cv))\bigr).
                                                        \tag{2.3}
\]
Consequently
\[
 \mathcal F(0,v)=A(\Psi)v^{-2/3}
           +O_\Psi(e^{-c_\Psi/v})\quad(v\longrightarrow0),
 \qquad
 \mathcal F(0,v)=O_\Psi(e^{-c_\Psi v})
                  \quad(v\longrightarrow\infty),       \tag{2.4}
\]
where
\[
 A(\Psi)=\sigma_\theta
   \sum_{\substack{h_0,\ {\rm active\ sets}\\3\mid c_F}}
   \widehat\phi(h_0)\bar\kappa_F q_{c_Fr}^{-2/3}
   \prod_{p\ {\rm inactive}}(1-q_p^{-1})
   \prod_{p\mid r}\left[
       \chi_p(\sigma_p)^{-2}
       \sum_{h_p\ne0}C_{p,j_p}(h_p)\chi_p(h_p)^{-2}
                 \right].                              \tag{2.5}
\]
The large-\(v\) constant vanishes because the total original Fourier
multiplier at zero is zero, as \(\phi(0)=0\).
Logarithmic derivatives satisfy the corresponding exponential estimates.

The moving-prime constant sum is
\[
 \sum_{h\ne0}C_{p,j}(h)\chi_p(h)^{-2}=
 \begin{cases}
  q_p^{1/2}(1-q_p^{-1})\tau_{p,4}^{-},&j=4,\\
  0,&j\ne4.
 \end{cases}                                           \tag{2.6}
\]
For \(j=0\), its active branch is zero by cubic-character orthogonality;
its inactive branch has factor \(1-q_p^{-1}\). For \(j\ne0\), insert
\(C_{p,j}(h)=q_p^{-1/2}\tau_{p,j}^{-}\chi_p(h)^{-j}\)
and sum \(\chi_p(h)^{-j-2}\). The sum is nonzero exactly when \(j=4\).
Multiplication by \(q_r^{-2/3}\) proves the local size
\(q_p^{-1/6}(1-q_p^{-1})\).

Thus exactly one active set can contribute to the residue: all and only
the \(j=4\) primes. The number of surviving terms is at most \(q_L\),
independent of the number or sizes of the moving primes. The fixed
\(q_{c_F}^{-2/3}\), \(\widehat\phi\), and sector phases are uniformly
bounded. This proves the claimed support and size for \(A(\Psi)\).

## 3. Mellin normalization and the reflected identity

Define, initially in \(\Re s>1\),
\[
 J_0(s)=\int_0^\infty\mathcal F(0,v)v^{2s-2}\,dv .
\]
The same coefficient isolation as in the pinned proof, without
differentiation, gives
\[
 J_0(s)={3^{5/2}\over4}
     \left({27\over(2\pi)^2}\right)^s
     \Gamma(s-1/6)\Gamma(s+1/6)T_0(s,\Psi).
                                                        \tag{3.1}
\]
Indeed the Mellin integral of \(vK_{1/3}(4\pi|\mu|v)\) against
\(v^{2s-2}dv\) is
\[
 {1\over4}(2\pi)^{-2s}
   \Gamma(s-1/6)\Gamma(s+1/6)q_\mu^{-s}.
 \]
Equation (2.4), with a smooth subtraction near zero, continues \(J_0\)
with its only possible pole at \(5/6\), of residue \(A(\Psi)/2\).
Reciprocal gamma factors are entire. Hence \(T_0\) has no other poles,
and
\[
 \mathcal R(\Psi)=
 {2(2\pi)^{5/3}\over3^5\Gamma(2/3)}A(\Psi).              \tag{3.2}
\]
This proves (1.2), including the assertion about every possible pole.

On \(\Re s<0\), change \(v\) to \(1/(q_cu)\) in each translated term,
remove its explicit constant, and integrate the nonconstant cusp
expansion. The result is
\[
 {1\over4}(2\pi)^{2s-2}q_c^{1-2s}\bar\kappa(G)
 \Gamma(5/6-s)\Gamma(7/6-s)
 \sum_{\mu\ne0}d_H(\mu)\check e(-\delta'\mu/c)
                          q_\mu^{s-1}.                \tag{3.3}
\]
This statement concerns the finite weighted sum of all translated terms.
The pure-power integrals are regularized only via the preceding
subtraction: splitting at \(1\) gives opposite rational terms that
cancel. The total nonconstant dual expansion is integrable at zero
on this half-plane, and its termwise Mellin series converges absolutely
there by the pinned coefficient bound.

The quotient of (3.3) and (3.1), with \(t=1/2-s\), has gamma quotient
(1.5) and scalar \(1/81\). The finite arithmetic calculation is unchanged,
since neither the local masks nor the cusp multipliers depend on the
archimedean derivative. It yields (1.4) and the pinned \(B_p\).
Shifting the original Mellin contour across its single pole gives (1.3).

The transformed gamma quotient has its nearest negative numerator pole
at \(t=-1/3\). Stirling gives polynomial vertical growth on
\(-a_0\le\Re t\le A\) for every \(a_0<1/3\); the denominator reciprocal
gamma functions are entire. Moving the kernel contour to \(-a_0,0,A\),
and repeating the pinned integration-by-parts argument, proves the
finite-seminorm bounds. A pole-subtracted Phragmen--Lindelof argument
gives polynomial strip growth of \(T_0\), justifying the Mellin shift.

## 4. Exact selected-prime action on the residue

Let \(p\) be a good prime absent from the moving local set. Inserting
\(1_{p\nmid nb^3}\) adds a digit \(j_p=0\).
By (2.6), only its inactive branch survives in \(A(\Psi)\). The pinned
simultaneous branch convention says that this branch has the identical
\(c_F,r,H,\kappa_F\), kernel and fixed data, multiplied solely by
\(1-q_p^{-1}\). Therefore, as exact complex identities,
\[
 \mathcal R(\Psi\,1_{p\nmid nb^3})
       =(1-q_p^{-1})\mathcal R(\Psi),\qquad
 \mathcal R(\Psi\,1_{p\mid nb^3})
       =q_p^{-1}\mathcal R(\Psi).                       \tag{4.1}
\]
If \(p\) already belongs to a zero-extension modulus, the second residue
is zero. These identities retain complex phases and fixed conductor.

For distinct selected primes, (4.1) iterates. Hence a fixed number of
disjoint selected lists in dyadic prime annuli, with bounded coefficient
functions \(b_i\), multiply the residue by
\[
 \prod_i\ \sum_{\substack{p\in\mathcal P_i\\
                         p\text{ not forbidden}}}
                        {b_i(p)\over q_p}.             \tag{4.2}
\]
Each factor is \(O(1)\) by ideal counting. An exact priority restriction
only removes summands and preserves this absolute bound.

This is the full-index selection law. The squarefree-index law
\(1/(q_p+1)\) in RESONANT_RESIDUE_MEAN.md is compatible with it:
cube completion contributes \(1-q_p^{-2}\) to the complementary
coprimality weight.

## 5. Consequence for reflected inverse states

For a row \(k\), squarefree amplifier label \(f\), and fixed finite
twist \(\xi\), the moving digit in the source induction is
\[
 j_p(k,f)=v_p(k)+4v_p(f)\pmod6.
\]
The fixed finite character \(\xi\) is absorbed into \(\Psi_0\).
The source's puncture \(\rho(n)=1_{(n,\mathfrak r_\rho)=1}\) is
different: its prime support may move and is kept among the moving
local primes, with digit zero at primes not already in \(kf\).
At an overlap the existing digit and its natural zero are retained.
Hence (1.2) is uniform in this puncture; it is never put into \(L\).
Equations (1.2), (1.3), and (4.1) prove the four conditions of the
residue interface in RESIDUE_INDUCTION_INTERFACE.md over \(E\):

* The sole extra term is \(X^{1/3}\widehat V(1/3)\mathcal R\).
* Its squared row weight has only digits \(\{0,4\}\), bounded by
  \(\prod_{j_p=4}q_p^{-1/3}\); its conjugate has only \(\{0,2\}\).
* Each full-index selected prime contributes \(1/q_p\).
* After separating that term, the coefficient family, finite phase
  algebra, fixed profile control, and kernel power \(1/4\) are those
  required by the source argument.

Allowing the union \(\{0,2,4\}\) gives the convenient row bound
\[
 \sum_{q_k\le H}|\mathcal R(k,f;\xi,\rho)|^2
       \ll_{\epsilon,L}H^{1/3+\epsilon}q_f^\epsilon.
                                                        \tag{5.1}
\]
The \(\{0,4\}\) orientation has the sharper exponent
\(H^{1/6+\epsilon}\) proved in the interface file.

At a reflected terminal state with \(F=N+V\) and
\(F-M-Q\ge c>0\), normalized residue energy is
\[
 \mathcal E_{\rm res}\ll
   Z^{(2N+M)/3+\epsilon}
   \le Z^{F-c/3+\epsilon}.                             \tag{5.2}
\]
Selected margins are stronger, and (4.2) adds no scale power.
The cube-completion coefficient \(1/q_h\) times the residue at length
\(Z^N/q_h^3\) is \(Z^{N/3}/q_h^2\), an absolutely summable weight.
Primes assigned to the cube variable in the exact priority partition
have weight at most \(q_p^{-2}\); their annular sums are also bounded.
The residue estimate therefore applies before or after selected cube
completion.

This authenticates the previously conditional terminal residue insertion
over \(E\), uniformly through the fixed finite twist orbit. Promoting
it to a unitary zero-free theorem also requires the complete angular
inverse induction and initial comparison to be checked with this
insertion; this file does not silently import that global closure.
