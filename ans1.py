answers=[
        ["Yes","No","Machine dependent","None of the mention"],
        ["31 Characters","63 Characters","79 Characters","None of the mention"],
        [" _a=1","_a_=1","__str__=1","none of the mention"],
        ["Oval","Assert","Nonlocal","pass"],
        ["Lower case ","upper case"," capitalized "," None "],
        ["abc=1,000,000 ","abc= 1000,20000 3000 "," a,b,c = 1000,2000,3000 ","a_b_c=1,000,000"],
        ["__init__ "," in "," it "," on "],
        [" x^y "," x**y "," x^^y "," None "],
        [" / "," // "," % "," None "],
        [" Parentheses "," Exponential "," Multiplication "," Division "],


        [" 7 ", " 1 "," 0 "," 5 "],
        [" Left to Right "," Right to Left "," Can't say "," None "],
        [" 27 "," 9 "," 3 "," 3 "," 1 "],
        ["  0 1 2 3 0 " , " 0 1 2 0 " , " 0 1 2 3 " , " e r r o r " ],
        ["Exponential","Addition","Multiplication","Parentheses"],
        [" True "," False ","Machine dependent"," Error "],
        ["k = 2 +3j "," k= complex(2,3) "," k = j + 3l"," k = 2 + J"],
        [" a B C D " , " a b c d " , " A B C D " , " e r r o r " ],
        [" Boolean "," Integer "," Float "," complex "],
        [" -5 "," -4 "," -3 "," 3 "],

        [" x = 0b101 "," x = 0x4f5 "," x = 19023 "," x = 03964 "],
        [" 81 "," 12 "," 0.75 "," 7 "],
        [" a B C D " , " a b c d " , " A B C D " , " e r r o r " ],
        [" a B c d " , " a b c " , " 0 a 1 b 2 c " , " 0 a 1 b 2 c " , " none of the mention "],
        [" 1 2 3 4 " , " 4 3 2 1 " , " e r r o r " , " none of mention "],
        [" 0 1 2 3 4 ...", " 0 - 2 ", " 0 ", " e r r o r "],
        [" 0 1 2 3 4  H e r e" , " 0 1 3 4 5  H e r e " , " 0 1 2 3 4 " , " 1 2 3 4 5 "],
        [" 0 1 2 3 " , " 0 1 2 2 " , " 3 3 3 3 " , " e r r o r "],
        [" 2 2 4 " , " E r r o r " , " 1 2 " , " N o n e "],
        [" D C B A ", " A , B , C , D ", " D , C , B , A ", " D,C,B,,A Display on four lines"],

        [" s1.__contains__(s2)", " s2 in s1", " s1.contains(s2)", " si.in(s2)"],
        [" 3 " , " 5 " , " 6 " , " 33 "],
        [" 1 ", " 3 ", " 5 ", " 6 "],
        [" 1 2  3 4 " , " 4 , 5 , 6 , 7 " , " 1 , 3 , 8 , 1 , 2 " , " 1 3 8 1 2 " , " 2 5 9 1 3 "],
        [" 3 3 3" , " 4 3 3 " , " 3 3 5 " , " 5 3 3 "],
        [" 1 " , " 2 " , " 4 " , " 5 "],
        [" 1 " , " 2  " , " 4  " , " 5 "],
        [" 3 " , " 5 " , " 6 " , " 3 3 "],
        [" 1 " , " 3 " , " 5 " , " 6 "],
        [" 1 2 3 4 " , " 4 5 6 7 " , " 1 3 8 1 2 " , " 2 5 9 1 3 "],

        ["[[1,2],[3,1,5],[0,5,0,5]]","[[3,1,5],[1,2],[0,5,0.5]]","[[0.5,0.5],[1,2],[3,1.5]]","[[0.5,0.5],[3,1.5],[1,2]]. "],
        ["[13,56,17,[87],45,67].","[13,56,17,87,45,67].","[13,56,17,87,[45,67]].","[13,56,17,[87],[45,67]]."],
        [" 2 , -24 , -46 , -6 " , " [(2 , -2) , (4 , -4) , (6,-6)]" , " (2 , -2) (4 , -4) (6 , -6)" , "[-4 , -16 , -36]"],
        [" 1 4 7 2 5 8 3 6 9 " , " (1 4 7) (2 5 8) (3 6 9) ", " [(1,4,7) , (2,5,8) , (3,6,9) " , " E r r o r "],
        [" [4 , 5 , 6] " , " [3 , 6 , 9] " , " [1 , 4 , 7 ] " , " [1, 2 , 3] "],
        [" A[ 2 ][ 3 ] " , " A[ 2 ][ 1 ] " , " A[ 1 ][ 2 ] " , " A[ 3 ][ 2 ] "],
        [" N o   o u t p u t " , " E r r o r " , " [[1 , 2 ,3] , [4 , 5 , 6]] " , " [[11 , 12 , 13] , [14 , 15 , 16 ]] "],
        [" [1 , 5 , 9] " , " [4 , 5 , 6] " , " [3 , 5 , 7] " , " [2 , 5 , 8] "],
        [" 30 " , " 24 " , " 3 3 " , " 12 "],
        [" E r r o r " , " (('check',),) " , " (('check',),),). " , " (('check',)'check',) "],

        [" a(i = 4 , j = 7) " , " obj(i = 4 , j = 7 ) " , " (4 , 7) " , " ( none ) "],
        [" 3 ", " 1 ", " 2 ", " 0 "],
        [" 1 " , " 2 " , " 4 " , " E r r o r , the keys "],
        [" Error , dictonary in a dictionary can't exist. " , " 'Numbers': {1 : 56 , 3 : 7} " , " {'Numbers' : {1:56},'Letters': {4: B'}} " ,
         " {'Numbers':{1:56,3:7},'Letters':{4:B'}}"],
        [" 0 " , " 2 " , " Error of keys value pair " , " 1 "],
        [" An exception is thrown " , " 3 " , " 6 " , " 2 "],
        [" {(3 , 4) , (1 , c)} " , " E r r o r " , " {(4 , 2) , (3 , 1) , (4 , 1) , (5 , 2)} " , " {(3 , 1) , (4 , 2)} "],
        [" { 3 }{1 , 2 , 3 , 4 , 5 , 6 , 8} " , " {1 , 2 , 4 , 5 , 6 , 8} " , " { 3 }{ 3 } " , " {1 , 2 , 3 , 4 , 5 , 8}{1 , 2 , 3 , 4 , 5 , 6 , 8} "],
        [" True  False " , "  False  False " , " False True " , " True True "],
        [" Dictionary  makes use of ________ ", " keys , keys " , " key values, keys " , " keys , key values " ],

        ["Error no method caled update for set"," {1 , 2 , 3 , 4 , 5 } " , " Error,list can't be added to set"," E r r o r "],
        [" E r r o r " , " [(1 , 2) , (2 , 3)] " , " [(0 , 2) , (1 , 3)] " , " [( 2 , 3 )] "],
        [" enumerate( ) " , " all(  ) " , " chr( ) " , " max ( ) "],
        [" removes " , " pop " , " discard " , " dispose "],
        [" {1 , 4 , 9 , 16} ", " {0 , 1 , 4 , 9 , 16 } ", " E r r o r ", " {0 , 1 , 4 , 9} "],
        [" Tuple " , " Integer " , " List " , " Both tuple and intger "],
        [" E r r o r " , " [2 , 3]. " , " (2 , 3 , 4) " , " (2 , 3) "],
        [" Array of tuples " , " List of tuples " , " Tuples of lists " , " Invalid type "],
        [" [2 , 3 , 9] " , " [1 , 2 , 4 , 3 , 8 , 9] " , " [1 , 4 , 8] " , " (1 , 4 , 8 ) "],
        [" 40 " , " 45 " , " 'john' " , " 'peter' "],

        [" true " , " False " , " Error " , " Error " , " None "],
        [" 1 " , " 2 " , " 5 " , " Error "],
        ["[x for w in v i x in v " , "[x for x in w if x in v]","[x for x in v if w in v]" , "[x for v in w for x in w]"],
        [" ['good', 'oh', 'excellent', '450'] " , " [ 'good' ] " , " ['good', '#450'] " , " ['oh', 'excellent', '#450'] "],
        [" 8 " , " 1 2 " , " 1 6 " , " 3 2 "],
        [" 3 3 3 " , " 3 3 5 " , " 3 3 5 " , " 5 3 3 "],
        [" 1 " , " 2 " , " 4 " , " 5 "],
        [" 8 " , " 12 " , " 16 " , " 16 " , " 32 "],
        [" [ 1 ][ 2 ][ 3 ]. " , " [ 1 ][1 , 2][1 , 2 , 3]." , " [1 , 2 ,3 ] " , " [2 , 1 , 3] "],
        [" N o n e " , " 1 " , " 2 " , " E r r o r "],

        [" 4 " , " 5 " , " 8 " , " 1 2 " ],
        [" [1 , 3] " , " [4 , 3] ", " [1 , 4] " , " [1 , 3 , 4] " ],
        [" [2 , 6 , 4]. " , " [1 , 3 , 2 , 1 , 3]. " , " [1 , 3 , 2 , 1 , 3 , 2]. " , " [1 , 3 , 2 , 3 , 2 ,1]. " ],
        [" list1  add( 5 ) " , " list1 . append( 5 ) " , " list1 . addLast( 5 ) " , " list1 . addEnd( 5 ) "],
        [" 0 " , " 1 " , " 4 " , " 2 "],
        [" 0 " , " 4 " , " 1 " , " 2 "],
        [" [3,4,5,20,5,25,1,3]. " , " [1,3,3,4,5,5,20,25]. " , " [25,20,5,54,3,3,1 " , " [3,1,25,5,20,5,4,3]. "],
        [" 3 ", " 7 "," 2 "," 0 "],
        [" + "," // "," % "," ** "],
        [" 43 "," 44 "," 22 "," 23 "],

        [" (6.0, 16.0 )","(6.00,16.00)","(6,16)","(6.00,16.0)"],
        ["( 1.0, 4.0 )","(1.0,1.0 )","(4.0 , 1.0)","(4.0 , 4.0)"],
        [" 8.5 "," 8 "," 8.3 "," 8.33 "],
        [" 1101010 ", "0b11101", " 0b11111 ", " 0b11011"],
        [" 0b10111 ", " 8 ", " 4 ", " 2 ", " 1 "],
        [" 1011 ", " 11 ", " 13 ", " 1101 "],
        [" & ", " ^ ", " | ", " ! "],
        [" 115 ", " 116", " 117 ", " 118 "],
        [" 1101010 ", " 110010101 ", " 1101011 ", " 110010100 "],
        [" OR ", " AND ", " XOR ", " NOT "],

        [" 1011011 ", " 11010100 ", " 11101011 ", " 10110011 "],
        [" true ", " False ", " error ", " no output "],

]


correct_ans=[0,3,3,0,3,1,1,1,1,0,1,0,2,1,3,1,2,1,2,0,
             3,3,1,1,1,1,0,1,2,3,0,3,0,3,3,3,2,3,0,3,
             2,0,3,0,0,2,3,2,2,1,0,2,2,3,1,2,2,3,2,2,
             1,2,2,1,3,1,3,1,2,0,1,3,1,1,2,3,3,2,2,2,
             1,2,2,1,3,3,0,1,3,1,0,0,1,1,0,0,1,2,0,2,
             1,1]
# print(len(correct_ans))


