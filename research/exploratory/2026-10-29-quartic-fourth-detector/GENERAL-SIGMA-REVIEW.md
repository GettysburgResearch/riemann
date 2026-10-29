# Independent check of the general-σ powered witness

This is a scalar and coefficient audit, conditional on the general-order rectangular-sieve replay and the buffered detector with common-profile and height controls. It does not prove those inputs, establish optimality, or give an individual zero-free region.

Fix an integer n≥5 and 1/2+2/n<σ<1, put δ=2σ−1, and define

    D=n(3−δ)+4,  L=2n/D,  U=3n/D,
    c=4/D,        a=[n(1+δ)−4]/[(n−2)D],
    R=1−δL.

Then 1<U<3/2, 1/n<c<1/2, 0<a<1/2 and c=1/n+(1−2/n)a. In particular, the two prime boxes with exponents a and 1−a have positive widths and distinct scales. The source-qualified squared-moment exponent is E(x)=max{1,c+x,1−c+2x/n}. Because δ>4/n>2/n, the first and third faces of f(x)=E(x)−δx decrease and the second increases. Direct calculation gives

    1−δL = 1−c+(2/n−δ)L = c+(1−δ)U = R.

Consequently f≤R on [L,U]. With detector cutoff t=U, any inverse witness with r≥L is counted by f(r); otherwise m≥U−r>L/2 and m≤1/2 give 2m∈[L,1]⊂[L,U], so the ordinary fourth-moment witness is counted by f(2m). This uses the actual m interval, not m=t−r. Fixed O(η) overflows are absorbed after choosing η in terms of the strict margin and the final ε; the permitted height power may shrink accordingly. These calculations establish an upper bound within the named source replays, not a global minimax.

At σ=4/5, the same scalar exponent can instead be obtained with any fixed short cutoff t∈(L,1) by finitely many higher ordinary moments. For U=3L/2, the intervals [L/p,U/p], p≥2, cover (0,U/2] because U/(p+1)≥L/p exactly when p≥2. Since the low-r branch has m>t−L, a finite number of powers suffice. Choosing t=(1+L)/2 bounds p by 15n/(n+10)<15, so powers 2 through 14 suffice uniformly for all n≥7. This short-cutoff argument reproduces the same exponent as the fourth-moment long cutoff; it is not an additional numerical improvement.

For each fixed p, multiplication of a common ordinary Dirichlet polynomial p times produces coefficients bounded by the p-fold ideal divisor function, hence by X^ε after adjusting ε. In the decomposition q=q₁v² with q₁ squarefree, the q₁-vector has squared ℓ² mass ≪X^ε/(Nv)². For each fixed v the factor χ_g(v²) is retained as a row contraction until its L² norm is taken; Minkowski and the harmonic ideal sum cost X^ε. The Markov exponent is E(pm)−δpm. The common-profile reduction must cover the finite list of powers and their differentiated profiles, with constants allowed to depend on p; this is part of the analytic replay and is not implied by a bound for one undifferentiated profile.

For K=Q(ζ_p), the powered-family bridge and all-place conductor identity transfer the result to cyclic p-degree relative zeta quotients, after a finite union over the nontrivial powers. Illustrations are p=7, σ=9/10, a=43/485, R=41/97 and discriminant exponent 41/582; and p=5, σ=19/20, a=11/87, R=11/29 and discriminant exponent 11/116. Prime-pair boxes give ≫X/(log X)² fields, and the common polynomial height requires the same small-conductor dyadic split as the field notes. All bounds remain conditional on the named analytic inputs.
