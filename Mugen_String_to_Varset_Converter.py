import time

null_header = "[State STRING Table | {} |] \ntype = null \ntriggerall = !fvar(0)\n"
set_form = "trigger1 = 1 || var({}) := {} ; {} \n"
footer = "persistent = 0"

#Used to index special characters
#         ,  .SPACE !    ?
remap1 =[-2,-4,-16,-15, -17]
remap2 =[39,38,-1, 36, 37]

###CHANGE THIS STRING TO GENERATE NEW VARSET TABLES#####
input_string = "HELLO WORLD!"

#Ensure input is upper case
input_string = input_string.upper()

def output_varsets(in_string):
    out = ""
    index = 0
    out += null_header.format(input_string)
    for c in in_string:
        val = ord(c) - 48
        if val >= 10 and val <= 16:
            val = -val-2
        if val >= 17:
            val = val-7
    #Remap Special characters
        for x in range(0, len(remap1), 1):
            if val == remap1[x]:
                val = remap2[x]
        print(c, val, index)
        out += set_form.format(index,val,c)
        index += 1
    #End of String
    out += set_form.format(index,-2,"End")
    out += footer
    print(out)
    time.sleep(7)

output_varsets(input_string)
