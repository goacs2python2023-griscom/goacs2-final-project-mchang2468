from bokeh.plotting import figure, show
import math

# Analysis of Data
f = open("Advanced.csv", "r", encoding="utf8")
efficiencyDict = {}

for line in f:
    line = line.strip()
    line = line.split(",")
    
    try:
        if int(line[10]) >= 20: # at least 20 games played in that season
            efficiencyDict[line[1] + " " + line[3]] = float(line[12])
    except ValueError:
        continue

sortedList = sorted(efficiencyDict.items(), key=lambda x:x[1], reverse=True)
vizList = sortedList[:25]

f.close()


# Visualization
names = []
per = []

p = figure(title = "NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Player Efficiency Rating (PER)")

for i in range(len(vizList)):
    names.append(vizList[i][0])
    per.append(vizList[i][1])

for i in range(len(names)):
    p.vbar(i,1.1, per[i], 0)
    p.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "white")

print(vizList)

show(p)