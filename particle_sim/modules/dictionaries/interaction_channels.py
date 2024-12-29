INTERACTION_CHANNELS = {
    # Baryonic interactions
    ("Proton", "Neutron"): [("Deuterium", "Photon")],
    ("Proton", "Electron"): [("Neutron", "Electron Neutrino")],
    ("Neutron", "Electron Neutrino"): [("Proton", "Electron")],
    # Synthesis of Tritium (H-3)
    ("Deuterium", "Neutron"): [("Tritium", "Photon")],
    ("Proton", "Neutron", "Neutron"): [("Tritium",)],

    # Decay of Tritium
    ("Tritium",): [("Helium-3", "Electron", "Anti-Electron Neutrino")],

    # Synthesis of Helium-3 (He-3)
    ("Deuterium", "Proton"): [("Helium-3", "Photon")],
    ("Tritium", "Proton"): [("Helium-3", "Neutron")],

    # Synthesis of Helium-4 (He-4)
    ("Helium-3", "Neutron"): [("Helium-4", "Photon")],
    ("Deuterium", "Deuterium"): [("Helium-4", "Neutron", "Photon")],


    # Leptonic interactions
    ("Electron", "Positron"): [("Photon", "Photon")],
    ("Muon", "Anti-Muon"): [("Photon", "Photon")],
    ("Tau", "Anti-Tau"): [("Photon", "Photon")],
    ("Electron", "Photon"): [("Electron", "Photon")],
    ("Muon", "Photon"): [("Muon", "Photon")],
    ("Tau", "Photon"): [("Tau", "Photon")],
    ("Electron", "W Boson"): [("Electron Neutrino",)],
    ("Muon", "W Boson"): [("Muon Neutrino",)],
    ("Tau", "W Boson"): [("Tau Neutrino",)],

    # Quark interactions
    ("Up Quark", "Anti-Up Quark"): [("Photon",), ("Gluon",), ("Z Boson",)],
    ("Down Quark", "Anti-Down Quark"): [("Photon",), ("Gluon",), ("Z Boson",)],
    ("Charm Quark", "Anti-Charm Quark"): [("Photon",), ("Gluon",), ("Z Boson",)],
    ("Strange Quark", "Anti-Strange Quark"): [("Photon",), ("Gluon",), ("Z Boson",)],
    ("Top Quark", "Anti-Top Quark"): [("Photon",), ("Gluon",), ("Z Boson",)],
    ("Bottom Quark", "Anti-Bottom Quark"): [("Photon",), ("Gluon",), ("Z Boson",)],

    # Quark-gluon interactions
    ("Up Quark", "Gluon"): [("Up Quark", "Gluon")],
    ("Down Quark", "Gluon"): [("Down Quark", "Gluon")],
    ("Charm Quark", "Gluon"): [("Charm Quark", "Gluon")],
    ("Strange Quark", "Gluon"): [("Strange Quark", "Gluon")],
    ("Top Quark", "Gluon"): [("Top Quark", "Gluon")],
    ("Bottom Quark", "Gluon"): [("Bottom Quark", "Gluon")],

    # Boson interactions
    ("Photon", "Electron"): [("Photon", "Electron")],
    ("Photon", "Muon"): [("Photon", "Muon")],
    ("Photon", "Tau"): [("Photon", "Tau")],
    ("Photon", "Proton"): [("Photon", "Proton")],
    ("Photon", "Neutron"): [("Photon", "Neutron")],
    ("Gluon", "Gluon"): [("Gluon", "Gluon")],
    ("W Boson", "Z Boson"): [("Photon",)],

    # Pion interactions
    ("Pi+", "Electron"): [("Muon", "Muon Neutrino")],
    ("Pi-", "Electron"): [("Muon", "Anti-Muon Neutrino")],
    ("Pi0", "Photon"): [("Photon", "Photon")],

    # Higgs interactions
    ("Higgs Boson", "Top Quark"): [("Top Quark",)],
    ("Higgs Boson", "Bottom Quark"): [("Bottom Quark",)],
    ("Higgs Boson", "Electron"): [("Electron",)],
    ("Higgs Boson", "Muon"): [("Muon",)],
    ("Higgs Boson", "Tau"): [("Tau",)],

    # Neutrino interactions
    ("Electron Neutrino", "W Boson"): [("Electron",)],
    ("Muon Neutrino", "W Boson"): [("Muon",)],
    ("Tau Neutrino", "W Boson"): [("Tau",)],
    ("Electron Neutrino", "Z Boson"): [("Electron Neutrino",)],
    ("Muon Neutrino", "Z Boson"): [("Muon Neutrino",)],
    ("Tau Neutrino", "Z Boson"): [("Tau Neutrino",)],

    # Pair production
    ("Photon", "Photon"): [("Electron", "Positron")],
("Gluon", "Gluon"): [
    ("Up Quark", "Anti-Up Quark"),
    ("Down Quark", "Anti-Down Quark"),
    ("Charm Quark", "Anti-Charm Quark"),
    ("Strange Quark", "Anti-Strange Quark"),
    ("Top Quark", "Anti-Top Quark"),
    ("Bottom Quark", "Anti-Bottom Quark"),
],
}
