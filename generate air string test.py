import time

set_form = ";TEXT STRING: {}\n[Begin Action {}]\n{},{},0,0,10\n"

def generate_anims():
    base_animno = 29846
    num_of_chars = 40
    out = ""
    for anim in range(base_animno,base_animno+num_of_chars,1):
        out += set_form.format(anim,anim,base_animno,anim-base_animno)
    print(out)
    time.sleep(7)

generate_anims()
