# Simultaneously excluding small finite-order twists

**Status.** This is a source-qualified consequence of [the common moving-twist density theorem](../2026-10-29-moving-unitary-twist-density/README.md), the fixed-field finite ray class count and its stated Hecke/FHL/Θₙ inputs. It is a polynomial-height density-one statement, not an individual all-height zero-free region. The recent sieve source and detector constants have not been externally verified here.

Fix K, n and FHL data as in the moving-twist theorem. Fix σ and a κ satisfying that theorem's strict range, and let R be its displayed density exponent. For every ε>0 there is one τ>0 such that all but

    O_{K,S,n,σ,κ,ε}(X^(R+2κ+ε))                              (1)

good n-free indices u of norm at most X have the following **simultaneous** property: for every finite-order Hecke character ν of K with primitive conductor norm `Nf_ν≤X^κ`, the primitive inducing L-function of νχ_u has no zeros in

    Re(s)≥σ,   |Im(s)|≤X^τ.                                   (2)

Here τ is uniform over every such ν. It is not necessary for ν to be coprime to u or to the FHL bad set. The possible pure-norm inducing character is principal because ν and χ_u are finite-order; its pole at s=1 is not a zero. The moving theorem treats its zeros by a uniform individual bound and retains all finite deleted Euler factors, which introduce no zeros in Re s>0.

## Proof and quantifiers

For a finite conductor ideal f, all primitive finite-order characters of exact conductor f factor through the corresponding narrow ray class group. Its size is `≪_K Nf`, up to the fixed class number and the fixed number of archimedean sign choices. There are `O_K(Q)` integral ideals with norm at most Q. Therefore

    #{finite-order primitive Hecke characters ν : Nf_ν≤Q}
       ≪_K Q²                                                (3)

(up to an innocuous Q^ε if desired). Finite-order characters have archimedean parameters in a fixed finite set; in the fields containing μ_n with n≥3 there are no real places. The moving theorem is uniform over this entire character set with **one** τ, not one τ chosen separately for each ν. Apply its zero-count bound to every ν in (3), then take a union bound over ν: any label violating (2) contributes at least one counted primitive zero for at least one twist. With Q=X^κ this gives (1). Choose the detector loss, ideal-count loss and global τ after κ and the desired ε, and absorb the finite principal-row zero count. If R+2κ<1, the ≫X squarefree good labels imply that the simultaneous property holds for a density-one subfamily.

## Examples

For n=4 and σ=4/5, the moving theorem has `R=35/52` and permits every fixed `κ<2/13`. Taking κ=1/10 gives

    R+2κ=35/52+1/5=227/260<1.                               (4)

Thus, for example over K=Q(i), all but `O(X^(227/260+ε))` good fourth-free labels of norm ≤X have property (2) simultaneously for every finite-order Hecke twist of conductor norm ≤X^(1/10). In particular this is a density-one statement among a family containing ≫X distinct characters. It says nothing about zeros above the stated polynomial height.

For n=3 and `σ=θ=4369347/5000000`, the high-cutoff theorem has

    R=6306530/11891959,   κ_high=608041/11891959>1/20.

Taking κ=1/20 gives `R+2κ=74957259/118919590≈0.630319<1`. This consequence is itself a density statement at σ=θ; it does not require the tracker candidate, since no fixed base-field factor is introduced. Applying it to finite extensions or to arbitrary angular twists would require additional arguments and is not asserted.

## Simultaneous quadratic twists

The same argument improves the character-count cost from `2κ` to `κ` when ν is restricted to order dividing 2. There are only `O_K(Q)` quadratic Hecke characters of conductor norm ≤Q. Indeed, away from primes over 2, a ramified quadratic local character has conductor exponent one, so its good conductor is a squarefree ideal a of norm ≤Q. At primes over 2 there are only finitely many local quadratic characters because `K_v^×/(K_v^×)²` is finite; the infinite sign data are also finite. For each a, two global quadratic characters with the same permitted local ramification differ by a character unramified outside that fixed finite set; class-field theory gives only finitely many such quadratic characters, with a bound depending on K. Summing over `O_K(Q)` squarefree ideals proves the claimed count.

Consequently the exceptional-label exponent in (1) improves to `R+κ+ε` for simultaneous **quadratic** twists, with the same one uniform τ and the same possible principal-row treatment. In particular, for n=4, σ=4/5 and κ=1/10, the exponent is

    35/52+1/10 = 201/260 < 1.                                (5)

Thus all but `O(X^(201/260+ε))` good fourth-free indices have the claimed polynomial-height zero-free rectangle simultaneously for every quadratic twist of conductor norm ≤X^(1/10). No assertion of all-height nonvanishing is made.

**Independent review.** High_match checked the ray-class Q² union bound, the uniform-height and pole quantifiers, the numerical examples, and the sharper quadratic O_K(Q) count via unique odd-prime quadratic inertia and the finite fixed 2-ramified subgroup. The moving-twist and source assumptions remain inputs.

[The expanded conductor-range calculation](../2026-10-29-moving-unitary-twist-density/EXPANDED-KAPPA.md) retains the endpoint face for larger κ and optimizes a fixed ordinary moment order. At n=3 and θ it yields, subject to the same source uniformity, density-one simultaneous nonvanishing for all finite-order twists when any fixed `κ<4346735/18783918≈.231407`, and for all quadratic twists when any fixed `κ<3108041/6891959≈.450966`. These thresholds concern one-per-X common-twist estimates followed by the indicated finite union; they are not all-height claims.
