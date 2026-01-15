class Statistics:
    def __init__(self):
        self.numbers = []
    
    def add_num(self,num):
        number = int(num)
        self.numbers.append(number)
    
    def display_num(self):
        extra_table = []
        for n in self.numbers:
            extra_table.append(str(n))
        return ', '.join(extra_table)
        #return ', '.join(str(n) for n in self.numbers)
    
    def greatest_num(self):
        return f'The greatest number: {max(self.numbers)}'
    
    def smallest_num(self):
        return f'The smallest number: {min(self.numbers)}'
    
    def arithmetic_mean(self):
        sum = 0
        for n in self.numbers:
            sum+=n
        result = sum/len(self.numbers)
        return f'Arithmetic mean: {result:.2f}'.replace('.',',')
    
    def median(self):
        sorted_table = sorted(self.numbers)
        if len(self.numbers)%2==1:
            x = (len(self.numbers)//2)
            return f'Median: {sorted_table[x]}'
        else:
            x = len(self.numbers)/2
            result = (sorted_table[x]+sorted_table[x+1])/2
            return f'Median: {result}'.replace('.',',')
def main():
    my_numbers = Statistics()
    my_numbers.add_num(12)
    my_numbers.add_num(37)
    my_numbers.add_num(6)
    my_numbers.add_num(9)
    my_numbers.add_num(17)

    print(my_numbers.display_num())
    print(my_numbers.greatest_num())
    print(my_numbers.smallest_num())
    print(my_numbers.arithmetic_mean())
    print(my_numbers.median())

if __name__ == '__main__':
    main()
        