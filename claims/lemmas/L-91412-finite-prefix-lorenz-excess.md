# L-91412 — The Lorenz row gap has a finite-prefix lower bound

Status: **PROVED EXACT REDUCTION**. RH remains unproved.

Use the notation of `L-91411`, and put `q_c=q(c)`. Since `U(D)=O(D)`,
\[
R_{sig}-R(nu)
=\int(q-q_c)\,dU-
 \int(q-q_c)\,dO.
\]
The cutoff satisfies `c>y`, and `L-91410` makes `q` nonincreasing for every source beyond `c`. Therefore
\[
q(d)-q_c\le0\qquad(d>c).
\]
Splitting the odd measure at `c` gives the exact identity
\[
\boxed{
R_{sig}-R(nu)
=G_{pre}+
 \int_{d>c}[q_c-q(d)]\,dO(d),
}
\]
where
\[
\boxed{
G_{pre}=
\int(q-q_c)\,dU-
\int_{d\le c}(q-q_c)\,dO.
}
\]
The tail term is nonnegative. Hence `G_pre>=0` is sufficient for the complete row gate.

On the live branch `c<2000`. Thus every row ratio occurring in `G_pre` is attached to a `P_61` divisor below `2000`: 185 positive-parity nodes including `1`, and 198 negative-parity nodes. The unbounded source tail enters only through the scalar amount fixing the fractional cutoff; it contributes no adverse row term.

This gives a second closure route, smaller than checking the full determinant over the whole active divisor set.
