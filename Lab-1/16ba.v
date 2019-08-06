`include "fba.v"
module s16ba(A,B,Cin,sum,carry);
input [15:0] A,B;
output [15:0] sum;
input Cin;
output carry;
wire w0,w1,w2;
fba s16a_0(A[3:0],B[3:0],Cin,sum[3:0],w0);
fba s16a_1(A[7:4],B[7:4],w0,sum[7:4],w1);
fba s16a_2(A[11:8],B[11:8],w1,sum[11:8],w2);
fba s16a_3(A[15:12],B[15:12],w2,sum[15:12],carry);
endmodule
