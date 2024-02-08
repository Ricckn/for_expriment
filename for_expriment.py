#実験用ファイル
import krs
import json
import math
#import linecache
import time
import webbrowser
krs.init("COM4")

def set_up():
    krs.krs_setPos_multi(1,krs.angle_to_pos(61.8))#サーボの元値:9331
    krs.krs_setPos_multi(2,krs.angle_to_pos(-42.3))#サーボの元値:6247
    krs.krs_setPos_multi(3,krs.angle_to_pos(34.155))#サーボの元値:8512
    krs.krs_setPos_multi(4,krs.angle_to_pos(29.16))#サーボの元値:8367
    krs.krs_setPos_multi(5,krs.angle_to_pos(-35.74)) #サーボの元値:4367　#まっすぐは-105.74
    krs.krs_setPos_multi(6,krs.angle_to_pos(169.68))#サーボの元値:9861　#まっすぐは79.68
    krs.krs_setPos_multi(7,krs.angle_to_pos(110))#まっすぐは0
    krs.krs_setPos_multi(8,krs.angle_to_pos(-60))#まっすぐは0
    krs.krs_setPos_multi(9,krs.angle_to_pos(0))
    krs.krs_setPos_multi(10,krs.angle_to_pos(0))
    krs.krs_setPos_multi(11,krs.angle_to_pos(0))
    krs.krs_setPos_multi(12,krs.angle_to_pos(0))
set_up()

l3 = []
l4 = []
l6 = []
l8 = []
l13 = []
l14 = []
l16 = []
l18 = []

def make_backup(file):
    global l3
    global l4
    global l6
    global l8
    global l13
    global l14
    global l16
    global l18
    with open(file) as f:
        j = json.load(f)
        max_list = []
        rotations = dict()
        for i, v in enumerate(j['animations'][0]['channels']):
            #バックアップ
            if i == 3:
                f3 = open(f'{file}_lhand.json', 'w') 
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 4:
                f4 = open(f'{file}_llowarm.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 6:
                f6 = open(f'{file}_lshoulder.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 8:
                f8 = open(f'{file}_luparm.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 13:
                f13 = open(f'{file}_rhand.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 14:
                f14 = open(f'{file}_rlowarm.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 16:
                f16 = open(f'{file}_rshoulder.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
            elif i == 18:
                f18 = open(f'{file}_ruparm.json', 'w')
                max_list.append(j['animations'][0]['channels'][i]['rotationkeys'][-1][0])
        max_number = max(max_list)

    z = [0,0,0,0]
    tmpl3 = []
    tmpl4 = []
    tmpl6 = []
    tmpl8 = []
    tmpl13 = []
    tmpl14 = []
    tmpl16 = []
    tmpl18 = []
    for i in range(max_number):
        tmpl3.append(z)
        tmpl4.append(z)
        tmpl6.append(z)
        tmpl8.append(z)
        tmpl13.append(z)
        tmpl14.append(z)
        tmpl16.append(z)
        tmpl18.append(z)
    l3 = tmpl3
    l4 = tmpl4
    l6 = tmpl6
    l8 = tmpl8
    l13 = tmpl13
    l14 = tmpl14
    l16 = tmpl16
    l18 = tmpl18

    #l_hand_hidarite
    r3 = rotations[j['animations'][0]['channels'][2]['name']] = j['animations'][0]['channels'][2]['rotationkeys']
    #l_low_arm_hidarihiji
    r4 = rotations[j['animations'][0]['channels'][3]['name']] = j['animations'][0]['channels'][3]['rotationkeys']
    #l_shoulder_hidarikata
    r6 = rotations[j['animations'][0]['channels'][5]['name']] = j['animations'][0]['channels'][5]['rotationkeys']
    #l_up_arm_hidarikata
    r8 = rotations[j['animations'][0]['channels'][7]['name']] = j['animations'][0]['channels'][7]['rotationkeys']
    #r_hand_migite
    r13 = rotations[j['animations'][0]['channels'][12]['name']] = j['animations'][0]['channels'][12]['rotationkeys']
    #r_low_arm_migihiji
    r14 = rotations[j['animations'][0]['channels'][13]['name']] = j['animations'][0]['channels'][13]['rotationkeys']
    #r_shoulder_migikata
    r16 = rotations[j['animations'][0]['channels'][15]['name']] = j['animations'][0]['channels'][15]['rotationkeys']
    #r_up_arm
    r18 = rotations[j['animations'][0]['channels'][17]['name']] = j['animations'][0]['channels'][17]['rotationkeys']
    # print(rotations)

    json.dump(r3,f3,indent=2)
    json.dump(r4,f4,indent=2)
    json.dump(r6,f6,indent=2)
    json.dump(r8,f8,indent=2)
    json.dump(r13,f13,indent=2)
    json.dump(r14,f14,indent=2)
    json.dump(r16,f16,indent=2)
    json.dump(r18,f18,indent=2)

    f3.close()
    f4.close()
    f6.close()
    f8.close()
    f13.close()
    f14.close()
    f16.close()
    f18.close()

    i3 = 0
    i4 = 0
    i6 = 0
    i8 = 0
    i13 = 0
    i14 = 0
    i16 = 0
    i18 = 0

    for i in range(max_number):
        if i3 < len(r3):
            l3[i3] = r3[i3][1]
            i3 += 1

        if i4 < len(r4):
            l4[i4] = r4[i4][1]
            i4 += 1

        if i6 < len(r6):
            l6[i6] = r6[i6][1]
            i6 += 1

        if i8 < len(r8):
            l8[i8] = r8[i8][1]
            i8 += 1

        if i13 < len(r13):
            l13[i13] = r13[i13][1]
            i13 += 1

        if i14 < len(r14):
            l14[i14] = r14[i14][1]
            i14 += 1

        if i16 < len(r16):
            l16[i16] = r16[i16][1]
            i16 += 1

        if i18 < len(r18):
            l18[i18] = r18[i18][1]
            i18 += 1  
    return max_number

def euler_from_quaternion(q_a):#()の中はｌたち
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        x = q_a[0]
        y = q_a[1]
        z = q_a[2]
        w = q_a[3]

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

        n_a =[]
        n_a.append(roll_x)
        n_a.append(pitch_y)
        n_a.append(yaw_z)
     
        return n_a # in radians  

def change_all_angle(n_a):
    n_r = []
    for n in range(len(n_a)):
        n_r.append(euler_from_quaternion(n_a[n]))
    return n_r

def send_information_fast(filename,max_number):
    with open(filename) as f:
        j = json.load(f)
        for n in range(0,max_number):#調整必要
            b = 20
            #print(n_l3)
            ang_1 = (n_l3[n][2]) * b
            krs.krs_setPos_multi(1, krs.angle_to_pos(61.8-(ang_1)))

            ang_2 = (n_l3[n][1]) * b
            krs.krs_setPos_multi(2, krs.angle_to_pos(-42.3-(ang_2)))

            ang_3 = (n_l4[n][1]) * b
            krs.krs_setPos_multi(3, krs.angle_to_pos(34.155-(ang_3)))

            ang_4 = (n_l6[n][1]) * b
            krs.krs_setPos_multi(4, krs.angle_to_pos(29.16-(ang_4)))

            ang_5 = (n_l8[n][2]) * b
            krs.krs_setPos_multi(5, krs.angle_to_pos(-35.74+(ang_5)))

            ang_6 = (n_l8[n][0]) * b
            krs.krs_setPos_multi(6, krs.angle_to_pos(169.68+(ang_6)))

            ang_7 = (n_l16[n][2]) * b
            krs.krs_setPos_multi(7, krs.angle_to_pos(110+(ang_7)))

            ang_8 = (n_l16[n][1]) * b
            krs.krs_setPos_multi(8, krs.angle_to_pos(-60+(ang_8)))

            ang_9 = (n_l18[n][2]) * b
            krs.krs_setPos_multi(9, krs.angle_to_pos(0+(ang_9)))

            ang_10 = (n_l14[n][0]) * b
            krs.krs_setPos_multi(10, krs.angle_to_pos(0-(ang_10)))

            ang_11 = (n_l13[n][1]) * b
            krs.krs_setPos_multi(11, krs.angle_to_pos(0+(ang_11)))

            ang_12 = (n_l13[n][2]) * b
            krs.krs_setPos_multi(12, krs.angle_to_pos(0+(ang_12)))
        
            time.sleep(0.5)
    return

def send_information_slow(filename,max_number):
    with open(filename) as f:
        j = json.load(f)
        for n in range(0,max_number,10):#調整必要
            b = 20
            ang_1 = (nl3[n][2]) * b
            krs.krs_setPos_multi(1, krs.angle_to_pos(61.8-(ang_1)))

            ang_2 = (nl3[n][1]) * b
            krs.krs_setPos_multi(2, krs.angle_to_pos(-42.3-(ang_2)))

            ang_3 = (nl4[n][1]) * b
            krs.krs_setPos_multi(3, krs.angle_to_pos(34.155-(ang_3)))

            ang_4 = (nl6[n][1]) * b
            krs.krs_setPos_multi(4, krs.angle_to_pos(29.16-(ang_4)))

            ang_5 = (nl8[n][2]) * b
            krs.krs_setPos_multi(5, krs.angle_to_pos(-35.74+(ang_5)))

            ang_6 = (nl8[n][0]) * b
            krs.krs_setPos_multi(6, krs.angle_to_pos(169.68+(ang_6)))

            ang_7 = (nl16[n][2]) * b
            krs.krs_setPos_multi(7, krs.angle_to_pos(110+(ang_7)))

            ang_8 = (nl16[n][1]) * b
            krs.krs_setPos_multi(8, krs.angle_to_pos(-60+(ang_8)))

            ang_9 = (nl18[n][2]) * b
            krs.krs_setPos_multi(9, krs.angle_to_pos(0+(ang_9)))

            ang_10 = (nl14[n][0]) * b
            krs.krs_setPos_multi(10, krs.angle_to_pos(0-(ang_10)))

            ang_11 = (nl13[n][1]) * b
            krs.krs_setPos_multi(11, krs.angle_to_pos(0+(ang_11)))

            ang_12 = (nl13[n][2]) * b
            krs.krs_setPos_multi(12, krs.angle_to_pos(0+(ang_12)))
        
            time.sleep(0.5)
    return

n_l3 = []
n_l4 = []
n_l6 = []
n_l8 = []
n_l13 = []
n_l14 = []
n_l16 = []
n_l18 = []

nl3 = []
nl4 = []
nl6 = []
nl8 = []
nl13 = []
nl14 = []
nl16 = []
nl18 = []

def move_robot_fast(filename):
    max_frame = make_backup(filename)
    global n_l3
    global n_l4
    global n_l6
    global n_l8
    global n_l13
    global n_l14
    global n_l16
    global n_l18

    n_l3 = change_all_angle(l3)
    n_l4 = change_all_angle(l4)
    n_l6 = change_all_angle(l6)
    n_l8 = change_all_angle(l8)
    n_l13 = change_all_angle(l13)
    n_l14 = change_all_angle(l14)
    n_l16 = change_all_angle(l16)
    n_l18 = change_all_angle(l18)

    send_information_fast(filename,max_frame)
    return

def move_robot_slow(filename):
    max_frame = make_backup(filename)
    global nl3
    global nl4
    global nl6
    global nl8
    global nl13
    global nl14
    global nl16
    global nl18

    nl3 = change_all_angle(l3)
    nl4 = change_all_angle(l4)
    nl6 = change_all_angle(l6)
    nl8 = change_all_angle(l8)
    nl13 = change_all_angle(l13)
    nl14 = change_all_angle(l14)
    nl16 = change_all_angle(l16)
    nl18 = change_all_angle(l18)
    send_information_slow(filename,max_frame)
    return

#motion_number
#supaer market period fast:0_0
#supaer market period slow:0_1

#fast food period fast:1_0
#fast food period slow:1_1

#hotel joint period fast:2_0
#hotel joint period slow:2_1

#airport joint period fast:3_0
#airport joint period slow:3_1

motion = str(input('input motion number: '))
#supaer market period fast:0_0
#supaer market period slow:0_1
if motion == '0_0':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_fast('stillness.json')
        #webbrowser.open('01supermp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_fast('02super.json')
            #webbrowser.open('02supermp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_fast('03super.json')
                #webbrowser.open('03supermp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_fast('stillness.json')
                    #webbrowser.open('04supermp3_voice.mp3')
elif motion == '0_1':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_slow('stillness.json')
        #webbrowser.open('01supermp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_slow('02super.json')
            #webbrowser.open('02supermp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_slow('03super.json')
                #webbrowser.open('03supermp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_slow('stillness.json')
                    webbrowser.open('04supermp3_voice.mp3')
#fast food period fast:1_0
#fast food period slow:1_1
elif motion == '1_0':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_fast('01fastfood.json')
        webbrowser.open('01fastfoodmp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_fast('stillness.json')
            webbrowser.open('02fastfoodmp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_fast('03fastfood.json')
                webbrowser.open('03fastfoodmp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_fast('stillness.json')
                    webbrowser.open('04fastfoodmp3_voice.mp3')
elif motion == '1_1':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_slow('01fastfood.json')
        webbrowser.open('01fastfoodmp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_slow('stillness.json')
            webbrowser.open('02fastfoodmp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_slow('03fastfood.json')
                webbrowser.open('03fastfoodmp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_slow('stillness.json')
                    webbrowser.open('04fastfoodmp3_voice.mp3')
#hotel joint period fast:2_0
#hotel joint period slow:2_1
elif motion == '2_0':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_fast('01hotel.json')
        webbrowser.open('01hotelmp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_fast('stillness.json')
            webbrowser.open('02hotelmp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_fast('03hotel.json')
                webbrowser.open('03hotelmp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_fast('stillness.json')
                    webbrowser.open('04hotelmp3_voice.mp3')
elif motion == '2_1':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_slow('01hotel.json')
        webbrowser.open('01hotelmp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_slow('stillness.json')
            webbrowser.open('02hotelmp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_slow('03hotel.json')
                webbrowser.open('03hotelmp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_slow('stillness.json')
                    webbrowser.open('04hotelmp3_voice.mp3')
#airport joint period fast:3_0
#airport joint period slow:3_1
elif motion == '3_0':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_fast('01airport.json')
        webbrowser.open('01airportmp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_fast('02airport.json')
            webbrowser.open('02airportmp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_fast('stillness.json')
                webbrowser.open('03airportmp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_fast('stillness.json')
                    webbrowser.open('04airportmp3_voice.mp3')
elif motion == '3_1':
    mover1 = str(input('Can I move the robot?'))
    if mover1 == 'y':
        move_robot_slow('01airport.json')
        webbrowser.open('01airportmp3_voice.mp3')
        mover2 = str(input('Can I move the robot?'))
        if mover2 == 'y':
            move_robot_slow('02airport.json')
            webbrowser.open('02airportmp3_voice.mp3')
            mover3 = str(input('Can I move the robot?'))
            if mover3 == 'y':
                move_robot_slow('stillness.json')
                webbrowser.open('03airportmp3_voice.mp3')
                mover4 = str(input('Can I move the robot?'))
                if mover4 == 'y':
                    move_robot_slow('stillness.json')
                    webbrowser.open('04airportmp3_voice.mp3')