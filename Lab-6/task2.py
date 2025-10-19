def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move remaining largest disk to destination
    print(f"Move disk {n} from {source} → {destination}")

    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Example: 3 disks, rods A, B, C
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
