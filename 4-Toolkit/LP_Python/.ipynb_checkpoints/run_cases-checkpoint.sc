#!/bin/bash
# semi-colon means wait until process is completed
python3 2D-SteadyConfinedJacobi.py < input0.txt > base-case.out;
python3 2D-SteadyConfinedJacobi.py < input1.txt > pump1.out;
python3 2D-SteadyConfinedJacobi.py < input2.txt > pump2.out;
python3 2D-SteadyConfinedJacobi.py < input3.txt > pump3.out;
python3 2D-SteadyConfinedJacobi.py < input4.txt > pump4.out;
python3 2D-SteadyConfinedJacobi.py < input5.txt > pump5.out;
python3 2D-SteadyConfinedJacobi.py < input6.txt > pump6.out;
python3 2D-SteadyConfinedJacobi.py < input7.txt > pump7.out;
python3 2D-SteadyConfinedJacobi.py < input8.txt > pump8.out;
python3 2D-SteadyConfinedJacobi.py < input9.txt > pump9.out;
python3 2D-SteadyConfinedJacobi.py < input10.txt > pump10.out;
python3 2D-SteadyConfinedJacobi.py < input11.txt > pump11.out;
python3 2D-SteadyConfinedJacobi.py < input12.txt > pump12.out;
python3 2D-SteadyConfinedJacobi.py < input13.txt > pump13.out;
python3 2D-SteadyConfinedJacobi.py < input14.txt > pump14.out;
python3 2D-SteadyConfinedJacobi.py < input15.txt > pump15.out;
python3 2D-SteadyConfinedJacobi.py < input16.txt > pump16.out;
python3 2D-SteadyConfinedJacobi.py < input17.txt > pump17.out;
python3 2D-SteadyConfinedJacobi.py < input18.txt > pump18.out;
python3 2D-SteadyConfinedJacobi.py < input19.txt > pump19.out;
python3 2D-SteadyConfinedJacobi.py < input20.txt > pump20.out;
python3 2D-SteadyConfinedJacobi.py < input21.txt > pump21.out;
python3 2D-SteadyConfinedJacobi.py < input22.txt > pump22.out;
python3 2D-SteadyConfinedJacobi.py < input23.txt > pump23.out;
python3 2D-SteadyConfinedJacobi.py < input24.txt > pump24.out;
python3 2D-SteadyConfinedJacobi.py < input25.txt > pump25.out;
cat base-case.out pump1.out pump2.out pump3.out pump4.out pump5.out pump6.out pump7.out pump8.out pump9.out pump10.out pump11.out pump12.out pump13.out pump14.out pump15.out pump16.out pump17.out pump18.out pump19.out pump20.out pump21.out pump22.out pump23.out pump24.out pump25.out > influence-matrices-out1.txt;
# now kill all the intermediate files
rm -rf base-case.out pump1.out pump2.out pump3.out pump4.out pump5.out pump6.out pump7.out pump8.out pump9.out pump10.out pump11.out pump12.out pump13.out pump14.out pump15.out pump16.out pump17.out pump18.out pump19.out pump20.out pump21.out pump22.out pump23.out pump24.out pump25.out