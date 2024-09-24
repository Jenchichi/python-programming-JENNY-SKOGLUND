
# matcha rader med varandra, ex. quotes matchas med [] och i med 1
# import re
# quotes, i = [], 1

# Matte 2:
# Polynom, första graden. ex. P[x] = kx + m. Det som står på högersidan av likamed.
# Polynom, andragraden. ex. P[x] = ax^2 + bx + c

# I datorn så kan vi representera polynom som vektorer (listor).
# [a.0, .... , a.n] = a.0 + a.1x + a.2x^2 + .... + a.nx^n

# Kvadrering / Konjugat
# (X + y)^2 = x^2 + 2xy + y^2
# (x - y)^2 = x^2 - 2xy + y^2
# (x + y) (x - y) = x^2 + y^2

# Faktorisering
# x^2 - 2x + 1 = 0
# x = 1 +- rotenur(0)
# dubbelrot x.0 = alfa (dubbelrot på grund av plus och minus framför roten ur)
# (x - 1)^2 är samma sak som x^2 - 2x + 1

# Polynom används till linjära ekvationssystem (kx + m). Kolla upp Matriser, det kommer vi använda en massa i programmeringen.
# Linjära ekvationssystem har tre fall = ingen lösning, entydig lösning eller oändligt många lösningar.
# ex. på två kurvor (två linjer):
# 2x + 1 = y
# -x + 1 = y
# Kan lösa det som ovan grafiskt eller med substitution
# Substitution:
# 2x + 1 = -x + 1
# 3x = 0
# Radoperation (Additionsmetoden):
# 2x + 1 - (-x +1) = y - y
# 2x + 1 + x - 1 = 0
# 3x = 0

# Potenser och logaritmer (logaritmer ln)
# 10^3 (där 10 är bas och 3 exponent)
# Naturliga logaritmer ln e = 1
# Logaritm lagar:
# ln x^a =(är samma sak som) a * ln x
# ln e = 1
# ln e^a = a * ln e = a
# e^lna = a = ln e^a
# ln (x*y) = lnx + lny är samma som (e^a * e^b = e^a+b)
# ln(x/y) = lnx - lny är samma som (ln(1/x) = -x)

# Bevisföring. Vad är ett bevis: " Logiskt resonemang som leder till en viss slutsats."
# exempel: Pythagoras sats
# exempel på bevis/algoritm/program: "En sekvens av operationer som leder till ett visst sluttillstånd"

