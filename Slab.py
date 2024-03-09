# slab_tag = input()
# slab_thickness = int(input())  # mm unit
# tributary_length = float(input())  # m unit
# concrete_strength = float(input())  # list of choices
# support = ()  # list of choices
# bar_diameter = ()  # list of choices
# bars_strength = ()  # list of choices
# loading = float(input())  # for SDL and LL

# Define a list to store slabs
slabs = []


# Function to add a slab to the list
def add_slab():
    tag = input("Input Slab Tag: ")
    thickness = float(input("Input Slab Thickness: "))
    length = float(input("Input Slab Length: "))
    load = float(input("Input Slab Load: "))

    slab = {
        'tag': tag,
        'thickness': thickness,
        'length': length,
        'load': load
    }
    slabs.append(slab)


# Example usage:

while True:
        user_input = input("Define Slab? Y/N: ")
        if user_input.lower() == "n":
            break
        if user_input.lower() == "y":
            add_slab()


# Print the list of slabs
print("\nList of Slabs:")
for i, slab in enumerate(slabs, 1):
    print(f"Slab {i}: Tag={slab['tag']}, Thickness={slab['thickness']}, Length={slab['length']}, Load={slab['load']}")
