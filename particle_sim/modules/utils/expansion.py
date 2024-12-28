from modules.constants import H0

def hubble_expansion(volume, adjusted_timestep):
    H = H0 * 1e3 / (3.086e22)
    return volume * (1 + H * adjusted_timestep)
