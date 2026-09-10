# Resource Allocation Graph Cycle Detector

def detect_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        # Node is already in current path
        if node in recursion_stack:
            return True

        # Already completely checked
        if node in visited:
            return False

        visited.add(node)
        recursion_stack.add(node)

        # Visit all connected nodes
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        recursion_stack.remove(node)

        return False

    # Check every node
    for node in graph:
        if dfs(node):
            return True

    return False


# --------------------------------
# Resource Allocation Graph
# --------------------------------

graph = {
    "P1": ["R2"],
    "R2": ["P2"],
    "P2": ["R1"],
    "R1": ["P1"]
}


# --------------------------------
# Check for Cycle
# --------------------------------

print("================================")
print(" Resource Allocation Graph")
print("================================")

print("\nGraph:")

for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")


if detect_cycle(graph):
    print("\n❌ Cycle Detected!")
    print("⚠️ Possible Deadlock")
else:
    print("\n✅ No Cycle Detected")
    print("System is not in Deadlock")