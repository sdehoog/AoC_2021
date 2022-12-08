##fin = open('test_input.txt')
fin = open('input.txt')
day_max = 256

initial = fin.read().split(',')

fin.close()

fish = [0]*9

for i_fish in initial:
    fish[int(i_fish)] += 1

print(fish)

for day in range(day_max):
    zero_fish = fish[0]
    
    for fish_day in range(8):
        fish[fish_day]= fish[fish_day + 1]
    
    fish[6] += zero_fish
    fish[8] = zero_fish


fish_sum = 0

for fish_num in fish:
    fish_sum += fish_num

print(fish_sum)
