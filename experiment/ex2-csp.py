colors = ['Red', 'Blue', 'Green']
states = ['wa', 'nt', 'sa', 'q', 'nsw', 'v']
neighbors = {} #adjacent pairing neighbors of different states
neighbors['wa'] = ['nt', 'sa']
neighbors['nt'] = ['wa', 'sa', 'q']
neighbors['sa'] = ['wa', 'nt', 'q', 'nsw', 'v']
neighbors['q'] = ['nt', 'sa', 'snw']
neighbors['nsw'] = ['q', 'sa', 'v']
neighbors['v'] = ['sa', 'nsw']
colors_of_states = {}
def promising(state, color): #function to check a promising color - returns a promising color
for neighbor in neighbors.get(state):
color_of_neighbor = colors_of_states.get(neighbor)
if color_of_neighbor == color: #same color (of neighbor and state) -> rejected
return False
return True #if not same -> color accepted
def get_color_for_state(state): #promising color is assigned to the state
for color in colors:
if promising(state, color):
return color
def main():
for state in states:
colors_of_states[state] = get_color_for_state(state)
print(colors_of_states)
main()
