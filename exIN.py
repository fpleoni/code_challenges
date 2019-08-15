# Find duplicates in a list using classes

# This first class is slower, but uses less memory
class DupesFinder(object):
    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers

    def find(self):
        counter = 0
        repeated = []
        for number in self.list_of_numbers:
            for element in self.list_of_numbers:
                if element == number:
                    counter += 1
                if counter > 1 and element not in repeated:
                    repeated.append(element)
            counter = 0
        return repeated    

# This class is faster, but takes up more memory
class FastDupesFinder(DupesFinder):
    def __init__(self, list_of_numbers):
        self.dupes_dict = {}
        super().__init__(list_of_numbers)

    def show_all_count(self):
        self.find()
        return self.dupes_dict
    
    def find(self):
        for number in self.list_of_numbers:
            if number in self.dupes_dict.keys():
                self.dupes_dict[number] = self.dupes_dict[number]+1
            else:
                self.dupes_dict[number] = 1
        results = []
        for key, value in self.dupes_dict.items():
            if value > 1:
                results.append(key)
        print("I'm faster!!")
        return results

                
# testing out the classes               
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 6, 7, 11, 11]

print(DupesFinder(my_numbers).find())
print(FastDupesFinder(my_numbers).find())

print(FastDupesFinder(my_numbers).show_all_count())



