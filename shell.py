from interpreter.make_tokens import Tokenizer
from interpreter.parse import Parser
from interpreter.interpreter import Interpreter

"""##(/((##%//////////////////////##%%((((##########%##&///////////////////////////////////////////////
#######%%//////////////////////##%%##/########%%%%##&///////////////////////////////////////////////
///////////////////////////////##%%%##(((/##%#((%%##&///////////////////////////////////////////////
///////////////////////////////##%&#(%.              ,#/////////////////////////////////////////////
///////////////////////////////###%. .            .    ..#//////////////////////////////////////////
///////////////////////////////#% ..                      .,(///////////////////////////////////////
(//////////////////////////////*                              ////////////////////////(#####(#(((#((
%%##/////////////////////////( .                               .  /(//////////////////(#((#%%%%%%((%
//##(%((////////////////////%. .                                 . .  *(//////////////(#((#%####%((%
//////#####(///////////////#.                                          . .(///////////(#(((%####%%%%
//////////##(##(//////////(..                                              . (////////(#(((%####%((&
///////////////%(##((////(..                                                  .(//////(#(((%##(((#(#
#//////////////////##(#(/. ..                                          .     ...#/////(((((%####%((%
(#(##/////////////////( .                                       ..,(.                 *#(((%%%%%%((%
(%####((%////////////(  .                                    (.                           .#((((((((
////#%###%((&(.                 ,*,...                   ,,                                  .%%%((%
####(###%.                            /.  .            (                                        &((%
((((##.                                  *..         *                                           #(%
###%                                       / .      #                                             ((
((*                                                /                                               (
#.                                           . .  ,                                                %
,                   @@/@@@                    * . *                      *@@@&@*                   /
                   &@@@@@(                    *.  *                      /@@@@@,                   (
                    #*#                       ..  ..                       *@%,                    #
                                              ,.   (                                              /#
                                              *.    (                                            ((#
%                                            /     ..(                                         ..  #
%%                                          . .   . . ,//((((*                               ,..    
&##.                                     .*..,,,,,,,,,,,,,,,,,,,,,/                       ,,...     
(#  ./                                 (.,,,,,,,,,,,,,,,,,,,.,,,.,,,                  (,......      
#    .../                         .(,.,.,,,,..,,,,.,*((/*,,,,,,,,,,,(*,...,*(/*,,..........         
 .   . ....../*,.          ,*/*.,,,,,.,,,,,*//,,,,.,,,,,,,,,,,,,,,,,%.................              
         ..................*,,,,,,,,.#.,.,,,,,,,,,,,,,,,,,,,,,,,,,( .                               
                         .*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,/*,.                                      
                          *,,,,,,,,,,,,,,,,,,,,..         .                                         
                            **,,.,,.,,...  ..                                                       
                              ..                                                                    
                                                                                                    
                                                                                                    
                                                                .  ..... .                           """
line = input(">>> ")

tokens = Tokenizer(line).make_tokens()
print(tokens)

tokens_tree = Parser(tokens).parse()
print(tokens_tree)

# output = Interpreter(tokens_tree).interpret()
# print(output)