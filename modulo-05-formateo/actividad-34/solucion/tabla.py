ultrasonidos = 40
infrarrojos = 12
luz = 7

barra_ultrasonidos = "#" * (ultrasonidos // 5)
barra_infrarrojos = "#" * (infrarrojos // 5)
barra_luz = "#" * (luz // 5)

print(f"ultrasonidos {ultrasonidos:.1f} {barra_ultrasonidos}")
print(f"infrarrojos {infrarrojos:.1f} {barra_infrarrojos}")
print(f"luz {luz:.1f} {barra_luz}")
