text = "X-DSPAM-Confidence:    0.8475";

find1 = text.find(':')
number = text[find1+1 : ]
snumber = number.strip()
fnum = float(snumber)
print(fnum)
