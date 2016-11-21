#!/usr/bin/env python2

from blessings import Terminal
import time
FRAME = 0.08


FRAMES = [
"""
                                                   
                                                   
                                                   
                                                   
                                                   
                     @/t@                          
                    @//t@  @@@                     
                    @/(t@ %GGGG@                   
                    @((tt@~GOOG@                   
                     @(tt@~OOOO@                   
                     @tt^@~GGOG@                   
                     @^^^@tt~G~@ @@@COOOOO@@       
                    @s/^^@%tt~t@@    O(///OO@      
                   @s   OOO((((OG     /////OOO@    
                  @s   OO(@@@(((G       //OO(OOO@  
                  @sG  O(@ @@(((G       ///O/OOO@  
                  @GGGGO(@@@(((OG        /(//Ot(O@ 
                  @GG   ((((((OGG        (///Ot((@(
                  @  G   ((((OGG        ((//tOt((@(
                   @ ~   GGGGG         (t/%ttt((^@@
                        @%%            ((((((%%%@  
                        @  %~         (((((%%%%%@  
                      @  t     @ @  ss%%%%%%%%@    
                        @@@@@@  @@@@@@@@@@@@@@@    
  """,
  """
                                                   
                                                   
                                                   
                                                   
                     @/t@                          
                    @//t@ @%GG@                    
                    @/(t@ %GGGG@                   
                    @((tt@~GOOG@                   
                     @tt^@~GOOG@                   
                     @tt^@~GGOG@                   
                     @^^^@tt~G~@                   
                    @s  t@C(ttOOG@@@COOOOO@@       
                   @s   OOO((((OG    O(///OO@      
                  @s   OO(@@@(((G     /////OOO@    
                  @GGGGO(@@@@(((G       //OO(OOO@  
                  @GGGGO(@@@(((OG       ///O/OOO@  
                  @GG   ((((((OGG        /(//Ot(O@ 
                   @OOO  O((OGG          (///Ot((@(
                   @ ~   GGGGG          ((//tOt((@(
                        @%%            (t/%ttt((^@^
                       @  %%    @      ((((((%%%@  
                      @  t     @@@    (((((%%%%%@  
                        @@@@@@   @  ss%%%%%%%%@    
                                 @@@@@@@@@@@@@@    
  """,
  """
                                                   
                                                   
                                                   
                      @@                           
                    @//t@  @@@                     
                    @/(t@ %GGGG@                   
                    @/(t@@%GGOG@                   
                     @(tt@~OOOO@                   
                     @tt^@~GGOG@                   
                     @t^^@t~GO~@                   
                    @s/^^@%tt~t@@   @@@@@@         
                   @s   OOO((((OG    O(///OO@      
                   @s   O(((((((G     ////OOO@     
                  @sG  O(@ @@(((G      ///OOOOO@   
                  @GGGGO(@@@(((OG       ///O/OOO@  
                  @GGGG((((((((OG        /OO/OOO@  
                  @  G   ((((OGG         ((//Ot((@@
                   @ ~   GGGGG          ((//tOt((@(
                    @@@@s%              (//%tt%(^@(
                        @  %~          (%%tt((((^@@
                       @ t@@  ^@@@@@@@@((((%((%%@  
                       @/@ @  @       @@(%%((((@   
                            @@     @@@ss%%%%%%%@   
                                   @@@@@@@@@@      
  """,
"""
                                                   
                                                   
                                                   
                                                   
            @/t@                                   
           @//t@ @%GG@                             
           @/(t@ %GGGG@                            
           @((tt@~GOOG@                            
            @tt^@~GOOG@      @@@@OOOO@             
            @tt^@~GGOG@    @COOOOOOOOO@            
            @^^^@tt~G~@  @    /////OOOOO@          
           @s  t@C(ttOOG       ///O/O/OOO@         
          @s   OOO((((OG        ///OO/OOO@         
         @s   OO(((((((G         //(//Ot((@@       
         @GGGGO(@@(((((G         (///tOt((@(@      
         @GGGGO(@(((((OG         (//%tt%(^@(@      
         @GG   ((((((OGG        (/ttt((((^@@       
          @OOO  O((OGG         (%%((%((%%@         
          @ ~   GGGGG       @  ((@%%(((%@          
                @%%      @       @%@@%%@@          
                @ %@   @           @%@%@@          
               @ t@@  @             @@  @          
               @@ @ /@                @@           
                                                   
  """,
  """
                                                   
                                                   
                                                   
                                                   
        ##                                         
      #OO(#  @@@                                   
      #OO(# @t  @                                  
      #O/(@@t  O @                                 
       #/((@^OOOO@       ###OOOOO#                 
       #((%@^ OO @     #~OOOOOOOOO#                
       #(%%@(^ O^@  @@    OOOOOOOOOO#              
      #^O%%@t((^(@#        OOOOOOOOOO#             
      #^  (@~/((OO          OOOOOOOOO#             
     #^   O///////           OO/OOO(//# @          
    @^   O/@ @@///           /OOO(O(//#/O@         
    @    O/@@@@///           /OOt((t/%#/%@         
    @    ////////O          /O(((////%#@           
    @      ////O      O  O@/tt//t//tt#             
     #OOO  O//O      O@@@@@@/%tt///t@              
      #@##^t        @         @@@tt%@              
          #  t^   @            @t@t%@              
         #  tt   @              @@  @              
         ##@   @                  @@               
                                                   
  """,
  """
                                                   
                                                   
                                                   
                                                   
                                                   
   @/t@                                            
  @//t@  @@@                                       
  @/(t@ %GGGG@                                     
  @((tt@~GOOG@                                     
   @(tt@~OOOO@                                     
   @tt^@~GGOG@                                     
   @^^^@tt~G~@ @@@COOOOO@@                         
  @s/^^@%tt~t@@    O(///OO@                        
 @s   OOO((((OG     /////OOO@                      
@s   OO(@@@(((G       //OO(OOO@                    
@sG  O(@@ @(((G       ///O/OOO@                    
@GGGGO(@@@(((OG        /(//Ot(O@                   
@GG   ((((((OGG        (///Ot((@/@                 
@  G   ((((OGG        ((//tOt((@/@                 
 @ ~   GGGGG         (t/%ttt((^@@                  
      @%%            ((((((%%%@                    
      @  %~         (((((%%%%%@                    
    @  t     @ @  ss%%%%%%%%@                      
      @@@@@@  @@@@@@@@@@@@@@@                      
  """
]

FRAMES_REV = ['\n'.join(line[::-1] for line in f.splitlines()) for f in FRAMES]

TURN_LR = [
"""
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
       @  @
     @Ott@((@
     @Ott@((@
     @Ott@(@
     @tt@(@
     @%t@(@    @@@COOOOO@@
    @@C(%@@@ @@O   O(///OO@
  @OO((((((OOOO     /////OOO@
 s (@@@(((((OOG       //OO(OOO@
@sO@ @@/((((OOG       ///O/OOO@
@GG@@@//(((OOOG        /(//Ot(O@
@GG((((((((OOGG        (///Ot((@/@
@   (((((OOOOG        ((//tOt((@/@
  @@   GGGGG         (t/%ttt((^@@
      @%%            ((((((%%%@
      @ @           (((((%%%%%@
    @ @t   @   @  ss%%%%%%%%@
      @@@@    @@@@@@@@@@@@@@@
""",
"""
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
          @O@@(@
         @Ott@((@
         @Ott@((@
         @tt@((@
         @tt@(@
         @%t@(@
       @ttttttt@@@COOOOO@@
       @tttttt@O  /O(O//OO@
      @((((tOOO    OO/O//OOO@
      @(((((OOG    //O//OO(OOO@
      @/((((OOG    ///O//O/OOO@
      @/(((OOOG   //////(//O(O@
        @((OOGG   /////(///O@(//@
         @OOOG    /////(///O((//@
          @G      t///t/%//^^((@
           @       ttttt((((^%@
          @%       //((((%%^^%@
          @@@  @  ss%%%%%%%%@
              @@@@@@@@@@@@@@@
""",
"""
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
               @O@   @O@
              @((O@ @O((@
              @((O@ @O((@
               @((@ @((@
               @((@ @((@
               @(t@ @t(@
             @@(OOOOOOOO##
            @(OOOOOO/OOOOO#
          @(OOOOOOOOOOOOOOOO#
         @//OO OOOOOOOOOOO/OOO#
         @//OOOOOOOOO/O#OOOOOO#
        @//OOOOOOOOOO@/OO@OOOO(@
        @(OOOOOOOOOO@O//O@OOOOO@
        @((OOOOOOOOOt%//@OOOO((@
         @t((OOO@@(Ottttt7@O((t@
           @tt(@77@t((((@77@%t#
            @@t@77@ttttt@tt@%@
               @77@     @77@                                             
                                                                         
""",
"""
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                          @/@@O@
                         @//@((O@
                         @//@((O@
                 ######@  @//@((@
               ##OOOOO~#@  @/@((@
             #OOOOOOOOO   @@/@(t@
           #OOOOOOOOOO     (((((((@
          #OOO/OOOOOOO     @((((((@
          #OOOOOOOOOOOO    OOO(////@
         @#@/OOO//OOOOO     OO/////@
        @OO/@OOOO/OOOOO     OO////O@
        @O//OOOtOOOOOO      OOO///O@
          #%%%/O(tt/O((      OO//@
          #t%////(((((       OOO@
           #tt///t////##       @
            #^t@@t^^@^@@@@@   @
            @@tt@@tt@@  # @@  t@
               @@@@ @@   @#  @@@
""",
"""
                                                                         
                                                                         
                                                                         
                                                                         
                                   @t/@
                             @GG%@ @t//@
                            @GGGG% @t(/@
                            @GOOG~@tt((@
                            @GOOG~@^tt@
                            @GOGG~@^tt@
                @@OOOOOC@@@ @~G~tt@^^^@
              @OOO////     GOOtt(C@t  s@
             @OOO/////     GO((((OOO   s@
           @OOO(OO//       G(((@@@(OO   s@
           @OOO/OO/        G(((@@@@(OGGGG@
          @O(tO//(/        GO(((@@@(OGGGG@
        @(@((tO///(        GGO((((((   GG@
        @(@^(%tt%//(         GGO((O  OOO@
         @@^((ttt%/t(         GGGGG   ~ @
           @%%%((((((            %%@
            @%%%%%%((((@@@@@    %%  @
             @%%%%%%%%ss  @ @     t  @
             @@@@@@@@@@@@@@@  @@@@@@
"""
]

TURN_RL = [
  """
                          @@
                         @t/@
                  @GG%@ @t//@
                 @GOGG%@@t(/@
                 @GOOG~@tt((@
                 @GOOG~@^tt@
                 @~OG~t@^^t@
                 @~G~tt@^^^@
          @@@@@ GOOtt(C@t  s@
       @OO///(  G(((((((O   s@
      @OOO////  G(((@@@(OO   s@
    @OOOOO///   G(((@@@@(OGGGG@
   @OOO/O///    GO((((((((GGGG@
  @ OOO/OO/     GGO((((((   GG@
 @@((tO//((       GGO((O  OOO@
@/@((tOt//(((          %s@@@@
@/@^(%tt%//((         %%@
  @^((((tt%%(((@@@   @% @
   @%%%%%(((((@(@  @  @  @
    @%%%%%%((( @@@ @  @@ @
     @sssssssss  @
  """,
  """
          @@
        @//t@  @@@
        @/(t@ %GGGG@
        @/(t@@%GGOG@
         @(tt@~OOOO@
         @tt^@~GGOG@OOOOO@@
         @t^^@t~GO~@/OOOOO@@
        @s/^^@%tt~t@@ OOOOOOO@
       @s   OOO((((OG  OOO(OOO@
       @s   O(((((((G  OOO(OOO @
      @sG  O(@ @@(((G  O(((Ot((@
      @GGGGO(@@@(((OG  ((((Ot((@
      @GGGG((((((((OG ((((((%(^@
      @  G   ((((O/G  ((((tt((^@
       @ ~   GGGGG    ((ttt%%%@
        @@@@s%        (ttt%%%@
            @///// /@t%%%%%%@
           @  @  @ /@@@  @%%@
           @  @  @ /@(@   @ @
           @@     @@
"""
]


t = Terminal()

while 1:
    tty_y = t.height
    tty_x = t.width

    sizef = len(FRAMES[0].splitlines()[1])

    times = (tty_x - 34 - 8 - 3) / 18 - 1
    
    for i in xrange(times, -1, -1):
        for f in FRAMES:
            print t.clear()
            print '\n'.join(map(lambda line: (' ' * 18 * i) + line, f.splitlines()))
            time.sleep(FRAME)

    for f in TURN_LR:
        print t.clear()
        print f
        time.sleep(FRAME)

    for i in xrange(0, times + 1):
        for f in FRAMES_REV:
            print t.clear()
            print '\n'.join(map(lambda line: (' ' * (18 * i + 8)) + line, f.splitlines()))
            time.sleep(FRAME)

    for f in TURN_RL:
        print t.clear()
        print '\n'.join(map(lambda line: (' ' * (18 * times + 8 + 17)) + line, f.splitlines()))
        time.sleep(FRAME)
