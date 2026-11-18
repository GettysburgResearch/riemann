# An automatic heat barrier from a verified physical height

**Proposed theorem.** There is an absolute \(H_*\) such that if all zeta zeros through height \(H\ge H_*\) satisfy RH, then
\[
                       \Lambda\le \frac{2.541}{\log H}.
\]
This implication needs no separate numerical verification at positive heat time. The threshold \(H_*\) is unevaluated, so the theorem does not give a new numerical upper bound from the currently published height. Polymath15, §10, suggested a logarithmic-height implication while setting aside the third, lateral-barrier hypothesis of their Theorem 1.2. Here the barrier follows from actual-zeta increment moments and zero density. The [reverse estimate](nov18b-heat-drift.md) gives a lower bound of the same logarithmic order if a zero with fixed positive defect exists. [Polymath15, Theorems 1.2 and 1.5, §10](https://arxiv.org/abs/1904.12438)

## Small heat time at a retained physical ordinate

Use the [local density proof](nov18b-heat-local-density.md), with \(L=\log X\), \(F=L^{1/4}\), \(h_0=F/L\). If \(T\) satisfies its source conditions (1), then for some fixed \(c>0\)
\[
 F_u(1/2+y+iv)\ne0\quad
 (|v-T|\le c h_0,\ h_0\le y\le1/2,\ 0\le u\le F/L^2).
                                                               \tag{1}
\]
At \(u=0\) this follows directly from the depth exclusion. For \(u>0\) let \(h=uL\le h_0\), \(Y=y+h\). This scale satisfies \(Y\ge h_0\). The complex logarithmic derivative bound (2) of the local density proof applies when the real displacement is at least \(d_0Y\) in a fixed height neighborhood of size \(Y\). Thus the full Gaussian integral has its saddle at \(s_*=s+2u(\log\xi)'(s_*)\), within \(C\varepsilon h\) of \(s+h\). Its relative error on the local segment \(h+[-Y/4,Y/4]\) is \(O(\varepsilon h/Y)+O(e^{-c_1Y^2/u})\) by exactly the Taylor bound there. The local segment can include negative Gaussian coordinates because the full integral is used. In particular \(Y^2/u\ge h_0^2/(F/L^2)=F\).

For completeness, the log cost in replacing the positive real anchor by the complex saddle is \(O(\varepsilon^2 hL)\). Outside the segment, on the positive side of the physical axis the Gaussian penalty \((q-h)^2/(4u)\) dominates the linear error \(\varepsilon L|q-h|\) since \(|q-h|\ge Y/4\ge h/4\). Inside the central core of width \(2d_0 Y\) the reflected-factor estimate (3) of the local density proof loses \(O(d_0YL)\), whereas \((q-h)^2/u\gg Y^2/u\ge YL\). On the negative side beyond the core the reflected Gaussian loses at least \(yL-O(\varepsilon yL+\varepsilon^2hL)\), with \(y\ge h_0\ge h\) and \(yL\ge F\). The fixed-strip outer tails have the same quadratic domination as before. These estimates prove (1) for small fixed \(d_0,\varepsilon\). They are uniform down to \(u=0\).

## Selecting the whole slab

Take \(X=H/2\). Choose the left endpoint \(T_b\) in \([X,3X/2]\). Impose the retained-center conditions on \(T_b+j c' h_0\) for all integers \(0\le j\le \lceil 1/(c' h_0)\rceil\). Here \(c'\) is smaller than both the constant in (1) and the neighborhood constant in the local density theorem. With normalized measure on this interval, the union of the failure sets has measure \(O_A(h_0^{-1}F^{-A})=o(1)\), for example with \(A=8\). All shifted points lie in the dyadic range for large \(H\). A suitable \(T_b\) therefore exists. On the entire slab \(T_b\le v\le T_b+1\), (1) excludes physical displacement \(y\ge h_0\) at the early times. From \(u=F/L^2\) through \(u=1/8\) the [local heat theorem](nov18b-heat-local-density.md) excludes every strictly positive displacement there. No choice of the center depends on \(u\).

## Applying the published criterion

In Polymath coordinates take \(X_b=2T_b\) and \(t_0=2.541/\log H\). We have \(H\le X_b\) and \(X_b/2\le H\). For every sufficiently small \(y_0>0\), condition (i) of Polymath15, Theorem 1.2, follows from the physical height hypothesis, and condition (ii) follows from [uniform high reality](nov18b-heat-forward.md) at \(t_0\) for every \(x\ge X_b\).

For condition (iii) the required horizontal interval has width \(\sqrt{1-y_0^2}\le1\), inside the selected slab after scaling. For \(4F/L^2\le t\le t_0\) every strictly positive displacement is excluded there. For \(0\le t\le4F/L^2\) the required lower edge \(\sqrt{y_0^2+2(t_0-t)}\) in Polymath's imaginary coordinate is greater than \(2h_0\) for large \(H\), since it is \(\gg L^{-1/2}\) and \(h_0=L^{-3/4}\). Formula (1), with \(u=t/4\), therefore covers the rest of the required slab. The theorem gives \(\Lambda\le t_0+y_0^2/2\). Letting \(y_0\downarrow0\) proves the assertion.
