def support_list(chosen_support, slab_length):
    while True:
        if chosen_support.lower() == 'a':
            slab_support = slab_length/20
        elif chosen_support.lower() == 'b':
            slab_support = slab_length/24
        elif chosen_support.lower() == 'c':
            slab_support = slab_length/28
        elif chosen_support.lower() == 'd':
            slab_support = slab_length/10
        else:
            print("Unsupported answer.")
            return False
        return slab_support

def input_parameters():
    slab_tag = input("Slab Tag: ")
    slab_length = float(input("Length: "))

    slab_parameters['slab_tag'] = slab_tag
    slab_parameters['slab_length'] = slab_length

    chosen_support = input("Select type of support\n"
                           " A. Simply Supported\n"
                           " B. One-end Continuous\n"
                           " C. Both-end Continuous\n"
                           " D. Cantilever\n")

    slab_parameters['slab_support'] = support_list(chosen_support, slab_length)

def slab_analysis():
    while True:
        open_input = input("Open Slab Analysis Program? Y/N : ")
        if open_input.lower() == 'n':
            break
        if open_input.lower() == 'y':
            input_parameters()

slab_parameters = {}
slab_analysis()
print(slab_parameters)
# for parameters, value in slab_parameters:
#     print(parameters, " : ", value)
