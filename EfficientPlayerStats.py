from bokeh.plotting import figure, show
from bokeh.layouts import row
import math

embiid = []
jokic = []
giannis = []
wilt = []
lebron = []
mj = []
curry = []
davis = []
david = []
harden = []


# 2024 Joel Embiid (PER: 34.8)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "31473":
        embiid.append(round(float(line[34]), 3)) # PPG
        embiid.append(round(float(line[28]), 3)) # RPG
        embiid.append(round(float(line[29]), 3)) # APG
        embiid.append(round(float(line[15]) * 100, 3)) # FG%
        embiid.append(round(float(line[18]) * 100, 3)) # 3P%
        embiid.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2024 Joel Embiid (PER: 34.8)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(embiid)
print()

f.close()

# 2022 Nikola Jokic (PER: 32.8)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "30247":
        jokic.append(round(float(line[34]), 3)) # PPG
        jokic.append(round(float(line[28]), 3)) # RPG
        jokic.append(round(float(line[29]), 3)) # APG
        jokic.append(round(float(line[15]) * 100, 3)) # FG%
        jokic.append(round(float(line[18]) * 100, 3)) # 3P%
        jokic.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2022 Nikola Jokic (PER: 32.8)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(jokic)
print()

f.close()

# 2022 Giannis Antetokounmpo (PER: 32.1)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "29918":
        giannis.append(round(float(line[34]), 3)) # PPG
        giannis.append(round(float(line[28]), 3)) # RPG
        giannis.append(round(float(line[29]), 3)) # APG
        giannis.append(round(float(line[15]) * 100, 3)) # FG%
        giannis.append(round(float(line[18]) * 100, 3)) # 3P%
        giannis.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2022 Giannis Antetokounmpo (PER: 32.1)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(giannis)
print()

f.close()

# 1962 Wilt Chamberlain (PER: 32.1)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "2445":
        wilt.append(round(float(line[34]), 3)) # PPG
        wilt.append(round(float(line[28]), 3)) # RPG
        wilt.append(round(float(line[29]), 3)) # APG
        wilt.append(round(float(line[15]) * 100, 3)) # FG%
        wilt.append("N/A") # 3P%
        wilt.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("1962 Wilt Chamberlain (PER: 32.1)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(wilt)
print()

f.close()

# 2009 Lebron James (PER: 31.7)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "21909":
        lebron.append(round(float(line[34]), 3)) # PPG
        lebron.append(round(float(line[28]), 3)) # RPG
        lebron.append(round(float(line[29]), 3)) # APG
        lebron.append(round(float(line[15]) * 100, 3)) # FG%
        lebron.append(round(float(line[18]) * 100, 3)) # 3P%
        lebron.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2009 Lebron James (PER: 31.7)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(lebron)
print()

f.close()

# 1988 Michael Jordan (PER: 31.7)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "11208":
        mj.append(round(float(line[34]), 3)) # PPG
        mj.append(round(float(line[28]), 3)) # RPG
        mj.append(round(float(line[29]), 3)) # APG
        mj.append(round(float(line[15]) * 100, 3)) # FG%
        mj.append(round(float(line[18]) * 100, 3)) # 3P%
        mj.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("1988 Michael Jordan (PER: 31.7)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(mj)
print()

f.close()

# 2016 Stephen Curry (PER: 31.5)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "26260":
        curry.append(round(float(line[34]), 3)) # PPG
        curry.append(round(float(line[28]), 3)) # RPG
        curry.append(round(float(line[29]), 3)) # APG
        curry.append(round(float(line[15]) * 100, 3)) # FG%
        curry.append(round(float(line[18]) * 100, 3)) # 3P%
        curry.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2016 Stephen Curry (PER: 31.5)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(curry)
print()

f.close()

# 2015 Anthony Davis (PER: 30.8)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "25137":
        davis.append(round(float(line[34]), 3)) # PPG
        davis.append(round(float(line[28]), 3)) # RPG
        davis.append(round(float(line[29]), 3)) # APG
        davis.append(round(float(line[15]) * 100, 3)) # FG%
        davis.append(round(float(line[18]) * 100, 3)) # 3P%
        davis.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2015 Anthony Davis (PER: 30.8)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(davis)
print()

f.close()

# 1994 David Robinson (PER: 30.7)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "13717":
        david.append(round(float(line[34]), 3)) # PPG
        david.append(round(float(line[28]), 3)) # RPG
        david.append(round(float(line[29]), 3)) # APG
        david.append(round(float(line[15]) * 100, 3)) # FG%
        david.append(round(float(line[18]) * 100, 3)) # 3P%
        david.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("1994 David Robinson (PER: 30.7)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(david)
print()

f.close()

# 2019 James Harden (PER: 30.6)
f = open("Player Per Game.csv", "r", encoding="utf8")
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[0] == "27871":
        harden.append(round(float(line[34]), 3)) # PPG
        harden.append(round(float(line[28]), 3)) # RPG
        harden.append(round(float(line[29]), 3)) # APG
        harden.append(round(float(line[15]) * 100, 3)) # FG%
        harden.append(round(float(line[18]) * 100, 3)) # 3P%
        harden.append(round(float(line[25]) * 100, 3)) # FT%
        break

print("2019 James Harden (PER: 30.6)")
print("[PPG, RPG, APG, FG%, 3P%, FT%]")
print(harden)
print()

f.close()


# Visualization
top10names = ["2024 Joel Embiid (PER: 34.8)", "2022 Nikola Jokic (PER: 32.8)", "2022 Giannis Antetokounmpo (PER: 32.1)", "1962 Wilt Chamberlain (PER: 32.1)", "2009 Lebron James (PER: 31.7)", "1988 Michael Jordan (PER: 31.7)", "2016 Stephen Curry (PER: 31.5)", "2015 Anthony Davis (PER: 30.8)", "1994 David Robinson (PER: 30.7)", "2019 James Harden (PER: 30.6)"]
top10stats = [embiid,jokic,giannis,wilt,lebron,mj,curry,davis,david,harden]

# Points Per Game
ppgDict = {}
for i in range(len(top10stats)):
    ppgDict[top10names[i]] = top10stats[i][0]

sortedPpgList = sorted(ppgDict.items(), key=lambda x:x[1], reverse=True)

names = []
ppg = []

a = figure(title = "PPG of the NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Points Per Game (PPG)")

for i in range(len(sortedPpgList)):
    names.append(sortedPpgList[i][0])
    ppg.append(sortedPpgList[i][1])

for i in range(len(names)):
    a.vbar(i,1.1, ppg[i], 0)
    a.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "orange")

# Rebounds Per Game
rpgDict = {}
for i in range(len(top10stats)):
    rpgDict[top10names[i]] = top10stats[i][1]

sortedRpgList = sorted(rpgDict.items(), key=lambda x:x[1], reverse=True)
names = []
rpg = []

b = figure(title = "RPG of the NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Rebounds Per Game (RPG)")

for i in range(len(sortedRpgList)):
    names.append(sortedRpgList[i][0])
    rpg.append(sortedRpgList[i][1])

for i in range(len(names)):
    b.vbar(i,1.1, rpg[i], 0)
    b.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "orange")

# Assists Per Game
apgDict = {}
for i in range(len(top10stats)):
    apgDict[top10names[i]] = top10stats[i][2]

sortedApgList = sorted(apgDict.items(), key=lambda x:x[1], reverse=True)
names = []
apg = []

c = figure(title = "APG of the NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Assists Per Game (APG)")

for i in range(len(sortedApgList)):
    names.append(sortedApgList[i][0])
    apg.append(sortedApgList[i][1])

for i in range(len(names)):
    c.vbar(i,1.1, apg[i], 0)
    c.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "orange")

# Field Goal Percentage
fgpDict = {}
for i in range(len(top10stats)):
    fgpDict[top10names[i]] = top10stats[i][3]

sortedFgpList = sorted(fgpDict.items(), key=lambda x:x[1], reverse=True)
names = []
fgp = []

d = figure(title = "FG'%' of the NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Field Goal Percentage (FG%)")

for i in range(len(sortedFgpList)):
    names.append(sortedFgpList[i][0])
    fgp.append(sortedFgpList[i][1])

for i in range(len(names)):
    d.vbar(i,1.1, fgp[i], 0)
    d.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "orange")

# Three Point Percentage
tppDict = {}
for i in range(len(top10stats)):
    if top10names[i] != top10names[3]:
        tppDict[top10names[i]] = top10stats[i][4]

sortedTppList = sorted(tppDict.items(), key=lambda x:x[1], reverse=True)
names = []
tpp = []

e = figure(title = "3P'%' of the NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Three Point Percentage (3P%)")

for i in range(len(sortedTppList)):
    names.append(sortedTppList[i][0])
    tpp.append(sortedTppList[i][1])

for i in range(len(names)):
    e.vbar(i,1.1, tpp[i], 0)
    e.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "orange")

# Free Throw Percentage
ftpDict = {}
for i in range(len(top10stats)):
    ftpDict[top10names[i]] = top10stats[i][5]

sortedFtpList = sorted(ftpDict.items(), key=lambda x:x[1], reverse=True)
names = []
ftp = []

f = figure(title = "FT'%' of the NBA Players With the Highest Season PERs", x_axis_label = "Season and Player Name", y_axis_label = "Free Throw Percentage (FT%)")

for i in range(len(sortedFtpList)):
    names.append(sortedFtpList[i][0])
    ftp.append(sortedFtpList[i][1])

for i in range(len(names)):
    f.vbar(i,1.1, ftp[i], 0)
    f.text(i, 0, [names[i]], math.pi/2, text_font_size = "10pt", text_color = "orange")


show(row(children=[a, b, c, d, e, f], sizing_mode="scale_width"))