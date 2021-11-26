Alien = {'Speed':'Fast','Color':'Green'}
point_value = Alien.get('Point','No points((((')
print(point_value)
print(Alien)

for a,b in Alien.items():
    print(f"Kay:{a}")
    print(f"Value:{b}")

for a in Alien.keys():
    print(a.title())
