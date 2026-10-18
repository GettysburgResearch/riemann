# Two complete actual diagonal strips cost only row size

**PROPOSED source-qualified exact centering.** This removes complete
signed portions of the actual mixed mean at every primitive conductor.
It proves no bound for the remaining both-different covariance.

Use the original corner D=U, N=sqrt(U), all good sixth-power-free physical
rows, one nonnegative bounded annular row weight w, and the actual common
character, orientation, finite twist, height and smooth profiles. Write

    M_u=sum_d a_d psi_u(d),    S_u=sum_n b_n psi_u(n),
    a_d=D^(-1/2)mu(d)nu(d)W_M(Nd/D),
    b_n=N^(-1/2)nu(n)W_S(Nn/N).                         (1)

Here `psi_u(a)=chi_a(u)^varsigma`; the common fixed finite twist nu is
already in a_d,b_n and is not inserted into psi_u a second time.

All original nonunit zeros and fixed exclusions remain. The profile
seminorms and the compact real-part range give

    sum_d |a_d|^2 << 1,       sum_n |b_n|^2 << 1,        (2)

with fixed profile constants. The pinned source's amplified inverse
second moment at r=1, e(1)=1, and the complete plain second moment at
N=sqrt(U) give

    sum_u w_u |M_u|^2 + sum_u w_u |S_u|^2
          << U^(1+epsilon)(1+T)^A.                     (3)

These are the same actual source inputs identified in
`TRANSPOSED_GAUSS_MODE.md`; no new arbitrary-coefficient inverse
estimate is assumed.

Expand the COMPLETE mixed mean

    E=sum_u w_u |M_u S_u|^2.

Let E_D be the entire strip d1=d2, without restricting n1,n2. Then
exactly

    E_D=sum_u w_u |S_u|^2
                  sum_d |a_d|^2 |psi_u(d)|^2.

The original zero extensions satisfy |psi_u(d)|<=1. Equations (2)--(3)
therefore give `0<=E_D<<U^(1+epsilon)(1+T)^A`. Similarly the entire
strip n1=n2 obeys `0<=E_N<<U^(1+epsilon)(1+T)^A`. Their common strip is

    E_DN=sum_u w_u
       [sum_d |a_d|^2|psi_u(d)|^2]
       [sum_n |b_n|^2|psi_u(n)|^2],

which is nonnegative and O(U) by (2) and the row count. These bounds
retain every n power, every shared input prime and every physical row.
They do not remove a zero mask before opening an oscillatory sector.

Let C_diff be the full signed form with BOTH d1!=d2 and n1!=n2. Exact
inclusion-exclusion gives

    E=E_D+E_N-E_DN+C_diff,
    E=C_diff+O(U^(1+epsilon)(1+T)^A).                    (4)

The sum C_diff is real by conjugate pairing; it need not be nonnegative.
This genuinely pays parts of the large-conductor form: for example,
the complete n1=n2 strip can contain primitive conductors of norm up
to order D^2=U^2. The estimate concerns the whole strip, not its
arbitrarily projected conductor pieces.

One can separately partition C_diff by its EXACT primitive conductor
C, using exponent differences modulo six for A_i=d_i n_i, retaining
the original zero-only mask at every shared prime. The absolute
small-conductor proof in `ACTUAL_SIXTHFREE_SECTOR.md` remains valid
after this additional fixed pair restriction, since its pair-count
majorant took absolute values. Consequently for 1<=Q<=U^2,

    |C_diff,NC<=Q|
       << (U+U^(1/6)Q^(11/12))U^epsilon(1+T)^A.         (5)

For Q=U^(9/8), the second exponent is 115/96, strictly less than
6/5 by 1/480. Thus a sufficient remaining corner estimate is the
upper bound

    C_diff,NC>U^(9/8) << U^(6/5+epsilon)(1+T)^A,         (6)

with the complete physical windows and all shared-prime corrections.
An absolute bound would also suffice but is not required by (4).
Equation (6) is OPEN. The previous small-conductor theorem alone does
not prove it, and the artificial positive completion in
`POSITIVE_COMPLETION_BARRIER.md` cannot replace this signed form.
Other witness lengths still require their full consumer optimization;
this corner statement by itself is not a new zeta boundary.
