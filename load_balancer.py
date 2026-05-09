import bisect

from hashing import get_hash


class ConsistentHashLoadBalancer:

    def __init__(self, nodes=None):

        self.nodes = nodes or []

        self.ring = {}

        self.sorted_keys = []

        self.build_ring()

    def build_ring(self):

        self.ring.clear()

        self.sorted_keys.clear()

        for node in self.nodes:

            node_hash = get_hash(node)

            self.ring[node_hash] = node

            self.sorted_keys.append(node_hash)

        self.sorted_keys.sort()

    def add_node(self, node):

        if node not in self.nodes:

            self.nodes.append(node)

            self.build_ring()

    def remove_node(self, node):

        if node in self.nodes:

            self.nodes.remove(node)

            self.build_ring()

    def get_node(self, ip):

        if not self.ring:
            return None

        ip_hash = get_hash(ip)

        index = bisect.bisect(self.sorted_keys, ip_hash)

        if index == len(self.sorted_keys):
            index = 0

        selected_hash = self.sorted_keys[index]

        return self.ring[selected_hash]