from ase.io import read

structure = read("initial_guess.xyz")

from ase.calculators.vasp import Vasp

calc = Vasp(
    # General
    prec = 'Accurate',
    istart = 0, # start new calculation
    xc = "PBE", # set PBE exchange correlation functional
    ismear = 0, # Gaussian smearing,
    sigma = 0.02, # smearing constant, found optimal value
    isym = -1, # ingnore symmetires
    ispin = 2, # for spin-polarized calculations
    
    # electronic SC
    encut = 400, # energy cutoff, default depend on type
    nelm = 120, # max number of SC steps default = 60

    # ionic SC 
    nsw = 40,  # Maximum number of ionic steps, default = 0
    ibrion = 1, # Determines ion update method # -1 of nsw 0 ot -1
    ediffg = -0.05, # force criteria

    # Parallell controll
    ncore = 20, # optimal value for 4 nodes

    # Output controll
    lcharg = False, # toggels if CHGCAR is written, default = True
    lwave = False, # toggels if WAVECAR is written, default = True
)

structure.calc = calc # attach calculator
structure.get_potential_energy() # perform computations
