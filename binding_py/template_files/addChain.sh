 #!/bin/bash
 
time /dors/meilerlab/apps/rosetta/rosetta-3.13/main/source/bin/rosetta_scripts.default.linuxgccrelease
-l $1 -parser:protocol $2 @AddChain_FastRelax_Multi.options  -out:prefix Add_Rlx_ > AddRel.log
