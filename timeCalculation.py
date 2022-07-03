def add_time(time, toadd, d="noday"):
    a = [time, toadd, d]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    c = a[0].split()
    minadd = (int(a[1].split(":")[0]) * 60) + int(a[1].split(":")[1]) #calculate total minutes to add
    if a[0].split()[1] == "PM": #check if AM or PM if PM add 12 hours
        totminutes = ((int(c[0].split(':')[0]) + 12) * 60) + int(c[0].split(':')[1]) #convert time hh:mm to minutes
    else:
        totminutes = (int(c[0].split(':')[0]) * 60) + int(c[0].split(':')[1]) #convert time hh:mm to minutes
    #print("totmin " + str(totminutes))
    totminutes = int(totminutes) + minadd
    #print(totminutes)
    h = str(totminutes / 60).split(".")[0]
    m = str(totminutes % 60).zfill(2)
    day = str(int(h) / 24).split(".")[0]
    mer = "AM"

    if int(day) > 0:
        h = int(h) % 24
        if int(h) >= 12:
            mer = "PM"
            h = int(h) - 12
        elif int(h) == 12:
            mer = "PM"
        elif int(h) == 0:
            h = 12
        if a[2] != "noday":
            dp = (days.index(a[2].casefold()) + int(day)) % 7
            if int(day) == 1:
                return(str(h) + ":" + str(m) + " " + mer + ", " + days[dp].capitalize() + " (next day)")
            else:
                return(
                    str(h) + ":" + str(m) + " " + mer + ", " + days[dp].capitalize() + " (" + str(day) + " days later)")
        else:
            if int(day) == 1:
                return(str(h) + ":" + str(m) + " " + mer + " " + "(next day)")
            else:
                return(str(h) + ":" + str(m) + " " + mer + " (" + str(day) + " days later)")

    else:
        if int(h) > 12:
            mer = "PM"
            h = int(h) - 12
        elif int(h) == 12:
            mer = "PM"
        elif int(h) == 0:
            h = int(h)
        if a[2] != "noday":
            dp = (days.index(a[2].casefold()) + int(day)) % 7
            return(str(h) + ":" + str(m) + " " + mer + ", " + days[dp].capitalize())
        else:
            return(str(h) + ":" + str(m) + " " + mer)