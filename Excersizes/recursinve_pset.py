def get_power_set(ss):
    p_set = [] 
    def _recur_power_set(s, e): 
        if len (s) ==0:
            p_set.append(e)
        else:
            for element in s:
                _recur_power_set(s[1:], e)
                z = list(e)
                z.append(element)   
                _recur_power_set(s[1:], z)
    
    _recur_power_set(ss, e= [])
    return p_set

print(get_power_set([1, 2]))


