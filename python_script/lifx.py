from packet import Packet

if __name__ == "__main__":
    with open("ip.txt") as f:
        ip_list = f.readlines()

    light_control = Packet(ip_list[0])

    print("""LIFX Light Controller\n""")

    print("List of lights:")
    for ip in ip_list:
        print(ip)
    
    print("""Control Keys:
                o) On
                p) off 
                h 0-360) Hue
                b 0 - 100) Brightness
                s 0 - 100) Saturation
                q) Quit""")

    print(u"\u001b[38;2;255;255;255;48;2;255;0;0m 0",
            u"\u001b[38;2;0;0;0;48;2;255;128;0m 30",
            u"\u001b[38;2;0;0;0;48;2;255;255;0m 60",
            u"\u001b[38;2;0;0;0;48;2;128;255;0m 90",
            u"\u001b[38;2;0;0;0;48;2;0;255;0m 120",
            u"\u001b[38;2;0;0;0;48;2;0;255;128m 150",
            u"\u001b[38;2;0;0;0;48;2;0;255;255m 180",
            u"\u001b[38;2;255;255;255;48;2;0;128;255m 210",
            u"\u001b[38;2;255;255;255;48;2;0;0;255m 240",
            u"\u001b[38;2;255;255;255;48;2;128;0;255m 270",
            u"\u001b[38;2;255;255;255;48;2;255;0;255m 300",
            u"\u001b[38;2;255;255;255;48;2;255;0;128m 330",
            u"\u001b[38;2;255;255;255;48;2;255;0;4m 360",
            u"\u001b[0m")

    while True:
        options = list(input("Please enter option and value if applicable: ").split())

        if options[0] == "o":
            light_control.on()
        elif options[0] == "p":
            light_control.off()
        elif options[0] == "h":
            light_control.change_color(0,0,80)
        elif options[0] == "b":
            pass 
        elif options[0] == "s":
            pass 
        elif options[0] == "q":
            break
        else:
            print("That was not a valid command")

        print(light_control)