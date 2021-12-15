from collections import Counter
def init_even_fast():
    s1 = set(range(0, 10))
    ret = []
    evens = []
    _1 = []
    _2 = []
    _3 = []
    _4 = []
    for i in s1:
        if i == 0: continue
        _1+=(i,)
        s2 = s1.copy()
        s2.remove(i)
        for j in s2:
            _2+=(j,)
            s3 = s2.copy()
            s3.remove(j)
            for k in s3:
                _3+=(k,)
                s4 = s3.copy()
                s4.remove(k)
                for l in s4:
                    ret.append((i, j, k, l))
                    if l%2 == 0: evens.append((i, j, k, l))
                    _4+=(l,)
    fir = Counter(_1).most_common()
    sec = Counter(_2).most_common()
    thr = Counter(_3).most_common()
    last = Counter(_4).most_common()
    return ret,evens,fir,sec,thr,last
all,evens,fir,sec,thr,last=init_even_fast()
nums_e = len(evens)
nums_a = len(all)
pers = nums_e/nums_a
print(f"""
    All Possibilities with Non-duplication:{all}
    
    
    -------------------------------------
    All Evens in above result: {evens}
    
    
    -------------------------------------
    Evens/All = {nums_e}/{nums_a} ≈ {pers}
    -------------------------------------
    Syntax: (Number,Times)
    
    First Digit: {fir}
    Second Digit: {sec}
    Third Digit: {thr}
    Last Digit: {last}

    Python solution for XXXX_Analysis.
"""
)