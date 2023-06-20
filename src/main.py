

class finde_name():
    def __init__(self, firstlist:list, secondlist:list, people_fill:list):
        self.firstlist = firstlist
        self.secondlist = secondlist
        self.people_fill = people_fill

    def list_fillbox(self,countinu = 'y', *arg, **kwarg):
        while countinu == 'y':
            self.people_fill.append(input())
            duplicate_people_fill = list(dict.fromkeys(self.firstlist))
            countinu = input(f'do you want keep input?')
        return self.people_fill, duplicate_people_fill

    def counter_repetetive_name(self):
        duplicate_people_fill = self.people_fill
        number_of_repetetive_name = {}
        for i in self.people_fill:
            name = i
            self.number_of_repetetive_name[name] = self.secondlist.count(i)
        return number_of_repetetive_name
    
    
    def result(self):
        people_repeats = self.number_of_repetetive_name

        for i in list(self.people_fill.keys()):
            if people_repeats[i] == 1:
                fake_box = i
                break
            elif people_repeats[i] % 2 == 1:
                fake_box = i
                break
