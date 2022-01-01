#This program is intended to solve the NYT Spelling Bee.

print("This program is intended to solve the NYT Spelling Bee.");
cenLet=input("Enter the Center Letter: "); #cenLet = Center Letter
perLet1=input("Enter the 1st Permieter Letter: "); #perLet = PerimeterLetter
perLet2=input("Enter the 2nd Permieter Letter: "); #perLet = PerimeterLetter
perLet3=input("Enter the 3rd Permieter Letter: "); #perLet = PerimeterLetter
perLet4=input("Enter the 4th Permieter Letter: "); #perLet = PerimeterLetter
perLet5=input("Enter the 5th Permieter Letter: "); #perLet = PerimeterLetter
perLet6=input("Enter the 6th Permieter Letter: "); #perLet = PerimeterLetter
perLets=perLet1+perLet2+perLet3+perLet4+perLet5+perLet6;

#cenLet="c"; # for Autmomatic input.
#perLets="noamry"; #for Automatic input.

cenLet=cenLet.lower();

perLets=perLets.lower();


#print("Input Letters: ",cenLet, perLet1, perLet2, perLet3, perLet4, perLet5, perLet6);
print("Center Letter: ",cenLet);
print("Perimeter Letters: ",perLets);
#print(len(perLets));

letFreq = "EARIOTNSLCUDPMHGBFYWKVXZJQ"; #This is a list containing the Roman Alphabet in order of letter frequency in the Oxford English Dictonary (OED) from: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
letFreq = letFreq.lower();
#print(len(letFreq));

#This will reorganize perLets in order of frequency in the OED.
orgPerLets="";
for a in letFreq:
    #print ("Chcecking Postition ",a," in Letter Frequency");
    for b in perLets:
        #print ("Chcecking Postition ",b," in Permimeter Letters");
        if a==b:
            #print ("Match Found");
            orgPerLets+=a;
print("Organized Perimeter Letters: ",orgPerLets);




#This is intended to loop through the dictionaries and clean them of short words and words with spaces, and append them into a new dictionary.
def dictBuilder(source):
    dict=open("dictionary.txt", "a"); # This will hold the newly generated dictionary. It uses 'append' mode.
    source=open(source, "r"); # This opens the source file. It uses 'read' mode.
    sourceLines=source.readlines();
    source.close();
    prevWord="xxxPreviousWordxxx";
    for a in sourceLines:
        invalidChars=False;
        #print(len(a));
        if len(a)>5: # Filter out short words.
            if "-" in a:
                invalidChars=True;
            if "\'" in a:
                invalidChars=True;            
            if invalidChars==False:
                if a != prevWord: #Need to fix this.
                    dict.writelines(a);
                    prevWord=a;
    dict.close();


#This builds the dictionary.
dictBuilder("Aword.txt");
dictBuilder("Bword.txt");
dictBuilder("Cword.txt");
dictBuilder("Dword.txt");
dictBuilder("Eword.txt");
dictBuilder("Fword.txt");
dictBuilder("Gword.txt");
dictBuilder("Hword.txt");
dictBuilder("Iword.txt");
dictBuilder("Jword.txt");
dictBuilder("Kword.txt");
dictBuilder("Lword.txt");
dictBuilder("Mword.txt");
dictBuilder("Nword.txt");
dictBuilder("Oword.txt");
dictBuilder("Pword.txt");
dictBuilder("Qword.txt");
dictBuilder("Rword.txt");
dictBuilder("Sword.txt");
dictBuilder("Tword.txt");
dictBuilder("Uword.txt");
dictBuilder("Vword.txt");
dictBuilder("Wword.txt");
dictBuilder("Xword.txt");
dictBuilder("Yword.txt");
dictBuilder("Zword.txt");


#This opens and reorganizes the dictionary by length
dict=open("dictionary.txt", "r");
dictLines=dict.readlines();
dict.close();

sortedDictLines=sorted(dictLines, key=len);

dictReorg=open("dictionaryReorganized.txt", "w");
dictReorg.writelines(sortedDictLines);
dictReorg.close();

#This searches the reorganized dictionary for matches.
dictReorg=open("dictionaryReorganized.txt", "r");
dictReorgLines=dictReorg.readlines();
dictReorg.close();

#Selects Solutions containing the cenLet
hasCenLet=open("hasCenLet.txt", "w+");
for a in dictReorgLines:
    if cenLet in a: #Excludes words that lack the center letter
        hasCenLet.writelines(a);
hasCenLet.close();

hasCenLet=open("hasCenLet.txt", "r");
#hasCenLet=open("test.txt", "r");
hasCenLetLines=hasCenLet.readlines(); #Pulls up ~15K responses.
hasCenLet.close();


#Final Solution - the fucking spaces are causeing problems......
solutions=open("solutions.txt","w");
orgPerLets=cenLet+orgPerLets;
print(orgPerLets);

for a in hasCenLetLines:
    invalidLetterInWord=False;
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    #print("RESET: invalidLetterInWord=",invalidLetterInWord);
    #print("Valid Letters=",orgPerLets);
    #print("Word=",a); # Successfully printing...
    for b in a:
        if b.isspace():
            continue;
        #print("Letter=",b); # Successfully printing...
        #print("Is ",b," in ",orgPerLets,"?:", b in orgPerLets);
        if b not in orgPerLets:
            #print("Invalid Letter Detected: ",b);
            invalidLetterInWord=True;
            #print("invalidLetterinWord=",invalidLetterInWord);
            #print("break");
            break;
    if invalidLetterInWord==False: #This never fires...?
        #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!All Letters Valid: Saved!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        solutions.writelines(a);

solutions.close();

print("Program Complete");
                 





                
                
                        
                    
        

