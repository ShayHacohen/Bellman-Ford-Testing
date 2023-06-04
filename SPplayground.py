# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Keeping the above auto-generated comments here because it's cool to know ^

from numpy import inf


# *** Bellman-Ford algorithm simple implementation for connected, directed graphs: ***
def BellmanFord(adj, src, w, verbose=False, edge_sorting_key=None):
    sp_tree = {node: [] for node in adj}
    dist = {n: inf for n in adj}
    dist[src] = 0
    tree_edges = {}
    edges = get_edges(adj)
    if edge_sorting_key is not None:
        edges.sort(key=edge_sorting_key)
    node_count = len(adj)
    for i in range(node_count - 1):
        changed = False
        for e in edges:
            if w(e) + dist[e[0]] < dist[e[1]]:
                dist[e[1]] = w(e) + dist[e[0]]
                tree_edges[e[1]] = e
                changed = True
        if verbose:
            print(f"Bellman-Ford iteration #{i} results:")
            print_dists(dist, src)

        if not changed:
            break  # No change had occurred so we can stop.
    for n in adj:
        adjacent = []
        if n in tree_edges:
            adjacent = tree_edges[n]
        sp_tree[n] = adjacent
    return dist, sp_tree


# *** Auxiliary functions: ***

def get_edges(adj):
    intermediate = [[(node, dst) for dst in adj[node]] for node in adj]
    return [es for l in intermediate for es in l]


def get_adj(G):
    adj = {n: [] for n in G[0]}
    for e in G[1]:
        adj[e[0]].append(e[1])
    return adj


def get_graph(adj):
    return adj.keys(), get_edges(adj)


def bf_as_graph(adj, src, w):
    return adj.keys(), BellmanFord(adj, src, w)[1]


def print_edges(G, w=None):
    edges = G[1]
    for e in edges:
        f_str = str(e)
        if w is not None:
            f_str = f'w({f_str})={w(e)}'
        print(f_str)
    print('\n')


def print_nodes(G):
    nodes = G[0]
    print('\n'.join(nodes) + '\n')


def print_dists(dist, src=None):
    if src is not None:
        print(f'd({src})={dist[src]}')
    for d in dist:
        if d != src:
            print(f'd({d})={dist[d]}')


def __flatten_to_set(d):
    return {l for x in d.values() for l in x}


def print_results(G, w, verbose=False):
    print('For graph G with nodes:')
    print_nodes(G)
    print('and edges:')
    print_edges(G)

    print('Testing with the following weight function:')
    print_edges(G, w)

    print('Obtained tree:')
    dist, sp_tree = BellmanFord(get_adj(G), 's', w, verbose, w)
    T = (V, [e for e in sp_tree.values() if e])
    print_nodes(T)
    print_edges(T)
    print_dists(dist, 's')


def prompt():
    input('Press ENTER to proceed...')


# *** Graph definitions: ***

w_1_d = {('s', 'a'): 9, ('s', 'b'): 2, ('b', 'c'): -3, ('b', 'd'): 4, ('c', 's'): 2, ('c', 'd'): 1, ('d', 'a'): -4}
w_1 = w_1_d.get

w_2_d = {('s', 'a'): 9+5, ('s', 'b'): 2+5, ('b', 'c'): -3+5, ('b', 'd'): 4+5, ('c', 's'): 5+5, ('c', 'd'): 1+5, ('d', 'a'): -4+5}
w_2 = w_2_d.get

w_3_d = {('s', 'a'): 9*5, ('s', 'b'): 2*5, ('b', 'c'): -3*5, ('b', 'd'): 4*5, ('c', 's'): 5*5, ('c', 'd'): 1*5, ('d', 'a'): -4*5}
w_3 = w_3_d.get

w_4 = lambda x: w_1(x) + w_3(x)

w_5_d = {('s', 'a'): 2, ('s', 'b'): 6, ('a', 'b'): 10, ('a', 'c'): 5, ('b', 'c'): 0, ('c', 'd'): -1, ('d', 'b'): 3}
w_5 = w_5_d.get

if __name__ == '__main__':
    E = w_1_d.keys()
    V = set([n for e in E for n in e])
    G1 = (V, E)

    print_results(G1, w_1)
    prompt()
    print_results(G1, w_2)
    prompt()
    print_results(G1, w_3)
    prompt()
    print_results(G1, w_4)
    prompt()

    E2 = list(w_5_d.keys())
    E2.sort(key=w_5)  # Want to iterate over the edges in increasing weight order this time.
    V2 = list(set([n for e in E for n in e]))
    V2.sort()
    G2 = (V2, E2)

    print_results(G2, w_5, True)

