# A primitive finite-character model for two Poisson steps

**Status.** An elementary finite Fourier calculation, not a spectral theorem for the physical unit-gcd/unit-projector block. It isolates what follows from Fourier involution alone and why the source's Möbius/Gauss phases cannot be assumed to force a sign. The physical recursion has changing moduli, smooth profiles, gcd and zero masks, so its operator is not identified with the finite operator below.

Let p≡1 mod 6 be prime and let χ be a primitive sextic character of F_p×, extended by zero at 0. On ℂ^(F_p) use the unitary Fourier transform

    (Ff)(y)=p^(−1/2) Σ_(x mod p) f(x)e^(2πixy/p).

For the normalized character vectors e_χ=χ/√(p−1) and e_barχ=barχ/√(p−1), the Gauss identity gives

    F e_χ = τ(χ)/√p · e_barχ,
    F e_barχ = τ(barχ)/√p · e_χ,
    τ(χ)τ(barχ)/p=χ(−1)∈{−1,1}.                            (1)

Thus F²f(x)=f(−x); on this two-dimensional character subspace F²=χ(−1)I and F is unitary. If χ(−1)=1 its eigenvalues are ±1; if χ(−1)=−1 they are ±i. Both cases have modulus one. Thus even a negative eigenvalue of a double transform is a sign, not a norm contraction.

For the opened-square analogue, let P_χ and P_barχ be the orthogonal rank-one projectors onto these two vectors, and let C(X)=F X F*. The unit Gauss phases cancel in a projector, so

    C(P_χ)=P_barχ,      C(P_barχ)=P_χ,
    C(P_χ+P_barχ)=P_χ+P_barχ,
    C(P_χ−P_barχ)=−(P_χ−P_barχ).                              (2)

The first combination is positive semidefinite and is a nonzero +1 eigenvector; the second is a −1 eigenvector but is indefinite. Both are fixed by C². In particular, the finite conjugation operator has no strict Hilbert–Schmidt contraction and contains both signs. Multiplying e_χ by a unit scalar, including a single Gauss-root or Möbius sign, leaves its projector unchanged and cannot remove the +1 example. Multiplication by an arbitrary nonconstant phase on the full vector space gives a different unitary operator; its spectrum requires a separate calculation, although unitarity still precludes a uniform norm contraction.

The source's arithmetic µ/γ identity is more elaborate than such a single scalar: it couples varying conductors, finite-ray phases, smoothing and masks. Equation (2) therefore proves neither that the physical unit-gcd block has a +1 eigencomponent nor that it lacks useful signed cancellation. It does show that bare finite Fourier involution, or an untracked unit Gauss phase, is insufficient to justify the contraction or negative sign that would close the same-scale inverse loop. A physical claim would need the exact common-scale operator, its domains and masks, and a proof of the relevant spectral projection or signed quadratic form.

**Independent review.** Families checked the primitive Gauss identities, parity and projector eigenvectors, retaining the distinction between this finite toy and the physical operator.
