"""Full finite Gibbs sums for exploratory theta-moment searches.

This module does not certify a root, a Lee--Yang theorem, or RH.
All numerical evaluation is ordinary binary64, not directed rounding.
"""
from __future__ import annotations
from itertools import product, combinations, combinations_with_replacement
import math
import numpy as np
from scipy.special import gammaln, logsumexp, roots_hermitenorm

class MomentModel:
    def __init__(self, groups: list[int], recurrence: list[float], *, gaussian: bool,
                 hidden: int = 0, pair_edges: bool = True, retain_dummy_pairs: bool = False):
        if not groups or any(type(n) is not int or n < 1 for n in groups):
            raise ValueError('groups must be positive integer multiplicities')
        if math.prod(n + 1 for n in groups) > 200_000:
            raise ValueError('state cap exceeded; choose a smaller graph')
        if hidden < 0 or hidden and any(n != 1 for n in groups):
            raise ValueError('hidden-spin implementation requires singleton visible groups')
        self.groups = np.asarray(groups, dtype=int)
        self.g = len(groups)
        self.gaussian, self.hidden = gaussian, hidden
        self.a = np.asarray(recurrence, dtype=float)
        if len(self.a) < 21 or np.any(self.a[1:21] <= 0):
            raise ValueError('positive recurrence coefficients through degree 20 required')
        self.M = np.asarray(list(product(*[range(-n,n+1,2) for n in groups])),dtype=float)
        self.logbase = sum(gammaln(n+1)-gammaln((self.M[:,i]+n)/2+1)
                           -gammaln((n-self.M[:,i])/2+1) for i,n in enumerate(groups))
        if pair_edges:
            if all(n == 1 for n in groups):
                self.pairs = list(combinations(range(self.g),2))
            else:
                self.pairs = [(i,j) for i,j in combinations_with_replacement(range(self.g),2)
                              if i != j or groups[i]>1 or retain_dummy_pairs]
        else:
            self.pairs = []
        self.V = np.column_stack([(self.M[:,i]**2-groups[i])/2 if i==j
                                  else self.M[:,i]*self.M[:,j] for i,j in self.pairs]) \
                 if self.pairs else np.empty((len(self.M),0))
        if gaussian:
            self.gn,self.gw=roots_hermitenorm(11); self.gw/=math.sqrt(2*math.pi)
        else:
            self.gn,self.gw=np.asarray([0.]),np.asarray([1.])
        self.count=self.g+int(gaussian)+len(self.pairs)+self.g*hidden
        self._cache=None

    def _law(self,z: np.ndarray):
        z=np.asarray(z,dtype=float)
        if z.shape != (self.count,) or not np.all(np.isfinite(z)):
            raise ValueError('wrong parameter count or nonfinite parameter')
        off=self.g+int(self.gaussian)
        lw=self.logbase+self.V@z[off:off+len(self.pairs)]
        scores=self.V
        if self.hidden:
            W=z[off+len(self.pairs):].reshape(self.hidden,self.g)
            fields=self.M@W.T
            lw=lw+np.logaddexp(fields,-fields).sum(axis=1)
            scores=np.c_[scores,np.concatenate([self.M*np.tanh(fields[:,h])[:,None]
                                                for h in range(self.hidden)],axis=1)]
        pr=np.exp(lw-logsumexp(lw))
        sd=z[self.g] if self.gaussian else 0.
        y=(self.M@z[:self.g])[None,:]+sd*self.gn[:,None]
        return z,pr,scores,y

    def evaluate(self,z: np.ndarray) -> tuple[np.ndarray,np.ndarray]:
        z=np.asarray(z,dtype=float)
        if self._cache is not None and np.array_equal(z,self._cache[0]):
            return self._cache[1].copy(),self._cache[2].copy()
        z,pr,scores,y=self._law(z)
        p0=np.ones_like(y); p1=y/self.a[1]
        d0=np.zeros_like(y); d1=np.ones_like(y)/self.a[1]
        ps=[];ds=[];gs=[]
        for k in range(1,20):
            p2=(y*p1-self.a[k]*p0)/self.a[k+1]
            d2=(p1+y*d1-self.a[k]*d0)/self.a[k+1]
            if (k+1)%2==0:
                ps.append(self.gw@p2);ds.append(self.gw@d2)
                if self.gaussian: gs.append((self.gw*self.gn)@d2)
            p0,p1=p1,p2;d0,d1=d1,d2
        P,D=np.asarray(ps),np.asarray(ds);f=P@pr
        components=[(D*pr)@self.M]
        if self.gaussian: components.append((np.asarray(gs)@pr)[:,None])
        components.append((P*pr)@scores-f[:,None]*(pr@scores)[None,:])
        jac=np.concatenate(components,axis=1)
        self._cache=(z.copy(),f.copy(),jac.copy())
        return f,jac

    def raw_moments(self,z: np.ndarray) -> np.ndarray:
        _,pr,_,y=self._law(z)
        return np.asarray([(self.gw@(y**r))@pr for r in range(21)])

    def admissibility(self,z: np.ndarray) -> dict:
        z=np.asarray(z,dtype=float);off=self.g+int(self.gaussian)
        weights_ok=bool(np.all(z[:self.g]>=0))
        gaussian_ok=bool(not self.gaussian or z[self.g]>=0)
        coupling_ok=bool(np.all(z[off:]>=0))
        return {'nonnegative_observable_weights':weights_ok,
                'nonnegative_gaussian_standard_deviation':gaussian_ok,
                'ferromagnetic_couplings':coupling_ok,
                'minimum_coupling':float(z[off:].min()) if len(z)>off else None,
                'passes_parameter_sign_conditions':weights_ok and gaussian_ok and coupling_ok,
                'root_certified':False,'source_intervals_used':False}
