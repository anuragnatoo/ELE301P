`include "fba.v"
module top;
reg [3:0] A,B;
wire [3:0] sum;
reg cin;
wire cout;
fba fba_0(A,B,cin,sum,cout);
initial
begin
A=4'b0000;B=4'b0000;cin=0;
#5 A[0]=1;
#5 A[1]=1;
#5 cin=1;
#5 B[0]=1;
#5 B[3]=1;
end
initial
begin
$monitor($time,"A=%b,B=%b,Cin=%b,sum=%b,carry=%b",A,B,cin,sum,cout);
$dumpfile("4ba.vcd");
$dumpvars;
end
endmodule

