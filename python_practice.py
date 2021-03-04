# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# temp = int(input("what da heat, man? "))
# if temp > 80:
#     print("Flip on da AC, Bro")
# else:
#     print("Open a window!")

# score = int(input("I say ole chap, what is your test score? "))
# if score >= 90:
#     print("Brilliant! Your grade is an A")
# elif score >= 80:
#     print("Amazing! Your grade is an B")
# elif score >= 70:
#     print("Wow! Your grade is an C")
# elif score >= 60:
#     print("Dude, really? Your grade is an D")
# else:
#     print("Jerk. Your grade is an F")
    


#counties = ["Arapahoe", "Denver", "Jefferson"]
#counties_dict = {"Jefferson": 432438, "Arapahoe": 422829, "Denver": 463353}
# if "Arapahoe"  in counties or "El Paso"  in counties:
#     print("One of these is in the list of counties")
# else:
#     print("NOT FOUND")
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for county in counties_dict.values():
#     print(county)

# for county in counties_dict:
#     print(counties_dict[county])

# for k, v in counties_dict.items():
#    # print(str(k) + " county has " + str(v) + " registered voters") 
#    print(f" {k} county has {v:,} registered voters") 




voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]

# for i in voting_data:
#     print(i)

# for counties_dict in voting_data:
    # print(counties_dict['county'])

# for i in voting_data:
#     for v in i.values():
#        print(v)      

for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters")
    #for k, v in i.items():
       # print(f" {k} county has {v:} registered voters") 
        # print(k, v)
    # print(f'{k} county has {v:,} registered voters.')