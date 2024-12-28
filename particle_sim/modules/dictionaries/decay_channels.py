DECAY_CHANNELS = {
    # Lepton decays
    "Muon": [("Electron", "Electron Neutrino", "Muon Neutrino")],
    "Tau": [
        ("Muon", "Muon Neutrino", "Tau Neutrino"),
        ("Electron", "Electron Neutrino", "Tau Neutrino"),
        ("Pi-", "Tau Neutrino"),
    ],

    # Neutron decay
    "Neutron": [("Proton", "Electron", "Electron Neutrino")],

    # Boson decays
    "W Boson": [
        ("Electron", "Electron Neutrino"),
        ("Muon", "Muon Neutrino"),
        ("Tau", "Tau Neutrino"),
        ("Up Quark", "Down Quark"),
        ("Charm Quark", "Strange Quark"),
    ],
    "Z Boson": [
        ("Electron", "Positron"),
        ("Muon", "Anti-Muon"),
        ("Tau", "Anti-Tau"),
        ("Up Quark", "Anti-Up Quark"),
        ("Down Quark", "Anti-Down Quark"),
        ("Charm Quark", "Anti-Charm Quark"),
        ("Strange Quark", "Anti-Strange Quark"),
#        ("Neutrino", "Anti-Neutrino"),
    ],
    "Higgs Boson": [
        ("Bottom Quark", "Anti-Bottom Quark"),
        ("Tau", "Anti-Tau"),
        ("W Boson", "W Boson"),
        ("Z Boson", "Z Boson"),
        ("Photon", "Photon"),
    ],

    # Meson and baryon decays (examples)
    "Pi+": [("Muon", "Muon Neutrino"), ("Electron", "Electron Neutrino")],
    "Pi-": [("Muon", "Anti-Muon Neutrino"), ("Electron", "Positron")],
    "Pi0": [("Photon", "Photon")],

    # Quark-level decays
    "Top Quark": [("W Boson", "Bottom Quark")],
    "Bottom Quark": [
        ("Charm Quark", "W Boson"),
        ("Up Quark", "W Boson"),
    ],
    "Charm Quark": [
        ("Strange Quark", "W Boson"),
        ("Down Quark", "W Boson"),
    ],
    "Strange Quark": [("Up Quark", "W Boson")],
    "Up Quark": [],
    "Down Quark": [],

    # Neutrino decays (hypothetical, for flavor change)
    "Electron Neutrino": [("Muon Neutrino",)],
    "Muon Neutrino": [("Tau Neutrino",)],
    "Tau Neutrino": [("Electron Neutrino",)],
}
