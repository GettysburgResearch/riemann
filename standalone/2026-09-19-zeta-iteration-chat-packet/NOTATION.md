# Notation and normalization

All logarithms are natural. zeta^{circ n} means composition; zeta(s)^n means
an ordinary power. Neither is repeated integration of S(t).

Write a nontrivial zero as rho=beta+i*gamma=1/2+delta+i*gamma, and count zeros
with their multiplicities m_rho. xi(s)=s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)/2.
The symbol ell(s)=xi'(s)/xi(s) is used here for the logarithmic derivative,
to avoid confusing it with the limiting approximation error L.

    dmu(t)=dt/[2*pi*(1/4+t^2)]       (a probability measure)
    D=integral log|zeta(1/2+it)| dmu(t)
    I(T)=integral_{-T}^T log|zeta(1/2+it)|/(1/4+t^2) dt.

D has the factor 1/(2*pi); I(T) does not.

The Hilbert space is complex, with inner product LINEAR IN THE FIRST ARGUMENT:

    <f,g> = sum_{k>=1} f(k) conjugate(g(k)) / [k(k+1)].

The constant sequence 1 has norm 1. b_n(k)={k/n}, n>=2; b_1=0 by convention.
B_N=span(b_2,...,b_N), B=closure union B_N, P_N and P their projections.

    A_N=P_N 1, e_N=1-A_N, E_N=||e_N||^2, L=lim E_N;
    G_N(m,n)=<b_m,b_n>, v_n=log(n)/n;
    c_N=G_N^{-1}v, E_N=1-v^T G_N^{-1}v.

Real coefficients suffice for this real target and real Gram matrix; use
Hermitian transposes for arbitrary complex coefficients. Matrices indexed
2,...,N have dimension N-1, not N.

The transform and evaluation kernel are

    T f(s)=sum f(k)[k^{-s}-(k+1)^{-s}], Re s>1/2;
    h_z(k)=k(k+1)[k^{-conj(z)}-(k+1)^{-conj(z)}];
    <f,h_z>=T f(z).

T f(s)=s integral_1^infinity f(floor(x))x^{-s-1}dx. Consequently the ordinary
Mellin transform of the step function is T f(s)/s. This factor must not be lost.

For the PRESCRIBED, not optimized, mollifier:

    c^log_{N,n}=-mu(n)(1-log n/log N), 2<=n<=N;
    U_N=sum c^log_{N,n} b_n, u_N=1-U_N, Q_N=||u_N||^2;
    Lambda_N(m)=sum_{d|m,d<=N}mu(d)log(N/d);
    T_N^scalar=sum_{d<=N}mu(d)log(N/d)/d;
    Psi_N(k)=sum_{m<=k}Lambda_N(m), tau_N=T_N^scalar/log N.

psi(k)=sum_{m<=k}Lambda(m) is Chebyshev's prime-power function.
psi_Gamma denotes the digamma function; they are unrelated objects.

Ramanujan coordinates:

    s_d=sum_{n|d}mu(d/n)n b_n;
    lambda_d=<1,s_d>=Lambda(d);
    K_N(d,e)=<s_d,s_e>.

Periodic averaging is denoted M_per; it is NOT the Hilbert inner product.
J_2(d)=d^2 product_{p|d}(1-p^{-2}); phi(d) is Euler's totient.

Vasyunin duals and the latest packet:

    U_r^div(k)=1_{k|r}mu(r/k), d_r(k)=k(k+1)[U_r^div(k)-U_r^div(k+1)];
    F_N(r,s)=<d_r,d_s>, V_N^dual=span(d_2,...,d_N);
    a_N=H_{N+1}-1, z_N=N+1-H_{N+1};
    t_{N,n}=sum_{k<=N}b_n(k)/(k+1);
    T_N^tail(m,n)=sum_{k>N}b_m(k)b_n(k)/[k(k+1)];
    R_N^Gram=G_N-F_N^{-1}=t_Nt_N^T/z_N+T_N^tail.

The scalar finite mollifier discrepancy R_N^arith from Chapter 05 is NOT
R_N^Gram. The scalar best-linear-fit variance V_N^psi from Chapter 07 is NOT
the dual subspace V_N^dual. F in the numerical optimization certificate denotes
a candidate's squared error and is NOT the matrix F_N.

These collisions occurred as the chat evolved. The archived notebooks retain
their original notation; the chapter context and this dictionary govern reading.
