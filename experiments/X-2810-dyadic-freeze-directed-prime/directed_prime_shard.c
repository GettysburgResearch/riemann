#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

#include "mpfr_compat.h"

typedef struct { mpfr_t lo, hi; } iv;
static mpfr_prec_t PREC=256;
static mpfr_t tmpv[16];

static void iv_init(iv *x){ mpfr_init2(x->lo,PREC); mpfr_init2(x->hi,PREC); }
static void iv_set_ui(iv *x, unsigned long v){mpfr_set_ui(x->lo,v,MPFR_RNDD);mpfr_set_ui(x->hi,v,MPFR_RNDU);}
static void iv_set_zero(iv *x){iv_set_ui(x,0);}
static void iv_set_str_int_scaled(iv *x,const char*s,unsigned bits){
  if(mpfr_set_str(x->lo,s,10,MPFR_RNDD)||mpfr_set_str(x->hi,s,10,MPFR_RNDU)){
    fprintf(stderr,"bad integer %s\n",s);exit(2);
  }
  mpfr_div_2ui(x->lo,x->lo,bits,MPFR_RNDD);
  mpfr_div_2ui(x->hi,x->hi,bits,MPFR_RNDU);
}
static void iv_copy(iv*out,const iv*a){mpfr_set(out->lo,a->lo,MPFR_RNDD);mpfr_set(out->hi,a->hi,MPFR_RNDU);}
static void iv_add(iv*out,const iv*a,const iv*b){mpfr_add(out->lo,a->lo,b->lo,MPFR_RNDD);mpfr_add(out->hi,a->hi,b->hi,MPFR_RNDU);}
static void iv_sub(iv*out,const iv*a,const iv*b){mpfr_sub(out->lo,a->lo,b->hi,MPFR_RNDD);mpfr_sub(out->hi,a->hi,b->lo,MPFR_RNDU);}
static void iv_mul(iv*out,const iv*a,const iv*b){
  mpfr_mul(tmpv[0],a->lo,b->lo,MPFR_RNDD);mpfr_mul(tmpv[1],a->lo,b->hi,MPFR_RNDD);
  mpfr_mul(tmpv[2],a->hi,b->lo,MPFR_RNDD);mpfr_mul(tmpv[3],a->hi,b->hi,MPFR_RNDD);
  int mi=0;for(int i=1;i<4;i++)if(mpfr_cmp(tmpv[i],tmpv[mi])<0)mi=i;mpfr_set(out->lo,tmpv[mi],MPFR_RNDD);
  mpfr_mul(tmpv[4],a->lo,b->lo,MPFR_RNDU);mpfr_mul(tmpv[5],a->lo,b->hi,MPFR_RNDU);
  mpfr_mul(tmpv[6],a->hi,b->lo,MPFR_RNDU);mpfr_mul(tmpv[7],a->hi,b->hi,MPFR_RNDU);
  int ma=4;for(int i=5;i<8;i++)if(mpfr_cmp(tmpv[i],tmpv[ma])>0)ma=i;mpfr_set(out->hi,tmpv[ma],MPFR_RNDU);
}
static void iv_mul_ui(iv*out,const iv*a,unsigned long n){mpfr_mul_ui(out->lo,a->lo,n,MPFR_RNDD);mpfr_mul_ui(out->hi,a->hi,n,MPFR_RNDU);}
static void iv_div(iv*out,const iv*a,const iv*b){
  if(mpfr_cmp_si(b->lo,0)<=0){fprintf(stderr,"division interval not positive\n");exit(2);}
  mpfr_div(tmpv[0],a->lo,b->lo,MPFR_RNDD);mpfr_div(tmpv[1],a->lo,b->hi,MPFR_RNDD);
  mpfr_div(tmpv[2],a->hi,b->lo,MPFR_RNDD);mpfr_div(tmpv[3],a->hi,b->hi,MPFR_RNDD);
  int mi=0;for(int i=1;i<4;i++)if(mpfr_cmp(tmpv[i],tmpv[mi])<0)mi=i;mpfr_set(out->lo,tmpv[mi],MPFR_RNDD);
  mpfr_div(tmpv[4],a->lo,b->lo,MPFR_RNDU);mpfr_div(tmpv[5],a->lo,b->hi,MPFR_RNDU);
  mpfr_div(tmpv[6],a->hi,b->lo,MPFR_RNDU);mpfr_div(tmpv[7],a->hi,b->hi,MPFR_RNDU);
  int ma=4;for(int i=5;i<8;i++)if(mpfr_cmp(tmpv[i],tmpv[ma])>0)ma=i;mpfr_set(out->hi,tmpv[ma],MPFR_RNDU);
}
static void iv_log(iv*out,const iv*a){
  if(mpfr_cmp_si(a->lo,0)<=0){fprintf(stderr,"log nonpositive\n");exit(2);}
  mpfr_log(out->lo,a->lo,MPFR_RNDD);mpfr_log(out->hi,a->hi,MPFR_RNDU);
}
static void iv_sqrt(iv*out,const iv*a){
  if(mpfr_cmp_si(a->lo,0)<0){fprintf(stderr,"sqrt negative\n");exit(2);}
  mpfr_sqrt(out->lo,a->lo,MPFR_RNDD);mpfr_sqrt(out->hi,a->hi,MPFR_RNDU);
}
static void iv_sub_ui(iv*out,const iv*a,unsigned long n){
  mpfr_set_ui(tmpv[8],n,MPFR_RNDN);
  mpfr_sub(out->lo,a->lo,tmpv[8],MPFR_RNDD);
  mpfr_sub(out->hi,a->hi,tmpv[8],MPFR_RNDU);
}
static void iv_one_minus(iv*out,const iv*a){
  mpfr_set_ui(tmpv[8],1,MPFR_RNDN);
  mpfr_sub(out->lo,tmpv[8],a->hi,MPFR_RNDD);
  mpfr_sub(out->hi,tmpv[8],a->lo,MPFR_RNDU);
}
static void iv_sincos_lipschitz(iv*sout,iv*cout,const iv*x){
  /* Evaluate at a rounded midpoint and widen by the larger outward distance
     to an endpoint. Since sine and cosine are 1-Lipschitz, this encloses the
     whole input interval without assuming the rounded midpoint is exact. */
  mpfr_add(tmpv[8],x->lo,x->hi,MPFR_RNDN);
  mpfr_div_2ui(tmpv[8],tmpv[8],1,MPFR_RNDN);
  mpfr_sub(tmpv[9],tmpv[8],x->lo,MPFR_RNDU);
  mpfr_sub(tmpv[14],x->hi,tmpv[8],MPFR_RNDU);
  if(mpfr_cmp(tmpv[14],tmpv[9])>0)mpfr_set(tmpv[9],tmpv[14],MPFR_RNDU);
  mpfr_sin(tmpv[10],tmpv[8],MPFR_RNDD);mpfr_sub(sout->lo,tmpv[10],tmpv[9],MPFR_RNDD);
  mpfr_sin(tmpv[11],tmpv[8],MPFR_RNDU);mpfr_add(sout->hi,tmpv[11],tmpv[9],MPFR_RNDU);
  mpfr_cos(tmpv[12],tmpv[8],MPFR_RNDD);mpfr_sub(cout->lo,tmpv[12],tmpv[9],MPFR_RNDD);
  mpfr_cos(tmpv[13],tmpv[8],MPFR_RNDU);mpfr_add(cout->hi,tmpv[13],tmpv[9],MPFR_RNDU);
  if(mpfr_cmp_si(sout->lo,-1)<0)mpfr_set_si(sout->lo,-1,MPFR_RNDD);
  if(mpfr_cmp_si(sout->hi,1)>0)mpfr_set_si(sout->hi,1,MPFR_RNDU);
  if(mpfr_cmp_si(cout->lo,-1)<0)mpfr_set_si(cout->lo,-1,MPFR_RNDD);
  if(mpfr_cmp_si(cout->hi,1)>0)mpfr_set_si(cout->hi,1,MPFR_RNDU);
}

static uint64_t *simple_primes_u64(uint64_t limit,size_t*outn){
  uint8_t*mark=malloc((size_t)limit+1);if(!mark){fprintf(stderr,"base sieve alloc\n");exit(2);}
  memset(mark,1,(size_t)limit+1);mark[0]=0;if(limit>=1)mark[1]=0;
  for(uint64_t p=2;p*p<=limit;p++)if(mark[p])for(uint64_t q=p*p;q<=limit;q+=p)mark[q]=0;
  size_t n=0;for(uint64_t p=2;p<=limit;p++)if(mark[p])n++;
  uint64_t*a=malloc(n*sizeof(uint64_t));if(!a)exit(2);
  size_t j=0;for(uint64_t p=2;p<=limit;p++)if(mark[p])a[j++]=p;
  free(mark);*outn=n;return a;
}
static uint64_t *segment_primes_u64(uint64_t low,uint64_t high,const uint64_t*base,size_t nb,size_t*outn){
  size_t len=(size_t)(high-low);uint8_t*mark=malloc(len);if(!mark){fprintf(stderr,"segment alloc %zu\n",len);exit(2);}memset(mark,1,len);
  uint64_t root=(uint64_t)sqrt((long double)(high-1));
  while((root+1)*(root+1)<=high-1)root++;while(root*root>high-1)root--;
  for(size_t i=0;i<nb;i++){
    uint64_t p=base[i];if(p>root)break;uint64_t start=p*p;
    uint64_t multiple=((low+p-1)/p)*p;if(multiple>start)start=multiple;
    if(start<high)for(uint64_t q=start;q<high;q+=p)mark[q-low]=0;
  }
  size_t n=0;for(size_t i=0;i<len;i++)if(mark[i]&&low+i>=2)n++;
  uint64_t*a=malloc(n*sizeof(uint64_t));if(!a)exit(2);
  size_t j=0;for(size_t i=0;i<len;i++)if(mark[i]&&low+i>=2)a[j++]=low+i;
  free(mark);*outn=n;return a;
}

int main(int argc,char**argv){
  if(argc<10){
    fprintf(stderr,"usage: %s cutoff carrier autocorr.txt segment_size start_segment end_segment include_higher output.json precision\n",argv[0]);
    return 2;
  }
  uint64_t cutoff=strtoull(argv[1],0,10);const char*carrier_text=argv[2];const char*autocorr_file=argv[3];
  uint64_t segment_size=strtoull(argv[4],0,10);uint64_t segment_start=strtoull(argv[5],0,10),segment_end=strtoull(argv[6],0,10);
  int include_higher=atoi(argv[7]);const char*output_path=argv[8];PREC=atol(argv[9]);
  uint64_t total_segments=(cutoff-2)/segment_size+1;
  if(!(segment_start<segment_end&&segment_end<=total_segments)){
    fprintf(stderr,"bad segment range total=%llu\n",(unsigned long long)total_segments);return 2;
  }
  for(int i=0;i<16;i++)mpfr_init2(tmpv[i],PREC);

  FILE*input=fopen(autocorr_file,"r");if(!input){perror("autocorr");return 2;}
  int cells;unsigned scale_bits;if(fscanf(input,"%d %u",&cells,&scale_bits)!=2)return 2;
  iv *auto_real=calloc(cells,sizeof(iv)),*auto_imag=calloc(cells,sizeof(iv));
  char real_text[1024],imag_text[1024];
  for(int lag=0;lag<cells;lag++){
    iv_init(&auto_real[lag]);iv_init(&auto_imag[lag]);
    if(fscanf(input,"%1023s %1023s",real_text,imag_text)!=2)return 2;
    iv_set_str_int_scaled(&auto_real[lag],real_text,scale_bits);
    iv_set_str_int_scaled(&auto_imag[lag],imag_text,scale_bits);
  }
  fclose(input);

  iv zero,one,pi,cutoff_iv,log_cutoff,carrier,sum,log_p,log_q,q_iv,p_iv,sqrt_q,denominator,weight,r,fraction,one_minus_fraction,rho_real,rho_imag,phase,sin_value,cos_value,t1,t2,scalar,term,scratch;
  iv *all[]={&zero,&one,&pi,&cutoff_iv,&log_cutoff,&carrier,&sum,&log_p,&log_q,&q_iv,&p_iv,&sqrt_q,&denominator,&weight,&r,&fraction,&one_minus_fraction,&rho_real,&rho_imag,&phase,&sin_value,&cos_value,&t1,&t2,&scalar,&term,&scratch};
  for(size_t i=0;i<sizeof(all)/sizeof(all[0]);i++)iv_init(all[i]);
  iv_set_zero(&zero);iv_set_ui(&one,1);iv_set_ui(&cutoff_iv,(unsigned long)cutoff);iv_log(&log_cutoff,&cutoff_iv);
  mpfr_const_pi(pi.lo,MPFR_RNDD);mpfr_const_pi(pi.hi,MPFR_RNDU);
  if(mpfr_set_str(carrier.lo,carrier_text,10,MPFR_RNDD)||mpfr_set_str(carrier.hi,carrier_text,10,MPFR_RNDU))return 2;
  iv_set_zero(&sum);

  uint64_t root=(uint64_t)sqrt((long double)cutoff);
  while((root+1)*(root+1)<=cutoff)root++;while(root*root>cutoff)root--;
  size_t base_count=0;uint64_t*base=simple_primes_u64(root,&base_count);
  uint64_t prime_count=0,higher_count=0,total_terms=0;long ambiguous_lags=0;time_t started=time(0);

#define PROCESS_TERM(P,Q,EXPONENT,IS_HIGHER) do { \
      uint64_t _p=(P),_q=(Q);unsigned _e=(EXPONENT);total_terms++;if(IS_HIGHER)higher_count++; \
      iv_set_ui(&p_iv,(unsigned long)_p);iv_log(&log_p,&p_iv);iv_set_ui(&q_iv,(unsigned long)_q);iv_sqrt(&sqrt_q,&q_iv); \
      iv_mul(&denominator,&pi,&sqrt_q);iv_div(&weight,&log_p,&denominator); \
      iv_mul_ui(&log_q,&log_p,_e);iv_mul_ui(&scratch,&log_q,(unsigned long)cells);iv_div(&r,&scratch,&log_cutoff); \
      long lower_lag=mpfr_get_si(r.lo,MPFR_RNDD),upper_lag=mpfr_get_si(r.hi,MPFR_RNDD); \
      if(lower_lag!=upper_lag){ambiguous_lags++;fprintf(stderr,"ambiguous lag q=%llu [%ld,%ld]\n",(unsigned long long)_q,lower_lag,upper_lag);return 3;} \
      long lag=lower_lag; \
      if(lag>=0&&lag<cells){ \
        iv_sub_ui(&fraction,&r,(unsigned long)lag);iv_one_minus(&one_minus_fraction,&fraction); \
        iv_mul(&t1,&one_minus_fraction,&auto_real[lag]);if(lag+1<cells)iv_mul(&t2,&fraction,&auto_real[lag+1]);else iv_set_zero(&t2);iv_add(&rho_real,&t1,&t2); \
        iv_mul(&t1,&one_minus_fraction,&auto_imag[lag]);if(lag+1<cells)iv_mul(&t2,&fraction,&auto_imag[lag+1]);else iv_set_zero(&t2);iv_add(&rho_imag,&t1,&t2); \
        iv_mul(&phase,&carrier,&log_q);iv_sincos_lipschitz(&sin_value,&cos_value,&phase); \
        iv_mul(&t1,&cos_value,&rho_real);iv_mul(&t2,&sin_value,&rho_imag);iv_add(&scalar,&t1,&t2); \
        iv_mul(&term,&weight,&scalar);iv_add(&scratch,&sum,&term);iv_copy(&sum,&scratch); \
      } \
    } while(0)

  for(uint64_t segment=segment_start;segment<segment_end;segment++){
    uint64_t low=2+segment*segment_size,high=low+segment_size;if(high>cutoff+1||high<low)high=cutoff+1;
    size_t count=0;uint64_t*primes=segment_primes_u64(low,high,base,base_count,&count);
    for(size_t i=0;i<count;i++){uint64_t p=primes[i];PROCESS_TERM(p,p,1,0);prime_count++;}
    free(primes);
    fprintf(stderr,"segment=%llu primes=%llu terms=%llu elapsed=%ld\n",(unsigned long long)segment,(unsigned long long)prime_count,(unsigned long long)total_terms,(long)(time(0)-started));
  }
  if(include_higher){
    for(size_t i=0;i<base_count;i++){
      uint64_t p=base[i],q=p*p;unsigned exponent=2;
      while(q<=cutoff){PROCESS_TERM(p,q,exponent,1);if(q>cutoff/p)break;q*=p;exponent++;}
    }
  }

  double sum_lower=mpfr_get_d(sum.lo,MPFR_RNDD),sum_upper=mpfr_get_d(sum.hi,MPFR_RNDU);
  uint64_t coverage_low=2+segment_start*segment_size,coverage_high=2+segment_end*segment_size;
  if(coverage_high>cutoff+1||coverage_high<coverage_low)coverage_high=cutoff+1;
  FILE*output=fopen(output_path,"w");if(!output){perror("output");return 2;}
  fprintf(output,"{\n \"schema\":\"riemann.mpfr-fixed-vector-shard.v1\",\n \"cutoff\":%llu,\n \"carrier\":\"%s\",\n \"cells\":%d,\n \"precision_bits\":%ld,\n \"segment_size\":%llu,\n \"total_segments\":%llu,\n \"segment_start\":%llu,\n \"segment_end\":%llu,\n \"integer_low_inclusive\":%llu,\n \"integer_high_exclusive\":%llu,\n \"include_higher_powers\":%s,\n \"prime_count\":%llu,\n \"higher_prime_power_count\":%llu,\n \"total_terms\":%llu,\n \"prime_rayleigh_lower_hex\":\"%a\",\n \"prime_rayleigh_upper_hex\":\"%a\",\n \"ambiguous_lags\":%ld,\n \"status\":\"DIRECTED_MPFR_SHARD\"\n}\n",(unsigned long long)cutoff,carrier_text,cells,(long)PREC,(unsigned long long)segment_size,(unsigned long long)total_segments,(unsigned long long)segment_start,(unsigned long long)segment_end,(unsigned long long)coverage_low,(unsigned long long)coverage_high,include_higher?"true":"false",(unsigned long long)prime_count,(unsigned long long)higher_count,(unsigned long long)total_terms,sum_lower,sum_upper,ambiguous_lags);
  fclose(output);free(base);
  fprintf(stderr,"done prime=%llu higher=%llu total=%llu interval=[%.17g,%.17g] elapsed=%ld\n",(unsigned long long)prime_count,(unsigned long long)higher_count,(unsigned long long)total_terms,sum_lower,sum_upper,(long)(time(0)-started));
  return 0;
}
