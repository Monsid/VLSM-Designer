
import ipaddress
import sys


def repeats():
    answer = input("Run Again? y/n - ").lower()
    while True:
        if answer == "":
            print("you did not type anything")
            repeats()
        elif answer == "y":
            main()
            break

        else:
            sys.exit()


def justOne_calc(targetIP):


    ip = ipaddress.IPv4Network(targetIP, strict=False)

    if ip.is_private:
        print("This is a private range")
    else:
        print("\nThis is an Unclassed Range")


    print ("The Network ID is {}".format(targetIP))
    print ("The First IP assignable for an host is {}".format(ip.network_address +1))
    print ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    print ("The Broadcast address is {}".format(ip.broadcast_address))
    print ("The number of assignable IP is {}".format(ip.num_addresses -2))

def calcTwo(targetIP):

    ip = ipaddress.IPv4Network(targetIP, strict=False)

    print("\n\nThese are {} Summary Address details".format(str(ip)))

    if ip.is_private:
        print("\nThis is a private range")
    else:
        print("\nThis is an Unclassed Range")

    vone = ("\nThe Network ID is {}".format(ip.with_netmask))
    vtwo = ("The First IP assignable for an host is {}".format(ip.network_address + 1))
    vthree = ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    vfour = ("The Broadcast address is {}".format(ip.broadcast_address))
    vseven = ip.network_address
    vsix = ("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print(vone)
    print(vtwo)
    print(vthree)
    print(vfour)
    print(vsix)

    newnetwork = (vseven) + 1
    print("\n!!!Your .:!FIRST!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIRST!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    theAdress = str(ip.network_address + 1) + str(bb)

    ip = ipaddress.IPv4Network(theAdress, strict=False)

    if ip.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 1:".format(theAdress))
    print("The Network ID is {}".format(ip.with_netmask))
    print("The First IP assignable for an host is {}".format(ip.network_address + 1))
    print("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    print("The Broadcast address is {}".format(ip.broadcast_address))
    print("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print("\n!!!Your .:!SECOND!:. subnet network will begin with an IP of {}!!!".format(str(ip.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!SECOND!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = ip.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 2:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))

def calcThree(targetIP):

    ip = ipaddress.IPv4Network(targetIP, strict=False)

    print("\n\nThese are {} Summary Address details".format(str(ip)))

    if ip.is_private:
        print("\nThis is a private range")
    else:
        print("\nThis is an Unclassed Range")

    vone = ("\nThe Network ID is {}".format(ip.with_netmask))
    vtwo = ("The First IP assignable for an host is {}".format(ip.network_address + 1))
    vthree = ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    vfour = ("The Broadcast address is {}".format(ip.broadcast_address))
    vseven = ip.network_address
    vsix = ("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print(vone)
    print(vtwo)
    print(vthree)
    print(vfour)
    print(vsix)

    newnetwork = (vseven) + 1
    print("\n!!!Your .:!FIRST!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIRST!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    theAdress = str(ip.network_address + 1) + str(bb)

    ip = ipaddress.IPv4Network(theAdress, strict=False)

    if ip.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 1:".format(theAdress))
    print("The Network ID is {}".format(ip.with_netmask))
    print("The First IP assignable for an host is {}".format(ip.network_address + 1))
    print("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    print("The Broadcast address is {}".format(ip.broadcast_address))
    print("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print("\n!!!Your .:!SECOND!:. subnet network will begin with an IP of {}!!!".format(str(ip.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!SECOND!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = ip.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 2:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!THIRD!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!THIRD!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 3:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))

def calcFour(targetIP):

    ip = ipaddress.IPv4Network(targetIP, strict=False)

    print("\n\nThese are {} Summary Address details".format(str(ip)))

    if ip.is_private:
        print("\nThis is a private range")
    else:
        print("\nThis is an Unclassed Range")

    vone = ("\nThe Network ID is {}".format(ip.with_netmask))
    vtwo = ("The First IP assignable for an host is {}".format(ip.network_address + 1))
    vthree = ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    vfour = ("The Broadcast address is {}".format(ip.broadcast_address))
    vseven = ip.network_address
    vsix = ("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print(vone)
    print(vtwo)
    print(vthree)
    print(vfour)
    print(vsix)

    newnetwork = (vseven) + 1
    print("\n!!!Your .:!FIRST!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIRST!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    theAdress = str(ip.network_address + 1) + str(bb)

    ip = ipaddress.IPv4Network(theAdress, strict=False)

    if ip.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 1:".format(theAdress))
    print("The Network ID is {}".format(ip.with_netmask))
    print("The First IP assignable for an host is {}".format(ip.network_address + 1))
    print("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    print("The Broadcast address is {}".format(ip.broadcast_address))
    print("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print("\n!!!Your .:!SECOND!:. subnet network will begin with an IP of {}!!!".format(str(ip.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!SECOND!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = ip.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 2:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!THIRD!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!THIRD!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 3:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!FOURTH!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FOURTH!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 4:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))

def calcFive(targetIP):

    ip = ipaddress.IPv4Network(targetIP, strict=False)

    print("\n\nThese are {} Summary Address details".format(str(ip)))

    if ip.is_private:
        print("\nThis is a private range")
    else:
        print("\nThis is an Unclassed Range")

    vone = ("\nThe Network ID is {}".format(ip.with_netmask))
    vtwo = ("The First IP assignable for an host is {}".format(ip.network_address + 1))
    vthree = ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    vfour = ("The Broadcast address is {}".format(ip.broadcast_address))
    vseven = ip.network_address
    vsix = ("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print(vone)
    print(vtwo)
    print(vthree)
    print(vfour)
    print(vsix)

    newnetwork = (vseven) + 1
    print("\n!!!Your .:!FIRST!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIRST!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    theAdress = str(ip.network_address + 1) + str(bb)

    ip = ipaddress.IPv4Network(theAdress, strict=False)

    if ip.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 1:".format(theAdress))
    print("The Network ID is {}".format(ip.with_netmask))
    print("The First IP assignable for an host is {}".format(ip.network_address + 1))
    print("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    print("The Broadcast address is {}".format(ip.broadcast_address))
    print("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print("\n!!!Your .:!SECOND!:. subnet network will begin with an IP of {}!!!".format(str(ip.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!SECOND!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = ip.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 2:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!THIRD!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!THIRD!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 3:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!FOURTH!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FOURTH!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 4:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!FIFTH!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIFTH!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 5:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))

def CalculateSubs(targetIP):


    ip = ipaddress.IPv4Network(targetIP, strict=False)

    print("\n\nThese are {} Summary Address details".format(str(ip)))

    if ip.is_private:
        print("\nThis is a private range")
    else:
        print("\nThis is an Unclassed Range")

    vone =("\nThe Network ID is {}".format(ip.with_netmask))
    vtwo = ("The First IP assignable for an host is {}".format(ip.network_address +1))
    vthree = ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    vfour = ("The Broadcast address is {}".format(ip.broadcast_address))
    vseven = ip.network_address
    vsix = ("The number of assignable IP is {}".format(ip.num_addresses -2))
    print (vone)
    print (vtwo)
    print (vthree)
    print (vfour)
    print (vsix)

    newnetwork = (vseven) + 1
    print("\n!!!Your .:!FIRST!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork)))


#Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIRST!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0



#rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    theAdress = str(ip.network_address + 1) + str(bb)

    ip = ipaddress.IPv4Network(theAdress, strict=False)

    if ip.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 1:".format(theAdress))
    print("The Network ID is {}".format(ip.with_netmask))
    print ("The First IP assignable for an host is {}".format(ip.network_address + 1))
    print ("The Last IP assignable for an host is {}".format(ip.broadcast_address - 1))
    print ("The Broadcast address is {}".format(ip.broadcast_address))
    print("The number of assignable IP is {}".format(ip.num_addresses - 2))
    print("\n!!!Your .:!SECOND!:. subnet network will begin with an IP of {}!!!".format(str(ip.broadcast_address + 2)))


    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!SECOND!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0


    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")



    vseven = ip.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)


    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 2:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!THIRD!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!THIRD!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 3:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!FOURTH!:. subnet network will begin with an IP of {}!!!".format(str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FOURTH!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 4:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!FIFTH!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!FIFTH!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 5:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))
    print("\n!!!Your .:!SIXTH!:. subnet network will begin with an IP of {}!!!".format(
        str(newnetwork.broadcast_address + 2)))

    # Specifying ranges for allocating /notation
    x = input("Please input required number of hosts for your .:!SIXTH!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")

    vseven = newnetwork.broadcast_address + 2
    addManP = str(vseven) + str(bb)
    newnetwork = ipaddress.IPv4Network(addManP, strict=False)

    if vseven.is_private:
        print("\nThis is a Private IP range!")
    else:
        print("\nThis is an Unclassed IP range!")

    print("\nDetails for {}: Subnet 6:".format(addManP))
    print("The Network ID is {}".format(newnetwork.with_netmask))
    print("The First IP assignable for an host is {}".format(newnetwork.network_address + 1))
    print("The Last IP assignable for an host is {}".format(newnetwork.broadcast_address - 1))
    print("The Broadcast address is {}".format(newnetwork.broadcast_address))
    print("The number of assignable IP is {}".format(newnetwork.num_addresses - 2))

def main():


    # Specifying ranges for allocating /notation
    print("NOTES:")
    print("/32 = 0\n/24 = 256 - 2\n/16 = 65536 - 2 \n/8 = 16777216 - 2\n/0 = 4294967296 - 2")
    x = input("Please input required number of hosts for your .:!SUMMARY!:. subnet - ")
    xxx = range(1, 1)  # /32
    xx = range(1, 2)  # /31
    ab = range(1, 4)  # /30
    bbb = range(1, 8)  # /29
    cb = range(1, 16)  # /28
    db = range(1, 32)  # /27
    eb = range(1, 64)  # /26
    fb = range(1, 128)  # /25
    gb = range(1, 256)  # /24
    hb = range(1, 512)  # /23
    ib = range(1, 1024)  # /22
    jb = range(1, 2048)  # /21
    kb = range(1, 4096)  # /20
    lb = range(1, 8192)  # /19
    mb = range(1, 16384)  # /18
    nb = range(1, 32768)  # /17
    ob = range(1, 65536)  # /16
    pb = range(1, 131072)  # /15
    qb = range(1, 262144)  # /14
    rb = range(1, 524288)  # /13
    sb = range(1, 1048576)  # /12
    tb = range(1, 2097152)  # /11
    ub = range(1, 4194304)  # /10
    vb = range(1, 8388608)  # /9
    wb = range(1, 16777216)  # /8
    xb = range(1, 33554432)  # /7
    yb = range(1, 67108864)  # /6
    zb = range(1, 134217728)  # /5
    mar = range(1, 268435456)  # /4
    para = range(1, 536870912)  # /3
    nadar = range(1, 1073741824)  # /2
    terra = range(1, 2147483648)  # /1
    liberta = range(1, 4294967296)  # /0

    # rounding based on range into subnetmask notation
    if int(x) in ab:
        bb = ("/30")
    elif int(x) in bbb:
        bb = ("/29")
    elif int(x) in cb:
        bb = ("/28")
    elif int(x) in db:
        bb = ("/27")
    elif int(x) in eb:
        bb = ("/26")
    elif int(x) in fb:
        bb = ("/25")
    elif int(x) in gb:
        bb = ("/24")
    elif int(x) in hb:
        bb = ("/23")
    elif int(x) in ib:
        bb = ("/22")
    elif int(x) in jb:
        bb = ("/21")
    elif int(x) in kb:
        bb = ("/20")
    elif int(x) in lb:
        bb = ("/19")
    elif int(x) in mb:
        bb = ("/18")
    elif int(x) in nb:
        bb = ("/17")
    elif int(x) in ob:
        bb = ("/16")
    elif int(x) in pb:
        bb = ("/15")
    elif int(x) in qb:
        bb = ("/14")
    elif int(x) in rb:
        bb = ("/13")
    elif int(x) in sb:
        bb = ("/12")
    elif int(x) in tb:
        bb = ("/11")
    elif int(x) in ub:
        bb = ("/10")
    elif int(x) in vb:
        bb = ("/9")
    elif int(x) in wb:
        bb = ("/8")
    elif int(x) in xb:
        bb = ("/7")
    elif int(x) in yb:
        bb = ("/6")
    elif int(x) in zb:
        bb = ("/5")
    elif int(x) in mar:
        bb = ("/4")
    elif int(x) in para:
        bb = ("/3")
    elif int(x) in nadar:
        bb = ("/2")
    elif int(x) in terra:
        bb = ("/1")
    elif int(x) in liberta:
        bb = ("/0")
    elif int(x) in xx:
        print("Um....\n")
        print("I'll calculate this but, this is silly! You only have a gateway and broadcast address...")
        bb = ("/1")
    elif int(x) in xxx:
        print("Um....\n")
        print("I'll calculate this but, this is super silly! You are gonna theoretically have negative addresses!")
        bb = ("/0")

    else:
        print("I DON'T KNOW WHATS HAPPENING! IM NOT BROKEN!!! IM SORRY I DON'T UNDERSTAND YOU! PLEASE LEARN VLSM!!!")
        repeats()

    zz = input("What is the Private Network Class you wish to use? A (10.0.0.0), B (172.16.0.0), C (192.168.0.0) or D (other) - ").lower()
    if zz == "a":
        ip = "10.0.0.0"
    elif zz == "b":
        ip = "172.16.0.0"
    elif zz == "c":
        ip = "192.168.0.0"
    elif zz == "d":
        ip = input("What address would you like to use? (e.g. 14.200.1.0) - ")
    else:
        print("invalid input")

    x = (ip + bb)

    maxIs6 = input("How many subnets would you like to calculate/design? (Max is 6) - ")
    while True:
        if maxIs6 == "6":
            CalculateSubs(x)
            repeats()
        elif maxIs6 == "5":
            calcFive(x)
            repeats()
        elif maxIs6 == "4":
            calcFour(x)
            repeats()
        elif maxIs6 == "3":
            calcThree(x)
            repeats()
        elif maxIs6 == "2":
            calcTwo(x)
            repeats()
        elif maxIs6 == "1":
            justOne_calc(x)
            repeats()
        else:
            print("invalid input")
            break
main()



