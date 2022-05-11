def conditionNumber(M):
    inverseNorm = 0
    for i in range(12):
        r =  random()*10
        theta = random()*2*pi
        phi = random() * pi
        v = vector([r*sin(phi)*cos(theta),r*sin(phi)*sin(theta),r*cos(phi)])
        z = M*v
        temp = z.norm()/v.norm()
        if(temp > inverseNorm):
            inverseNorm = temp
    return n(M.norm()*inverseNorm)
