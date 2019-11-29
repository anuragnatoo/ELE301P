`include "c17.v"
module top;
reg N1,N2,
	N3,N6,N7;
wire N22,N23;
c17  m0(N1,N2,N3,N6,N7,N22,N23);
initial begin
	N1=1'b0 ; N2=1'b0 ; N3=1'b0 ; N6=1'b0 ; N7=1'b0 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b0 ; N6=1'b0 ; N7=1'b1 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b0 ; N6=1'b1 ; N7=1'b0 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b0 ; N6=1'b1 ; N7=1'b1 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b1 ; N6=1'b0 ; N7=1'b0 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b1 ; N6=1'b0 ; N7=1'b1 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b1 ; N6=1'b1 ; N7=1'b0 ; 
	#5 N1=1'b0 ; N2=1'b0 ; N3=1'b1 ; N6=1'b1 ; N7=1'b1 ; 
	#5 N1=1'b0 ; N2=1'b1 ; N3=1'b0 ; N6=1'b0 ; N7=1'b0 ; 
	#5 N1=1'b0 ; N2=1'b1 ; N3=1'b0 ; N6=1'b0 ; N7=1'b1 ; 
end

initial begin
$monitor ($time, ": N1=%b N2=%b N3=%b N6=%b N7=%b N22=%b N23=%b ",N1,N2,N3,N6,N7,N22,N23);
$dumpfile("c17.vcd");
$dumpvars;
end

endmodule