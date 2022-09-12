def clamp(x):
    return max(0, min(x, 255))

def rgb(r, g, b):
    #return('{:02X}{:02X}{:02X}').format(r,g,b)
    return ('{:02X}{:02X}{:02X}').format(max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255)))

print(rgb(-20,275,125))