print("LFE5U-12-TG144")
print("")
print("Pin, Unit, Type, Name")
ln = 0

with open("../FPGA-SC-02032-2-0-ECP5U-12-Pinout.csv") as f:

    for l in f:
        ll = l.strip().split(',')

        ln += 1

        if ln < 10:
            continue

#        print (ln, ll)

        if ll[10] != '-':
            pn = ""

            if ll[4][0] == 'C':
                pn = "-"
            if ll[4][0] == 'T':
                pn = "+"
            
            p = ""
            p += ll[1]
            if pn:
                p += "/" + pn

            if ll[5] != '-':
                p += "/HS"

            if ll[6] != '-':
                p += "/" + ll[6]

            if ll[3] != '-':
                p += "/" + ll[3]

            if ll[2] != '-':
                b = ll[2]

            t = "bidirectional"

            if ll[1][0:3] == 'GND':
                t = "power_out"
            if ll[1][0:3] == 'VCC':
                t = "power_in"
            if ll[1][0:3] == 'VSS':
                t = "power_out"

            print(ll[10] + "," + b + "," + t + "," + p)
