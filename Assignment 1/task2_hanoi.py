
# Tower of Hanoi Implementation

def tower_of_hanoi(n, source, dest, aux):
    # Base Case: If there is only 1 disk, move it directly from Source to Destination
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    
    # Step 1: Move top (n-1) disks from Source to Auxiliary (using Destination as helper)
    tower_of_hanoi(n - 1, source, aux, dest)
    
    # Step 2: Move the nth (the largest) disk from Source to Destination
    print(f"Move disk {n} from {source} to {dest}")
    
    # Step 3: Move the (n-1) disks from Auxiliary to Destination (using Source as helper)
    tower_of_hanoi(n - 1, aux, dest, source)

# Execution for N=3 trace
print("Tower of Hanoi Trace (N=3):")
tower_of_hanoi(3, 'A', 'C', 'B')