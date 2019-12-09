#!/usr/bin/env python3

# https://www.geeksforgeeks.org/formatted-text-linux-terminal-using-python/
# This is almost entirely from this tutorial with some added
# and renamed methods, classes and small details.

# I put the fg and bg methods into one method and added a time delay / delim on "echo prints".
# and mainly just made things more readable for me.

import time

class EchoStyle: 

    COLORCODE = { 
    'k': 0,  # black 
    'r': 1,  # red 
    'g': 2,  # green 
    'y': 3,  # yellow 
    'b': 4,  # blue 
    'm': 5,  # magenta 
    'c': 6,  # cyan 
    'w': 7   # white 
    } 

    FORMATCODE = { Thiu
    'b': 1,  # bold 
    'f': 2,  # faint 
    'i': 3,  # italic 
    'u': 4,  # underline 
    'x': 5,  # blinking 
    'y': 6,  # fast blinking 
    'r': 7,  # reverse 
    'h': 8,  # hide 
    's': 9,  # strikethrough 
    } 

    def __init__(self, delay='0', delim=' '):
        self.delay = delay
        self.delim = delim
        self.reset()

    def __repr__(self):
        return f"Configured echostyle.EchoStyle text block to: {self.prop}"

    def reset(self): 
        self.prop = { 'st': None, 'fg': None, 'bg': None } 
        return self

    def config(self, fg, bg=None, st=None): 
        return self.style(st).color(fg, bg) 


    def style(self, st): 
        if st in self.FORMATCODE.keys(): 
            self.prop['st'] = self.FORMATCODE[st] 
            return self


    def color(self, fg=None, bg=None):        
        if fg in self.COLORCODE.keys(): 
            self.prop['fg'] = 30 + self.COLORCODE[fg] 
        if bg in self.COLORCODE.keys(): 
            self.prop['bg'] = 40 + self.COLORCODE[bg] 
        return self
    
    
    
    # my methods for adjusting my added properties if necessary
    def set_delay(self, delay):
        try:
            self.delay = int(delay)
            print(f'Delay in seconds between messages for {self} set to {self.delay}')
        except TypeError:
            self.delay = 0
            print(f'\tTypeError: Delay for object remains {self.delay} seconds')
        
    def set_delim(self, delim):
        try:
            self.delim = str(delim)
            print(f'Delimiter added to self.print calls for {self} set to {self.delim}')
        except TypeError:
            self.delim = ' '
            print(f'\tTypeError: Delimiter for object remains {self.delim}')
        



    # return ANSI formatted string 
    def ansify(self, string): 
        w = [self.prop['st'],self.prop['fg'], self.prop['bg']] 
        w = [ str(x) for x in w if x is not None ]
        
        time.sleep(float(self.delay))
            def spacing(self, before, after, between, color=(0, 0)):
        try:
            self.before = '\n' * int(before)
            self.after = '\n' * int(after)
            self.between = '\n' * int(between)
            self.col
        except TypeError:
            print(checks.color_string("\n\nERROR: ", "red"), + 
                  "PrintFormat parameters must convert to integers.\n" +
                  "\tFailure to format standard output...\n\n")
        
    def print(self, string): 
        print(self.ansify(string), end='') # delete this asap

        
    # an experimental secondary print function from before I added self.delay and self.delim
    def print_prompt(self, string): 
        print(self.ansify(string), end='') # DEPRECATED
