__author__ = 'priya'

import networkx as nx

# Function that computes peak numbers (i.e. performs k-peak decomposition)
def get_kpeak_decomposition(G):
	G.remove_edges_from(nx.selfloop_edges(G))
	#G = removeSingletons(G)
	#G.remove_edges_from(G.selfloop_edges())
	orig_core_nums = nx.core_number(G)
	H = G.copy(); H_nodes = set(G.nodes())
	current_core_nums = orig_core_nums.copy()
	peak_numbers = {}

    # Each iteration of the while loop finds a k-contour
	while(len(H.nodes()) > 0):
	# degen_core is the degeneracy of the graph
		degen_core = nx.k_core(H) # Degen-core

		# Nodes in the k-contour. Their current core number is their peak number.
		kcontour_nodes = degen_core.nodes()
		for n in kcontour_nodes:
			peak_numbers[n] = current_core_nums[n]

		# Removing the kcontour (i.e. degeneracy) and re-computing core numbers.
		H_nodes = H_nodes.difference(set(kcontour_nodes))
		H = G.subgraph(list(H_nodes))
		current_core_nums = nx.core_number(H)

	return peak_numbers, orig_core_nums


# Function that computes peak numbers while also keeping track of which k-contour (removal) affected a node the most
def get_kpeak_mountainassignment(G, orig_core_nums):
    # Initializing node_CNdrops_mountainassignment
    # 'node_CNdrops_mountainassignment' is a dict where keys are nodeIDS
    # Each value is tuple of the maximum drop in core number observed for this node and the mountain to which it is assigned.
    node_CNdrops_mountainassignment = {}
    for n in G.nodes():
        node_CNdrops_mountainassignment[n] = [0, -1] #diff in core number, assignment to a mountain

    H = G.copy()
    H_nodes = set(G.nodes())
    current_core_nums = orig_core_nums.copy()
    current_d = max(current_core_nums.values())

    # 'current_plotmountain_id' keeps track of numbering of the plot-mountains
    current_plotmountain_id = 0
    peak_numbers = {}

    # Each iteration of the while loop finds a k-contour
    while(len(H.nodes()) > 0):
        # degen_core is the degeneracy of the graph
        degen_core = nx.k_core(H) # Degen-core

        # Note that the actual mountains may consist of multiple components.
        # To  analyze each component, use the following line to find the components
        # components_of_mountain = nx.connected_component_subgraphs(induced_subgraph_of_mountain)
        # But in the mountain plot we plot the separate components related to a k-contour as a single mountain.

        # Nodes in the k-contour. Their current core number is their peak number.
        kcontour_nodes = degen_core.nodes()
        for n in kcontour_nodes:
            peak_numbers[n] = current_core_nums[n]

        # Removing the kcontour (i.e. degeneracy) and re-computing core numbers.
        H_nodes = H_nodes.difference(set(kcontour_nodes))
        H = G.subgraph(list(H_nodes))
        new_core_nums = nx.core_number(H)

        for n in kcontour_nodes:
            # For the nodes in kcontour, its removal causes its core number to drop to 0.
            # Checking is this drop is greater than the drop in core number observed for these nodes in previous iterations
            if current_core_nums[n] - 0 > node_CNdrops_mountainassignment[n][0]:
                node_CNdrops_mountainassignment[n][0] = current_core_nums[n]
                node_CNdrops_mountainassignment[n][1] = current_plotmountain_id

        for n in new_core_nums:
            # Checking is this drop is greater than the drop in core number observed for these nodes in previous iterations
            if current_core_nums[n] - new_core_nums[n] > node_CNdrops_mountainassignment[n][0]:
                node_CNdrops_mountainassignment[n][0] = current_core_nums[n] - new_core_nums[n]
                node_CNdrops_mountainassignment[n][1] = current_plotmountain_id

        current_plotmountain_id += 1
        current_core_nums = new_core_nums.copy()


    # Creating a dictionary of dictionary,
    # such that a key represents the ID of a mountain
    # and the value represents the a dictionary of nodes assigned to that mountain.
    # eg. permountain_ID_core_peak_numbers[0] is a dict of mountain 0.
    # Keys of the inner dictionary are nodes and value is a tuple <nodeID, corenumber, peak number>
    permountain_ID_corenumber_peaknumber = {}
    for n in orig_core_nums.keys():
        if node_CNdrops_mountainassignment[n][1] not in permountain_ID_corenumber_peaknumber:
            permountain_ID_corenumber_peaknumber[node_CNdrops_mountainassignment[n][1]] = {}
        permountain_ID_corenumber_peaknumber[node_CNdrops_mountainassignment[n][1]][n] = (n, orig_core_nums[n],peak_numbers[n])

    return permountain_ID_corenumber_peaknumber, peak_numbers

# Function that computes peak numbers while also keeping track of which k-contour (removal) affected a node the most
# This function plots each component separately
def get_kpeak_mountainassignment_component(G, orig_core_nums):
    # Initializing node_CNdrops_mountainassignment
    # 'node_CNdrops_mountainassignment' is a dict where keys are nodeIDS
    # Each value is tuple of the maximum drop in core number observed for this node and the mountain to which it is assigned.
    node_CNdrops_mountainassignment = {}
    for n in G.nodes():
        node_CNdrops_mountainassignment[n] = [0, -1] #diff in core number, assignment to a mountain

    H = G.copy()
    H_nodes = set(G.nodes())
    current_core_nums = orig_core_nums.copy()
    current_d = max(current_core_nums.values())

    # 'current_plotmountain_id' keeps track of numbering of the plot-mountains
    current_plotmountain_id = 0
    peak_numbers = {}

    # Each iteration of the while loop finds a k-contour
    while(len(H.nodes()) > 0):
        # degen_core is the degeneracy of the graph
        degen_core = nx.k_core(H) # Degen-core

        # Note that the actual mountains may consist of multiple components.
        # To  analyze each component, use the following line to find the components
        # components_of_mountain = nx.connected_component_subgraphs(induced_subgraph_of_mountain)
        # But in the mountain plot we plot the separate components related to a k-contour as a single mountain.

        # Nodes in the k-contour. Their current core number is their peak number.
        degen_core_comps = nx.connected_component_subgraphs(degen_core)
        for comp in degen_core_comps:
            kcontour_nodes = comp.nodes()
            for n in kcontour_nodes:
                peak_numbers[n] = current_core_nums[n]
    
            # Removing the kcontour (i.e. degeneracy) and re-computing core numbers.
            H_nodes = H_nodes.difference(set(kcontour_nodes))
            H = G.subgraph(list(H_nodes))
            new_core_nums = nx.core_number(H)
    
            for n in kcontour_nodes:
                # For the nodes in kcontour, its removal causes its core number to drop to 0.
                # Checking is this drop is greater than the drop in core number observed for these nodes in previous iterations
                if current_core_nums[n] - 0 > node_CNdrops_mountainassignment[n][0]:
                    node_CNdrops_mountainassignment[n][0] = current_core_nums[n]
                    node_CNdrops_mountainassignment[n][1] = current_plotmountain_id
    
            for n in new_core_nums:
                # Checking is this drop is greater than the drop in core number observed for these nodes in previous iterations
                if current_core_nums[n] - new_core_nums[n] > node_CNdrops_mountainassignment[n][0]:
                    node_CNdrops_mountainassignment[n][0] = current_core_nums[n] - new_core_nums[n]
                    node_CNdrops_mountainassignment[n][1] = current_plotmountain_id
    
            current_plotmountain_id += 1
            current_core_nums = new_core_nums.copy()


    # Creating a dictionary of dictionary,
    # such that a key represents the ID of a mountain
    # and the value represents the a dictionary of nodes assigned to that mountain.
    # eg. permountain_ID_core_peak_numbers[0] is a dict of mountain 0.
    # Keys of the inner dictionary are nodes and value is a tuple <nodeID, corenumber, peak number>
    permountain_ID_corenumber_peaknumber = {}
    for n in orig_core_nums.keys():
        if node_CNdrops_mountainassignment[n][1] not in permountain_ID_corenumber_peaknumber:
            permountain_ID_corenumber_peaknumber[node_CNdrops_mountainassignment[n][1]] = {}
        permountain_ID_corenumber_peaknumber[node_CNdrops_mountainassignment[n][1]][n] = (n, orig_core_nums[n],peak_numbers[n])

    return permountain_ID_corenumber_peaknumber, peak_numbers


def removeSingletons(G):
    degrees=G.degree()
    for node in degrees.keys():
        if degrees[node]==0:
            G.remove_node(node)
    return G
