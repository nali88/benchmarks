import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu239', 5.5748e-05)
mat.add_nuclide('Pu240', 2.4339e-06)
mat.add_nuclide('N14', 1.0468e-03)
mat.add_nuclide('H1', 6.4569e-02)
mat.add_nuclide('O16', 3.5018e-02)
mat.add_element('Fe', 1.4557e-06)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "347 Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 6.0386e-02)
mat.add_element('Cr', 1.6678e-02)
mat.add_element('Ni', 9.8504e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Cadmium"
mat.set_density('sum')
mat.add_element('Cd', 4.6340e-02)
mats.append(mat)

mats.export_to_xml()
