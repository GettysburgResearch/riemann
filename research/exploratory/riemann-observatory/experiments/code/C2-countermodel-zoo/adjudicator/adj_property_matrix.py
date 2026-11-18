#!/usr/bin/env python3
"""ADJUDICATOR (C2-countermodel-zoo): write the adjudicated property matrix.

Input : experiments/results/C2-countermodel-zoo/property_matrix.csv (investigator; left unchanged).
Output: experiments/results/C2-countermodel-zoo/adjudicator/property_matrix_adjudicated.csv
Changes (each traced to FINAL.md):
  * cell corrections for M0, M1, M2, M2b, M3, M4, M5d, M8, M9 (skeptic findings F2-F7 as adjudicated);
  * new row M10 = zeta(s)(1 + c 2^{-s} + 2 4^{-s}) (skeptic F1, adjudicated THEOREM);
  * repair of two malformed investigator rows (M5c, M7: unquoted commas in the member name);
  * new column lacks_vs_zeta: which of the predicates P1..P11 (defined in FINAL.md sect. 4) the member violates.
Tags: [T] theorem/proof in FINAL or REPORT; [I] imported; [NR] numerical-rigorous; [NN] numerical-nonrigorous;
      [H] heuristic; [C] conditional; [ADJ] changed by the adjudicator.
Usage: python3 adj_property_matrix.py RESULTS_DIR
"""
import sys, os, csv, hashlib

FIX = {
    ('M0', 'li_coefficients'): "lambda_n>0 <=> RH [I Li 1997]; Johansson 2014 lambda_1e5=462580.78241 [I]; adjudicator replay 462580.78242 with the S(T*) boundary term (462581.69 without it) [NN, ADJ]",
    ('M0', 'jensen_turan'): "Turan ineq. all m [I CNV 1986]; J^{d,n} hyperbolic for n>=N(d), each d [I GORZ 2019]; d,n<=40 and J^{d,0} d<=240 hyperbolic (rounded polys) [NN]",
    ('M1', 'jensen_turan'): "Turan certified k<=78 [NR]; all J^{d,n}, d+n<=79, d,n<=40, hyperbolic (50-digit rounded polys) [NN; not independently replayed]",
    ('M1', 'known_offline_zeros'): "exactly 5 (plus reflections) with |t|<=300, first 0.80851718245663738555+85.69934848537759217193i [NR; completeness NR by argument principle, two implementations, ADJ]; none for |t|<=85.6 [NR]; infinitely many in sigma>1 [I DH 1936]; none for sigma>=1.13514 [T, computer-assisted]; N_0(T)>>T(log T)^{1/2-eps} on line [I Karatsuba 1990]",
    ('M2', 'known_offline_zeros'): "exactly 35 (plus reflections) with |t|<=200, first 0.93296969748541410476+15.66824953127847236i [NR; completeness NR, ADJ]; sigma>1 zeros certified at t=1193.9464 (sigma=1.011049), 4108.1083 (1.015071) [NR, 2 independent methods, ADJ], 148065.85, 272795.96, 506416.50, 939506.18 [NR, skeptic], 3587891.15, 4125904.91, 5000977.10 [NR]; lowest sigma>1 zero for t<=4200 is t=1193.95 [NN screen]; none for sigma>=1.17816 [T]; infinitely many in sigma>1 [I DH 1936]; positive proportion on line [I Rezvyakova 2024]",
    ('M2b', 'known_offline_zeros'): "real zero 0.654651202577622799100319554(093..488) and mirror [NR]; for rectangular forms x^2+k^2y^2: real zero in (1/2,1) for every k>k*=7.0555079554481827625 (exact Chowla-Selberg + IVT) [T, ADJ]; BST Conjecture 1.1 (threshold exactly 4pi e^{-gamma}) is FALSE: Delta*-e^gamma/(4pi)=5.95e-21 [T + NN, ADJ]",
    ('M3', 'jensen_turan'): "Turan inequalities b_m(t)^2>((2m-1)/(2m+1))b_{m-1}(t)b_{m+1}(t) for ALL m>=1 and ALL real t [T given I Csordas-Varga 1988 log-concavity of Phi(sqrt v) (L0+) and the moment lemma proved in FINAL, ADJ]; checked m<=40 at t=-1,-20,-100 [NN]",
    ('M4', 'li_coefficients'): "lambda_n(xi~)=lambda_n(xi)+4-term sum [T]; first negative n: (0.6,14)->20855, (0.75,14)->7477, (0.6,30)->112538, (0.75,30)->40908 [NN; two independent codes, ADJ; investigator's 20857/7395/112929/41098 withdrawn]",
    ('M4', 'jensen_turan'): "Turan certified k<=78 [NR]; J^{d,0} hyperbolic d<=240 for (0.6,5),(0.75,10),(0.9,14) [NN]; first non-hyperbolic J^{d,0} at d=40 for (0.9,5) [NN, replayed]; 'J^{d,n} hyperbolic for all d once n>=n0' is CONDITIONAL on zeta having finitely many off-line zeros [C, ADJ]; unconditional for the H_{0.2}-based analogue [T given I CCS 1987, Platt-Trudgian 2021]",
    ('M5c', 'known_offline_zeros'): "BDR Thm 1.1: for every alpha in [0,1) and beta in [1/2,1) an [alpha,beta]-system exists (psi=x+O(x^{alpha+eps}), N=ax+O(x^{beta+eps}), both sharp); zeros with Re>1/2 exist iff alpha>1/2; Thm 1.3 (CONDITIONAL on RH for zeta): RH-false systems with beta<1/2 for 1/2<alpha<2/3, 2alpha/(alpha+2)<=beta<1/2 [I BDR 2023, L1; ADJ wording]",
    ('M5d', 'euler_product'): "continuous Beurling 'Euler product': zeta=exp(int x^{-s} dPi), dPi>=0 (no discrete primes) [T]",
    ('M8', 'known_offline_zeros'): "nontrivial real zeros s in (1/2,1) with s(1-s)=lambda_j<1/4 (besides the zero s=1 from lambda_0=0 and topological trivial zeros); surfaces with arbitrarily small lambda_1 exist [I Randol 1974]",
    ('M9', 'known_offline_zeros'): "RH analogue concerns POLES of Z(u), u=q^{-s}: adjacency eigenvalue lambda=q^s+q^{1-s}; poles with 0<Re s<1 all on Re s=1/2 <=> Ramanujan graph [I Ihara 1966; Stark-Terras 1996; Terras 2011]",
}

LACKS = {
    'M0': 'reference (has P1-P11)',
    'M1': 'P2,P3,P4,P5,P6,P8,P10',
    'M2': 'P2,P3,P4,P5,P8 (degree 2; a_1=2 unless normalised)',
    'M2b': 'P2,P3,P4,P5,P8',
    'M3': 'P1-P6,P8,P10,P11 (not a Dirichlet series)',
    'M4': 'P1-P6,P10,P11 (not a Dirichlet series)',
    'M5a': 'P1 (g-integers not N),P7,P8,P9',
    'M5b': 'P1,P7,P8,P9',
    'M5c': 'P1,P7,P8,P9',
    'M5d': 'P1,P7,P8,P9 (infinite order)',
    'M6': 'P2,P3,P4,P5,P7,P8,P10',
    'M7': 'P2,P3,P4,P5,P7,P8',
    'M8': 'P1,P2,P6,P8,P9 (order 2),P11',
    'M9': 'P1,P2,P6,P8,P9,P11',
    'M10': 'P4,P5,P8 (conductor 4)',
}

M10 = {
    'member': 'M10 zeta(s)(1+c2^{-s}+2*4^{-s}), c>2sqrt2 (e.g. c=3; c=2^{3/4}+2^{1/4}) [ADJ, skeptic F1]',
    'dirichlet_series_multiplicative': 'yes: a_n = 1 + c[2|n] + 2[4|n], multiplicative, 0<=a_n<=1+c+2 [T]',
    'euler_product': 'yes over rational primes; factor at 2 is (1+a2^{-s})(1+b2^{-s})/(1-2^{-s}), ab=2, a+b=c; local roots -a,-b with |alpha|>1 [T]',
    'functional_equation': 'pi^{-s/2}Gamma(s/2)zeta(s)(2^s+c+2^{1-s}) symmetric under s->1-s; degree 1, conductor 4 [T]',
    'order_genus': '(s-1)F entire of order 1 [T]',
    'hadamard_product': 'yes [T]',
    'explicit_formula': 'yes, but Lambda_F(2^k)<0 for even k (c=3: Lambda_F(4)=-4log2); log-coefficients b(2^k)~a^k/k violate the Selberg bound b(n)<<n^theta, theta<1/2 [T]',
    'coefficient_positivity': 'a_n>=0 [T]',
    'ramanujan_bound': 'a_n bounded [T]; local roots violate |alpha_p|<=1 [T]',
    'almost_periodicity': 'yes in sigma>1 [T]',
    'weil_positivity': 'fails (off-line zeros) [T]',
    'li_coefficients': 'some lambda_n<0 [T via Bombieri-Lagarias 1999 multiset theorem]',
    'jensen_turan': 'not computed',
    'known_offline_zeros': 'all s with 2^{-s}=-1/a or -1/b: Re s=log2(a), 1-log2(a), Im s=(2k+1)pi/log2 (c=3: Re s=0,1; c=2^{3/4}+2^{1/4}: Re s=1/4,3/4, first at 4.5324i) [T, exact]; RH-true for 0<c<=2sqrt2 iff RH [T]',
}


def main():
    rd = sys.argv[1]
    src = os.path.join(rd, 'property_matrix.csv')
    raw = list(csv.reader(open(src, newline='')))
    header = raw[0]
    rows = []
    for r in raw[1:]:
        # the investigator's CSV has two malformed rows (M5c, M7): unquoted commas in the member name shift
        # the columns; repair by re-joining the leading fields until the row has len(header) fields
        while len(r) > len(header):
            r = [r[0] + ',' + r[1]] + r[2:]
        rows.append(dict(zip(header, r)))
    fields = header + ['lacks_vs_zeta']
    out = []
    for r in rows:
        key = r['member'].split()[0]
        for (k, col), val in FIX.items():
            if k == key:
                r[col] = val
        r['lacks_vs_zeta'] = LACKS.get(key, '')
        out.append(r)
    m10 = dict(M10); m10['lacks_vs_zeta'] = LACKS['M10']
    out.append(m10)
    od = os.path.join(rd, 'adjudicator'); os.makedirs(od, exist_ok=True)
    fn = os.path.join(od, 'property_matrix_adjudicated.csv')
    with open(fn, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(out)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn, len(out), 'rows')


if __name__ == '__main__':
    main()
