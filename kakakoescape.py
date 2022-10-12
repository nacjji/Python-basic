'''1) 1에서 2000까지 숫자를 적어나갔을 때, 2 보다 0 을 더 많이 쓴다.'''

# li=[]
# lii=[]
# for i in range(1,2001):
#     li.append(i)


'''2) 2**1987 에서 0, 2, 4, 6, 8 의 등장횟수 보다는 
1, 3, 5, 7, 9 의 등장횟수가 더 많습니다.
'''
# s=0
# for i in range(2**1987):
#     for j in (1,i+1):
#         if j==2:
#             s+=1
# print(s)

# Q5. 약수관련 문제입니다. 약수 중 두 자리수인 약수들의 합이 그렇지 
# 않은 약수들의 합보다 큰 수들을 "두약수" 라고 하겠습니다.

# ex) 100 [1, 2, 4, 5, 10, 20, 25, 50, 100]
# 1 + 2 + 4 + 5 + 100 = 112
# 10 + 20 + 25 + 50 = 105    
# 112 > 105 이므로 두약수가 아님

# lii=[]
# li=[631, 806, 833, 192, 807, 121, 770, 891, 847, 491, 783, 744, 752, 296, 728, 568, 396, 859, 178, 748, 738, 130, 158, 625, 210, 397, 387, 719, 194, 386, 884, 859, 410, 133, 422, 614, 746, 669, 206, 439, 273, 879, 146, 680, 668, 662, 600, 731, 716, 260, 879, 730, 661, 674, 423, 195, 423, 631, 268, 455, 657, 413, 319, 505, 924, 598, 639, 363, 795, 592, 395, 794, 320, 674, 707, 705, 349, 127, 816, 405, 106, 809, 228, 477, 700, 847, 311, 473, 241, 851, 537, 359, 816, 779, 874, 654, 295, 168, 839, 720, 930, 213, 198, 280, 569, 765, 100, 744, 714, 670, 133, 527, 898, 232, 816, 758, 637, 737, 265, 424, 556, 293, 412, 543, 550, 667, 287, 370, 441, 819, 318, 816, 609, 917, 498, 676, 179, 461, 980, 164, 776, 146, 813, 834, 382, 617, 151, 254, 952, 698, 880, 330, 771, 794, 397, 692, 147, 748, 104, 930, 347, 631, 301, 283, 941, 337, 682, 550, 894, 668, 329, 564, 278, 300, 416, 506, 448, 137, 341, 314, 521, 792, 551, 524, 535, 135, 962, 616, 598, 513, 204, 803, 588, 284, 196, 720, 803, 894, 580, 447, 556, 685, 946, 371, 876, 132, 178, 417, 942, 242, 416, 241, 740, 330, 201, 891, 815, 869, 738, 325, 582, 938, 561, 702, 356, 402, 196, 137, 318, 589, 617, 154, 488, 152, 226, 917, 638, 666, 679, 101, 156, 251, 168, 476, 207, 816, 968, 417, 129, 615, 619, 914, 642, 377, 823, 273, 199, 806, 898, 360, 517, 919, 860, 926, 759, 473, 332, 208, 329, 551, 840, 323, 410, 173, 590, 193, 554, 912, 875, 485, 887, 401, 867, 680, 190, 379, 713, 639, 534, 198, 955, 554, 954, 580, 904, 131, 214, 592, 925, 634]
# lii=[]
# liii=[]
# for i in li:
#     for j in range(1,i+1):
#         if i%j==0:
#             lii.append(j)
#             if 10<=lii[i+1]<=99:
#                 liii.append(j)
# print(liii)

a='''d 는 a 로 바꾸면 된다네!
r 는 b 로 바꾸면 된다네!
t 는 c 로 바꾸면 된다네!
o 는 d 로 바꾸면 된다네!
a 는 e 로 바꾸면 된다네!
l 는 f 로 바꾸면 된다네!
i 는 g 로 바꾸면 된다네!
w 는 h 로 바꾸면 된다네!
v 는 i 로 바꾸면 된다네!
x 는 j 로 바꾸면 된다네!
b 는 k 로 바꾸면 된다네!
p 는 l 로 바꾸면 된다네!
u 는 m 로 바꾸면 된다네!
e 는 n 로 바꾸면 된다네!
j 는 o 로 바꾸면 된다네!
n 는 p 로 바꾸면 된다네!
c 는 q 로 바꾸면 된다네!
y 는 r 로 바꾸면 된다네!
m 는 s 로 바꾸면 된다네!
q 는 t 로 바꾸면 된다네!
h 는 u 로 바꾸면 된다네!
f 는 v 로 바꾸면 된다네!
g 는 w 로 바꾸면 된다네!
z 는 x 로 바꾸면 된다네!
s 는 y 로 바꾸면 된다네!
k 는 z 로 바꾸면 된다네!
P 는 A 로 바꾸면 된다네!
D 는 B 로 바꾸면 된다네!
N 는 C 로 바꾸면 된다네!
T 는 D 로 바꾸면 된다네!
J 는 E 로 바꾸면 된다네!
U 는 F 로 바꾸면 된다네!
X 는 G 로 바꾸면 된다네!
E 는 H 로 바꾸면 된다네!
Z 는 I 로 바꾸면 된다네!
S 는 J 로 바꾸면 된다네!
F 는 K 로 바꾸면 된다네!
H 는 L 로 바꾸면 된다네!
O 는 M 로 바꾸면 된다네!
Q 는 N 로 바꾸면 된다네!
R 는 O 로 바꾸면 된다네!
G 는 P 로 바꾸면 된다네!
Y 는 Q 로 바꾸면 된다네!
L 는 R 로 바꾸면 된다네!
V 는 S 로 바꾸면 된다네!
C 는 T 로 바꾸면 된다네!
I 는 U 로 바꾸면 된다네!
B 는 V 로 바꾸면 된다네!
K 는 W 로 바꾸면 된다네!
M 는 X 로 바꾸면 된다네!
A 는 Y 로 바꾸면 된다네!
W 는 Z 로 바꾸면 된다네!'''.split("\n")




tx='''wveq! Ima jeps aeibjy lhetqvje!
ow.. gncxcopman ohyqp ibm osoexmop cwmjm qblbdabcyem...
ibgpdbm, lbopculxlp ibdqelul oposoibgp obmiyw ibmbibmb cxmohyoul ibl yxq ybzobqx geoybmgeoybmon celfplosibm demyelul qxLox mwiynCmn
oeqxm ypdtpKpyjon ajibm opovyplw qpgbyijcwawlwy ibgp..
ypdtpKpyjmum ibmyey oslp geo ibmbopm ypdtpKpyjmum ypdtplul ypcbmoulw ibmum yeydeloslpov.
ypdtplul cwLoum aboud deloul ceox Luliopmum cbocxcoulw gwlpibgp.
awpmgboKpyjowb ibdLn ibmyeyopmonyn qbgbo qxmiwawpmum ibmqpyopgpdbm,
mbmum yjopmgxyoulw awpmgboKpyjcwabmum ypdtpKpyjlul gwiobibgp
fjquoexaumum dblopov gbdqpieon obllhgeawlwy ibgp
dbloul opoxybgbdhm gbmn iwyqp 'dhoawoKpyjdboul' oplbyw oblywopCmb.
mbonynmum 'kbdbluzbgp' ybzoum ywqopmn!
opgn qulqul op cbooup fponoponquonquaxculorowoblaplul dblijcwlLb
cellxgelznmp gblgxyouqpyn~
txqcxmKj yulgbmum qwdemgb onm, aecxmKjmum qeqgb opl, qncxmKjmum ajdemgb Cp kwllwykwllwy....
dpobmibmn yptpdoul tbdoul qeyb oxcqoxCmn...
op yptpdoplbm yxqop dblopov ieaelul fwibdij ypawoup gbyuyon oupijqx cbmqbgxyoulw cblqjoibmum yxqop ajcecemopman
ohmyp, dxmgp, opdel auooup owpcedelgploup iucopcon oupibm ypaw gbyuyon oupijqxaw oploxmbypaw ibgp
dbmovyon yptpdop owljybmabdhm 'mnytboplnmwl' oul dxyoudhm isywbgxyopov
mjyb oxapLbgp ijCaxlb..? oud ob qncxmKjmum ajdemgb Cp, mncxmKjmum qeqgb qbd, abqxqcxmKjmum, abqxqcxmKj gblponmum ajdemgb gep     
ob tbd yulxman gbmn gngeawon ordhoibm iwpqgpcop opCabmumyxl oblywopCmumyb?
'mwihoonmiwpqgpc'oplbmum ywqno ibmcxm ybcwmumyxm oxJxmyb
obdb dbmgwyiblyxlqn, opgn Judaulopgp obmiyw dbgpdby qngblplul cellxgeynCmn
qwdemgb ow, qeqgb oho, qwdemgb ap oplqn.
obdeKwlwy obfoulw ibyqucibdon opCox yeoyudibmyn opCoudhm oxldbaumgp ohmlbygeqpyn
ohypcezxmum deqpijaw awpmum ybcqaulop mbowmabmn
awoijdelywb cjyaeqbmop dbluyw abliawlwy ibmumpdop cwoeibqb oelpmblbdbmqn
deyeoiwb qbdtxmlp iwblhyboqbm ajibmqbldb ajibmoulw yplopcwgxmibqn
opqboijCpyb gpmiwbibdhm opqboijfelopawpyw opqboijfelop gpmiwbibdhm opqboijLwtopawpyw
obyedwmop gpmiwbibdhm yulnopdwmopawpyw yulnopdwmop gpmiwbibdhm dnzblyulnopdwmopawpyw
dnzblyulnopdwmop gpmiwbibdhm oexyulnopdwmop awpgp'''
liLow=[]
liUpp=[]
li4Low=[]
li4Upp=[]
for i in a:
    print(i)
#     if i[0].islower:
#         liLow.append(i)
#     elif i[0].isupper:
#         liUpp.append(i)
#     if i[4].islower():
#         li4Low.append(i)
#     elif i[4].isupper:
#         li4Upp.append(i)
# # print(liLow,li4Low,li4Low,li4Upp)

# for j in liLow:
#     jl=j[0]
#     jl4=j[4]
#     print(jl[0])