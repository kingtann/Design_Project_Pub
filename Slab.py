
def minimum_thickness():
    def min_thickness_fy_414(chosen_support, slab_length):
        while True:
            if chosen_support.lower() == 'a':
                slab_support = slab_length / 20
            elif chosen_support.lower() == 'b':
                slab_support = slab_length / 24
            elif chosen_support.lower() == 'c':
                slab_support = slab_length / 28
            elif chosen_support.lower() == 'd':
                slab_support = slab_length / 10
            else:
                print("Unsupported answer.")
                return False
    def min_thickness_fy_lessthan_414(chosen_support, slab_length, Fy):
        while True:
            if chosen_support.lower() == 'a':
                minimum_thickness = ((slab_length / 20) * (0.4 + (Fy / 700)))
            elif chosen_support.lower() == 'b':
                minimum_thickness = ((slab_length / 24) * (0.4 + (Fy / 700)))
            elif chosen_support.lower() == 'c':
                minimum_thickness = ((slab_length / 28) * (0.4 + (Fy / 700)))
            elif chosen_support.lower() == 'd':
                minimum_thickness = ((slab_length / 10) * (0.4 + (Fy / 700)))
            else:
                print("Unsupported answer.")
                return False




def global_parameter():

    ## Concrete Strength
    while True:
        try:
            fc = float(input("Concrete Strength (f'c (MPa)): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Concrete Strength.")

    def input_parameters():
        slab_tag = input("Slab Tag: ")
        slab_length = float(input("Length: "))

        ## Support
        while True:
            chosen_support = input("Type of Support: \n"
                                   " A. Simply Supported\n"
                                   " B. One-end Continuous\n"
                                   " C. Both-end Continuous\n"
                                   " D. Cantilever\n"
                                   "Select Type of Support : ")
            if chosen_support.lower() == 'a':
                slab_support = 'Simply Supported'
                break
            elif chosen_support.lower() == 'b':
                slab_support = 'One-end Continous'
                break
            elif chosen_support.lower() == 'c':
                slab_support = 'Both-end Continous'
                break
            elif chosen_support.lower() == 'd':
                slab_support = 'Cantilever'
                break
            else:
                print("Unsupported Answer.\n"
                      "Please select again: ")

        ## Thickness
        while True:
            user_input_ilt = input("Initial Slab Thickness: 125mm (Continue? Y/N) ")
            if user_input_ilt.lower() == 'n':
                while True:
                    try:
                        slab_thickness = int(input('Input thickness (mm): '))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid slab thickness (mm).")
                break
            elif user_input_ilt.lower() == 'y':
                slab_thickness = 125
                break
            else:
                print("Invalid input. Please enter either 'Y' or 'N'.")


        ## Rebars

        while True:
            user_input_irs = input("Initial Rebars: Ø10 for both Main and Temp Bars (Continue? Y/N) ")
            if user_input_irs.lower() == 'n':
                while True:
                    try:
                        main_bar = int(input('Input Main Bar: '))
                        if main_bar <= 10:
                            Fy = 276
                        else:
                            Fy = 414
                        temp_bar = int(input('Input Temperature Bar: '))
                    except ValueError:
                        print("Invalid input. Please enter a valid bar diameter.")
                break
            elif user_input_irs.lower() == 'y':
                main_bar = 10
                if main_bar <= 10:
                    Fy = 276
                else:
                    Fy = 414
                temp_bar = 10
                break
            else:
                print("Invalid input. Please enter either 'Y' or 'N'.")

        slab_parameters['Tag'] = slab_tag
        slab_parameters['Thickness'] = slab_thickness
        slab_parameters['Length'] = slab_length
        slab_parameters['f\'c'] = fc
        slab_parameters['Support'] = slab_support
        slab_parameters['Main Bar'] = main_bar
        slab_parameters['Temp Bar'] = temp_bar

        print()

        return slab_parameters


    return input_parameters()


def slab_analysis():
    while True:
        open_input = input("Open Slab Analysis Program? Y/N : ")
        if open_input.lower() == 'n':
            break
        if open_input.lower() == 'y':
            global_parameter()







slab_parameters = {}
slab_analysis()
print()
for key, value in slab_parameters.items():
    print(key, " : ", value)
# for parameters, value in slab_parameters:
#     print(parameters, " : ", value)
