
# -*- coding: utf-8 -*-

global_var = 'global' # Inner can refer

class Outer:
    outer_var = 'outer' # Inner can't refer
    class Inner:
        nonlocal outer_var
        inner_var = 'inner' # Naturally Inner can refer 
        var = outer_var        # NameError: name 'Outer' is not defined
        var = Outer.outer_var  # NameError: name 'Outer' is not defined

if __name__ == '__main__':
    outer = Outer()