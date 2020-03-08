# Written By Matteo Vidali
# Instructions -
# This file is designed to go on the end of your assembler file and will run all of your functions 
# and test them for correctness.

# Copy the first block into the bottom of your file. it has some variables that are used later. 

# Each funciton test is seperate from the others, and are compleatly portable. You can put 
# The entire file at the end of your assembler.py file, and run it - if you do this, it will
# print all the errors/successes of your code.

# However, if you just want to test one of your cases, you can put just one case into your file.
# Each line of '-' characters split the function testers, you can just find the one you need!
# It is designed to be used in a step like process, so you can work on one function, get the tester,
# Test, debug, and then move on. You can stack them all on the end of your file and it should work!

# If anything goes wrong, or you have problems, or you just have suggestions on how to make this better,
# my email is mvidali@iu.edu.
# Feel free to email me with your questions or suggestions! I am looking for any constructive criticism!

# ----------------------------------------------------------------------------------------------------------------
#------------------------------TESTERS- INCLUDE THIS FIRST SEGMENT IN YOUR FILE NO MATTER WHAT--------------------
# ----------------------------------------------------------------------------------------------------------------

# This statment is just to say - "If we are running this code as an application, then run this. But if we are running
# this code as a library, (if it was included in another piece of code, then don't run it.

if __name__ == "__main__":

    # Setting a bunch of variables that will capture the success or failure of each of the functions so we can get
    # an overview later
    
    aTest = False
    cTest = False
    lTest = False
    gsTest = False
    gdTest = False
    gcTest = False
    gjTest = False
    cdTest = False
    ccTest = False
    cjTest = False
  
    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR is_a_instruction ------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Can copy just this to next line for just is_a_instruction test

    print("Testing is_a_instruction function:\n")
    a = is_a_instruction("@A")
    b = is_a_instruction("(LOOP)")
    c = is_a_instruction("@25")
    d = is_a_instruction("D=3")
    e = is_a_instruction("@3")

    if a and c and e and not b and not d:
        print("is_a_instruciton is correct!\n\n")
        aTest = True
    else:
        print("Something is wrong with your function\n\n")

    print("     @A - " + str(a) + " --> Should be True")
    print("     (LOOP) - " + str(b) + " --> Should be False")
    print("     @25 - " + str(c) + " --> Should be True")
    print("     D=3 - " + str(d) + " --> Should be False")
    print("     @3 - " + str(e) + " --> Should be True")
  
    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR is_c_instruction ------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for the is_c_instruction test

    # Test cases
    print("\n\nTesting is_c_instruction:\n")

    a = is_c_instruction("0:JMP")
    b = is_c_instruction("(LOOP)")
    c = is_c_instruction("@25")
    d = is_c_instruction("D=3")
    e = is_c_instruction("@3")

    if a and not b and not c and d and not e:
        print("is_c_instruction is correct!\n\n")
        cTest = True
    else:
        print("Something is wrong with your function\n\n")

    print("     0:JMP - " + str(a) + " --> Should be True")
    print("     (LOOP) - " + str(b) + " --> Should be False")
    print("     @25 - " + str(c) + " --> Should be False")
    print("     D=3 - " + str(d) + " --> Should be True")
    print("     @3 - " + str(e) + " --> Should be False")
  
    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR is_label --------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Just copy this for testing is_label
    
    print("\n\nTesting is_label:\n")

    a = is_label("0:JMP")
    b = is_label("(LOOP)")
    c = is_label("@25")
    d = is_label("D=3")
    e = is_label("(SCREEN)")

    if not a and b and not c and not d and e:
        print("is_label is correct!\n\n")
        lTest = True
    else:
        print("Something is wrong with your function\n\n")

    print("     0:JMP - " + str(a) + " --> Should be False")
    print("     (LOOP) - " + str(b) + " --> Should be True")
    print("     @25 - " + str(c) + " --> Should be False")
    print("     D=3 - " + str(d) + " --> Should be False")
    print("     (SCREEN) - " + str(e) + " --> Should be True")

    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR get_symbol ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for testing get_symbol

    print("\n\nTesting get_symbol:\n")

    a = get_symbol("@SIGN")
    b = get_symbol("(LOOP)")
    c = get_symbol("@25")
    d = get_symbol("(START)")
    e = get_symbol("D=5")

    if a == "SIGN" and b == "LOOP" and c == "25" and d == "START" and not e:
        print("get_symbol is correct!\n\n")
        gsTest = True

    else:
        print("Something is wrong with your function\n\n")

    print("     @SIGN - " + str(a) + " --> Should be 'SIGN'")
    print("     (LOOP) - " + str(b) + " --> Should be 'LOOP'")
    print("     @25 - " + str(c) + " --> Should be '25'")
    print("     (START) - " + str(d) + " --> Should be 'START'")
    print("     D=5 - " + str(e) + " --> Should be False")
    
    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR get_dest --------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for get_dest
    
    print("\nTesting get_dest:\n")

    a = get_dest("0;JMP")
    b = get_dest("D=MA")
    c = get_dest("@25")
    d = get_dest("MD=A")
    e = get_dest("D;JGT")

    if a == "NULL" and b == "D" and not c and d == "MD" and e == "NULL":
        print("get_dest is correct!\n\n")
        gdTest = True

    else:
        print("Something is wrong with your function\n\n")

    print("     0;JMP - " + a + " --> Should be 'NULL'")
    print("     D=MA - " + b + " --> Should be 'D'")
    print("     @25 - " + str(c) + " --> Should be False")
    print("     MD=A - " + d + " --> Should be 'MD'")
    print("     D;JGT - " + e + " --> Should be 'NULL'")
    
    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR get_comp --------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for get_comp

    print("\n\nTesting get_comp:\n")
    a = get_comp("0;JMP")
    b = get_comp("D=D+1")
    c = get_comp("@25")
    d = get_comp("MD=A")
    e = get_comp("D;JGT")

    if a == "0" and b == "D+1" and not c and d == "A" and e == "D":
        print("get_comp is correct!\n\n")
        gcTest = True

    else:
        print("Something is wrong with your function\n\n")

    print("     0;JMP - " + a + " --> Should be '0'")
    print("     D=D+1 - " + b + " --> Should be 'D+1'")
    print("     @25 - " + str(c) + " --> Should be False")
    print("     MD=A - " + d + " --> Should be 'A'")
    print("     D;JGT - " + e + " --> Should be 'D'")
  
    # ----------------------------------------------------------------------------------------------------------------
    # TESTER FOR get_jmp ---------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for get_jmp

    print("\n\nTesting tet_jmp:\n")
    a = get_jump("0;JMP")
    b = get_jump("D;JGT")
    c = get_jump("M;JLT")
    d = get_jump("MD=A")
    e = get_jump("D;JNE")

    if a == "JMP" and b == "JGT" and c == "JLT" and d == 'NULL' and e == "JNE":
        print("get_jmp is correct!\n\n")
        gjTest = True

    else:
        print("Something is wrong with your function\n\n")

    print("     0:JMP - " + a + " --> Should be 'JMP'")
    print("     D;JGT - " + b + " --> Should be 'JGT'")
    print("     M;JLT - " + c + " --> Should be 'JLT'")
    print("     MD=A - " + d + " --> Should be 'NULL'")
    print("     D;JNE - " + e + " --> Should be 'JNE'")
    
    # ----------------------------------------------------------------------------------------------------------------
    # RIGOROUS TESTER FOR convert_dest -------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for convert_dest
    
    print("\n\nTesting convert_dest:\n")
    a = convert_dest("NULL")
    b = convert_dest("M")
    c = convert_dest("D")
    d = convert_dest("MD")
    e = convert_dest("A")
    f = convert_dest("AM")
    g = convert_dest("AD")
    h = convert_dest("AMD")

    if (a == '000' and b == '001' and c == '010' and d == '011' and e == '100'
            and f == '101' and g == '110' and h == '111'):
        print("convert_dest is 100% successful:\n")
        cdTest = True
    else:
        print("There seems to be a problem with your function:\n")

    print("     NULL -- " + a + " --> Should be '000'")
    print("     M -- " + b + " --> Should be '001'")
    print("     D -- " + c + " --> Should be '010'")
    print("     MD -- " + d + " --> Should be '011'")
    print("     A -- " + e + " --> Should be '100'")
    print("     AM -- " + f + " --> Should be '101'")
    print("     AD -- " + g + " --> Should be '110'")
    print("     AMD -- " + h + " --> Should be '111'")

    # ----------------------------------------------------------------------------------------------------------------
    # RIGOROUS TESTER FOR convert_comp -------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for convert_comp
    
    print("\n\nTesting convert_comp:\n")
    a = [('0', convert_comp("0")), ('1', convert_comp("1")), ('-1', convert_comp("-1")), ('D', convert_comp("D")),
         ('A', convert_comp("A")), ('!D', convert_comp("!D")), ('!A', convert_comp("!A")), ('-D', convert_comp("-D")),
         ('-A', convert_comp("-A")), ('D+1', convert_comp("D+1")), ('A+1', convert_comp("A+1")),
         ('D-1', convert_comp("D-1")), ('A-1', convert_comp("A-1")), ('D+A', convert_comp("D+A")),
         ('D-A', convert_comp("D-A")),('A-D', convert_comp("A-D")),('D&A', convert_comp("D&A")),
         ('D|A', convert_comp("D|A")),('M', convert_comp("M")),('!M', convert_comp("!M")),('-M', convert_comp("-M")),
         ('M+1', convert_comp("M+1")),('M-1', convert_comp("M-1")),('D+M', convert_comp("D+M")),
         ('D-M', convert_comp("D-M")),('M-D', convert_comp("M-D")), ('D&M', convert_comp("D&M")),
         ('D|M', convert_comp("D|M"))]


    comp_COMPARE = {
        "0": '0101010',
        "1": '0111111',
        "-1": '0111010',
        "D": '0001100',
        "A": '0110000',
        "!D": '0001101',
        "!A": '0110001',
        "-D": '0001111',
        "-A": '0110011',
        "D+1": '0011111',
        "A+1": '0110111',
        "D-1": '0001110',
        "A-1": '0110010',
        "D+A": '0000010',
        "D-A": '0010011',
        "A-D": '0000111',
        "D&A": '0000000',
        "D|A": '0010101',
        "M": '1110000',
        "!M": '1110001',
        "-M": '1110011',
        "M+1": '1110111',
        "M-1": '1110010',
        "D+M": '1000010',
        "D-M": '1010011',
        "M-D": '1000111',
        "D&M": '1000000',
        "D|M": '1010101'
    }
    for element in a:
        b = comp_COMPARE.get(element[0])
        if b == element[1]:
            print("     Successful: " + element[0] + " - Becomes - " + element[1])
            ccTest = True
        else:
            print("     Unsuccessful: " + element[0] + " - Became - " + element [1] + " - It should have been - " + b)
            ccTest = False
            break
            
    # ----------------------------------------------------------------------------------------------------------------
    # RIGOROUS TESTER FOR convert_jump -------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    
    # Copy just this for convert_jump
    
    print("\n\nTesting convert_jump:\n")
    a = convert_jump("NULL")
    b = convert_jump("JGT")
    c = convert_jump("JEQ")
    d = convert_jump("JGE")
    e = convert_jump("JLT")
    f = convert_jump("JNE")
    g = convert_jump("JLE")
    h = convert_jump("JMP")

    if (a == '000' and b == '001' and c == '010' and d == '011' and e == '100'
            and f == '101' and g == '110' and h == '111'):
        print("convert_jump is 100% successful:\n")
        cjTest = True
    else:
        print("There seems to be a problem with your function:\n")

    print("     NULL -- " + a + " --> Should be '000'")
    print("     JGT -- " + b + " --> Should be '001'")
    print("     JEQ -- " + c + " --> Should be '010'")
    print("     JGE -- " + d + " --> Should be '011'")
    print("     JLT -- " + e + " --> Should be '100'")
    print("     JNE -- " + f + " --> Should be '101'")
    print("     JLE -- " + g + " --> Should be '110'")
    print("     JMP -- " + h + " --> Should be '111'")

    # -------------------------------------------------------------------------------------------------------
    # Testing all correctness - CAN COPY THIS IN AT END. WILL GIVE COMPREHENSIVE OVERVIEW OF RESULTS---------
    
    if aTest and cTest and lTest and gsTest and gdTest and gcTest and gjTest and cdTest and ccTest and cjTest:
        print("\n\n\n\n All tests were successful! Congratulations YOU DID IT!")
    else:
        print("\n\n\n\n One or more of your functions is causing a problem...")
        print("\nAll should be true:")
        results = [('is_a_instruction: ', str(aTest)),('is_c_instruction: ', str(cTest)),('is_label: ', str(lTest)),
                   ('get_symbol: ', str(gsTest)),('get_dest: ', str(gdTest)),('get_comp: ', str(gcTest)),
                   ('get_jump: ', str(gjTest)),('convert_destination: ', str(cdTest)),('convert_comp: ', str(gcTest)),
                   ('convert_jump: ', str(cjTest))]
        for e in results:
            print(e[0] + e[1])

# ---------------------------------------------------------------------------------------------------------------------
