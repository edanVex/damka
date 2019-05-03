class unit(object):

    def __init__(self, positionx, positiony):
        self.type = 'soldier'
        self.alive = True
        self.position = [positionx,positiony]
        self.team = None
        self.game = None

    def moveSoldier(self, newX, newY):
        nowY = self.position[1]
        nowX = self.position[0]
        if newX <= 7 and newY <= 7 and newX >= 0 and newY >=0:
            if type(self.game.board[newY][newX]) == int:
                FnewY = self.game.line - newY
                FnowY = self.game.line - nowY
                if self.team == 'black':
                    if FnewY - FnowY == 1 and (newX - nowX == 1 or nowX -newX == 1 ):
                            self.position = [newX, newY]
                            self.game.board[newY][newX] = self
                            self.game.board[nowY][nowX] = 0
                    elif FnewY - FnowY == 2 and (newX - nowX == 2 or nowX - newX == 2):
                        betweenX = (nowX+newX)/2
                        betweenY = (nowY+newY)/2
                        if self.game.board[betweenY][betweenX].team != self.team:
                            self.game.team1.livingUnits -= 1
                            self.game.board[betweenY][betweenX].death()
                            self.position = [newX, newY]
                            self.game.board[newY][newX] = self
                            self.game.board[nowY][nowX] = 0
                        elif type(self.game.board[betweenY][betweenX]) == int:
                            print 'you cant move over empty spot'
                        else:
                            print 'you cant move over your unit'
                    else:
                        print 'eligle move'

                else:
                    if newY - nowY == 1 and (newX - nowX == 1 or nowX -newX == 1 ):
                            self.position = [newX, newY]
                            self.game.board[newY][newX] = self
                            self.game.board[nowY][nowX] = 0
                    elif newY - nowY == 2 and (newX - nowX == 2 or nowX - newX == 2):
                        betweenX = (nowX+newX)/2
                        betweenY = (nowY+newY)/2
                        if self.game.board[betweenY][betweenX].team != self.team:
                            self.game.team2.livingUnits -= 1
                            self.game.board[betweenY][betweenX].death()
                            self.position = [newX, newY]
                            self.game.board[newY][newX] = self
                            self.game.board[nowY][nowX] = 0
                        elif type(self.game.board[betweenY][betweenX]) == int:
                            print 'you cant move over empty spot'
                        else:
                            print 'you cant move over your unit'
                    else:
                        'eligle move'

            else:
                print 'destination taken'

        else:
            print 'position is out of the board'


    def death(self):
        self.alive = False
        self.game.board[self.position[1]][self.position[0]] = 0


    def setAsQueen(self):
        self.type = 'Queen'

    def move(self, newX, newY):
        if self.type == 'soldier':
            self.moveSoldier(newX, newY)

class team(object):

    def __init__(self):
        self.units = []
        self.livingUnits=12

    def addUnit(self, unit):
        self.units.append(unit)


class board(object):

    def __init__(self, lines, collums):
        self.line = lines
        self.collum = collums
        self.board = [[0 for x in xrange(lines)] for y in xrange(collums)]
        self.team1 = None
        self.team2 = None

    def start(self):
        self.team1 = team()
        self.team2 = team()
        YCouner = 0
        for indexY in [0, 1, 2]:
            for indexX in range(0,self.collum,2):
                unit1 = unit(indexX+(YCouner%2),indexY)
                unit1.team = 'white'
                unit1.game = self
                self.team1.addUnit(unit1)
                self.board[indexY][indexX+(YCouner%2)] = unit1
            YCouner += 1
        YCouner = 5
        for indexY in [5,6,7]:
            for indexX in range(0,self.collum,2):
                unit1 = unit(indexX+(YCouner%2),indexY)
                unit1.team = 'black'
                unit1.game = self
                self.team2.addUnit(unit1)
                self.board[indexY][indexX+(YCouner%2)] = unit1
            YCouner += 1

    def printBoard(self):
        lineCounter = 0
        counter = 0
        for y in self.board:
            line = []
            for x in y:
                if x != 0:
                    line.append(x.type + ' ' + x.team)
                    counter += 1
                else:
                    if (counter+lineCounter)%2 == 0:
                        line.append('blank white')
                        counter += 1
                    else:
                        line.append('blank black')
                        counter += 1
            print '      '.join(line)
            print
            lineCounter += 1

    def printScore(self):
        print ('team1 have %d soldiers left\nteam2 have %d soldiers left' %(self.team1.livingUnits, self.team2.livingUnits))


    def play(self):
        self.start()
        self.printBoard()
        while (self.team1.livingUnits != 0) and (self.team2.livingUnits != 0):
            position = (raw_input("position of the unit you want to move, like this coulumn,line: ")).split(',')
            dest = (raw_input("destination position, like this coulumn,line: ")).split(',')
            newX = int(dest[0])
            newY = int(dest[1])
            if (position[0] <= 7) and (position[1] <= 7) and (position[1] >= 0) and (position[0] >= 0):
                if self.board[int(position[1])][int(position[0])] != 0:
                    self.board[int(position[1])][int(position[0])].move(newX,newY)
                else:
                    print 'square is empty'
                self.printBoard()
                self.printScore()
            else:
                print("position is out of the board")


board1 = board(8, 8)
board1.play()