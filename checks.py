from pathlib import Path
from colorama import Fore, Back
import calmsize, sys, string



def path_exists(path):
    
    path.resolve()
    if path.exists():
        return True
    else:
        return False
    
def path_info(path):
    
    stats = ['exists', 'dir', 'file']
    
    info = {key: False for key in stats}
    
    info['path'] = dict(name=path.name, absolute=path.resolve()) 
    
    if path_exists(path):
        info['exists'] = True
        
        if path.resolve().is_dir():
            info['dir'] = True
            print(f"{path} leads to an existing directory")
            
            info['contains'] = {'files': 
                    [f for f in path.glob('*') if f.is_file()], 
                        'dirs': 
                    [f for f in path.glob('*')if f.is_dir()]}
            
        if path.resolve().is_file():
            info['file'] = True
            print(f"{path} leads to an existing file...")
            
            info['ext'] = path.suffix
            
        info['time'] = dict(a=path.stat()[7],
                            m=path.stat()[8],
                            c=path.stat()[9])
        
        
        
        info['size'] = path.stat()[6], calmsize.size(path.stat()[6])
        
        
    else:
        print(f"{path} doesn't even exist.")
    
    return info

def confirm_or_deny(word_prompt,             # the instruction
                    valid_confirm="",        # response to valid yes
                    valid_deny="",           # response to valid no,
                    invalid_response="",     # cannot confirm either
                    question="\vY/N?",       # the question
                    invalid_terminates=True, # False is Retry
                    deny_terminates=True,    # or can just returns False
                    char_prompt="\n> "):
    
    valid_confirm = color_string(valid_confirm, 'green')
    word_prompt = color_string(word_prompt, 'green')
    question = color_string(question, 'red')
    valid_deny = color_string(valid_deny, 'red')
    invalid_response = color_string(invalid_response, 'red')
    char_prompt = color_string(char_prompt, 'blue')
   
    inp = input("\n" + word_prompt + question \
                + char_prompt).lower()
    
    if inp.startswith('y'):
        print(valid_confirm)
        return True
    
    elif inp.startswith('n'):
        print(valid_deny)
        if deny_terminates:
            terminating("\n\tNo means no afterall.", 1)
        return False
    
    else:
        print(invalid_response)
        
        if invalid_terminates:
            terminating("\n\tFailure to validate...\n", 2)
            
        else: # recursive option if False
            
            confirm_or_deny(word_prompt, question, valid_confirm, 
                            valid_deny, invalid_response, 
                            invalid_terminates, char_prompt)
            
def terminating(error_message="", error_num=1):
    error_message = color_string(error_message, 'red')
    print(error_message + Fore.MAGENTA + "\nTerminating..." + Fore.RESET)
    sys.exit(error_num)
    

def color_string(string, color):
    colors = {'black': Fore.BLACK + Back.WHITE,
          'blue': Fore.BLUE,
          'cyan': Fore.CYAN,
          'magenta': Fore.MAGENTA,
          'red': Fore.RED,
          'white': Fore.WHITE + Back.BLACK,
          'yellow': Fore.YELLOW,
          'green': Fore.GREEN,
          'reset': Fore.RESET}
    
    effect = colors[color]
    
    try:
        return effect + string + colors['reset']
    except ValueError:
        return string
    
    
    
