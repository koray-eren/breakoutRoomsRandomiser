import random

# to select groups leave as 1, can increase to simulate use over long term,
# and see statistics this helps answer the question 'is there a risk that I
# won't match at least once with everyone over x iterations?'
ITERATIONS = 1

# if true, will print the group selections for all iterations
PRINTGROUPS = True

# if true, will print data on how many times each user has matched with every other user
PRINTSTATS = False

w, h = 16, 16
meetings = [[0 for x in range(w)] for y in range(h)]

dictionary = {"Angela":0, "Daisy":1, "Iryna":2, "Jacob":3,
              "James":4,"Jesse":5,"Jihyung":6, "Kate":7,
              "Koray":8,"Leigh":9, "Luke":10, "Nicholas":11,
              "Shriya":12,"Tiger":13, "Van":14, "Zachariah":15}

inverseDictionary = {0: "Angela", 1: "Daisy", 2: "Iryna", 3: "Jacob",
                4: "James", 5:"Jesse",6:"Jihyung", 7:"Kate",
                8:"Koray", 9:"Leigh", 10:"Luke", 11:"Nicholas",
                12:"Shriya", 13:"Tiger", 14:"Van", 15:"Zachariah"}

for x in range(ITERATIONS):
    students = ["Angela", "Daisy", "Iryna", "Jacob",
                "James", "Jesse","Jihyung", "Kate",
                "Koray", "Leigh", "Luke", "Nicholas",
                "Shriya", "Tiger", "Van", "Zachariah"]

    group1 = [0, 0, 0, 0]
    group2 = [0, 0, 0, 0]
    group3 = [0, 0, 0, 0]
    group4 = [0, 0, 0, 0]

    groups = [group1, group2, group3, group4]


    for i in range(4):
        for j in range(4):
            if(len(students) > 0):
                groups[j][i] = random.choice(students)
                students.remove(groups[j][i] )


    for group in groups:
        for person in group:
            for person2 in group:
                if(person2 != person):
                    personIndex = dictionary[person]
                    person2Index = dictionary[person2]
                    meetings[personIndex][person2Index] += 1

    if(PRINTGROUPS == True):
        print("=======   GROUPS   ========")
        print("group 1: " + str(group1))
        print("group 2: " + str(group2))
        print("group 3: " + str(group3))
        print("group 4: " + str(group4))
        print("===========================")
        print()
    
if(PRINTSTATS == True):
    for outerIndex in range(16):
        print(inverseDictionary[outerIndex] + " MATCHES")
        for innerIndex in range(16):
            print(inverseDictionary[innerIndex] + ": " + str(meetings[outerIndex][innerIndex]) )
        print()
        print("========================")
        print()
