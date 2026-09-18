from rh_gram_followup import *
N=1024
W=w_table(N);G=gram(N,W)
C=Certificate();out=Path(__file__).resolve().parent/'results';out.mkdir(exist_ok=True)
for n in [256,512,1024]:
    t=time.monotonic();ix=np.arange(2,n+1);v=np.log(ix)/ix
    with threadpool_limits(limits=2):c=cho_solve(cho_factor(G[:n-1,:n-1],lower=True),v)
    den=10**15;z=[int(round(float(x)*den)) for x in c]
    cert=C.run(z,den);cert['seconds']=time.monotonic()-t
    (out/f'certificate_N{n}.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(n,cert['proved_D_less_than'],cert['exact_optimal_E_interval'],cert['seconds'],flush=True)
