class metrica:
    def __init__(self, v1, v2, coefRest = 0.3, fr = 0, r1 = None, r2 = None, m1 = None, m2 = None):
        self.fr = fr # frictional force
        self.r1 = r1 # radius of ball 1
        self.r2 = r2 # radius of ball 2
        self.v1 = v1 # velocity of ball 1
        self.v2 = v2 # velocity of ball 2
        self.coefRest = coefRest # Coefficient of Restitution (0.3 - 0.5)
        self.elastic = True 
        return 

    def compute(self):
        nv1, nv2 = None, None 
        if self.v2 == 0:
            # only ball 2 is static
            nv1 = (self.v1* (1 + self.coefRest))/2
            nv2 = self.v1 - nv1
        elif self.v1 == 0:
            # only ball 1 is static
            nv1 = (self.v2 * (1+self.coefRest))/2
            nv2 = self.v2 - nv1 
        else:
            # that is, none of the ball is static
            if self.elastic == True: # else, it's inelastic
                

        return nv1, nv2