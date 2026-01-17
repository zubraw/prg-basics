class C:
    def __init__(self, stadium):
        self.stadium = stadium
    
    def m1(self, s, n):
        number = int(n)
        fsector = s.upper()
        self.stadium[fsector] = number
    
    def m2(self, s):
        sectors= s.upper()
        total = 0
        for sector in sectors:
            if sector in self.stadium:
                total += self.stadium[sector]
            else:
                total = total
        return total
    
def main():
    camp_nou = {"A":120,"D":150,"G":90,"K":110}
    obj = C(camp_nou)
    obj.m1("G",130)
    print(obj.m2("GD"))
    print(obj.m2("KEJ"))

if __name__ == '__main__':
    main()
