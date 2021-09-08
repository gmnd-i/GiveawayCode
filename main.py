winners = {"indalpha30": 4990.2,
           "SwordKnave": 7739.3,
           "crier": 4979.0,
           "NeverWinter": 45674.70,
           "dkaine": 7304.69,
           "OomNomNom": 2337.49,
           "hoperises": 462.80,
           "JohnDoe44": 6453.69,
           "Prutske": 624.80,
           "EnidLaliwen": 160.30};

Reward = 1705.1/2;


#calculating the constant 'k'
k_ = 0
for w in winners.keys():
    k_ += 1/(winners[w]**0.5);

k = 1/k_;


sum = 0
print ("username", '\t', "Reward", '\t', "Rounded to the closest whole number");
print("----------------------------------------------------------------------");
#rewards
for w in winners.keys():
    r = Reward*k/(winners[w]**0.5);
    print(w, '\t', r, '\t', int(round(r)));
    sum += int(round(r))

print( sum)


