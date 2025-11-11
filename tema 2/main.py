elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note = [9, 10, 4, 7, 8]

# A1
for e, n in zip(elevi, note):
    print(f"{e} are nota {n}")

# A2
print(f"Nota max: {max(note)} - {elevi[note.index(max(note))]}")
print(f"Nota min: {min(note)} - {elevi[note.index(min(note))]}")

# A3
print(f"Media clasei: {sum(note)/len(note):.2f}")

# A4
print("Promovați:", [e for e, n in zip(elevi, note) if n >= 5])

elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note = [9, 10, 4, 7, 8]

# A
for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])

print("Max:", max(note), elevi[note.index(max(note))])
print("Min:", min(note), elevi[note.index(min(note))])
print("Media:", round(sum(note)/len(note),2))

print("Promovati:")
for i in range(len(elevi)):
    if note[i] >= 5:
        print(elevi[i])

# B
for i in range(len(note)):
    note[i] += 1
    if note[i] > 10:
        note[i] = 10

elevi.append("Felix")
note.append(6)

if "Darius" in elevi:
    p = elevi.index("Darius")
    elevi.pop(p)
    note.pop(p)

for i in range(len(elevi)):
    print(elevi[i], "-", note[i])

# C
interogari = ["Ana", "Mara", "Elena", "stop"]
i = 0
while interogari[i] != "stop":
    if interogari[i] in elevi:
        j = elevi.index(interogari[i])
        print(interogari[i], "are nota", note[j])
    else:
        print(interogari[i], "nu exista")
    i += 1

prom = 0
resp = 0
for n in note:
    if n >= 5: prom += 1
    else: resp += 1
print("Promovati:", prom, "Respinși:", resp)

s = 0
nr = 0
for n in note:
    if n >= 5:
        s += n
        nr += 1
if nr > 0:
    print("Media promovaților:", round(s/nr,2))
else:
    print("Nimeni promovat")