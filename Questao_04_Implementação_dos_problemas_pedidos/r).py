# ─────────────────────────────────────
# r) Apuração de eleição (3 candidatos)
# ─────────────────────────────────────
print("\nr) Apuração de eleição")
eleitores = int(input("Total de eleitores: "))
a = int(input("Votos candidato A: "))
b = int(input("Votos candidato B: "))
c = int(input("Votos candidato C: "))
nulos = int(input("Votos nulos: "))
brancos = int(input("Votos em branco: "))

validos = a + b + c
total_votos = validos + nulos + brancos

print("\n=== RESULTADO FINAL ===")
print(f"% A sobre válidos: {a/eleitores*100:.2f}%")
print(f"% B sobre válidos: {b/eleitores*100:.2f}%")
print(f"% C sobre válidos: {c/eleitores*100:.2f}%")
print(f"% Nulos sobre eleitores: {nulos/eleitores*100:.2f}%")
print(f"% Brancos sobre eleitores: {brancos/eleitores*100:.2f}%")
print(f"% Válidos sobre eleitores: {validos/eleitores*100:.2f}%")