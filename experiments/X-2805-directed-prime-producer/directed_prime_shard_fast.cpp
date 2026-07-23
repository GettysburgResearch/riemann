#include <mpfr.h>
#include <gmp.h>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

struct Number {
    mpfr_t x;
    explicit Number(mpfr_prec_t p) { mpfr_init2(x,p); }
    ~Number(){ mpfr_clear(x); }
    Number(const Number&)=delete; Number& operator=(const Number&)=delete;
};
struct Interval {
    Number lo,hi;
    explicit Interval(mpfr_prec_t p):lo(p),hi(p){}
};
struct ComplexIntervals {
    std::vector<std::unique_ptr<Interval>> re,im;
};

static_assert(sizeof(unsigned long) >= 8, "producer requires a 64-bit unsigned long ABI");
static void set_ui(Interval& a, uint64_t x){ mpfr_set_ui(a.lo.x,(unsigned long)x,MPFR_RNDD); mpfr_set_ui(a.hi.x,(unsigned long)x,MPFR_RNDU); }
static void set_zero(Interval& a){ mpfr_set_ui(a.lo.x,0,MPFR_RNDN); mpfr_set_ui(a.hi.x,0,MPFR_RNDN); }
static void set_fraction(Interval& a, const mpz_t num, unsigned long bits){
    mpfr_set_z(a.lo.x,num,MPFR_RNDD); mpfr_div_2ui(a.lo.x,a.lo.x,bits,MPFR_RNDD);
    mpfr_set_z(a.hi.x,num,MPFR_RNDU); mpfr_div_2ui(a.hi.x,a.hi.x,bits,MPFR_RNDU);
}
static void copy_i(Interval& out,const Interval& a){ mpfr_set(out.lo.x,a.lo.x,MPFR_RNDD); mpfr_set(out.hi.x,a.hi.x,MPFR_RNDU); }
static void add_i(Interval& o,const Interval&a,const Interval&b){ mpfr_add(o.lo.x,a.lo.x,b.lo.x,MPFR_RNDD); mpfr_add(o.hi.x,a.hi.x,b.hi.x,MPFR_RNDU); }
static void sub_i(Interval& o,const Interval&a,const Interval&b){ mpfr_sub(o.lo.x,a.lo.x,b.hi.x,MPFR_RNDD); mpfr_sub(o.hi.x,a.hi.x,b.lo.x,MPFR_RNDU); }
static void scale_ui_i(Interval&o,const Interval&a,uint64_t k){ mpfr_mul_ui(o.lo.x,a.lo.x,k,MPFR_RNDD); mpfr_mul_ui(o.hi.x,a.hi.x,k,MPFR_RNDU); }

struct Scratch {
    std::vector<std::unique_ptr<Number>> t;
    Scratch(mpfr_prec_t p,int n=16){ for(int i=0;i<n;i++) t.emplace_back(std::make_unique<Number>(p)); }
};
static void mul_i(Interval&o,const Interval&a,const Interval&b,Scratch&s){
    for(int i=0;i<4;i++) mpfr_set_ui(s.t[i]->x,0,MPFR_RNDN);
    mpfr_mul(s.t[0]->x,a.lo.x,b.lo.x,MPFR_RNDD); mpfr_mul(s.t[1]->x,a.lo.x,b.hi.x,MPFR_RNDD);
    mpfr_mul(s.t[2]->x,a.hi.x,b.lo.x,MPFR_RNDD); mpfr_mul(s.t[3]->x,a.hi.x,b.hi.x,MPFR_RNDD);
    mpfr_set(o.lo.x,s.t[0]->x,MPFR_RNDD); for(int i=1;i<4;i++) if(mpfr_cmp(s.t[i]->x,o.lo.x)<0) mpfr_set(o.lo.x,s.t[i]->x,MPFR_RNDD);
    mpfr_mul(s.t[0]->x,a.lo.x,b.lo.x,MPFR_RNDU); mpfr_mul(s.t[1]->x,a.lo.x,b.hi.x,MPFR_RNDU);
    mpfr_mul(s.t[2]->x,a.hi.x,b.lo.x,MPFR_RNDU); mpfr_mul(s.t[3]->x,a.hi.x,b.hi.x,MPFR_RNDU);
    mpfr_set(o.hi.x,s.t[0]->x,MPFR_RNDU); for(int i=1;i<4;i++) if(mpfr_cmp(s.t[i]->x,o.hi.x)>0) mpfr_set(o.hi.x,s.t[i]->x,MPFR_RNDU);
}
static void div_pos_i(Interval&o,const Interval&a,const Interval&b){
    if(mpfr_cmp_ui(b.lo.x,0)<=0) throw std::runtime_error("nonpositive interval divisor");
    mpfr_div(o.lo.x,a.lo.x,b.hi.x,MPFR_RNDD); mpfr_div(o.hi.x,a.hi.x,b.lo.x,MPFR_RNDU);
}
static void hull_i(Interval&o,const Interval&a,bool first){
    if(first){copy_i(o,a);return;} if(mpfr_cmp(a.lo.x,o.lo.x)<0)mpfr_set(o.lo.x,a.lo.x,MPFR_RNDD); if(mpfr_cmp(a.hi.x,o.hi.x)>0)mpfr_set(o.hi.x,a.hi.x,MPFR_RNDU);
}
static void clamp_unit(Interval&a){ if(mpfr_cmp_si(a.lo.x,-1)<0) mpfr_set_si(a.lo.x,-1,MPFR_RNDN); if(mpfr_cmp_ui(a.hi.x,1)>0) mpfr_set_ui(a.hi.x,1,MPFR_RNDN); }
static void unary_nearest_enclosure(Interval& out, const Interval& exact, int (*fn)(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t)) {
    fn(out.lo.x, exact.lo.x, MPFR_RNDN);
    mpfr_set(out.hi.x, out.lo.x, MPFR_RNDN);
    mpfr_nextbelow(out.lo.x);
    mpfr_nextabove(out.hi.x);
}

struct Manifest {
    int K=0,vector_bits=0,ac_bits=0,cutoff_power10=0;
    uint64_t cutoff=0,segment_size=0,total_segments=0;
    std::string vector_sha,normalization_sha,parameter_sha,carrier_num,carrier_den;
    std::vector<std::string> are,aim;
};
static Manifest read_manifest(const std::string& path){
    std::ifstream in(path); if(!in) throw std::runtime_error("cannot open manifest"); std::string magic; in>>magic; if(magic!="RIEMANN_D0801_AUTOCORRELATION_V1") throw std::runtime_error("bad manifest magic");
    Manifest m; std::string key; int a_count=0;
    while(in>>key){
        if(key=="cells")in>>m.K; else if(key=="vector_scale_bits")in>>m.vector_bits; else if(key=="autocorr_scale_bits")in>>m.ac_bits;
        else if(key=="vector_sha256")in>>m.vector_sha; else if(key=="normalization_sha256")in>>m.normalization_sha; else if(key=="parameter_sha256")in>>m.parameter_sha;
        else if(key=="cutoff_power10")in>>m.cutoff_power10; else if(key=="cutoff")in>>m.cutoff; else if(key=="carrier_num")in>>m.carrier_num; else if(key=="carrier_den")in>>m.carrier_den;
        else if(key=="segment_size")in>>m.segment_size; else if(key=="total_segments")in>>m.total_segments; else if(key=="a_count"){in>>a_count;m.are.resize(a_count);m.aim.resize(a_count);}
        else if(key=="a"){int d;in>>d; if(d<0||d>=a_count)throw std::runtime_error("bad autocorrelation index"); in>>m.are[d]>>m.aim[d];}
        else throw std::runtime_error("unknown manifest key: "+key);
    }
    if(m.K<1||a_count!=m.K+1||m.cutoff<2||m.carrier_den=="0")throw std::runtime_error("incomplete manifest");
    if(m.normalization_sha!="65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be")throw std::runtime_error("normalization fingerprint mismatch");
    uint64_t expected=1;for(int i=0;i<m.cutoff_power10;i++){if(expected>UINT64_MAX/10)throw std::runtime_error("cutoff overflow");expected*=10;}if(expected!=m.cutoff)throw std::runtime_error("cutoff does not match cutoff_power10");
    uint64_t expected_segments=(m.cutoff-2)/m.segment_size+1;if(expected_segments!=m.total_segments)throw std::runtime_error("total_segments mismatch"); return m;
}

static std::vector<uint32_t> simple_primes(uint64_t limit){ std::vector<uint8_t> mark(limit+1,1); if(limit>=0)mark[0]=0; if(limit>=1)mark[1]=0; for(uint64_t p=2;p*p<=limit;p++)if(mark[p])for(uint64_t k=p*p;k<=limit;k+=p)mark[k]=0; std::vector<uint32_t> out; for(uint64_t p=2;p<=limit;p++)if(mark[p])out.push_back((uint32_t)p); return out; }
static std::vector<uint64_t> segment_primes(uint64_t low,uint64_t high,const std::vector<uint32_t>&base){
    std::vector<uint8_t> mark(high-low,1); uint64_t root=(uint64_t)std::sqrt((long double)(high-1)); while((root+1)*(root+1)<=high-1)++root; while(root*root>high-1)--root;
    for(uint32_t p:base){ if(p>root)break; uint64_t start=std::max<uint64_t>((uint64_t)p*p, ((low+p-1)/p)*p); for(uint64_t k=start;k<high;k+=p)mark[k-low]=0; }
    std::vector<uint64_t> out; for(uint64_t i=0;i<high-low;i++)if(mark[i]&&low+i>=2)out.push_back(low+i); return out;
}

struct Evaluator {
    mpfr_prec_t prec; int K; Interval pi,L,T;
    ComplexIntervals ac; Scratch scratch;
    Interval pval,logp,u,qval,sqrtq,denom,amp,r,phi,rad,cs,sn,cre,cim,rho,term,tmp1,tmp2,tmp3,tmp4,f,diff,seg;
    uint64_t knot_hulls=0; double max_phase_width=0;
    Evaluator(const Manifest&m,mpfr_prec_t p):prec(p),K(m.K),pi(p),L(p),T(p),scratch(p,20),pval(p),logp(p),u(p),qval(p),sqrtq(p),denom(p),amp(p),r(p),phi(p),rad(p),cs(p),sn(p),cre(p),cim(p),rho(p),term(p),tmp1(p),tmp2(p),tmp3(p),tmp4(p),f(p),diff(p),seg(p){
        ac.re.reserve(K+1);ac.im.reserve(K+1); for(int d=0;d<=K;d++){ac.re.emplace_back(std::make_unique<Interval>(p));ac.im.emplace_back(std::make_unique<Interval>(p)); mpz_t z;mpz_init(z);mpz_set_str(z,m.are[d].c_str(),10);set_fraction(*ac.re[d],z,m.ac_bits);mpz_set_str(z,m.aim[d].c_str(),10);set_fraction(*ac.im[d],z,m.ac_bits);mpz_clear(z);} 
        mpfr_const_pi(pi.lo.x,MPFR_RNDN);mpfr_set(pi.hi.x,pi.lo.x,MPFR_RNDN);mpfr_nextbelow(pi.lo.x);mpfr_nextabove(pi.hi.x);
        set_ui(tmp1,m.cutoff);unary_nearest_enclosure(L,tmp1,mpfr_log);
        mpz_t zn,zd;mpz_init_set_str(zn,m.carrier_num.c_str(),10);mpz_init_set_str(zd,m.carrier_den.c_str(),10); mpfr_set_z(T.lo.x,zn,MPFR_RNDD);mpfr_set_z(tmp1.lo.x,zd,MPFR_RNDU);mpfr_div(T.lo.x,T.lo.x,tmp1.lo.x,MPFR_RNDD); mpfr_set_z(T.hi.x,zn,MPFR_RNDU);mpfr_set_z(tmp1.hi.x,zd,MPFR_RNDD);mpfr_div(T.hi.x,T.hi.x,tmp1.hi.x,MPFR_RNDU);mpz_clear(zn);mpz_clear(zd);
    }
    void interpolate(){
        long d0=mpfr_get_si(r.lo.x,MPFR_RNDD), d1=mpfr_get_si(r.hi.x,MPFR_RNDD); if(d0<0)d0=0;if(d1>K)d1=K; bool first=true; if(d1>d0)knot_hulls++;
        for(long d=d0;d<=d1;d++){
            if(d>=K){set_zero(tmp3);set_zero(tmp4);hull_i(cre,tmp3,first);hull_i(cim,tmp4,first);first=false;continue;}
            mpfr_set(f.lo.x,r.lo.x,MPFR_RNDD);if(mpfr_cmp_ui(f.lo.x,d)<0)mpfr_set_ui(f.lo.x,d,MPFR_RNDN);mpfr_sub_ui(f.lo.x,f.lo.x,d,MPFR_RNDD);
            mpfr_set(f.hi.x,r.hi.x,MPFR_RNDU);if(mpfr_cmp_ui(f.hi.x,d+1)>0)mpfr_set_ui(f.hi.x,d+1,MPFR_RNDN);mpfr_sub_ui(f.hi.x,f.hi.x,d,MPFR_RNDU); if(mpfr_cmp(f.lo.x,f.hi.x)>0)continue;
            sub_i(diff,*ac.re[d+1],*ac.re[d]);mul_i(tmp1,diff,f,scratch);add_i(tmp3,*ac.re[d],tmp1);
            sub_i(diff,*ac.im[d+1],*ac.im[d]);mul_i(tmp1,diff,f,scratch);add_i(tmp4,*ac.im[d],tmp1);
            hull_i(cre,tmp3,first);hull_i(cim,tmp4,first);first=false;
        }
        if(first){set_zero(cre);set_zero(cim);}
    }
    void evaluate(uint64_t q,uint64_t pbase,unsigned exponent,Interval&out){
        set_ui(pval,pbase);unary_nearest_enclosure(logp,pval,mpfr_log);scale_ui_i(u,logp,exponent);
        set_ui(qval,q);unary_nearest_enclosure(sqrtq,qval,mpfr_sqrt);mul_i(denom,pi,sqrtq,scratch);div_pos_i(amp,logp,denom);
        scale_ui_i(tmp1,u,K);div_pos_i(r,tmp1,L);interpolate();
        mul_i(phi,T,u,scratch);
        mpfr_add(tmp1.lo.x,phi.lo.x,phi.hi.x,MPFR_RNDN);mpfr_div_2ui(tmp1.lo.x,tmp1.lo.x,1,MPFR_RNDN);
        mpfr_sub(rad.hi.x,tmp1.lo.x,phi.lo.x,MPFR_RNDU);mpfr_sub(tmp2.hi.x,phi.hi.x,tmp1.lo.x,MPFR_RNDU);if(mpfr_cmp(tmp2.hi.x,rad.hi.x)>0)mpfr_set(rad.hi.x,tmp2.hi.x,MPFR_RNDU);mpfr_set_ui(rad.lo.x,0,MPFR_RNDN);
        max_phase_width=std::max(max_phase_width,2*mpfr_get_d(rad.hi.x,MPFR_RNDU));
        mpfr_sin_cos(sn.lo.x,cs.lo.x,tmp1.lo.x,MPFR_RNDN);mpfr_set(sn.hi.x,sn.lo.x,MPFR_RNDN);mpfr_set(cs.hi.x,cs.lo.x,MPFR_RNDN);mpfr_nextbelow(sn.lo.x);mpfr_nextabove(sn.hi.x);mpfr_nextbelow(cs.lo.x);mpfr_nextabove(cs.hi.x);
        mpfr_sub(cs.lo.x,cs.lo.x,rad.hi.x,MPFR_RNDD);mpfr_add(cs.hi.x,cs.hi.x,rad.hi.x,MPFR_RNDU);clamp_unit(cs);
        mpfr_sub(sn.lo.x,sn.lo.x,rad.hi.x,MPFR_RNDD);mpfr_add(sn.hi.x,sn.hi.x,rad.hi.x,MPFR_RNDU);clamp_unit(sn);
        mul_i(tmp1,cre,cs,scratch);mul_i(tmp2,cim,sn,scratch);add_i(rho,tmp1,tmp2);mul_i(out,amp,rho,scratch);
    }
};

static std::string mpz_string(const mpz_t z){char*raw=mpz_get_str(nullptr,10,z);std::string s(raw);void(*freefunc)(void*,size_t);mp_get_memory_functions(nullptr,nullptr,&freefunc);freefunc(raw,s.size()+1);return s;}
static std::pair<std::string,std::string> rational_strings(mpfr_srcptr x){mpz_t z,den;mpz_init(z);mpz_init_set_ui(den,1);mpfr_exp_t e=mpfr_get_z_2exp(z,x);if(e>=0)mpz_mul_2exp(z,z,e);else mpz_mul_2exp(den,den,-e);std::string a=mpz_string(z),b=mpz_string(den);mpz_clear(z);mpz_clear(den);return {a,b};}
int main(int argc,char**argv){
    try{
        std::map<std::string,std::string> opt; bool include=false; for(int i=1;i<argc;i++){std::string a=argv[i];if(a=="--include-higher-powers")include=true;else if(a.rfind("--",0)==0&&i+1<argc)opt[a]=argv[++i];else throw std::runtime_error("bad argument: "+a);} 
        auto req=[&](const std::string&k)->std::string{if(!opt.count(k))throw std::runtime_error("missing "+k);return opt[k];};
        Manifest m=read_manifest(req("--manifest"));uint64_t start=std::stoull(req("--start-segment")),end=std::stoull(req("--end-segment"));mpfr_prec_t prec=std::stol(opt.count("--precision")?opt["--precision"]:"192");std::string output=req("--output");if(!(start<end&&end<=m.total_segments))throw std::runtime_error("bad segment range");
        Evaluator ev(m,prec);Interval sum(prec),term(prec);set_zero(sum);auto base=simple_primes((uint64_t)std::sqrt((long double)m.cutoff)+1);uint64_t pc=0,hc=0;
        for(uint64_t s=start;s<end;s++){uint64_t low=2+s*m.segment_size,high=std::min<uint64_t>(m.cutoff+1,low+m.segment_size);auto ps=segment_primes(low,high,base);for(uint64_t p:ps){ev.evaluate(p,p,1,term);mpfr_add(sum.lo.x,sum.lo.x,term.lo.x,MPFR_RNDD);mpfr_add(sum.hi.x,sum.hi.x,term.hi.x,MPFR_RNDU);}pc+=ps.size();}
        if(include){for(uint32_t p:base){uint64_t q=(uint64_t)p*p;unsigned e=2;while(q<=m.cutoff){ev.evaluate(q,p,e,term);mpfr_add(sum.lo.x,sum.lo.x,term.lo.x,MPFR_RNDD);mpfr_add(sum.hi.x,sum.hi.x,term.hi.x,MPFR_RNDU);hc++;if(q>m.cutoff/p)break;q*=p;e++;}}}
        auto lo=rational_strings(sum.lo.x),hi=rational_strings(sum.hi.x);std::ofstream out(output);out<<"{\n  \"schema\": \"riemann.piecewise-carrier-directed-shard.v1\",\n";
        out<<"  \"segment_start\": "<<start<<", \"segment_end\": "<<end<<",\n  \"include_higher_powers\": "<<(include?"true":"false")<<",\n";
        out<<"  \"prime_count\": "<<pc<<", \"higher_prime_power_count\": "<<hc<<", \"total_terms\": "<<(pc+hc)<<",\n";
        out<<"  \"vector_sha256\": \""<<m.vector_sha<<"\",\n  \"parameter_sha256\": \""<<m.parameter_sha<<"\",\n  \"normalization_sha256\": \""<<m.normalization_sha<<"\",\n";
        out<<"  \"precision_bits\": "<<prec<<", \"mpfr_version\": \""<<mpfr_get_version()<<"\",\n  \"phase_method\": \"MPFR nearest unary enclosure, directed interval algebra, combined sin/cos, and Lipschitz phase widening\",\n";
        out<<"  \"knot_hulls\": "<<ev.knot_hulls<<", \"maximum_phase_interval_width_upper\": "<<std::setprecision(17)<<ev.max_phase_width<<",\n";
        out<<"  \"prime_rayleigh_interval\": {\n    \"lower\": {\"numerator\": "<<lo.first<<", \"denominator\": "<<lo.second<<"},\n    \"upper\": {\"numerator\": "<<hi.first<<", \"denominator\": "<<hi.second<<"}\n  }\n}\n";
    }catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<"\n";return 2;}return 0;
}
