cd

echo '
______________________________________________
|                                            |
|              .,-:;//;:=,                   |
|            . :H@@@MM@M#H/.,+%;,            |
|         ,/X+ +M@@M@MM%=,-%HMMM@X/,         |
|       -+@MM; $M@@MH+-,;XMMMM@MMMM@+-       |
|      ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.     |
|    ,%MM@@MH ,@%=            .---=-=:=,.    |
|    =@#@@@MX .,              -%HX$$%%%+;    |
|   =-./@M@M$                  .;@MMMM@MM:   |
|   X@/ -$MM/                    .+MM@@@M$   |
|  ,@M@H: :@:                    . =X#@@@@-  |
|  ,@@@MMX, .                    /H- ;@M@M=  |
|  .H@@@@M@+,                    %MM+..%#$.  |
|   /MMMM@MMH/.                  XM@MH; =;   |
|    /%+%$XHH@$=              , .H@@@@MX,    |
|     .=--------.           -%H.,@@@@@MX,    |
|     .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.     |
|       =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=       |
|         =%@M@M#@$-.=$@MM@@@M; %M%=         |
|           ,:+$+-,/H#MMMMMMM@= =,           |
|                 =++%%%%+/:-.               |
|____________________________________________|

'


cd

cd MOSQ_SYSTEM_VALVE_PUMP/

git pull

echo  "MOSQUITO UPDATED SUCCESFULLY"
echo "STARTING MOSQ SYSTEM "



echo ""

echo "       _                 _         "
echo " _   _| |__  _   _ _ __ | |_ _   _ "
echo "| | | | '_ \| | | | '_ \| __| | | |"
echo "| |_| | |_) | |_| | | | | |_| |_| |"
echo " \__,_|_.__/ \__,_|_| |_|\__|\__,_|"

echo ""



python3 main.py
