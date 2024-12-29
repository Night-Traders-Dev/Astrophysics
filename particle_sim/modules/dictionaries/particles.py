# Particle Data with Vacuum Appearance Probability
import math

PARTICLES = {
    # Leptons
    "Electron": {"mass": 0.000511, "charge": -1, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (0.000511 * 1e30)},
    "Positron": {"mass": 0.000511, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (0.000511 * 1e30)},
    "Muon": {"mass": 0.105, "charge": -1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion", "vacuum_prob": 1 / (0.105 * 2.2e-6)},
    "Anti-Muon": {"mass": 0.105, "charge": +1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion", "vacuum_prob": 1 / (0.105 * 2.2e-6)},
    "Tau": {"mass": 1.777, "charge": -1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion", "vacuum_prob": 1 / (1.777 * 2.9e-13)},
    "Anti-Tau": {"mass": 1.777, "charge": +1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion", "vacuum_prob": 1 / (1.777 * 2.9e-13)},
    "Electron Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (1e-9 * 1e30)},
    "Muon Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (1e-9 * 1e30)},
    "Tau Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (1e-9 * 1e30)},
    "Anti-Electron Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (1e-9 * 1e30)},
    "Anti-Muon Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (1e-9 * 1e30)},
    "Anti-Tau Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (1e-9 * 1e30)},

    # Quarks
    "Up Quark": {"mass": 2.16e-3, "charge": +2/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (2.16e-3 * 1e30)},
    "Anti-Up Quark": {"mass": 2.16e-3, "charge": -2/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (2.16e-3 * 1e30)},
    "Down Quark": {"mass": 4.67e-3, "charge": -1/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (4.67e-3 * 1e30)},
    "Anti-Down Quark": {"mass": 4.67e-3, "charge": +1/3, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (4.67e-3 * 1e30)},
    "Charm Quark": {"mass": 1.27, "charge": +2/3, "spin": 0.5, "lifetime": 1.56e-12, "type": "fermion", "vacuum_prob": 1 / (1.27 * 1.56e-12)},
    "Anti-Charm Quark": {"mass": 1.27, "charge": -2/3, "spin": 0.5, "lifetime": 1.56e-12, "type": "fermion", "vacuum_prob": 1 / (1.27 * 1.56e-12)},
    "Strange Quark": {"mass": 0.093, "charge": -1/3, "spin": 0.5, "lifetime": 1.24e-8, "type": "fermion", "vacuum_prob": 1 / (0.093 * 1.24e-8)},
    "Anti-Strange Quark": {"mass": 0.093, "charge": +1/3, "spin": 0.5, "lifetime": 1.24e-8, "type": "fermion", "vacuum_prob": 1 / (0.093 * 1.24e-8)},
    "Top Quark": {"mass": 172.76, "charge": +2/3, "spin": 0.5, "lifetime": 5e-25, "type": "fermion", "vacuum_prob": 1 / (172.76 * 5e-25)},
    "Anti-Top Quark": {"mass": 172.76, "charge": -2/3, "spin": 0.5, "lifetime": 5e-25, "type": "fermion", "vacuum_prob": 1 / (172.76 * 5e-25)},
    "Bottom Quark": {"mass": 4.18, "charge": -1/3, "spin": 0.5, "lifetime": 1.3e-12, "type": "fermion", "vacuum_prob": 1 / (4.18 * 1.3e-12)},
    "Anti-Bottom Quark": {"mass": 4.18, "charge": +1/3, "spin": 0.5, "lifetime": 1.3e-12, "type": "fermion", "vacuum_prob": 1 / (4.18 * 1.3e-12)},

    # Baryons
    "Proton": {"mass": 0.938, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion", "vacuum_prob": 1 / (0.938 * 1e30)},
    "Neutron": {"mass": 0.939, "charge": 0, "spin": 0.5, "lifetime": 880.2, "type": "fermion", "vacuum_prob": 1 / (0.939 * 880.2)},

    # Bosons
    "Photon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson", "vacuum_prob": 1 / (1e30)},  # No mass, infinite probability
    "Gluon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson", "vacuum_prob": 1 / (1e30)},  # No mass, infinite probability
    "W Boson": {"mass": 80.379, "charge": +1, "spin": 1, "lifetime": 3e-25, "type": "boson", "vacuum_prob": 1 / (80.379 * 3e-25)},
    "Z Boson": {"mass": 91.1876, "charge": 0, "spin": 1, "lifetime": 3e-25, "type": "boson", "vacuum_prob": 1 / (91.1876 * 3e-25)},
    "Higgs Boson": {"mass": 125.1, "charge": 0, "spin": 0, "lifetime": 1.56e-22, "type": "boson", "vacuum_prob": 1 / (125.1 * 1.56e-22)},

    # Composite
    "Deuterium": {"mass": 2.014, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "composite", "vacuum_prob": 1 / (2.014 * 1e30)},
    "Tritium": {"mass": 3.016, "charge": 0, "spin": 1, "lifetime": 3.88e8, "type": "composite", "vacuum_prob": 1 / (3.016 * 3.88e8)},
    "Helium-3": {"mass": 3.016, "charge": +2, "spin": 0.5, "lifetime": 1e30, "type": "composite", "vacuum_prob": 1 / (3.016 * 1e30)},
    "Helium-4": {"mass": 4.002, "charge": +2, "spin": 0, "lifetime": 1e30, "type": "composite", "vacuum_prob": 1 / (4.002 * 1e30)},

    # Pions
    "Pi+": {"mass": 0.13957, "charge": +1, "spin": 0, "lifetime": 2.6e-8, "type": "boson", "vacuum_prob": 1 / (0.13957 * 2.6e-8)},
    "Pi-": {"mass": 0.13957, "charge": -1, "spin": 0, "lifetime": 2.6e-8, "type": "boson", "vacuum_prob": 1 / (0.13957 * 2.6e-8)},
    "Pi0": {"mass": 0.13498, "charge": 0, "spin": 0, "lifetime": 8.4e-17, "type": "boson", "vacuum_prob": 1 / (0.13498 * 8.4e-17)},
}

