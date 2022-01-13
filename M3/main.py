#####IMPORT######
import Def
####Menus########
menu_principal = ("Iniciar Sesion", "Crear Usuario", "Repetir Aventura", "Reportes", "Salir")
menu_report = ("Most used answer", "Play with more games played", "Games played by user", "Back")
#####FLAG######
Menu_Inicio = True
Menu_reports = True
#####CODIGO######
while Menu_Inicio:
    print("*"*126)
    banner = print("    ####   ######   #######    ##              ######   ##   ##           ######   ######    #####   ######    ####      ##","\n","  ##  ##   ##  ##   ##   #   ####             # ## #   ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##      ####","\n"," ##        ##  ##   ## #    ##  ##              ##     ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##     ##  ##","\n"," ##        #####    ####    ##  ##              ##     ##   ##            #####    #####   ##   ##   #####     ##     ##  ##","\n"," ##        ## ##    ## #    ######              ##     ##   ##            ##       ## ##   ##   ##   ##        ##     ######","\n","  ##  ##   ##  ##   ##   #  ##  ##              ##     ##   ##            ##       ##  ##  ##   ##   ##        ##     ##  ##","\n","   ####   #### ##  #######  ##  ##             ####     #####            ####     #### ##   #####   ####      ####    ##  ##")
    print("")
    print("                         ##   ##   ####     #####   ######    #####   ######    ####      ##")
    print("                         ##   ##    ##     ##   ##  # ## #   ##   ##   ##  ##    ##      ####")
    print("                         ##   ##    ##     #          ##     ##   ##   ##  ##    ##     ##  ##")
    print("                         #######    ##      #####     ##     ##   ##   #####     ##     ##  ##")
    print("                         ##   ##    ##          ##    ##     ##   ##   ## ##     ##     ######")
    print("                         ##   ##    ##     ##   ##    ##     ##   ##   ##  ##    ##     ##  ##")
    print("                         ##   ##   ####     #####    ####     #####   #### ##   ####    ##  ##")
    print("*"*126)
    Def.menu(menu_principal)
    opc = Def.revision(menu_principal)
    if opc == 1:
        print(1)
    if opc == 2:
        print(2)
    if opc == 3:
        print(3)
    if opc == 4:
        print(4)
        while Menu_reports:
            print("*" * 126)
            print("######")
            print("                         #     # ###### #####   ####  #####  #####")
            print("                         #     # #      #    # #    # #    #   #   ")
            print("                         ######  #####  #    # #    # #    #   #   ")
            print("                         #   #   #      #####  #    # #####    #   ")
            print("                         #    #  #      #      #    # #   #    #   ")
            print("                         #     # ###### #       ####  #    #   # ")
            print("*" * 126)
            Def.menu(menu_report)
            opc = Def.revision(menu_report)
            if opc == 1:
                print(1)
            if opc == 2:
                print(2)
            if opc == 3:
                print(3)
            if opc == 4:
                print(4)
                Menu_reports = False
    if opc == 5:
        print(5)
        Menu_Inicio = False