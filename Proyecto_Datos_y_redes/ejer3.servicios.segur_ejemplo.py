class Node:
    def __init__(self, name):
        self.name = name
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)


class Vulnerability:
    def __init__(self, name):
        self.name = name

import random

class Simulator:
    def __init__(self):
        self.network = {}

    def add_node(self, node):
        self.network[node.name] = node

    def simulate_brute_force_attack(self, attacker, target, attempts):
        if attacker in self.network and target in self.network:
            for _ in range(attempts):
                if random.random() > 0.5:
                    print(f"Brute force attack successful: {attacker} compromised {target}.")
                    return True
            print(f"Brute force attack failed: {attacker} could not compromise {target}.")
            return False
        else:
            print("Node not found in the network.")
            return False
def main():
    # Create nodes and vulnerabilities
    node1 = Node("Server1")
    node1.add_vulnerability(Vulnerability("XSS"))
    node2 = Node("Server2")
    node2.add_vulnerability(Vulnerability("BruteForce"))

    # Build the network
    simulator = Simulator()
    simulator.add_node(node1)
    simulator.add_node(node2)

    # Simulate attacks
    simulator.simulate_brute_force_attack("Server2", "Server1", 5)

if __name__ == '__main__':
    main()
