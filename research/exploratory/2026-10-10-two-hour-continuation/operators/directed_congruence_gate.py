"""Exact dyadic congruence proposal followed by full directed Gershgorin gate."""
from fractions import Fraction as Q
from flint import arb, arb_mat, ctx
from enclose_analytic_upper import require, cholesky, identity

def exact(x):return Q(str(x.fmpq()))
def gate(A,shift):
    require(ctx.prec>=256,'reviewed congruence precision at least256bits')
    n=A.nrows();require(n==A.ncols() and n>0,'square congruence input')
    for i in range(n):
        for j in range(n):
            require(A[i,j].is_finite() and
                    exact(A[i,j].lower())==exact(A[j,i].lower()) and
                    exact(A[i,j].upper())==exact(A[j,i].upper()),'finite symmetric interval input')
    # This centered Cholesky is only a proposal generator. Its inverse is
    # replaced by exact dyadic points; no inverse identity is an acceptance premise.
    center=arb_mat([[arb(A[i,j].mid().fmpq()) for j in range(n)] for i in range(n)])
    proposal=cholesky(center-shift*identity(n)).transpose().inv()
    P=arb_mat([[arb(proposal[i,j].mid().fmpq()) for j in range(n)] for i in range(n)])
    for i in range(n):
        for j in range(n):require(P[i,j].is_exact(),'literal exact dyadic preconditioner entry')
    C=P.transpose()*(A-shift*identity(n))*P
    margins=[]
    for i in range(n):
        margin=exact(C[i,i].lower())
        for j in range(n):
            if j!=i:margin-=max(abs(exact(C[i,j].lower())),abs(exact(C[i,j].upper())))
        require(margin>0,('full directed congruence Gershgorin row',i,str(margin)))
        margins.append(margin)
    return {'status':'FULL_DIRECTED_DYADIC_CONGRUENCE_GERSHGORIN_PASS',
      'exact_dyadic_preconditioner':[[str(exact(P[i,j])) for j in range(n)] for i in range(n)],
      'shifted_congruence_matrix_balls':[[C[i,j].str(65,more=True) for j in range(n)] for i in range(n)],
      'exact_positive_row_margins':[str(x) for x in margins],
      'minimum_row_margin_exact':str(min(margins)),
      'proposal_is_an_acceptance_identity':False,'all_input_interval_errors_retained':True}
