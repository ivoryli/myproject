from phase2.Data.day02.sstack import *

text =  "a{sd([fa])s}df"

parens = "()[]{}"

left_parens = "([{"
opposite = {")":"(",']':'[','}':"{"}

def parent(s):
    i,text_len = 0,len(text)
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        else:
            yield text[i],i
            i += 1

st = SStack()
for pr,i in parent(text):
    if pr in left_parens:
        st.push((pr,i))
    elif st.is_empty() or st.pop()[0] != opposite[pr]:
        print("Unmatching is found at %d for %s"%(i,pr))
        break
else:
    if st.is_empty():
        print("All parentheres are matched")
    else:
        e = st.pop()
        print("Unmatching is found at %d for %s" % (e[1], e[0]))