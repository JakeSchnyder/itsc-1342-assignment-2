# Jake Schnyder - Assignment 2

def evaluate_packet(port, packet_size_bytes):

    # If port is equal to 80 or port is equal to 443, return "STANDARD_WEB_TRAFFIC". Otherwise (for any other port), check packet_size_bytes:
    if(port == 80 or port == 443):
        return("STANDARD_WEB_TRAFFIC")
    #If packet_size_bytes is greater than 1500, return "SUSPICIOUS_LARGE_PACKET".
    if(packet_size_bytes>1500):
        return("SUSPICIOUS_LARGE_PACKET")
    #If packet_size_bytes is less than 64, return "SUSPICIOUS_SMALL_PACKET".
    elif(packet_size_bytes<64):
        return("SUSPICIOUS_SMALL_PACKET")
    #For any other packet size, return "NORMAL_INTERNAL_TRAFFIC".
    else:
        return("NORMAL_INTERNAL_TRAFFIC")
    pass