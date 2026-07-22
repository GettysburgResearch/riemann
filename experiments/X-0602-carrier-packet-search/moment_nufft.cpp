#include <quadmath.h>
#include <vector>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <algorithm>
#include <fstream>
#include <string>
#include <limits>

using ld = long double;
using cd = std::complex<ld>;
static __float128 qpi(){ return acosq((__float128)-1); }

static void fft_plus(std::vector<cd>& a){
    const size_t n=a.size();
    for(size_t i=1,j=0;i<n;i++){
        size_t bit=n>>1;
        for(; j&bit; bit>>=1) j^=bit;
        j^=bit;
        if(i<j) std::swap(a[i],a[j]);
    }
    const ld pi=acosl(-1.0L);
    for(size_t len=2;len<=n;len<<=1){
        ld ang=2*pi/(ld)len;
        cd wlen(cosl(ang),sinl(ang));
        for(size_t i=0;i<n;i+=len){
            cd w(1,0);
            for(size_t j=0;j<len/2;j++){
                cd u=a[i+j], v=a[i+j+len/2]*w;
                a[i+j]=u+v; a[i+j+len/2]=u-v; w*=wlen;
            }
        }
    }
}

static bool is_power_two(uint64_t x){return x && !(x&(x-1));}

int main(int argc,char**argv){
    if(argc<7){
        std::fprintf(stderr,"usage: %s c n_center K M R output.json\n",argv[0]); return 2;
    }
    uint64_t C=strtoull(argv[1],nullptr,10);
    uint64_t n0=strtoull(argv[2],nullptr,10);
    int K=atoi(argv[3]); uint64_t M=strtoull(argv[4],nullptr,10); int R=atoi(argv[5]);
    std::string outpath=argv[6];
    if(!is_power_two(M) || K<0 || (uint64_t)K>=M/2 || R<0){
        std::fprintf(stderr,"invalid K/M/R\n"); return 2;
    }
    std::vector<uint8_t> isp(C+1,1); isp[0]=isp[1]=0;
    for(uint64_t p=2;p*p<=C;p++) if(isp[p]) for(uint64_t k=p*p;k<=C;k+=p) isp[k]=0;
    std::vector<uint32_t> primes; primes.reserve((size_t)(C/std::log((ld)C)*1.1));
    for(uint64_t p=2;p<=C;p++) if(isp[p]) primes.push_back((uint32_t)p);

    std::vector<std::vector<cd>> AS(R+1,std::vector<cd>(M));
    std::vector<std::vector<cd>> AD(R+1,std::vector<cd>(M));
    __float128 piq=qpi(), twoq=2*piq, Lq=logq((__float128)C);
    ld L=(ld)Lq;
    ld sumAbsS=0, sumAbsD=0;
    uint64_t ppcount=0;

    for(uint32_t p:primes){
        __float128 lpq=logq((__float128)p); uint64_t q=p;
        while(q<=C){
            ++ppcount;
            __float128 yq=logq((__float128)q);
            __float128 thetaq=twoq*yq/Lq;
            __float128 reduced=fmodq(thetaq,twoq); if(reduced<0) reduced+=twoq;
            __float128 gridq=reduced*(__float128)M/twoq;
            long long jj=llroundq(gridq); uint64_t j=(uint64_t)((jj%(long long)M+(long long)M)%(long long)M);
            __float128 phiq=twoq*(__float128)j/(__float128)M;
            __float128 deltaq=remainderq(reduced-phiq,twoq);
            ld delta=(ld)deltaq;
            __float128 baseq=remainderq(thetaq*(__float128)n0,twoq);
            ld base=(ld)baseq;
            cd z(cosl(base),sinl(base));
            ld w=(ld)(lpq/sqrtq((__float128)q));
            ld alpha=1-(ld)yq/L;
            ld wd=2*w*alpha;
            sumAbsS += fabsl(w); sumAbsD += fabsl(wd);
            ld powd=1;
            for(int r=0;r<=R;r++){
                AS[r][j] += z*(w*powd);
                AD[r][j] += z*(wd*powd);
                powd*=delta;
            }
            if (q > C / p) {
                break;
            }
            q *= p;
        }
    }

    for(int r=0;r<=R;r++){ fft_plus(AS[r]); fft_plus(AD[r]); }
    std::vector<ld> fact(R+1,1); for(int r=1;r<=R;r++) fact[r]=fact[r-1]*(ld)r;
    const int count=2*K+1;
    std::vector<ld> PS(count),PD(count);
    for(int kk=-K;kk<=K;kk++){
        uint64_t idx=(uint64_t)((kk%(int)M+(int)M)%(int)M);
        cd cs(0,0),cdv(0,0), ikpow(1,0), ik(0,(ld)kk);
        for(int r=0;r<=R;r++){
            cd coeff=ikpow/fact[r];
            cs += coeff*AS[r][idx]; cdv += coeff*AD[r][idx]; ikpow*=ik;
        }
        PS[kk+K]=cs.imag(); PD[kk+K]=cdv.real();
    }
    ld eta=(ld)K*acosl(-1.0L)/(ld)M;
    auto rem=[&](ld W){
        ld num=expl(eta), p=1; for(int r=0;r<R+1;r++) p*=eta;
        ld f=1; for(int r=2;r<=R+1;r++) f*=r;
        return W*num*p/f;
    };
    ld boundS=rem(sumAbsS),boundD=rem(sumAbsD);

    std::ofstream out(outpath);
    out.setf(std::ios::scientific); out.precision(std::numeric_limits<ld>::max_digits10);
    out << "{\n";
    out << "  \"c\": "<<C<<",\n  \"n_center\": "<<n0<<",\n  \"K\": "<<K<<",\n  \"M\": "<<M<<",\n  \"R\": "<<R<<",\n";
    out << "  \"prime_count\": "<<primes.size()<<",\n  \"prime_power_count\": "<<ppcount<<",\n";
    out << "  \"L\": \""<<L<<"\",\n";
    out << "  \"eta\": \""<<eta<<"\",\n";
    out << "  \"analytic_taylor_bound_PS\": \""<<boundS<<"\",\n";
    out << "  \"analytic_taylor_bound_PD\": \""<<boundD<<"\",\n";
    out << "  \"PS\": ["; for(int i=0;i<count;i++){if(i)out<<",";out<<"\""<<PS[i]<<"\"";} out<<"],\n";
    out << "  \"PD\": ["; for(int i=0;i<count;i++){if(i)out<<",";out<<"\""<<PD[i]<<"\"";} out<<"]\n}\n";
    std::fprintf(stderr,"primes=%zu pp=%llu eta=%.6Lg bounds S=%.3Le D=%.3Le\n",primes.size(),(unsigned long long)ppcount,eta,boundS,boundD);
}
