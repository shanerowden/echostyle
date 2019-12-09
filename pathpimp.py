#!/usr/bin/env python3

import calmsize, sys, string
from pathlib import Path
from echostyle import EchoStyle

    
    # COLORS
    green = EchoStyle();green.color('g')
    red = EchoStyle();red.color('r')
    blue = EchoStyle();blue.color('b')
    magenta = EchoStyle();magenta.color('m')
    
    
    def path_info(path):
        '''Use this to determine as much as you can about a file in one move.'''
        # boolean values any path has:
            stats = ['exists', 'dir', 'file']
            info = {key: False for key in stats}
            
            info['path'] = dict(name=path.name, absolute=path.resolve()) 
            
            if path.exists():
                info['exists'] = True
                print(f"{path} leads to an existing directory")
                
                if path.resolve().is_dir():
                    info['dir'] = True
                    print(f"{path} leads to an existing directory")
                    da
                    # creates sub dict of the files within a directory
                    info['contains'] = {'files': 
                                            [f for f in path.glob('*') if f.is_file()], 
                                            'dirs': 
                                                [f for f in path.glob('*')if f.is_dir()]}
                    
                    if path.resolve().is_file():
                        info['file'] = True
                        print(f"{path} leads to an existing file...")
                        
                        # file type
                        info['ext'] = path.suffix
                        
                        # accessed, modified, created timestamps
                        info['time'] = dict(a=path.stat()[7],
                                            m=path.stat()[8],
                                            c=path.stat()[9])
                        
                        info['size'] = path.stat()[6], calmsize.size(path.stat()[6])
                        
                        
                        else:
                            print(f"{path} doesn't even exist.")
                            
                            return info
