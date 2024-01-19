#include <iostream>
#include <cmath>
#include <random>

double fn(double x,double b=1){

    return (x/b)*exp(1-x/b);

}

double rn(double xmin=0, double xmax=10, double ymin=0, double ymax=1){

    double e=exp(1);
    double b=2;
    ymax=b/e;
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> uniformx(xmin, xmax);
    std::uniform_real_distribution<double> uniformy(ymin, ymax);
    
    double y =uniformy(gen);
    double x =uniformx(gen);
    double fx=fn(x);
    
    while (fx<y){
    
        y =uniformy(gen);
        x =uniformx(gen);
        fx=fn(x);
        
    }
    
    
    return x;
}

int main(){

    std::cout<<rn()<<std::endl;

}
