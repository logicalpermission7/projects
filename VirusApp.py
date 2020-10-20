from Virus import Virus

virus_1 = Virus("COVID-19", "China", 850, 200, 15, 0)
virus_2 = Virus("Ebola", "Africa", 450, 300, 10, 1)


print(virus_1.is_curable())

virusInfo = {
    1: 45674,
    2: 95,
    3: 234,
    4: 8921,
    5: 12,
    6: 1,
    7: 345,
    8: 23,
    9: 5354,
    10: "COVID",
}
count = 0
virusList = ["Ebola", "Langusta", "COVID19", "Delust56", "Herpees", "HIV", "AIDS"]
for row in virusList:
    count += 1
    print(str(count) + ")" + " " + row)

coronaList = [
    ["elvis", "marvin", "izzy"],
    ["jose", "sofia", "liz"],
    ["lennise", "ismael"],
    ["joshua", "mila"]
]

for row in coronaList:
    for col in row:
        print(col)