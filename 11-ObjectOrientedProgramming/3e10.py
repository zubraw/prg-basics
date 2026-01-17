class C:
    def __init__(self, list):
        self.list = list
    
    def m(self, n):
        counter = 0
        for point in self.list:
            if len(point)==2:
                if point[0]>0 and point[1]>0:
                    counter+=1
        if counter>=n:
            return True
        else:
            return False
    
def main():
    coords = [[2,3],[1,8],[-6,4],[3,-7]]
    obj = C(coords)

    print(obj.m(2))
    print(obj.m(3))

if __name__ == '__main__':
    main()
