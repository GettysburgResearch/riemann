# Low-height Artin regions from odd abelian Frobenius kernels

**Status:** Proposed elementary transfer from published Hecke and low-order results, awaiting independent mathematical review and literature comparison. No claim about Riemann's zeta function or global priority is made.

**Inputs:** Ahn–Kwon's [order-at-least-three Hecke zero-free region](https://doi.org/10.1016/j.jnt.2014.06.008) and the order-at-least-five coefficient `0.1149` quoted in [Zaman 2016, equation (1.1)](https://arxiv.org/html/1502.05679); [Das–Gaba–Lee–Savalia–Wong, Theorem 1.2](https://arxiv.org/html/2506.19319); Ahn–Kwon's low-height Dedekind zeta result; Stark's low-order theorem; Frobenius character theory, class field theory, full Artin induction and the conductor–discriminant formula. None of those source theorems is reproved here. The proof generalizes the [elementary-abelian Frobenius construction](../2026-10-29-frobenius-transfer/README.md).

## Theorem

Let `K/k` be a finite Galois extension of number fields with group `G`. Suppose `G` contains a subgroup

    H=N semidirect C_r,

where `N` is a nontrivial finite abelian group of odd order `n`, `r>=3`, and **every nonidentity** element of the cyclic complement acts without a nonzero fixed point on `N`. Let `E=exp(N)`, `F=K^(H^2)`, and `D=|disc(K/Q)|`. Assume `[F:Q]>=7`.

For

    Re(s)>1 - n phi(E)/[15.10 E log D],
    |Im(s)| < (1/3) tan(pi/8),                              (1)

all irreducible Artin L-functions of degree at least two and all nonreal one-dimensional Artin L-functions are holomorphic and nonzero. Across the real one-dimensional factors there can be at most one simple real zero. At `s=1` every nontrivial irreducible factor is holomorphic and nonzero, while the trivial factor has the usual zeta pole.

If `3` does not divide `E`, every nontrivial character of `N` has order at least five. In that case the same conclusions hold in the stronger-width region

    Re(s)>1 - 0.1149 n phi(E)/[E log D],   |Im(s)|<=0.13.  (2)

If `k=Q` and `G` has no quotient of order two, the only real one-dimensional character is trivial. Since the widths above are below `1/2` and the Riemann zeta function has no zero in `Re(s)>1/2`, `0<|Im(s)|<=1` by the cited [Platt–Trudgian verification](https://doi.org/10.1112/blms.12460), while its real-axis sign excludes real zeros in `(0,1)`, `zeta_K` itself is zero-free in the respective region apart from its pole at `1`.

## Proof

The fixed-point-free condition on each complement element implies the same condition on the dual group `N-hat`: for an element `c!=1`, the map `c-1` on finite `N` is injective and hence surjective, so its dual has no nonzero fixed character. Thus every nontrivial character `lambda` of `N` has an orbit of length `r`. Frobenius character theory, or the induced-character inner product and the dimension sum, gives exactly the irreducibles

- the `r` linear characters inflated from `H/N`, and
- `(|N|-1)/r` characters `Ind_N^H lambda`, one per nontrivial dual orbit, each of degree `r`.

Because `N` has odd order, every element of `N` is a square in `N`, so `N` is contained in `H^2`. Its image in `H/N=C_r` is the subgroup of squares; writing `g=gcd(2,r)`, we have

    H^2=N semidirect (C_r)^2,    |H^2|=n r/g.

Put `M=K^H` and `E0=K^N`. By the regular-representation factorization and Artin induction, the **full** quotient, including ramified local factors, is

    zeta_K/zeta_F = product_(omega in (H/N)^, ord(omega)>2) L_M(s,omega)
                    * product_([lambda] in (N-hat-{1})/C_r) L_E0(s,lambda)^r.  (3)

The removed linear characters of order at most two are exactly those factoring through `H/H^2`; this is the zeta factorization for `F/M`. All displayed factors are primitive Hecke L-functions of nonreal finite-order characters.

Let `lambda` have order `t|E`. Its kernel has cardinality `n/t`; the field `L=K^(ker lambda)` is cyclic of degree `t` over `E0`, and `[K:L]=n/t`. Let `Q_lambda` denote the norm of its finite primitive Hecke conductor over `E0`. Its `phi(t)` faithful powers have exactly the same conductor, while all other conductor norms are at least one. Thus

    d_L >= d_E0^t Q_lambda^phi(t)
        >= (d_E0 Q_lambda)^phi(t),
    D >= d_L^(n/t),
    log(d_E0 Q_lambda) <= [t/(n phi(t))] log D.             (4)

As `t|E`, `phi(t)/t >= phi(E)/E`, so Ahn–Kwon's `1/15.10` zero-free region for every nonreal `lambda` contains (1). If `3` does not divide `E`, every such `t` is at least five and the quoted `0.1149` region contains (2).

For the complement factors in (3), `E0/M` is cyclic of degree `r`. The faithful powers of a generator's character have the same conductor, and all other powers have conductor dividing it. The same conductor argument with `D>=d_E0^n` bounds every complement conductor parameter by `D^(1/[n phi(r)])`. Since `phi(r)>=2`, the generic Ahn–Kwon coefficient for those factors is at least `2n/15.10`, which exceeds both `n phi(E)/(15.10 E)` and `0.1149 n phi(E)/E` (using `phi(E)<=E` and `2/15.10>0.1149`). Thus all factors in (3) are holomorphic and nonzero in the applicable region.

The tower relation gives `d_F^(nr/g)<=D`, so the degree-at-least-seven Das low-order width is at least `nr/[g*11.51910 log D]`. Since `r/g>=2`, this is larger than both claimed widths. The only possible zero of `zeta_F` there is real and simple: simplicity follows from the separate Ahn–Kwon `1/(2 log d_F)` theorem. From (3), `ord zeta_K=ord zeta_F` away from one. Stark's theorem makes all irreducible Artin factors holomorphic, and the regular-character factorization then excludes zeros of degree at least two. A nonreal one-dimensional zero at the exceptional real point would occur also in the distinct conjugate factor, contradicting the simple order. This leaves at most one simple real one-dimensional exception; Brauer–Hecke nonvanishing handles the nontrivial factors at `s=1`.

For the optional `k=Q` zeta statement, choose a character of `N` of order `E`, which exists for any finite abelian group. From (4), `D >= A^(n phi(E)/E)` with `A=d_E0 Q_lambda>=2`. Therefore each claimed width is at most its coefficient (`1/15.10` or `0.1149`) divided by `log 2`, hence strictly below `1/2`. If `G` has no quotient `C2`, only the trivial real one-dimensional factor remains; the cited low-height zeta verification and the real-axis sign exclude its zeros. This completes the deduction.

## Explicit odd abelian example

Take `N=C7 x C13`, so `n=E=91` and `phi(E)=72`. For `r=3`, let a generator act by multiplication by `2 mod 7` and `3 mod 13`; each has order three, and neither nontrivial power is 1 in either component. For `r=6`, multiplication by `3 mod 7` and `4 mod 13` has order six in each component, so all five nonidentity powers are fixed-point-free. Both actions define Frobenius groups as in the theorem. In either case (2) gives the explicit coefficient

    0.1149 * 72 = 8.2728

in front of `1/log D`, at `|Im(s)|<=0.13`, for every extension satisfying the stated fixed-field degree condition. For `r=3` and `G=H`, every nontrivial irreducible is covered because `H` has odd order: its nontrivial one-dimensional characters are nonreal, and the remaining irreducibles have degree three. For `r=6`, a real one-dimensional factor may remain.

The example is not vacuous. The group `H` is solvable, so Shafarevich's solvable inverse-Galois theorem realizes it over `Q`; a precise reference for the corrected theorem is [Neukirch–Schmidt–Wingberg, Chapter IX, as cited in this survey](https://www.math.bas.bg/serdica/2011/2011-173-210.pdf). Choose a cyclic degree-seven field `k/Q` not contained in that fixed `H`-extension `L/Q` (there are infinitely many such fields and only finitely many subfields of `L`). Because `[k:Q]=7` and `L/Q` is Galois, `k` and `L` are linearly disjoint. Then `K=kL` is `H`-Galois over `k`, and `K^(H^2)` contains `k`, so the stipulated degree condition holds. This existence argument is separate from the analytic result; it does not furnish a small discriminant or a computation of any L-value.

**Review targets:** Verify full ramified induction, the source theorems' hypotheses and the fixed-point-free action, independently check the numeric example, and search for stronger prior results. No priority or optimality claim is made.
