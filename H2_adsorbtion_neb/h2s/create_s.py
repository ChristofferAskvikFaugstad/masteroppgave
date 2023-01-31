from ase.io import read
from ase.visualize import view

base_struc = read("C:/Users/chris/masteroppgave/masteroppgave_code/ni30/ni30_best.xyz")

ad_struc = read("C:/Users/chris/masteroppgave/masteroppgave_code/H2_adsorbtion_neb/fad/initial_guess.xyz")

s_struc = read("C:/Users/chris/masteroppgave/masteroppgave_code/H2_adsorbtion_neb/h2s/initial_guess.xyz")

view(ad_struc, viewer="avogadro")
view(s_struc, viewer="avogadro", block = True)


view([s_struc,ad_struc], block = True)




