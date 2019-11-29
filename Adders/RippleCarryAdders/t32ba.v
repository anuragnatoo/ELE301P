`include "16ba.v"
module t32ba(A,B,Cin,sum,carry);
input [31:0] A,B;
output [31:0] sum;
input Cin;
output carry;
wire w0;
s16ba t32ba_0(A[15:0],B[15:0],Cin,sum[15:0],w0);
s16ba t32ba_1(A[31:16],B[31:16],w0,sum[31:16],carry);
endmodule
