# Director adjudication: finite screw-line computation and a remote-quartet obstruction

17 November 2026. I read the full proponent analysis effective_cluster62_suzuki_finite_certificates.md and the independent suzuki_model63_review.md and independently checked the cancellation, contour identity and dominated tail arguments. This supplements the earlier corrected-source and Landau adjudications. The spectral counterexample is a symmetric polynomial model, not an arithmetic zeta function.

For the author-corrected Suzuki line, the prime-side formula is unconditionally evaluable at fixed time. On the real spectral axis A=ξ(1/2−ix) is real and ξ' is imaginary. Therefore the quotients A/E# and ξ'/E# have modulus at most1; their apparent common zeros are removable even at a multiple real root. Multiplying before evaluating the logarithmic derivative cancels its dangerous denominator. The remaining finite prime sum and digamma/Lerch differences give, on any fixed time window,

    |S_t(x)|≤B_T[1+log(2+|x|)]/(1+|x|),  |t|≤T.

The constants are effectively obtainable from the displayed elementary series. This gives a full norm-tail bound of order log²R/R and a route to interval quadrature without a lower bound for ζ on the critical line. Real-axis continuation and integration across possible common roots use the bounded canceled formulas, not raw division of overlapping balls. The compact-time modulus extends through zero after retaining the Lerch cancellation. Ψ itself has logarithmic behavior at zero and is not Lipschitz there.

Unconditional positivity of the norm Gram and the arithmetic screw kernel are different facts. Their global identification uses the RH model-space premise. The finite computations do not supply that premise or the all-tail deficit of the separately proved Landau criterion.

The obstruction can track both sides, not merely the zero sum. Choose a fixed even real-rooted polynomial A0 with no root at zero, and put E0=A0+iA0'. The real-root finite model has exactly matching norm and screw kernels with the journal π normalization; the independent proof evaluates the rational kernel integral by upper-half-plane residues. Now multiply A0 by

    Q_B(z)=((z−B)²+a²)((z+B)²+a²),  a>0,

adding four unit-multiplicity off-axis roots. On real x the logarithmic derivative of Q_B is uniformly bounded and tends to zero locally. The phase ratio1/(1−iA'/A) has a Lipschitz difference bounded by that derivative times the old bounded ratio. Each new resolvent has L² norm sqrt(π/a), and its coefficient is O_(T,a)(1/B) on |t|≤T. The independent estimates give convergence of the phase line in L² and its finite Gram/norm data at O_(T,a)(1/B), while the zero-kernel change is O_(T,a)(1/B²). The real-axis squared tails have an O(1/R) bound uniform in B on fixed time windows. Thus arbitrarily accurate bounded-window comparisons can coexist with a remote off-axis quartet in this model class.

At explicit later times2πj/B the perturbed screw diagonal eventually becomes negative, and its deficit grows beyond every exp(ωt) with ω<a. This agrees with the Landau obstruction. A generic rank-one perturbation in the orthogonal complement of a finite compression similarly leaves all compressed matrix entries unchanged. Neither construction preserves the arithmetic Euler product or explicit formula. They locate the additional arithmetic/tail information a finite certificate must use; they do not refute any actual-zeta theorem.
