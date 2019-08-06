`include "s64ba.v"
module top;
reg [63:0] A,B;
wire [63:0] sum;
reg cin;
wire cout;
s64ba s64ba_0(A,B,cin,sum,cout);
initial
begin
A=64'd50000;B=64'd35000;cin=0;
#5 A=64'd100000;
#5 A=64'd20000;
#5 cin=1;
#5 B=64'd76000;
#5 B=64'd54000;
end
initial
begin
$monitor($time,"A=%d,B=%d,Cin=%d,sum=%d,carry=%d",A,B,cin,sum,cout);
$dumpfile("s64ba.vcd");
$dumpvars;
end
endmodule

