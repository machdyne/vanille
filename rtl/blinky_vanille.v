// VANILLE BLINKY

module blinky #()
(

	input clk48,

	output led,

);

	reg [28:0] counter = 0;

   assign led = ~counter[25];

   always @(posedge clk48) begin
      counter <= counter + 1;
   end

endmodule
