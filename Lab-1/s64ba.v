`include "16ba.v"
module s64ba(A,B,Cin,sum,carry);
input [63:0] A,B;
output [63:0] sum;
input Cin;
output carry;
wire w0,w1,w2;
s16ba s64a_0(A[15:0],B[15:0],Cin,sum[15:0],w0);
s16ba s64a_1(A[31:16],B[31:16],w0,sum[31:16],w1);
s16ba s64a_2(A[47:32],B[47:32],w1,sum[47:32],w2);
s16ba s64a_3(A[63:48],B[63:48],w2,sum[63:48],carry);
endmodule
