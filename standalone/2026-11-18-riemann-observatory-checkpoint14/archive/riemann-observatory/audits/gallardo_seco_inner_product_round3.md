# Forensic reconstruction of the displayed Riesz-basis inner product

Date:2026-11-17. Contributor:equivalences. **Independent review pending.** This note traces the already independently verified endpoint obstruction to a specific calculation in the inspected proof. It must not inherit adjudication of the endpoint counterexample automatically. No new main-theorem failure or novelty claim is made.

Actual sources: PAPER-E012, journalPDFpp22–24, especiallyEq26p24; preprintv6pp18–19. The journal definitions andEq26 were visually inspected. Private images `gallardo_seco_journal_p22.png` and `gallardo_seco_journal_p24.png` preserve those passages.

The proof defines, for k>=−1,

t_k=(k+1)(k+2)^(alpha/2),

d_k=(k+1)^p/p, p=a−alpha+1/2,

g_k=t_k^−1[z^(k+1)−d_k^−1 sum_(n0..k)(d_n−d_(n−1))z^n].

Here d_(−1)=0, alpha in[−3,−2),a>0, so p>0 and all expressions are well-defined at the needed positive indices. The leading monomial and telescoping lower coefficients giveg_k(1)=0, henceT_ag_k is a polynomial of degreek.

## Exact coefficients before asymptotics

Putc=alpha−1/2 and

q_n=(a+n+1)d_n−(n+1)d_(n+1).

Direct differentiation and cumulative summation give

[z^n]T_ag_k=q_n/(t_kd_k),0<=n<k,

[z^k]T_ag_k=(k+1+a)/t_k.

The derivative atdegree n uses(d_(n+1)−d_n), not(d_n−d_(n−1)). The printed proof has the latter indices in an intermediate displayed expression. This shift does not change the leading asymptotic below, so it alone does not account for the constant discrepancy.

Fori>j, the exact inner product is therefore

<T_ag_i,T_ag_j>_(D_alpha)
 =[sum_(n0..j−1)q_n²(n+1)^alpha]/(t_id_it_jd_j)
  +q_j(j+1+a)(j+1)^alpha/(t_id_it_j).                       (IP1)

All quantities are real for these parameters; no conjugation convention changes this formula. The endpoint n=j is isolated because it is the leading coefficient ofg_j's image but a lower coefficient ofg_i's image.

## Leading constant, with a valid joint limit

The elementary fixed-parameter expansions are

q_n=(c/p)n^p+O(n^(p−1)),

t_k=k^(1+alpha/2)(1+O(1/k)),

d_k=k^p/p(1+O(1/k)).

Because2p+alpha+1=2a−alpha+2>0, the power sum in(IP1) has leading term

(c²/p²)j^(2p+alpha+1)/(2p+alpha+1).

Consequently, for example alongi=2j,j→infinity,

<T_ag_i,T_ag_j>_(D_alpha)
 =[c+c²/(2p+alpha+1)+o(1)]
    j^(p+alpha/2) i^(−p−1−alpha/2)

 =[(alpha−1/2)(2a+3/2)/(2a−alpha+2)+o(1)]
    j^(a+(1−alpha)/2) i^(−a+(alpha−3)/2).                   (IP2)

The source'sEq26 instead displays the same powers with constant

(alpha−1/2)(a+1)/(a−alpha+3/2).                             (printed)

At the already tested endpointalpha−3,a1, (IP2) is−7/4, whereas the printed value is−14/11. More explicitly,

lim_(j→infinity) (2j)^4/j³ *<T_1g_(2j),T_1g_j>_(D_−3)
 =−7/4,

not−14/11. The difference is a fixed nonzero constant, so it is not absorbed by the displayed1+o(1). The replacementsj+1,i+1 byj,i likewise do not alter the limit.

## Why this fits the endpoint obstruction

Atalpha−3,a1 the corrected leading kernel is−(7/4)j³/i⁴ fori>j. Its absolute symmetric Schur estimate with weightsi^−1/2 has limiting off-diagonal constant

2*(7/4)/(3+1/2)=1,

so this leading kernel supplies no strict diagonal-dominance margin. This is consistent with the exact approximate-null sequence. It is a diagnostic of the proof method, not a separate proof of the full spectral behavior of theGram matrix.

The actual source formula for its boundC1 uses the smaller constant fromEq26. Replacing only the non-strict parameter inequality at the theorem statement does not correct that calculation. The independent weighted-Hardy proof avoids the disputed Riesz-basis estimates altogether. A reviewer should check(IP1),(IP2) directly against the source definitions before this forensic finding is classified as verified.
