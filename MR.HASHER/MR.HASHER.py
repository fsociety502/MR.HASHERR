# Importing required libraries
import colorama
import re
import os
import hashlib



# Main program function
def main():
    Theme = colorama.Fore.GREEN + '''  
                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||   
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||    
         !.......:!?|||||!!^^""'            ||||    
         !.........||||                     ||||    
         !.........||||  ##                 ||||    
         !.........||||    Fsociety School  ||||    
         !.........||||       MR.HASHER     ||||    
         !.........||||          V1.0       ||||    
         !.........||||                     ||||    
         `.........||||                    ,||||    
          .;.......||||               _.-!!|||||    
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'    
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....  
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.  
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.  
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.  
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.  
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.  
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'  
    `........::::::::::::::::;iof688888888888888888888b.     `  
      `......:::::::::;iof688888888888888888888888888888b.  
        `....:::;iof688888888888888888888888888888888899fT!  
          `..::!8888888888888888888888888888888899fT|!^"'    
            `' !!988888888888888888888888899fT|!^"'          
                `!!8888888888888888899fT|!^"'                
                  `!988888888899fT|!^"'                    
                    `!9899fT|!^"'                          
                      `!^"' '''

    Services = colorama.Fore.BLUE + '''
============================================================        
 |[1] Text To Hash        - Generate hash from input text  |
 |[2] Hash a file         - Create hash of a file          |
 |[3] Identify The hash   - Recognize hash types from input|
 |[4] Comparing Hashes    - Compare two hashes for match   |
 |[5] Crack Passwords     - Crack password hash            |
 |[6] About This Tool     - Information about the tool     |
============================================================
'''
    print(Theme)
    print(Services)
    User_Option = input(colorama.Fore.RED + "ENTER YOUR OPTION -> ").strip()
    # Service 1 : TEXT_TO_HASH
    def TEXT_TO_HASH():
        input_text = input("ENTER THE TEXT -> ")
        Available_Algorithms = '''
        ++++++++++++++
        [1] MD5
        [2] SHA-1
        [3] SHA-256
        [4] SHA-224
        [5] SHA-512
        [6] SHA-384
        [7] SHA3-224
        [8] SHA3-256
        [9] SHA3-384
        [10]SHA3-512
        ++++++++++++++
        '''
        print(colorama.Fore.YELLOW + Available_Algorithms)
        User_choice = input("ENTER A CHOICE -> ")
        print("OK, YOUR CHOICE IS :", User_choice)

        hash_functions = {
            "1": hashlib.md5,
            "2": hashlib.sha1,
            "3": hashlib.sha256,
            "4": hashlib.sha224,
            "5": hashlib.sha512,
            "6": hashlib.sha384,
            "7": hashlib.sha3_224,
            "8": hashlib.sha3_256,
            "9": hashlib.sha3_384,
            "10": hashlib.sha3_512
        }

        if User_choice in hash_functions:
            hash_func = hash_functions[User_choice]
            hashed_result = hash_func(input_text.encode()).hexdigest()
            print(colorama.Fore.YELLOW + "THE RESULT -> ", hashed_result)
        else:
            print(colorama.Fore.RED + "[ERROR] Invalid choice")
    # NEEDED FUNCTION
    def CHECK_FILE(PATH):
        if os.path.isfile(PATH):
            print(colorama.Fore.GREEN + "[OK] THE FILE EXISTS ")
            return True
        else:
            print(colorama.Fore.RED + "[ERROR] THE FILE DOESN'T EXIST!!")
            return False
            exit()
    # Service 2 : HASH_A_FILE
    def HASH_A_FILE():
        File_PATH = input("ENTER THE FILE PATH -> ")
        if CHECK_FILE(File_PATH):
            AvailableAlgorithms = colorama.Fore.YELLOW + '''
            ++++++++++++++
            [1] MD5
            [2] SHA-1
            [3] SHA-256
            [4] SHA-224
            [5] SHA-512
            [6] SHA-384
            [7] SHA3-224
            [8] SHA3-256
            [9] SHA3-384
            [10]SHA3-512
            ++++++++++++++
            '''
            print(AvailableAlgorithms)
            User_Choice = input("ENTER A CHOICE -> ")
            hash_functions = {
                "1": hashlib.md5,
                "2": hashlib.sha1,
                "3": hashlib.sha256,
                "4": hashlib.sha224,
                "5": hashlib.sha512,
                "6": hashlib.sha384,
                "7": hashlib.sha3_224,
                "8": hashlib.sha3_256,
                "9": hashlib.sha3_384,
                "10": hashlib.sha3_512
            }

            if User_Choice in hash_functions:
                with open(File_PATH, 'rb') as file:
                    hash_func = hash_functions[User_Choice]
                    hashed_result = hash_func(file.read()).hexdigest()
                    print(colorama.Fore.YELLOW + "THE RESULT IS -> ", hashed_result)
            else:
                print(colorama.Fore.RED + "[ERROR] Invalid choice")
    # NEEDED FUNCTION
    def IS_IT__HASH(input_string):
        if not re.match('^[0-9a-fA-F]+$', input_string):
            print(colorama.Fore.RED + "[ERROR] INVALID HASH FORMAT !! ")
        # Second Function to Check the hashes it's true or not "2 hashes "
    def is_valid_hash(hash_string):
        return bool(re.match('^[0-9a-fA-F]+$', hash_string))
    # Service 3 : IDENTIFY_THE_HASH
    def IDENTIFY_THE_HASH(Hash):
        Hash = Hash.strip()
        if len(Hash) == 32:
            return "THIS IS -> MD5"
        elif len(Hash) == 40:
            return "THIS IS -> SHA-1"
        elif len(Hash) == 64:
            return "THIS IS -> SHA-256 or SHA3-256"
        elif len(Hash) == 56:
            return "THIS IS -> SHA-224 or SHA3-224"
        elif len(Hash) == 96:
            return "THIS IS -> SHA-384 or SHA3-384"
        elif len(Hash) == 128:
            return "THIS IS -> SHA-512 or SHA3-512"
        else:
            return "UNKNOWN HASH TYPE"

    # Service 4 : COMPARING_HASHES
    def COMPARING_HASHES():
        hash1 = input("ENTER THE FIRST HASH -> ")
        if not is_valid_hash(hash1):
            print(colorama.Fore.RED + "[ERROR]THIS IS NOT A HASH FORMAT !!")
            exit()
        hash2 = input("ENTER THE SECOND HASH -> ")
        if not is_valid_hash(hash2):
            print(colorama.Fore.RED + "[ERROR]THIS IS NOT A HASH FORMAT !!")
            exit()
        if hash1 == hash2:
            print(colorama.Fore.GREEN + "[OK] THE HASHES ARE THE SAME.")
        else:
            print(colorama.Fore.RED  + "[!] THE HASHES ARE DIFFERENT.")

    # Service 5 : CRACK_PASSWORD_HASHES
    def CRACK_PASSWORD_HASHES():
        Password_Hash = input("ENTER THE PASSWORD HASH YOU WANT TO CRACK -> ")
        if not is_valid_hash(Password_Hash):
            print(colorama.Fore.RED + "THIS IS NO A HASH FORMAT !!")
            return
        while is_valid_hash(Password_Hash):
            ht = IDENTIFY_THE_HASH(Password_Hash)
            print(ht)
            Wordlist = input("ENTER THE WORDLIST PATH -> ")
            CHECK_FILE(Wordlist)
            def md5_hash():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.md5(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)

            def Sha1_hash():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha1(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)

            def Sha224_hash():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha224(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ", Password_Hash, " : ",
                                  colorama.Fore.YELLOW + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)

            def Sha256_hash():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha256(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)
            def Sha512_hash():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha512(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)
            def Sha384_hash():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha3_384(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)
            def Sha3_224():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha3_224(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)
            def Sha3_256():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha3_256(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE +word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)
            def Sha3_384():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha3_384(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)
            def Sha3_512():
                with open(Wordlist, 'r') as file:
                    for word in file:
                        word = word.strip()
                        Hashed_Line = hashlib.sha3_512(word.encode()).hexdigest()
                        if Password_Hash == Hashed_Line:
                            print(colorama.Fore.GREEN + "THE PASSWORD IS -> ",Password_Hash," : ",colorama.Fore.BLUE + word)
                            exit()
                        else:
                            print(colorama.Fore.YELLOW + "NOT THIS -> ", word)

            if "THIS IS -> MD5" in ht:
                md5_hash()
            elif "THIS IS -> SHA-1" in ht:
                Sha1_hash()
            elif "SHA-256" in ht:
                Sha256_hash()
            elif "SHA3-256" in ht:
                Sha3_256()
            elif "SHA-224" in ht:
                Sha224_hash()
            elif "SHA3-224" in ht:
                Sha3_224()
            elif "SHA-384" in ht:
                Sha384_hash()
            elif "SHA3-384" in ht:
                Sha3_384()
            elif "SHA-512" in ht:
                Sha512_hash()
            elif "SHA3-512" in ht:
                Sha3_512()
    def About_THIS_Tool():
        description = '''
███████╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗    ███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗         
██╔════╝██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝    ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║         
█████╗  ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝     ███████╗██║     ███████║██║   ██║██║   ██║██║         
██╔══╝  ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝      ╚════██║██║     ██╔══██║██║   ██║██║   ██║██║         
██║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║       ███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗    
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝  

MR.HASHER V1.0 Created by FsocietySchool to help the people can work with hashes in simple mode
This tool can Provide These Services in V1.0 
------>> 
Generate Hashes from Text or Files:
Create secure hashes from plain text input or files using various cryptographic
algorithms such as MD5, SHA-1, SHA-256, and others. This helps ensure the integrity
of your data by creating unique digital signatures.
===============================================================================================
Identify Hash Types:
Easily identify the type of hash you are working with. Whether it's an MD5, SHA-1, or another
algorithm, this tool can recognize common hash formats and provide you with details on 
what kind of hash you're dealing with.
===============================================================================================
Compare Hashes to See if They Match:
Compare two hashes to determine if they match. This can be useful for validating the integrity 
of files or ensuring that a piece of data has not been tampered with. Simply input the two 
hashes, and the tool will tell you if they are identical or not.
===============================================================================================
Crack Password Hashes Using Wordlists:
Attempt to crack hashed passwords by comparing the hash with commonly used passwords in a
wordlist. The tool supports various hashing algorithms and allows you to provide a custom
wordlist to test for potential matches.
'''
        print(colorama.Fore.GREEN + description)
    # MAIN MENU
    if User_Option == "1":
        TEXT_TO_HASH()
    elif User_Option == "2":
        HASH_A_FILE()
    elif User_Option == "3":
        Hash_Value = input("ENTER THE HASH -> ")
        if not is_valid_hash(Hash_Value):
            print(colorama.Fore.RED + "[ERROR] THIS IS NOT A HASH FORMAT !! ")
        else:
            IDENTIFY_THE_HASH(Hash_Value)
    elif User_Option == "4":
        COMPARING_HASHES()
    elif User_Option == "5":
        CRACK_PASSWORD_HASHES()
    elif User_Option == "6":
        About_THIS_Tool()

# Execute main
if __name__ == "__main__":
    main()
