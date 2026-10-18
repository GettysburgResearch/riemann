"""Exact whole-cell exponent verification, conditional on an OPEN mixed row-size mean."""
from fractions import Fraction as F
from pathlib import Path
import json

def require(v, msg):
    if not v: raise ArithmeticError(msg)

def main():
    ell=F(3,16);x=y=(1-ell)/2;h=1-x+ell
    B=F(167,192)+F(1,10000);z0=F(17,50)
    delta0=F(1,50);deltamax=F(3,4)
    low=F(11,12)-ell/4
    # Every nonfloor witness has r+m>=3/2. The OPEN row-size mean
    # gives R<=max(0,1-3delta/2). No corner extrapolation is used.
    # delta+R is piecewise affine and maximized at one of these vertices.
    vertices=[delta0,F(2,3),deltamax]
    def Rp(d):return max(F(0),1-F(3,2)*d)
    worst_delta_plus_R=max(d+Rp(d) for d in vertices)
    common=F(1,6)-ell/2-B
    central_upper=common+h*worst_delta_plus_R
    a0=(1+delta0)/2
    floor=a0-B-a0*y-ell/2+(delta0/2)*ell+h*(1+a0-F(2,3))
    # At frequency drow=0, monotonicity in a and amplitude gives this bound.
    zero_endpoint=h*(F(7,8)+z0-F(1,6))-B-ell
    small=h*(z0-F(1,6))-y/2+F(63,50)*F(1,100)
    supply=ell/h-F(7,37)
    lowmargin=B-low
    require(ell<=F(1,5),'aggregate low range')
    require(x>ell and x-ell>=0,'Gram and rescaling lengths')
    require(min(central_upper,floor,zero_endpoint,small)<0,'strict gaps exist')
    require(all(v<0 for v in [central_upper,floor,zero_endpoint,small]),'all retained upper bounds negative')
    require(supply>0 and lowmargin>0,'supply and principal comparison')
    # The corrected whole-domain envelope for the weaker candidate input
    # U+D^(2/3)N is included as a regression against the invalid middle-bin
    # corner extrapolation. Linear maxima occur at polygon vertices.
    cells=[(F(1),F(1,2)),(F(3,2),F(0)),(F(3,2),F(1,2))]
    envelope_checks=0
    for k in range(151):
        d=F(k,200)
        direct=max(max(F(1),F(2,3)*r+m)-d*(r+m) for r,m in cells)
        formula=max(F(3,2)-2*d,F(7,6)-F(3,2)*d)
        require(direct==formula,'full-cell candidate envelope')
        envelope_checks+=1
    require(max(F(3,2)-2*F(1,4),F(7,6)-F(3,2)*F(1,4))==1,'middle-bin regression')
    # Check the aggregate tuple inequality at every rational breakpoint and
    # a large deterministic mesh; its analytic proof is piecewise linear.
    tuple_checks=0
    for k in range(201):
        e=F(k,1000)
        for j in range(101):
            d=e*F(j,100)
            lhs=-d+max(F(0),5*e-1+d)/8
            rhs=max(F(0),5*e-1)/8
            require(lhs<=rhs,'aggregate tuple inequality')
            tuple_checks+=1
    data={'status':'PASS','conditional_open_mixed_input':'sum |M(D)S(N)|^2 << U(UDN)^epsilon',
          'B':str(B),'B_decimal':float(B),'ell':str(ell),'x':str(x),'y':str(y),'h':str(h),
          'delta_domain':['1/50','3/4'],'amplitude_ratio_domain':['0','1/2'],
          'nonfloor_frequency_h_upper':str(central_upper),'floor_frequency_h_upper':str(floor),
          'frequency_zero_upper':str(zero_endpoint),'small_row_upper_dmin_1_100':str(small),
          'supply_margin':str(supply),'low_signal_margin':str(lowmargin),
          'whole_cell_candidate_envelope_checks':envelope_checks,'aggregate_tuple_checks':tuple_checks,
          'correction':'U+D^(2/3)N gives max(3/2-2delta,7/6-3delta/2); it does not give the second branch alone.',
          'scope':'Exact algebra only. The arithmetic mixed row-size estimate remains unproved.'}
    Path(__file__).with_name('MIXED_CONSUMER_CHECKS.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':main()
