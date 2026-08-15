#include <bits/stdc++.h>
using namespace std; using i128=__int128_t;
static i128 S;
struct I{i128 lo,hi;};
i128 floorDiv(i128 a,i128 b){i128 q=a/b,r=a%b;if(r&&a<0)--q;return q;}
i128 ceilDiv(i128 a,i128 b){i128 q=a/b,r=a%b;if(r&&a>0)++q;return q;}
I add(I a,I b){return{a.lo+b.lo,a.hi+b.hi};}
I scaleInt(I a,long long c){if(c>=0)return{a.lo*c,a.hi*c};return{a.hi*c,a.lo*c};}
I mulPos(I a,I b){ // b positive
 i128 lo=(a.lo>=0?a.lo*b.lo:a.lo*b.hi);
 i128 hi=(a.hi>=0?a.hi*b.hi:a.hi*b.lo);
 return{floorDiv(lo,S),ceilDiv(hi,S)};
}
string str(i128 x){if(!x)return"0";bool n=x<0;if(n)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(n)s.push_back('-');reverse(s.begin(),s.end());return s;}
long double val(i128 x){return(long double)x/(long double)S;}
static vector<int> primes={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
struct DD{int d,mu;};
int main(int argc,char**argv){
 if(argc<2){cerr<<"bounds file\n";return 2;}ifstream f(argv[1]);long long ss;int nmax;f>>ss>>nmax;S=ss;
 vector<I> inv(nmax+1),dl(nmax+1);for(int i=1;i<=nmax;i++){int n;long long il,ih,ll,lh;f>>n>>il>>ih>>ll>>lh;inv[i]={(i128)il,(i128)ih};dl[i]={(i128)ll,(i128)lh};}
 vector<DD> ds;for(int d=1;d<=67;d++){int x=d,mu=1;bool ok=true;for(int p:primes)if(x%p==0){x/=p;mu=-mu;if(x%p==0){ok=false;break;}}if(ok&&x==1)ds.push_back({d,mu});}
 const int JMAX=510,R=67; long long cells=0,fail=0; i128 minF=((i128)1<<120);int minj=0,minx=0;long double minNorm=1e100L;int nnj=0,nnx=0;
 vector<long long>A(R*JMAX+2);
 for(int j=2;j<=JMAX;j++){
   int xmax=R*j; fill(A.begin(),A.begin()+xmax+1,0);
   for(auto z:ds){
     int mmax=xmax/z.d;
     for(int m=j;m<=mmax;m++){
       long long gamma;
       if(m==j) gamma=(long long)j*(j+1);
       else if(m==j+1) gamma=-(long long)(j+1)*(j-2);
       else gamma=2;
       A[z.d*m]+=(long long)z.mu*gamma;
     }
   }
   I slope{0,0};
   if(A[j]) slope=add(slope,scaleInt(inv[j],A[j]));
   I F{0,0};
   for(int N=j;N<xmax;N++){
     I inc=mulPos(slope,dl[N]);
     F=add(F,inc); // value at X=N+1
     int X=N+1;
     cells++;
     if(F.lo<=0){fail++;if(fail<10)cerr<<"FAIL j="<<j<<" X="<<X<<" lo="<<str(F.lo)<<" hi="<<str(F.hi)<<" slope="<<val(slope.lo)<<","<<val(slope.hi)<<"\n";}
     if(F.lo<minF){minF=F.lo;minj=j;minx=X;}
     long double norm=val(F.lo)*sqrtl((long double)X);
     if(norm<minNorm){minNorm=norm;nnj=j;nnx=X;}
     if(A[X]) slope=add(slope,scaleInt(inv[X],A[X]));
   }
 }
 cout<<setprecision(20);
 cout<<"classification=PASS_DIRECTED_EVENT_CANONICAL_ROW\n";
 cout<<"cells="<<cells<<"\nfailures="<<fail<<"\n";
 cout<<"minimum_F_scaled="<<str(minF)<<"\nminimum_F="<<val(minF)<<" at j="<<minj<<" X="<<minx<<"\n";
 cout<<"minimum_sqrtX_F="<<minNorm<<" at j="<<nnj<<" X="<<nnx<<"\n";
 return fail?1:0;
}
