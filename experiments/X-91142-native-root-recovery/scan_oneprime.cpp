#include <bits/stdc++.h>
using namespace std;
vector<int> basep={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
struct DD{int d,mu; long double inv,lg;};
int main(int argc,char**argv){
 int p=argc>1?atoi(argv[1]):67;
 int JMAX=argc>2?atoi(argv[2]):800;
 int R=argc>3?atoi(argv[3]):500;
 long long XMAX=1LL*JMAX*R;
 vector<long double> inv(XMAX+3),lg(XMAX+3),prefI(XMAX+3),prefL(XMAX+3);
 for(int m=1;m<=XMAX+2;m++){inv[m]=1/sqrtl((long double)m);lg[m]=logl((long double)m);prefI[m]=prefI[m-1]+inv[m];prefL[m]=prefL[m-1]+inv[m]*lg[m];}
 vector<int> ps=basep;ps.push_back(p);sort(ps.begin(),ps.end());
 vector<pair<long long,int>> vals={{1,1}};
 for(int q:ps){int sz=vals.size();for(int i=0;i<sz;i++){long long nd=vals[i].first*q;if(nd<=R)vals.push_back({nd,-vals[i].second});}}
 sort(vals.begin(),vals.end());vector<DD> ds;for(auto [d,mu]:vals)ds.push_back({(int)d,mu,inv[d],lg[d]});
 long double mn=1e100L,mnn=1e100L;int mj=0,mN=0,mnj=0,mnN=0;long long cnt=0,neg=0;
 for(int j=2;j<=JMAX;j++){
  long double A=(long double)(j+1)/(j-1),B=-(long double)(j+1)*(j-2)/(j*(j-1)),C=2.0L/(j*(j-1));
  for(int N=j+1;N<=R*j;N++){
   long double D=0,logN=lg[N];int maxd=N/j;
   for(auto &z:ds){if(z.d>maxd)break;int M=N/z.d;long double logY=logN-z.lg,q=0;
    q+=A*inv[j]*(logY-lg[j]);if(M>=j+1)q+=B*inv[j+1]*(logY-lg[j+1]);
    if(M>=j+2)q+=C*(logY*(prefI[M]-prefI[j+1])-(prefL[M]-prefL[j+1]));
    D+=z.mu*z.inv*q;
   }
   if(D<mn){mn=D;mj=j;mN=N;}long double norm=D*j*(j-1)*sqrtl((long double)N);if(norm<mnn){mnn=norm;mnj=j;mnN=N;}
   if(D<-1e-15L){neg++;if(neg<10)cerr<<"NEG p="<<p<<" j="<<j<<" N="<<N<<" D="<<(double)D<<"\n";}
   cnt++;
  }
 }
 cout<<setprecision(20)<<"p="<<p<<" J="<<JMAX<<" R="<<R<<" count="<<cnt<<" neg="<<neg<<" min="<<mn<<" at "<<mj<<","<<mN<<" norm="<<mnn<<" at "<<mnj<<","<<mnN<<"\n";
}
