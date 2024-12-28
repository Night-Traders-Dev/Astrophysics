from collections import defaultdict
import random
import numpy as np
from modules.dictionaries.particles import PARTICLES
from modules.dictionaries.decay_channels import DECAY_CHANNELS
from modules.dictionaries.interaction_channels import INTERACTION_CHANNELS
from modules.constants import *
from modules.utils.calculations import *


def calculate_metrics(elapsed_time):
    """Calculate and return simulation metrics."""
    avg_appearance_time = elapsed_time / total_particles_created if total_particles_created > 0 else 0
    return {
        "timesteps": int(time_steps),
        "total_particles": total_particles_created,
        "decayed_natural": total_particles_decayed_natural,
        "decayed_interaction": total_particles_decayed_interaction,
        "avg_appearance_time": avg_appearance_time,
        "temperature": temperature,
        "entropy": entropy,
        "particle_counts": dict(particle_counts),
    }
