# import winsound
from myro import*
from time import sleep
from threading import Thread
bound = 1000
headerLength = 44

def playMusic(string):
    thread = Thread(target = mario)
    thread.start()
    thread.join()

def readChunk(f):
    temp = f.read(8)
    hi = ord(temp[7])%128*256*256*256+ord(temp[6])*256*256+ord(temp[5])*256+ord(temp[4])
    temp = f.read(hi)
    print "headerLength #1: "+str(hi)

def conv(ch):
    val = ord(ch)
    val = val%16 * 16 + val/16
    return val

def thing():
    f = open("test8000.wav","rb")
    value = 54315761
    try:
        temp = f.read(108)
        count = 0;
        spacing = 80
        time = 10#ms
        while True and count<bound*spacing:
            temp = f.read(spacing*4)
            count += spacing
            if len(temp)==0:
                break;
            value=0
            for i in range(0,spacing):
                tempNum = (conv(temp[i*4+2])+(conv(temp[i*4+3])%128)*256)
                if tempNum%2 == 1:
                    tempNum*=1
                value += tempNum/2
            value/=(spacing-1)
            print "Beep: "+str(value)+" with time: "+str(time)
            if value>36 and value<=20000:
                #winsound.Beep(value,time)
                myNote(value/4.0,time)
        print "Counted "+str(count)+" samples"
    finally:
        f.close()
    print "done!"

timeFactor = 0.6
lastNoteTime = 0
def myNote(f,t):
    lastNoteTime=t/1000.0
    beep(lastNoteTime*timeFactor,(int)(f*4))
    #print "beep at frq "+str(f*4)
def mySleep(t):
    sleep((t/1000.0-lastNoteTime)*timeFactor)

def beginOfMario():
    myNote(660, 100)
    mySleep(150)
    myNote(660, 100)
    mySleep(300)
    myNote(660, 100)
    mySleep(300)
    myNote(510, 100)
    mySleep(100)
    myNote(660, 100)
    mySleep(300)
    myNote(770, 100)
    mySleep(550)
    myNote(380, 100)
    mySleep(575)

    myNote(510, 100)
    mySleep(450)
    myNote(380, 100)
    mySleep(400)
    myNote(320, 100)
    mySleep(500)
    myNote(440, 100)
    mySleep(300)
    myNote(480, 80)
    mySleep(330)

def mario():
    myNote(660, 100)
    mySleep(150)
    myNote(660, 100)
    mySleep(300)
    myNote(660, 100)
    mySleep(300)
    myNote(510, 100)
    mySleep(100)
    myNote(660, 100)
    mySleep(300)
    myNote(770, 100)
    mySleep(550)
    myNote(380, 100)
    mySleep(575)

    myNote(510, 100)
    mySleep(450)
    myNote(380, 100)
    mySleep(400)
    myNote(320, 100)
    mySleep(500)
    myNote(440, 100)
    mySleep(300)
    myNote(480, 80)
    mySleep(330)
    myNote(450, 100)
    mySleep(150)
    myNote(430, 100)
    mySleep(300)
    myNote(380, 100)
    mySleep(200)
    myNote(660, 80)
    mySleep(200)
    myNote(760, 50)
    mySleep(150)
    myNote(860, 100)
    mySleep(300)
    myNote(700, 80)
    mySleep(150)
    myNote(760, 50)
    mySleep(350)
    myNote(660, 80)
    mySleep(300)
    myNote(520, 80)
    mySleep(150)
    myNote(580, 80)
    mySleep(150)
    myNote(480, 80)
    mySleep(500)

    myNote(510, 100)
    mySleep(450)
    myNote(380, 100)
    mySleep(400)
    myNote(320, 100)
    mySleep(500)
    myNote(440, 100)
    mySleep(300)
    myNote(480, 80)
    mySleep(330)
    myNote(450, 100)
    mySleep(150)
    myNote(430, 100)
    mySleep(300)
    myNote(380, 100)
    mySleep(200)
    myNote(660, 80)
    mySleep(200)
    myNote(760, 50)
    mySleep(150)
    myNote(860, 100)
    mySleep(300)
    myNote(700, 80)
    mySleep(150)
    myNote(760, 50)
    mySleep(350)
    myNote(660, 80)
    mySleep(300)
    myNote(520, 80)
    mySleep(150)
    myNote(580, 80)
    mySleep(150)
    myNote(480, 80)
    mySleep(500)

    myNote(500, 100)
    mySleep(300)

    myNote(760, 100)
    mySleep(100)
    myNote(720, 100)
    mySleep(150)
    myNote(680, 100)
    mySleep(150)
    myNote(620, 150)
    mySleep(300)

    myNote(650, 150)
    mySleep(300)
    myNote(380, 100)
    mySleep(150)
    myNote(430, 100)
    mySleep(150)

    myNote(500, 100)
    mySleep(300)
    myNote(430, 100)
    mySleep(150)
    myNote(500, 100)
    mySleep(100)
    myNote(570, 100)
    mySleep(220)

    myNote(500, 100)
    mySleep(300)

    myNote(760, 100)
    mySleep(100)
    myNote(720, 100)
    mySleep(150)
    myNote(680, 100)
    mySleep(150)
    myNote(620, 150)
    mySleep(300)

    myNote(650, 200)
    mySleep(300)

    myNote(1020, 80)
    mySleep(300)
    myNote(1020, 80)
    mySleep(150)
    myNote(1020, 80)
    mySleep(300)

    myNote(380, 100)
    mySleep(300)
    myNote(500, 100)
    mySleep(300)

    myNote(760, 100)
    mySleep(100)
    myNote(720, 100)
    mySleep(150)
    myNote(680, 100)
    mySleep(150)
    myNote(620, 150)
    mySleep(300)

    myNote(650, 150)
    mySleep(300)
    myNote(380, 100)
    mySleep(150)
    myNote(430, 100)
    mySleep(150)

    myNote(500, 100)
    mySleep(300)
    myNote(430, 100)
    mySleep(150)
    myNote(500, 100)
    mySleep(100)
    myNote(570, 100)
    mySleep(420)

    myNote(585, 100)
    mySleep(450)

    myNote(550, 100)
    mySleep(420)

    myNote(500, 100)
    mySleep(360)

    myNote(380, 100)
    mySleep(300)
    myNote(500, 100)
    mySleep(300)
    myNote(500, 100)
    mySleep(150)
    myNote(500, 100)
    mySleep(300)

    myNote(500, 100)
    mySleep(300)

    myNote(760, 100)
    mySleep(100)
    myNote(720, 100)
    mySleep(150)
    myNote(680, 100)
    mySleep(150)
    myNote(620, 150)
    mySleep(300)

    myNote(650, 150)
    mySleep(300)
    myNote(380, 100)
    mySleep(150)
    myNote(430, 100)
    mySleep(150)

    myNote(500, 100)
    mySleep(300)
    myNote(430, 100)
    mySleep(150)
    myNote(500, 100)
    mySleep(100)
    myNote(570, 100)
    mySleep(220)

    myNote(500, 100)
    mySleep(300)

    myNote(760, 100)
    mySleep(100)
    myNote(720, 100)
    mySleep(150)
    myNote(680, 100)
    mySleep(150)
    myNote(620, 150)
    mySleep(300)

    myNote(650, 200)
    mySleep(300)

    myNote(1020, 80)
    mySleep(300)
    myNote(1020, 80)
    mySleep(150)
    myNote(1020, 80)
    mySleep(300)

    myNote(380, 100)
    mySleep(300)
    myNote(500, 100)
    mySleep(300)

    myNote(760, 100)
    mySleep(100)
    myNote(720, 100)
    mySleep(150)
    myNote(680, 100)
    mySleep(150)
    myNote(620, 150)
    mySleep(300)

    myNote(650, 150)
    mySleep(300)
    myNote(380, 100)
    mySleep(150)
    myNote(430, 100)
    mySleep(150)

    myNote(500, 100)
    mySleep(300)
    myNote(430, 100)
    mySleep(150)
    myNote(500, 100)
    mySleep(100)
    myNote(570, 100)
    mySleep(420)

    myNote(585, 100)
    mySleep(450)

    myNote(550, 100)
    mySleep(420)

    myNote(500, 100)
    mySleep(360)

    myNote(380, 100)
    mySleep(300)
    myNote(500, 100)
    mySleep(300)
    myNote(500, 100)
    mySleep(150)
    myNote(500, 100)
    mySleep(300)

    myNote(500, 60)
    mySleep(150)
    myNote(500, 80)
    mySleep(300)
    myNote(500, 60)
    mySleep(350)
    myNote(500, 80)
    mySleep(150)
    myNote(580, 80)
    mySleep(350)
    myNote(660, 80)
    mySleep(150)
    myNote(500, 80)
    mySleep(300)
    myNote(430, 80)
    mySleep(150)
    myNote(380, 80)
    mySleep(600)

    myNote(500, 60)
    mySleep(150)
    myNote(500, 80)
    mySleep(300)
    myNote(500, 60)
    mySleep(350)
    myNote(500, 80)
    mySleep(150)
    myNote(580, 80)
    mySleep(150)
    myNote(660, 80)
    mySleep(550)

    myNote(870, 80)
    mySleep(325)
    myNote(760, 80)
    mySleep(600)

    myNote(500, 60)
    mySleep(150)
    myNote(500, 80)
    mySleep(300)
    myNote(500, 60)
    mySleep(350)
    myNote(500, 80)
    mySleep(150)
    myNote(580, 80)
    mySleep(350)
    myNote(660, 80)
    mySleep(150)
    myNote(500, 80)
    mySleep(300)
    myNote(430, 80)
    mySleep(150)
    myNote(380, 80)
    mySleep(600)

    myNote(660, 100)
    mySleep(150)
    myNote(660, 100)
    mySleep(300)
    myNote(660, 100)
    mySleep(300)
    myNote(510, 100)
    mySleep(100)
    myNote(660, 100)
    mySleep(300)
    myNote(770, 100)
    mySleep(550)
    myNote(380, 100)
    mySleep(575)
