### Design 4
def design(slab_parameters,wu):
    ### Transfer Parameters
    slab_thickness = slab_parameters['Thickness']
    slab_length = slab_parameters['Length']
    slab_support = slab_parameters['Support']
    main_bar = slab_parameters['Main Bar']

    ### Minimum Thickness
    if main_bar == 414:
        if slab_support == 'Simply Supported':
            minimum_thickness = round((slab_length*1000) / 20,2)
            ratio = round(minimum_thickness/slab_thickness,2)
            print("Thickness Minimum = L/20 mm"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
        elif slab_support == 'One-end Continuous':
            minimum_thickness= round((slab_length*1000) / 24,2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/24 mm"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
        elif slab_support == 'Both-end Continuous':
            minimum_thickness = round((slab_length*1000) / 28,2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/28 mm"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
        elif slab_support == 'Cantilever':
            minimum_thickness = round((slab_length*1000) / 10,2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/10 mm"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
    elif main_bar < 414:
        if slab_support == 'Simply Supported':
            minimum_thickness = round((((slab_length*1000) / 20) * (0.4 + (main_bar / 700))),2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/20 * (0.4+ (fy/700))"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
        elif slab_support == 'One-end Continuous':
            minimum_thickness = round((((slab_length*1000) / 24) * (0.4 + (main_bar / 700))),2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/24 * (0.4+ (fy/700))"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
        elif slab_support == 'Both-end Continuous':
            minimum_thickness = round((((slab_length*1000) / 28) * (0.4 + (main_bar / 700))),2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/28 * (0.4+ (fy/700))"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")
        elif slab_support == 'Cantilever':
            minimum_thickness = round((((slab_length*1000) / 10) * (0.4 + (main_bar / 700))),2)
            ratio = round(minimum_thickness / slab_thickness,2)
            print("Thickness Minimum = L/10 * (0.4+ (fy/700))"
                  "\nThickness Minimum =", minimum_thickness,
                  "\nRatio = ", ratio)
            if ratio < 1:
                print("PASS")
            else:
                print("FAIL")

    ### Design for shear
    print("\nDesign for Shear")
    Vu = wu
    print(Vu)


### ANALYSIS 3
def analysis(slab_parameters):
    ### Transfer Paramaters
    slab_thickness = slab_parameters['Thickness']
    slab_length = slab_parameters['Length']
    fc = slab_parameters['f\'c']
    slab_support = slab_parameters['Support']
    main_bar = slab_parameters['Main Bar']
    temp_bar = slab_parameters['Temp Bar']
    ### Loadings
    dead = (24 * slab_thickness) / 1000
    superimposed = float(input("Superimposed Load (Kpa): "))
    liveload = float(input("Live Load (Kpa): "))
    deadload = dead + superimposed
    ### Ultimate Load
    USD1 = 1.4 * deadload
    USD2 = (1.4*deadload) + (1.6*liveload)
    wu = max(USD1,USD2)
    print("\n"
          "USD1 = 1.4DL Kpa\n"
          "USD1 =", round(USD1,3)," Kpa",
          "\nUSD2 = 1.2DL + 1.6LL Kpa\n"
          "USD2 =", round(USD2,3)," Kpa",
          "\nWu =", round(wu,3)," Kpa")
    ### Ultimate Moment
    print("\nUltimate Moment")
    while True:
        if slab_support == 'Simply Supported':
            mudiscontedge = 0
            mumidspan = (wu * (slab_length ** 2)) / 8
            mucontedge = 0
            break
        elif slab_support == 'One-end Continuous':
            mudiscontedge = (wu * (slab_length ** 2)) / 24
            mumidspan = (wu * (slab_length ** 2)) / 14
            mucontedge = (wu * (slab_length ** 2)) / 10
            break
        elif slab_support == 'Both-end Continuous':
            mudiscontedge = 0
            mumidspan = (wu * (slab_length ** 2)) / 16
            mucontedge = (wu * (slab_length ** 2)) / 11
            break
        elif slab_support == 'Cantilever':

            mucontedge = (wu * (slab_length ** 2)) / 2
            break
    print("Mu Discontinuous:", round(mudiscontedge,2)," KN/m",
          "\nMu Midspan:", round(mumidspan,2)," KN/m",
          "\nMu Continuous:", round(mucontedge,2)," KN/m")
    ## Ultimate Shear
    print("\nUltimate Shear")
    vusimple = (wu * slab_length) / 2
    vucantilever = wu * slab_length
    print("Vu Simply Supported:",round(vusimple,2)," KN",
          "\nVu Cantilever:",round(vucantilever,2)," KN")

    ### Effective Depth
    effective_depth = slab_thickness - 20 - (10 / 2)

    return wu



### PARAMETERS 2
def parameters():
    slab_parameters = {}
    ### Concrete Strength
    while True:
        try:
            fc = float(input("Concrete Strength (f'c (MPa)): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Concrete Strength.")
    ### Slab Tag
    slab_tag = input("Slab Tag: ")
    ### Slab Length
    while True:
        try:
            slab_length = float(input("Length: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Slab Length")
    ### Support
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
            slab_support = 'One-end Continuous'
            break
        elif chosen_support.lower() == 'c':
            slab_support = 'Both-end Continuous'
            break
        elif chosen_support.lower() == 'd':
            slab_support = 'Cantilever'
            break
        else:
            print("Unsupported Answer.\n"
                  "Please select again: ")
    ### Thickness
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
    ### Rebars
    while True:
        user_input_irs = input("Initial Rebars: Ø10 for both Main and Temp Bars (Continue? Y/N) ")
        if user_input_irs.lower() == 'n':
            while True:
                try:
                    main_bar = int(input('Input Main Bar: '))
                    if main_bar <= 10:
                        Fymain = 276
                    else:
                        Fymain = 414
                    temp_bar = int(input('Input Temperature Bar: '))
                    if temp_bar <= 10:
                        Fytemp = 276
                    else:
                        Fytemp = 414
                    break
                except ValueError:
                        print("Invalid input. Please enter a valid bar diameter.")
        elif user_input_irs.lower() == 'y':
            main_bar = 10
            Fymain = 276
            temp_bar = 10
            Fytemp = 276
            break
        else:
            print("Invalid input. Please enter either 'Y' or 'N'.")
        break

    slab_parameters['Thickness'] = slab_thickness
    slab_parameters['Length'] = slab_length
    slab_parameters['f\'c'] = fc
    slab_parameters['Support'] = slab_support
    slab_parameters['Main Bar'] = main_bar
    slab_parameters['Main Bar Fy'] = Fymain
    slab_parameters['Temp Bar'] = temp_bar
    slab_parameters['Main Bar Fy'] = Fytemp
    slab[slab_tag] = slab_parameters
    return slab_parameters


### SLAB ANALYSIS 1
def slab_analysis():
    while True:
        open_input = input("\n"
                           "Open Slab Analysis Program? Y/N : ")
        if open_input.lower() == 'n':
            break
        if open_input.lower() == 'y':
            slab_parameters = parameters()
            analysis(slab_parameters)
            design(slab_parameters,analysis)





slab = {}
slab_analysis()
print()

for key, value in slab.items():
    print(key, ":")
    for inner_key, inner_value in value.items():
        print("  ", inner_key, ":", inner_value)

