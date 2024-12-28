from modules.dictionaries.interaction_channels import INTERACTION_CHANNELS

def handle_interactions(particle_counts):
    for pair, products in INTERACTION_CHANNELS.items():
        if particle_counts[pair[0]] > 0 and particle_counts[pair[1]] > 0:
            particle_counts[pair[0]] -= 1
            particle_counts[pair[1]] -= 1
            for product in products:
                particle_counts[product] += 1
