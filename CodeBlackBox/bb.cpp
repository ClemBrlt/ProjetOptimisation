#include <cmath>
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

double turbine1 (double debit, double hchute) {
    double pmw = 0;
    if (debit < 110) {
        pmw = 0;
    }
    else {
        pmw = 3.468 * pow(10, -5) * pow(debit, 3) - 0.02772 * pow(debit, 2) + 3.121 * debit + 0.264 * pow(hchute, 2)
            - 13.41 * hchute + 3.166 * pow(10, -4) * pow(debit, 2) * hchute - 0.001919 * debit * pow(hchute, 2)
            + 0.06052 * debit * hchute + 14.66;
    }
    return pmw;
}

double turbine2(double debit, double hchute) {
    double pmw = 0;
    if (debit < 110) {
        pmw = 0;
    }
    else {
        pmw = 1.664 * pow(10, -6) * pow(debit, 4) - 0.001098 * pow(debit, 3) + 0.599 * pow(debit, 2) - 131.8 * debit 
            + 6.876 * pow(hchute, 2) - 481.1 * hchute + 4.083 * pow(10, -6) * pow(debit, 3) * hchute
            + 2.888 * pow(10, -4) * pow(debit, 2) * pow(hchute, 2) - 0.02145 * pow(debit, 2) * hchute
            - 0.08983 * debit * pow(hchute, 2) + 6.387 * debit * hchute + 9044;
    }
    return pmw;
}

double turbine3(double debit, double hchute) {
    double pmw = 0;
    if (debit < 110) {
        pmw = 0;
    }
    else {
        pmw = 6.162 * pow(10, -5) * pow(debit, 3) - 0.03789 * pow(debit, 2) + 2.852 * debit
            + 0.5212 * pow(hchute, 2) - 28.94 * hchute + 2.034 * pow(10, -4) * pow(debit, 2) * hchute
            - 0.004112 * debit * pow(hchute, 2) + 0.2127 * debit * hchute + 115.4;
    }
    return pmw;
}

double turbine4(double debit, double hchute) {
    double pmw = 0;
    if (debit < 110) {
        pmw = 0;
    }
    else {
        pmw = 1.442 * pow(10, -6) * pow(debit, 4) - 7.968 * pow(10, -4) * pow(debit, 3) + 0.07851 * pow(debit, 2)
            + 9.675 * debit - 1.577 * pow(hchute, 2) + 109 * hchute - 1.248 * pow(10, -6) * pow(debit, 3) * hchute
            - 7.439 * pow(10, -5) * pow(debit, 2) * pow(hchute, 2) + 0.005468 * pow(debit, 2) * hchute
            + 0.02124 * debit * pow(hchute, 2) - 1.481 * debit * hchute - 1331;
    }
    return pmw;
}

double turbine5(double debit, double hchute) {
    double pmw = 0;
    if (debit < 110) {
        pmw = 0;
    }
    else {
        pmw = 1.615 * pow(10, -5) * pow(debit, 3) + 0.001932 * pow(debit, 2) - 1.935 * debit - 0.06146 * pow(hchute, 2)
            - 3.99 * hchute - 3.386 * pow(10, -4) * pow(debit, 2) * hchute
            - 4.68 * pow(10, -5) * debit * pow(hchute, 2) + 0.118 * debit * hchute + 111.1;
    }
    return pmw;
}

int main ( int argc , char ** argv ) {

  double f = 1e20, c1 = 1e20 , c2 = 1e20;
  double x[7];

  if ( argc >= 2 ) {
    c1 = 0.0 , c2 = 0.0;
    ifstream in ( argv[1] );
    for ( int i = 0 ; i < 7 ; i++ ) {
      in >> x[i];
    }
    f = -(turbine1(x[0],x[6]) + turbine2(x[1], x[6]) + turbine3(x[2], x[6]) + turbine4(x[3], x[6]) + turbine5(x[4], x[6]));
    if ( in.fail() )
      f = c1 = c2 = 1e20;
    else {
      c1 = -x[0] - x[1] - x[2] - x[3] - x[4] + x[5] - 2.6;
      c2 = x[0] + x[1] + x[2] + x[3] + x[4] - x[5] - 2.6;
    }
    in.close();
  }
  cout << f << " " << c1 << " " << c2 << endl;
  return 0;
}
