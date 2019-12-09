#!/usr/bin/env python3

from echostyle import EchoStyle


def confirm_or_deny(word_prompt,             # the instruction
                    valid_confirm="",        # response to valid yes
                    valid_deny="",           # response to valid no,
                    invalid_response="",     # cannot confirm either
                    question="\vY/N?",       # the question
                    invalid_terminates=True, # False is Retry
                    deny_terminates=True,    # or can just returns False
                    char_prompt="\n> "):
    
    green.print_prompt('\n' + word_prompt.lower())
    red.print('\t' + question.lower())
    blue.print_prompt(char_prompt.lower())
    inp = input("")
    
    if inp.startswith('y'):
        green.print(valid_confirm)
        return True
    
    elif inp.startswith('n'):
        red.print(valid_deny)
        if deny_terminates:
            terminating("\n\tNo means no afterall.", 1)
            return False
        
        else:
            red.print(invalid_response)
            
            if invalid_terminates:
                terminating("\n\tFailure to validate...\n", 2)
                
                else: # recursive option if False
                
                confirm_or_deny(word_prompt, question, valid_confirm, 
                                valid_deny, invalid_response, 
                                invalid_terminates, char_prompt)
                return
            
            

def terminating(error_message="", error_num=1):
    error_message = color_string(error_message, 'red')
    print(error_message + Fore.MAGENTA + "\nTerminating..." + Fore.RESET)
    sys.exit(error_num)
