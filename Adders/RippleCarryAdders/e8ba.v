`include "fba.v"
module e8ba(A,B,Cin,sum,carry);
input [7:0] A,B;
output [7:0] sum;
input Cin;
output carry;
wire w0;
fba e8ba_0(A[3:0],B[3:0],Cin,sum[3:0],w0);
fba e8ba_1(A[7:4],B[7:4],w0,sum[7:4],carry);
endmodule

