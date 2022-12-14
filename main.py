#Brian Lazarre
#This program finds the root note of a chord, simple or complext. This would be useful for a bass player and other mucisians. It will also display what string and fret.
def print_message():
   print("Bass Players! Input the chord name that the piano and/or the guitar player is playing to generate the root note in c major scale. Also it will generate the string and fret number for a standard tuned 4 string bass!")
print_message()
key_name=input("Enter key")
chord_name=input("Enter chord name")
if(chord_name==" C major"):
    Root_note_is_C= "Root note" +" "+"is C"
    Position_1_C=(2*1)
    Position_2_C=(3//1)
    print(Root_note_is_C)
    print("String #", Position_1_C)
    print("Fret #", Position_2_C)
if(chord_name==" D minor"):
    Position_1_D=(2**1)
    Position_2_D=(4+1)
    print("Root note is D")
    print("String #", Position_1_D)
    print("Fret #", Position_2_D)
if(chord_name==" E minor"):
    root_note="Root note is E"*1
    Position_1_E=(4-2)
    Position_2_E=(14/2)
    print(root_note)
    print("String #", Position_1_E)
    print("Fret #", Position_2_E)
if(chord_name==" F major"):
    Position_1_F=(4-1)
    Position_2_F=(3%9)
    print("Root note is F")
    print("String #", Position_1_F)
    print("Fret #", Position_2_F)
if(chord_name==" G major"):
    Position_1_G=(4-1)
    Position_2_G=(5*1)
    Root_note_is_G="Root note" +" "+"is G"
    print(Root_note_is_G)
    print("String #", Position_1_G)
    print("Fret #", Position_2_G)
if(chord_name==" A minor"):
    Position_1_A=(2+1)
    Position_2_A=(2+5)
    print("Root note", end =' ')
    print("is A")
    print("String #", Position_1_A)
    print("Fret #", Position_2_A)
if(chord_name==" B diminished"):
    Position_1_B=(5-1)
    Position_2_B=(4//2)
    print("Root note is B")
    print("String #", Position_1_B)
    print("Fret #", Position_2_B, sep='')
chord_name_2=input("Enter chord name")
###### This is the Key of D major########
if(key_name==" D"):
    chord_name_2=input("Enter chord name")
if(chord_name_2==" D major"):
    print("Root note is D")
    Position_1_Dmaj=2
    while Position_1_Dmaj<10:
        print("String #", Position_1_Dmaj)
        break
    Position_2_Dmaj= [str(5)]
    for fretdmaj in Position_2_Dmaj:
        print("Fret #", fretdmaj)
