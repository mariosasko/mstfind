from .graph import Graph


def loadtxt(fname):
    lineno = 1
    with open(fname, mode='r') as f:
        g = Graph()
        try:
            for line in f:
                v, neighbours = line.split('->')
                v, neighbours = v.strip(), neighbours.strip()
                g.add_vertex(v)
                for neigh in neighbours.split():
                    u, w = neigh.split(',')
                    g.add_edge((v, u), float(w))
                lineno += 1
        except:
            raise ValueError(f'error parsing line {lineno}')
    return g


def savetxt(g, fname):
    with open(fname, mode='w') as f:
        for v in sorted(g.vertices()):
            neighbors = ' '.join(f'{u},{w}' for u, w in g.vertex_neighbours(v))
            f.write(f'{v} -> {neighbors}\n')