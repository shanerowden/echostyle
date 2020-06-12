# echostyle

Pretty much the basis of this lib is: All the scripts within it use echostyle.EchoStyle objects to make their terminal interface prettier and prepared out of the box. 

Or they are random things that kinda sort of go with that.

+ **echostyle.py** -- simplifies getting strings wrapped in ANSI codes for coloring of the foreground, background, and style. 
+ **dialecterm.py**  -- a variety of functions involving interface with the user in the terminal in regard to expecting input and formatting output, sometimes with options; a dialectic at the console.
+ **pathpimp.py** -- simple function dumps every bit of data I can think of from the system about a given path's file into a dict.


## EchoStyle objects

These are based in this:

```
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
    
    FORMATCODE = { 
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
```

The color method take either `bg` or `fg` key arguments in place of positional arguments if you only wish to color one or the other. Both default to nothing changed if nothing entered.

```
green = EchoStyle()
green.color('g', 'k') # Green Fore, Black Back
green.style('u') # underline
```

You could also do

```
green.set_delay(2) # uses time.sleep(2) between outputs in this style
green.set_delim('\n\n\n') # several lines between lines using this style
```


and if you need to reset the object for some reason: `green.reset()`

The `ansify()` method puts it all together with magic. You don't need to touch this. :P

When you want to use the EchoStyle...

```
green.print("The object has its own print method.")
```

Regular prints will not be effected.

## "Socratic dialogue at the terminal" -- or something

Eh. It's basically just two methods right now. A `terminating()` display function and this very intense `confirm_or_deny(prompt)`

```
def confirm_or_deny(word_prompt,             # the instruction
                    valid_confirm="",        # response to valid yes
                    valid_deny="",           # response to valid no,
                    invalid_response="",     # cannot confirm either
                    question="\vY/N?",       # the question
                    invalid_terminates=True, # False is Retry
                    deny_terminates=True,    # or can just returns False
                    char_prompt="\n> "):
```

Many of these parameters are not necessary but add some functionality. Play with it. Wait for me to make more terminal interfacing to add to this... :P


## What type of data does pathpimp get?

Does it exist? Is it a file? is a dir? What size is the file? Accessed, modified, created times. If directory, list child  directories in files as lists. I think that's it. If you think of anything let me know.
