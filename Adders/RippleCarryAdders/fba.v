`include "FullAdder.v"
module fba(A,B,Cin,sum,carry);
input [3:0] A,B;
output [3:0] sum;
input Cin;
output carry;
wire w0,w1,w2;
FullAdder FA_0(A[0],B[0],Cin,sum[0],w0);
FullAdder FA_1(A[1],B[1],w0,sum[1],w1);
FullAdder FA_2(A[2],B[2],w1,sum[2],w2);
FullAdder FA_3(A[3],B[3],w2,sum[3],carry);
endmodule
