import streamlit as st

D={
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

d={
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}

def decoder(text,key):
    lower_text=text.lower()
    s=""
    k=0
    for i in range(0,len(text)):
        x=lower_text[i]
        if x==" ":
            s=s+x
        else:   
            x=D[lower_text[i]] 
            diff=x-int(key[k%len(key)])
            if diff<=0:
                diff=diff+26
            y=d[diff]  
            s=s+y
            k=k+1
    return s


st.header("**TIME CAPSULE**")
col1,col2=st.columns(2)
with col1:
    text=st.text_input(label="Enter your secret message:",placeholder="Type here")

with col2:
    key=st.text_input(label="Enter correct date:",placeholder="DDMMYYYY")    
button=st.button("Submit")
if button:
    ans=decoder(text,key)
    st.write(ans)


    