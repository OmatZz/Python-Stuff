text = "X-DSPAM-Confidence:    0.8475";
stext = text.strip()
find1 = stext.find(':')
number = stext[find1+1 : ]
snumber = number.strip()
fnum = float(snumber)
print(fnum)
