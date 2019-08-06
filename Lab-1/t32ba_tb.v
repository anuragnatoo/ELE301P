`include "t32ba.v"
module top;
reg [31:0] A,B;
wire [31:0] sum;
reg cin;
wire cout;
t32ba t32ba_0(A,B,cin,sum,cout);
initial
begin
A=32'd550000;B=32'd360000;cin=0;
#5 A=32'd640000;
#5 A=32'd16400000;
#5 cin=1;
#5 B=32'd350000;
#5 B=32'd135000;
end
initial
begin
$monitor($time,"A=%d,B=%d,Cin=%d,sum=%d,carry=%d",A,B,cin,sum,cout);
$dumpfile("t32ba.vcd");
$dumpvars;
end
endmodule
