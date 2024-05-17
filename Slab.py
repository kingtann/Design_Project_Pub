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
    print("\n\tMinimum Thickness:")
    if main_bar == 414:
        if slab_support == 'Simply Supported':
            minimum_thickness = round((slab_length*1000) / 20,2)
            ratiothickness = round(minimum_thickness/slab_thickness,2)
            print("\tThickness Minimum = L/20 mm"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\t\t",ratiothickness,"\tPASS")
            else:
                print("\t\t",ratiothickness,"\tFAIL")
        elif slab_support == 'One-end Continuous':
            minimum_thickness= round((slab_length*1000) / 24,2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\tThickness Minimum = L/24 mm"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\t\t",ratio,"\tPASS")
            else:
                print("\t\t",ratio,"\tFAIL")
        elif slab_support == 'Both-end Continuous':
            minimum_thickness = round((slab_length*1000) / 28,2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/28 mm"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\t\t",ratio,"\tPASS")
            else:
                print("\t\t",ratio,"\tFAIL")
        elif slab_support == 'Cantilever':
            minimum_thickness = round((slab_length*1000) / 10,2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/10 mm"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\t\t",ratio,"\tPASS")
            else:
                print("\t\t",ratio,"\tFAIL")
    elif main_bar < 414:
        if slab_support == 'Simply Supported':
            minimum_thickness = round((((slab_length*1000) / 20) * (0.4 + (Fymain / 700))),2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\tThickness Minimum = L/20 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\tRatio: ",ratiothickness,"\tPASS")
            else:
                print("\tRatio: ",ratiothickness,"\tFAIL")
        elif slab_support == 'One-end Continuous':
            minimum_thickness = round((((slab_length*1000) / 24) * (0.4 + (Fymain / 700))),2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/24 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\tRatio: ",ratiothickness,"\tPASS")
            else:
                print("\tRatio: ",ratiothickness,"\tFAIL")
        elif slab_support == 'Both-end Continuous':
            minimum_thickness = float((((slab_length*1000) / 28) * (0.4 + (Fymain / 700))))
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/28 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", round(minimum_thickness,2))
            if ratiothickness < 1:
                print("\tRatio: ",ratiothickness,"\tPASS")
            else:
                print("\tRatio: ",ratiothickness,"\tFAIL")
        elif slab_support == 'Cantilever':
            minimum_thickness = round((((slab_length*1000) / 10) * (0.4 + (Fymain / 700))),2)
            ratiothickness = round(minimum_thickness / slab_thickness,2)
            print("\n\tThickness Minimum = L/10 * (0.4+ (fy/700))"
                  "\n\tThickness Minimum =", minimum_thickness)
            if ratiothickness < 1:
                print("\tRatio: ",ratiothickness,"\tPASS")
            else:
                print("\tRatio: ",ratiothickness,"\tFAIL")

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
        print("\tØVc < Vu"
              "\tRatio = ", round(ratioshear,2),"\tFAIL")
    else:
        print("\tØVc > Vu"
              "\n\tRatio = ", round(ratioshear,2),"\tPASS")

    ### Design of Reinforcement
    print("\n\tDesign of Reinforcement:")

    ### Discontinuos Edge
    print("\tDiscontinuos Edge")
    rudiscon = (mudiscontedge*(10**6))/(0.9*1000*(effective_depth**2))
    print("\tRu: ",round(rudiscon,2))

    # if Mu is 0, spacing is 0
    while True:
        if rudiscon == 0:
            spacingdiscon = 0
            print("\tSpacing: ", round(spacingdiscon,2)," mm")
            break
        else:
            if fc < 27.6:
                betadiscon = 0.85
                print("\tB: ", round(betadiscon,2))
            else:
                betadiscon = 0.85 - ((0.05/7)*(fc/27.6))
                print("\tB: ", round(betadiscon,2))

            rhobalancediscon = (0.85*fc*betadiscon*600)/(Fymain*(Fymain+600))
            rhomaxdiscon = 0.75*rhobalancediscon

            if Fymain < 414:
                rhomindiscon = 0.02
            else:
                rhomindiscon = 0.018

            rhodiscon = ((0.85*fc)/Fymain) * (1-math.sqrt(1 - ((2*rudiscon)/(0.85*fc))))

            if rhomindiscon < rhodiscon < rhomaxdiscon:
                rhogoverndiscon = rhodiscon
            elif rhodiscon < rhomindiscon:
                rhogoverndiscon = rhomindiscon
            else:
                rhogoverndiscon = rhomaxdiscon

            steelareadiscon = rhogoverndiscon*1000*effective_depth
            spacingdiscon = min((0.25*math.pi*(main_bar**2)*1000),3*slab_thickness,450)
            print("\tSpacing: ",spacingdiscon,' mm')
            break

    ### Midspan
    print("\tMidspan")
    rumid = ( mumidspan * (10 ** 6)) / (0.9 * 1000 * (effective_depth ** 2))
    print("\tRu: ", round(rumid, 2))

    # if Mu is 0, spacing is 0
    while True:
        if rumid == 0:
            spacingmid = 0
            print("\tSpacing: ", round(spacingmid, 2), " mm")
            break
        else:
            if fc < 27.6:
                betamid = 0.85
                print("\tB: ", round(betamid, 2))
            else:
                betamid = 0.85 - ((0.05 / 7) * (fc / 27.6))
                print("\tB: ", round(betamid, 2))

            rhobalancemid = (0.85 * fc * betamid * 600) / (Fymain * (Fymain + 600))
            rhomaxmid = 0.75 * rhobalancemid

            if Fymain < 414:
                rhominmid = 0.02
            else:
                rhominmid = 0.018

            rhomid = ((0.85 * fc) / Fymain) * (1 - math.sqrt(1 - ((2 * rumid) / (0.85 * fc))))

            if rhominmid < rhomid < rhomaxmid:
                rhogovernmid = rhomid
            elif rhomid < rhominmid:
                rhogovernmid = rhominmid
            else:
                rhogovernmid = rhomaxmid

            steelareamid = rhogovernmid * 1000 * effective_depth
            spacingmid = min((0.25 * math.pi * (main_bar ** 2) * 1000), 3 * slab_thickness, 450)
            print("\tSpacing: ", spacingmid, ' mm')
            break

    ### Continuos Egde
    print("\tContinuous Edge")
    rucont = (mucontedge * (10 ** 6)) / (0.9 * 1000 * (effective_depth ** 2))
    print("\tRu: ", round(rucont, 2))

    # if Mu is 0, spacing is 0
    while True:
        if rucont == 0:
            spacingcont = 0
            print("\tSpacing: ", round(spacingcont, 2), " mm")
            break
        else:
            if fc < 27.6:
                betacont = 0.85
                print("\tB: ", round(betacont, 2))
            else:
                betacont = 0.85 - ((0.05 / 7) * (fc / 27.6))
                print("\tB: ", round(betacont, 2))

            rhobalancecont = (0.85 * fc * betacont * 600) / (Fymain * (Fymain + 600))
            rhomaxcont = 0.75 * rhobalancecont

            if Fymain < 414:
                rhomincont = 0.02
            else:
                rhomincont = 0.018

            rhocont = ((0.85 * fc) / Fymain) * (1 - math.sqrt(1 - ((2 * rucont) / (0.85 * fc))))

            if rhomincont < rhocont < rhomaxcont:
                rhogoverncont = rhocont
            elif rhomid < rhomincont:
                rhogoverncont = rhomincont
            else:
                rhogoverncont = rhomaxcont

            steelareacont = rhogoverncont * 1000 * effective_depth
            spacingcont = min((0.25 * math.pi * (main_bar ** 2) * 1000), 3 * slab_thickness, 450)
            print("\tSpacing: ", spacingcont, ' mm')
            break

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
    while True:
        try:
            dead = float((23.54 * slab_thickness) / 1000)
            superimposed = float(input("\n\tSuperimposed Load (Kpa): "))
            liveload = float(input("\tLive Load (Kpa): "))
            deadload = dead + superimposed
            break
        except(ValueError, ZeroDivisionError):
            print("Invalid input. Please try again with valid input!")
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
    print("\t\t\t\tOne-Way Slab Design")
    while True:
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


