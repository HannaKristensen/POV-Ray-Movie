//Hanna Kristensen 
// Standard pre-defined colors
//
#include "colors.inc" 
#include "woods.inc"  
#include "textures.inc"


plane{ <0,-1,0>, 0 texture{ pigment{ checker color rgb<1,1,1>*1.2 color rgb<0.25,0.15,0.1>*0}finish { phong 0.1}}}
camera{location<0.0,0.0,0.0> look_at < 0 , 0 , 0 >}
light_source  { <10, 10, 10>, White}  
sphere { <1,2,1>, 1.00 texture{ Cherry_Wood finish { phong 1 } } }
 