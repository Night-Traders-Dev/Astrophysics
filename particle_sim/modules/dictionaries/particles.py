# Particle Data
PARTICLES = {
    # Leptons
    "Electron": {"mass": 0.000511, "charge": -1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Positron": {"mass": 0.000511, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Muon": {"mass": 0.105, "charge": -1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion"},
    "Anti-Muon": {"mass": 0.105, "charge": +1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion"},
    "Tau": {"mass": 1.777, "charge": -1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion"},
    "Anti-Tau": {"mass": 1.777, "charge": +1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion"},
    "Electron Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Muon Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Tau Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Anti-Electron Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Anti-Muon Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Anti-Tau Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},

    # Quarks
    "Up Quark": {"mass": 2.16e-3, "charge": +2/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Anti-Up Quark": {"mass": 2.16e-3, "charge": -2/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Down Quark": {"mass": 4.67e-3, "charge": -1/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Anti-Down Quark": {"mass": 4.67e-3, "charge": +1/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Charm Quark": {"mass": 1.27, "charge": +2/3, "spin": 0.5, "lifetime": 1.56e-12, "type": "fermion"},
    "Anti-Charm Quark": {"mass": 1.27, "charge": -2/3, "spin": 0.5, "lifetime": 1.56e-12, "type": "fermion"},
    "Strange Quark": {"mass": 0.093, "charge": -1/3, "spin": 0.5, "lifetime": 1.24e-8, "type": "fermion"},
    "Anti-Strange Quark": {"mass": 0.093, "charge": +1/3, "spin": 0.5, "lifetime": 1.24e-8, "type": "fermion"},
    "Top Quark": {"mass": 172.76, "charge": +2/3, "spin": 0.5, "lifetime": 5e-25, "type": "fermion"},
    "Anti-Top Quark": {"mass": 172.76, "charge": -2/3, "spin": 0.5, "lifetime": 5e-25, "type": "fermion"},
    "Bottom Quark": {"mass": 4.18, "charge": -1/3, "spin": 0.5, "lifetime": 1.3e-12, "type": "fermion"},
    "Anti-Bottom Quark": {"mass": 4.18, "charge": +1/3, "spin": 0.5, "lifetime": 1.3e-12, "type": "fermion"},

    # Baryons
    "Proton": {"mass": 0.938, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Neutron": {"mass": 0.939, "charge": 0, "spin": 0.5, "lifetime": 880.2, "type": "fermion"},

    # Bosons
    "Photon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson"},
    "Gluon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson"},
    "W Boson": {"mass": 80.379, "charge": +1, "spin": 1, "lifetime": 3e-25, "type": "boson"},
    "Z Boson": {"mass": 91.1876, "charge": 0, "spin": 1, "lifetime": 3e-25, "type": "boson"},
    "Higgs Boson": {"mass": 125.1, "charge": 0, "spin": 0, "lifetime": 1.56e-22, "type": "boson"},

    # Composite
    "Deuterium": {"mass": 2.014, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "composite"},
    "Tritium": {"mass": 3.016, "charge": 0, "spin": 1, "lifetime": 3.88e8, "type": "composite"},
    "Helium-3": {"mass": 3.016, "charge": +2, "spin": 0.5, "lifetime": 1e30, "type": "composite"},
    "Helium-4": {"mass": 4.002, "charge": +2, "spin": 0, "lifetime": 1e30, "type": "composite"},


    # Pions
    "Pi+": {"mass": 0.13957, "charge": +1, "spin": 0, "lifetime": 2.6e-8, "type": "boson"},
    "Pi-": {"mass": 0.13957, "charge": -1, "spin": 0, "lifetime": 2.6e-8, "type": "boson"},
    "Pi0": {"mass": 0.13498, "charge": 0, "spin": 0, "lifetime": 8.4e-17, "type": "boson"}


}
