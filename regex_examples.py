
import re

alfabe = "Aa, Bb, Cc, Çç, Dd, Ee, Əə, Ff, Gg, Ğğ, Hh, Xx, Iı, İi, Jj, Kk, Qq, Ll, Mm, Nn, Oo, Öö, Pp, Rr, Ss, Şş, Tt, Uu, Üü, Vv, Yy, Zz "
alfabe = alfabe.replace(", ", "").strip()
print(alfabe)

#

# RE.MATCH: match a pattern with a given text
# RE.SPLIT: split by a criteria
# RE.REPLACE: replace by a pattern

my_text = "Kərtənkələ           bunları deyib! qulağını,daşdakı yarığa dayadı.   "
print(my_text.split(" "))

# REPLACE!!
my_text = re.sub("\s+", " ", my_text)


splitted = re.split("[^a-zA-ZÇçƏəĞğıİÖöŞşÜü]", my_text)
splitted = [s for s in splitted if len(s) > 0]
print(splitted)

"""
splitted = re.split("([^a-zA-ZÇçƏəĞğıİÖöŞşÜü])", my_text)
splitted = [s for s in splitted if len(s) > 0]
print(splitted)
"""

my_text = "Kərtənkələ,   200.50₼      bunları deyib! 3$ qulağını,daşdakı 2345353345 yarığa af sf dsfds sdaf fa fds ffdsfs   15.11.2022 tarihinde  asf kdsdsf jjlfjdslsjs 300€ dayadı. "

print(re.findall(r"([0-9]+(\.[0-9]+)?[₼$€])", my_text))

my_text = re.sub("[0-9]+[₼$]", "[PUL]", my_text)
my_text = re.sub("[0-9]{7,10}", "[ACC]", my_text)
my_text = re.sub("[123][0-9]\.[01][0-9]\.[12][0-9]{3}", "[DATE]", my_text)


print(my_text)
