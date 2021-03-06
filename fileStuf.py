import csv


def findHighScore():
    file = open('scores.csv')
    fileRead = csv.reader(file)
    data = list(fileRead)

    if data:
        highScore = data[0][1]
    else:
        highScore = 0
    file.close()

    return int(highScore)


def newHighScore(name,  score):
    file = open('scores.csv', 'r')
    readFile = csv.reader(file)
    data = list(readFile)

    file.close()

    file = open('scores.csv', 'w')
    write = csv.writer(file)
    write.writerow([name, str(score)])
    for row in data:
        write.writerow(row)
    file.close()
def addScore(name, score):
    file = open('scores.csv')
    readFile = csv.reader(file)
    data = list(readFile)
    print(data)
    file.close()

    file = open('scores.csv', 'w')
    write = csv.writer(file)
    index = 0
    for i in range(len(data)):
        if int(data[i][1])<score:   
            index = i
            break
    for i in range(len(data)):
        if i == index:
            write.writerow([name, str(score)])
        write.writerow(data[i])
    file.close()
    


def topScores():
    file = open('scores.csv', 'r')
    read = csv.reader(file)
    data = list(read)
    if len(data)>10:
        return data[:10]
    else:
        return data
