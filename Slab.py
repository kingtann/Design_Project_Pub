import math


### Design 4
def design(slab_parameters,slab_loadings):
    ### Transfer Parameters

    slab_thickness = slab_parameters['Thickness']
    slab_length = slab_parameters['Length']
    slab_support = slab_parameters['Support']
    main_bar = slab_parameters['Main Bar']
    fc = slab_parameters['f\'c']
    Fymain = slab_parameters['Main Bar Fy']

    ###Transfer Loadings

    wu = slab_loadings["Wu"]
    vusimply = slab_loadings["Vu Simply"]
    vucantilever = slab_loadings["Vu Cantilever"]
    effective_depth = slab_loadings["Effective Depth"]
    slab_loadings = slab_parameters["Slab Analysis"]
    mudiscontedge = slab_loadings["Mu Discontinuous Edge"]
    mucontedge = slab_loadings["Mu Continuous Edge"]
    mumidspan = slab_loadings["Mu Midspan"]

    ### Minimum Thickness
    print("\nDESIGN")
    print("\tMinimum Thickness:")
    if main_bar == 414:
        if slab_support == 'Simply Supported':
            minimum_thickness = round((slab_length*1000) / 20,2)
            ratiothickness = round(minimum_thickness/slab_thickness,2)
            print("\tThickness Minimum = L/20 mm"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("FAIL")
        elif slab_support == 'One-end Continuous':
            minimum_thickness= round((slab_length*1000) / 24,2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/24 mm"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")
        elif slab_support == 'Both-end Continuous':
            minimum_thickness = round((slab_length*1000) / 28,2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/28 mm"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")
        elif slab_support == 'Cantilever':
            minimum_thickness = round((slab_length*1000) / 10,2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/10 mm"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")
    elif main_bar < 414:
        if slab_support == 'Simply Supported':
            minimum_thickness = round((((slab_length*1000) / 20) * (0.4 + (Fymain / 700))),2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/20 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")
        elif slab_support == 'One-end Continuous':
            minimum_thickness = round((((slab_length*1000) / 24) * (0.4 + (Fymain / 700))),2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/24 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")
        elif slab_support == 'Both-end Continuous':
            minimum_thickness = float((((slab_length*1000) / 28) * (0.4 + (Fymain / 700))))
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/28 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", round(minimum_thickness,2),
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")
        elif slab_support == 'Cantilever':
            minimum_thickness = round((((slab_length*1000) / 10) * (0.4 + (Fymain / 700))),2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/10 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", minimum_thickness,
                  "\n\tRatio = ", ratiothickness)
            if ratiothickness < 1:
                print("\t\tPASS")
            else:
                print("\t\tFAIL")

    ### Design for shear
    print("\n\tDesign of Shear:")
    while True:
        if slab_support == 'Simply Supported' or 'One-end Continuous' or 'Both-end Continuous':
            vu = round(vusimply,2)
            print("\tVu = ", vu," kN")
            break
        elif slab_support == 'Cantilever':
            vu = round(vucantilever,2)
            print("\tVu = ", vu," kN")
            break

    print("\tØVc = 0.75 1/6 √f'c bwd")
    vc = 0.75*(1/6)*math.sqrt(fc)*effective_depth
    print("\tØVc = ",round(vc,2), " KN")
    ratioshear = vu / vc

    if ratioshear > 1:
        print("\tØVc > Vu"
              "\tRatio = ", round(ratioshear,2),"  PASS")
    else:
        print("\tØVc > Vu"
              "\n\tRatio = ", round(ratioshear,2),"  FAIL!!!")

    # ### Design of Reinforcement
    # print("\n\tDesign of Reinforcement:")
    # ### Discontinuos Edge
    # print("\tDiscontinuos Edge")
    # mu = mudiscontedge
    # ru = (mu*(10**6))*0.9*1000*(effective_depth**2)
    #
    # while True:
    #     if ru == 0:
    #         spacing = 0
    #         break
    #     else:
    #         while True:
    #             ## beta angle
    #             if fc < 27.6:
    #                 beta = 0.8
    #                 break
    #             else:
    #                 beta = 0.85 - ((0.05/7)*(fc-27.6))
    #                 break
    #
    #             rhobalance = (0.85*fc*beta*600) / (Fymain*(Fymain*600))
    #             rhomax = rhobalance *0.75
    #             ###rhomin
    #             while True:
    #                 if main_bar < 414:
    #                     rhomin = 0.002
    #                     break
    #                 else:
    #                     rhomin = 0.0018
    #                     break
    #
    #             rho = 0.85*(fc/Fymain)*(math.sqrt(1-((2*beta)/(0.85*fc))))
    #             while True:
    #                 if rhomin < rho < rhomax:
    #                     rhogovern = rho
    #                     break
    #
    #                 while True:
    #                     if rho < rhomin:
    #                         rhogovern = rhomin
    #                     else:
    #                         rhogovern = rho
    #                     break
    #             print(rhogovern)
    #             steelarea = rhogovern*effective_depth*1000
    #             spacing = min(((math.pi*(main_bar**2)*1000)/4)/steelarea,(slab_thickness*3),450)
    #             print(spacing)
    #
    #


### ANALYSIS 3
def analysis(slab_parameters):
    slab_loadings = {}
    ### Transfer Paramaters
    slab_thickness = slab_parameters['Thickness']
    slab_length = slab_parameters['Length']
    fc = slab_parameters['f\'c']
    slab_support = slab_parameters['Support']
    main_bar = slab_parameters['Main Bar']
    temp_bar = slab_parameters['Temp Bar']

    ### Loadings
    print("\nANALYSIS")
    dead = float((23.54 * slab_thickness) / 1000)
    superimposed = float(input("\n\tSuperimposed Load (Kpa): "))
    liveload = float(input("\tLive Load (Kpa): "))
    deadload = dead + superimposed
    ### Ultimate Load
    USD1 = 1.4 * deadload
    USD2 = (1.2*deadload) + (1.6*liveload)
    wu = max(USD1,USD2)
    print("\n\tUltimate Load"
          "\n\tUSD1 = 1.4DL Kpa"
          "\n\tUSD1 =", round(USD1,3)," Kpa",
          "\n\tUSD2 = 1.2DL + 1.6LL Kpa"
          "\n\tUSD2 =", round(USD2,3)," Kpa",
          "\n\tWu =", round(wu,3)," Kpa")
    ### Ultimate Moment
    print("\n\tUltimate Moment")
    while True:
        if slab_support == 'Simply Supported':
            mudiscontedge = 0
            mumidspan = float((wu * (slab_length ** 2)) / 8)
            mucontedge = 0
            break
        elif slab_support == 'One-end Continuous':
            mudiscontedge = float((wu * (slab_length ** 2)) / 24)
            mumidspan = float((wu * (slab_length ** 2)) / 14)
            mucontedge = float((wu * (slab_length ** 2)) / 10)
            break
        elif slab_support == 'Both-end Continuous':
            mudiscontedge = 0
            mumidspan = float((wu * (slab_length ** 2)) / 16)
            mucontedge = float((wu * (slab_length ** 2)) / 11)
            break
        elif slab_support == 'Cantilever':
            mudiscontedge = 0
            mumidspan = 0
            mucontedge = float((wu * (slab_length ** 2)) / 2)
            break
    print("\tMu Discontinuous:", round(mudiscontedge,2)," KN/m",
          "\n\tMu Midspan:", round(mumidspan,2)," KN/m",
          "\n\tMu Continuous:", round(mucontedge,2)," KN/m")
    ## Ultimate Shear
    print("\n\tUltimate Shear")
    vusimply = (wu * slab_length) / 2
    vucantilever = wu * slab_length
    print("\tVu Simply Supported:",round(vusimply,2)," KN",
          "\n\tVu Cantilever:",round(vucantilever,2)," KN")

    ### Effective Depth
    effective_depth = float(slab_thickness - 20 - (10 / 2))

    slab_loadings["DL"] = deadload
    slab_loadings["LL"] = liveload
    slab_loadings["Wu"] = wu
    slab_loadings["Mu Discontinuous Edge"] = mudiscontedge
    slab_loadings["Mu Continuous Edge"] = mucontedge
    slab_loadings["Mu Midspan"] = mumidspan
    slab_loadings["Vu Simply"] = vusimply
    slab_loadings["Vu Cantilever"] = vucantilever
    slab_loadings["Effective Depth"] = effective_depth
    slab_parameters["Slab Analysis"] = slab_loadings
    return slab_loadings



### PARAMETERS 2
def parameters():
    slab_parameters = {}
    ### Slab Tag
    print("\nSLAB PARAMETERS")
    slab_tag = input("\n\tSlab Tag: ")
    ### Concrete Strength
    while True:
        try:
            fc = float(input("\tConcrete Strength (f'c (MPa)): "))
            break
        except ValueError:
            print("\n\tInvalid input. Please enter a valid number for Concrete Strength.")

    ### Slab Length
    while True:
        try:
            slab_length = float(input("\tLength: "))
            break
        except ValueError:
            print("\n\tInvalid input. Please enter a valid number for Slab Length")
    ### Support
    while True:
        chosen_support = input("\n\tType of Support: \n"
                               "\t\tA. Simply Supported\n"
                               "\t\tB. One-end Continuous\n"
                               "\t\tC. Both-end Continuous\n"
                               "\t\tD. Cantilever\n"
                               "\n\tSelect Type of Support : ")
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
            print("\n\tUnsupported Answer.\n"
                  "\tPlease select again: ")
    ### Thickness
    while True:
        user_input_ilt = input("\tInitial Slab Thickness: 125mm (Continue? Y/N) ")
        if user_input_ilt.lower() == 'n':
            while True:
                try:
                    slab_thickness = int(input('\tInput thickness (mm): '))
                    break
                except ValueError:
                    print("\tInvalid input. Please enter a valid slab thickness (mm).")
            break
        elif user_input_ilt.lower() == 'y':
            slab_thickness = 125
            break
        else:
            print("\tInvalid input. Please enter either 'Y' or 'N'.")
    ### Rebars
    while True:
        user_input_irs = input("\tInitial Rebars: Ø10 for both Main and Temp Bars (Continue? Y/N) ")
        if user_input_irs.lower() == 'n':
            while True:
                try:
                    main_bar = int(input('\tInput Main Bar: '))
                    if main_bar <= 10:
                        Fymain = 276
                    else:
                        Fymain = 414
                    temp_bar = int(input('\tInput Temperature Bar: '))
                    if temp_bar <= 10:
                        Fytemp = 276
                    else:
                        Fytemp = 414
                    break
                except ValueError:
                        print("\tInvalid input. Please enter a valid bar diameter.")
        elif user_input_irs.lower() == 'y':
            main_bar = 10
            Fymain = 276
            temp_bar = 10
            Fytemp = 276
            break
        else:
            print("\tInvalid input. Please enter either 'Y' or 'N'.")
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
        print("\t\t\t\tOne-Way Slab Design")
        open_input = input("\nOpen Slab Analysis Program? Y/N : ")
        if open_input.lower() == 'n':
            break
        if open_input.lower() == 'y':
            slab_parameters = parameters()
            slab_loadings = analysis(slab_parameters)
            design(slab_parameters, slab_loadings)





slab = {}
slab_analysis()
print()

for key, value in slab.items():
    print(key, ":")
    for inner_key, inner_value in value.items():
        print("  ", inner_key, ":", inner_value)


