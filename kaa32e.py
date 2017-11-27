# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,ast,os
import requests,urllib,json
from bs4 import BeautifulSoup
from gtts import gTTS


cl = LINETCR.LINE()
cl.login(token='EsP6SwTbpJDYFYRTo35.QdLXoVPaKOU6WpvD80Sijq.NRQspAn7frRcRy++VaPN6duMhsFsLUExsyS4rG8aT1s=')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ES9tv3cNimennoQVhF8.geGv8cutIQAODYMXI18qca.yLMrfEdSmVZl4ECYJ/m+SK4PjmVd0d85uIkwsjst96A=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="Euhw5VeVrsuogN7lSW1.KQKXmkqkrMD7mJAXvaaK8q.Uzf+80+Dk4AapMujgLoDGDvUWV1XZaWFQOFGQwSLpGY=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EmSDW46YXTAc9dwdqw7.Hi/dd0UtGr4g+f2VnSXYXW.ppkh9QkmvHiGxPhVSHXIIlhb1/VM/4zXvrJ39yND7E8=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EdjDSl6We4mVbvNMTX1.wLC6dVfz8lLGaxhyio008q.7i2moCy+y4MYsxO6gmU/QAE8PqWfj4xQyeIYRyoD3Nk=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EVCmrdMKmXv6gVoYhvd.Zc4aKl/2Ri4I9uVZ3/5Dxq.ZsbM0sbrJEHIs48jXJSSBtTT/VqzPyZCqdlHqCY+368=")
ki5.loginResult()

#ki6 = LINETCR.LINE()
#ki6.login(token='ElnyygeY9Ryi9ssHmnc1.FTDC2gYUpTJqL7sBC2uAuq.IdbIZbedT1N3sDsco8Wu1DTm2AyMVD9HRr3rAXMvPBc=')
#ki6.loginResult()


#ki4 = LINETCR.LINE()
#ki4.login(token="Ekp9DIn7ZOF68PRT6NE2.ptORzz3sLbeG01QeTJsgeG.+43NBwiGAyx/HLhTUjf5hfcefo/pRN+IPs89ptqCQxQ=")
#ki4.loginResult()

#ki5 = LINETCR.LINE()
#ki5.login(token="EkZI8XiCp5ZTkYU29tC5.zNVivIokyd1dCo0dpANHvq.0LNZCi0tmVpGnI+hRRRA5P0wfU4xDv+PpBNcGYD0sY4=")
#ki5.loginResult()

#ki6 = LINETCR.LINE()
#ki6.login(token="EkJ5l49Apx6J60DHyfU4.tWI+bgToteDmanSLf3rEza.HEEAt8Hc5NEThS7g7tKGBL89uHYdJGZSOIc6N5deibQ=")
#ki6.loginResult()
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""       Self Bots Command:
『▀▄▀▄▀[ S̶E̶X̶ B̶O̶T̶ ]▀▄▀▄▀』

􀜁􀇔􏿿 [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅]
~>[Id]
~>[Mymid]
~>[Me]
~>[Join:Link Group]
~>[TL:Text] 
~>[MyName:Text]
~>[Mybio:Text]
~>[Gift]
~>[Mid: 「mid」]
~>[Glist]
~>[Group id]
~>[Group cancel]
~>[Contact on/off]
~>[Auto join on/off]
~>[Auto leave on/off]
~>[Auto add on/off]
~>[Bans:on]
~>[Unbans:on]
~>[Banlist]
~>[Mcheck] 
~>[Message Confirmation]
~>[Group bc Text]
~>[Contact bc Text]
~>[Allgbc Text]
~>[Allcbc Text]
~>[Reboot]

􀜁􀇔􏿿 ₣Ʉ₦₦Ɏ ₵Ø₥₥₳₦Đ

~>[#:Text]
~>[Spam on/off 10 TEXT]
~>[Hola @/Cuy @]
~>[Copy @]
~>[Default]
~>[Ava @]
~>[Cov @]
~>[Getava @]
~>[Yt:Text]
~>[Music:Text]
~>[Vn Text]
~>[Vn-id/en/kr/jp TEXT]
~>[Sid:ID LINE]
~>[Ig:ID IG]
~>[@crash]
~>[Tag]

􀜁􀇔􏿿 [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅ ̶̲̅ɪ̶̲̅ɴ̶̲̅ ̶̲̅G̶̲̅ʀ̶̲̅ᴏ̶̲̅ᴜ̶̲̅ᴘ̶̲̅]

~>[Invite:「mid」]
~>[Kick: Kick by mid]
~>[Kick @]
~>[1kick @]
~>[Ginfo]
~>[Cancel]
~>[Backup]
~>[Gn Text]
~>[Gurl]
~>[gurl「Group Id」]
~>[Nk「Name」] 
~>[Bye ]
~>[Ban:/@]
~>[Unban:/@]
~>[Clearban]
~>[Link on/off]
~>[Protect on/off] 
~>[Qr on/off] 
~>[Invite on/off] 
~>[Cancel on/off] 

􀜁􀇔􏿿 ᶜᴼᴹᴹᴬᴺᴰ ᴬˢˢᴵˢᵀᴬᴺᶜᴱ

~>[Allbots]
~>[All mid]
~>[All:Text - CN bots]
~>[Allbio:Text]
~>[Bots out]
~>[Creator]
~>[Respon]
~>[Slave]
~>[Allbye]
~>[Copy all @]
~>[Defaultall]

☆『—••÷[Ş̶̴̨͈̬̰̲̤͙̯̳̫̦̟̜̐͂̉ͪͦͧ͐͐̍̈́̔ͯͣͯͤ̿́͢͜͡Ȇ̢̨͉͙̯̼̙̠̣̳͖̪͙̩̹͘͜͜͢͢͝҉̷̵̵̛̕͜͢X̼͈̭͉̲̼̖̻͙̭̦̺̝̣̲̻̥ͤͫ͂͏̶̧̀̕҉҉̛̕͘͘͢͞͏̢͘͘S̶̳̪͙͙̪̗ͬ̑̉͑ͬ̂̑̄͝҉̴̸̡̡̡̧̧̕͢͟͠҉̛͉̜̫̃̉͂̆ͤ̒̽ͮ̅̂͗ͨ̈́̊͞͡ͅ҉̢́̕͜͞͝҉͘͠͡B̜͔ͫ͘͜͏̵̢̨̨́̕͜҉҉̶̧́͘̕͟͜͝Ớ̵̶̸̷̷̧͚̫̩̻̭̺̟̭͝T̳̺̙̩̝̪̝͕̘̟̰͚̤̤͓͎̰̔̓ͣͭ̆̒̓ͨͤ͂̀̅̓̾̍̍ͅ͏̀͢͜͟͏̴̶̢̛̀̀̀]÷••—』☆
http://line.me/ti/p/dsa3b_Uto-
"""

helo=""

KAC=[cl,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki5mid = ki5.getProfile().mid
#ki6mid = ki6.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid]
profile = cl.getProfile()
admsa = "ua839713afa40928bbac0f55df34b0825"
OA1 = "uec71b06b07a50a16a4dbff0408936cda"
OA2 = "uc38a9456e244f0e0575d8d25514cb87f"

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"""THX FOR ADD : 😉😉😉
Don't Ask Me How To Make A Baby
""",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"꧁􀰂􀇉Rakaa★􏿿􀜁􀅔ST􏿿꧂",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "detectMention":True,
    "Welcome":False,
    "Out":False,
    "copy":True,
    "copy2":"target",
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


contact = cl.getProfile()
contact1 = ki.getProfile()
contact2 = ki2.getProfile()
contact3 = ki3.getProfile()
contact4 = ki4.getProfile()
contact5 = ki5.getProfile()
backup = cl.getProfile()
backup1 = ki.getProfile()
backup2 = ki2.getProfile()
backup3 = ki3.getProfile()
backup4 = ki4.getProfile()
backup5 = ki5.getProfile()
backup.displayName = contact.displayName
backup1.displayName = contact1.displayName
backup2.displayName = contact2.displayName
backup3.displayName = contact3.displayName
backup4.displayName = contact4.displayName
backup5.displayName = contact5.displayName
backup.statusMessage = contact.statusMessage
backup1.statusMessage = contact1.statusMessage
backup2.statusMessage = contact2.statusMessage
backup3.statusMessage = contact3.statusMessage
backup4.statusMessage = contact4.statusMessage
backup5.statusMessage = contact5.statusMessage
backup.pictureStatus = contact.pictureStatus
backup1.pictureStatus = contact1.pictureStatus
backup2.pictureStatus = contact2.pictureStatus
backup3.pictureStatus = contact3.pictureStatus
backup4.pictureStatus = contact4.pictureStatus
backup5.pictureStatus = contact5.pictureStatus


def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
      akh = akh + 3
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 4
      akh = akh + 1
      bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1, "Thanks For Inviting Me To Your Group \n\nJangan Lupa Add Ya OA DIBAWAH INI \n\nDan Follow Juga Intagram gue: \ninstagram.com/_eummm")
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 15:
        	if wait["Out"] == True:
        	    cl.sendImageWithURL(op.param1, "http://dl.profile.line.naver.jp/0h-nj1PhPxckFXSF4-2ZkNFmsNfCwgZmMJOS09I3BPKnZ7eDITOC40cHEdJCR9cWFDOS80ISUbLSV_")
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nSEE YOU BITCH")
                print "kluar aja lu numpang crot doang..."
        if op.type == 17:
        	if wait["Welcome"] == True:
        	    cl.sendImageWithURL(op.param1, "http://dl.profile.line.naver.jp/0h-nj1vEWIckFXSF4vXMkNFmsNfCwgZmMJOS09I3BPKnZ7eDITOC40cHEdJCR9cWFDOS80ISUbLSV_")
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nWELCOME TO MY ROOM BITCH")
                print "Pelanggan baru Datang"
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ua839713afa40928bbac0f55df34b0825":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")

            elif 'MENTION' in msg.contentMetadata.keys() != None:
                    if wait["detectMention"] == True:
                        contact = cl.getContact(msg.from_)
                        cName = contact.displayName
                        balas = [cName + "Apasih ganggu aja dd lagi naena :v",cName + "ngapain ngetag? Kangen ya",cName + "Ngk usah tag!! klo pnting atw kangn pc aja",cName + "Gabut Loe Tag Tag",cName + "Tanggung Nih dkit lgi Croott"]
                        ret_ = "[This is Auto Reply]\n " + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees= mention['MENTIONEES']
                        for mention in mentionees:
                            if mention['M'] in Bots:
                                cl.sendText(msg.to,ret_)
                                break


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Allbots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
            elif "Rk1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Rk2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Rk3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Rk4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "Rk5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "Rk6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","1gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["I gift","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","2gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","3gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","4gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)
#--------------[All gift]------------
            elif msg.text in ["All gift","all gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
#-----------------------[Ats Section]------------------------
            elif msg.text in ["Tag","Ats"]:
                if msg.toType == 2:
                       group = cl.getGroup(msg.to)
                       nama = [contact.mid for contact in group.members]
                       nm1, nm2, nm3, nm4, nm5,  jml = [], [], [], [], [], len(nama)
                       if jml <= 100:
                          mention(msg.to, nama)
                       if jml > 100 and jml < 500:
                          for i in range(0, 99):
                              nm1 += [nama[i]]
                          mention(msg.to, nm1)
                          for j in range(100, len(nama)-1):
                              nm2 += [nama[j]]
                          mention(msg.to, nm2)
                          for k in range(200, len(nama)-1):
                              nm3 += [nama[k]]
                          mention(msg.to, nm3)
                          for l in range(300, len(nama)-1):
                              nm4 += [nama[l]]
                          mention(msg.to, nm4)
                          for m in range(400, len(nama)-1):
                              nm5 += [nama[m]]
                          mention(msg.to, nm5)
                       if jml > 500:
                           print "500mem wow"

            elif msg.text in ["B Cancel","Cancelall","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Nothing")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Nothing")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Rk1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Rk2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Rk3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Rk4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Rk5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Rk6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                #ki6.sendText(msg.to,ki6mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#----------[yt section]-----------------------------
            elif 'yt:' in  msg.text.lower():
                judul=msg.text.lower().replace('yt:', "")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'

                    url     = 'http://www.youtube.com/results'
                    params  = {'search_query': judul}

                    r       = s.get(url, params=params)
                    soup    = BeautifulSoup(r.content, 'html5lib')
                    hasil   = ""

                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ' '.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))

                    cl.sendText(msg.to,hasil)
#----------[music section]-----------
            elif 'music:' in msg.text.lower():
 	        songname=msg.text.lower().replace('music:','')
                params = {'songname': songname}
	        r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	        data     = r.text
	        data = json.loads(data)
                for path in data:
                    hasil = 'Music For You\n\n'
                    hasil += 'Title : ' + path[0]
                    hasil += '\nDuration : ' + path[1]
                    hasil += '\nDownload Link : ' + path[4]
                    hasil += '\nLirik : ' + path[2]
                    cl.sendAudioWithURL(msg.to,path[3])
                    #cl.sendAudioWithURL(msg.to, path[4])
                    cl.sendText(msg.to, hasil)
#-------------TTS ID-----------------
            elif "Vn-id " in msg.text:
                query = msg.text.replace("Vn-id ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url    = 'https://google-translate-proxy.herokuapp.com/api/tts'
                    params = {
                                'language': 'id',
                                'speed': '1',
                                'query': query
                                }
                    r    = s.get(url, params=params)
                    mp3  = r.url
                    cl.sendAudioWithURL(msg.to, mp3)
#-------------TTS EN-----------------
            elif "Vn-en " in msg.text:
                query = msg.text.replace("Vn-en ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url    = 'https://google-translate-proxy.herokuapp.com/api/tts'
                    params = {
                                'language': 'en',
                                'speed': '1',
                                'query': query
                                }
                    r    = s.get(url, params=params)
                    mp3  = r.url
                    cl.sendAudioWithURL(msg.to, mp3)
#-------------TTS KR-----------------
            elif "Vn-kr " in msg.text:
                query = msg.text.replace("Vn-kr ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url    = 'https://google-translate-proxy.herokuapp.com/api/tts'
                    params = {
                                'language': 'ko',
                                'speed': '1',
                                'query': query
                                }
                    r    = s.get(url, params=params)
                    mp3  = r.url
                    cl.sendAudioWithURL(msg.to, mp3)
#-------------TTS JP-----------------
            elif "Vn-jp " in msg.text:
                query = msg.text.replace("Vn-jp ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url    = 'https://google-translate-proxy.herokuapp.com/api/tts'
                    params = {
                                'language': 'ja',
                                'speed': '1',
                                'query': query
                                }
                    r    = s.get(url, params=params)
                    mp3  = r.url
                    cl.sendAudioWithURL(msg.to, mp3)
#-------SEARCH ID LINE---------------
            elif "Sid:" in msg.text:
                 userid = msg.text.replace("Sid:","")
                 contact = cl.findContactsByUserid(userid)
                 msg.contentType = 13
                 msg.contentMetadata = {'mid': contact.mid}
                 cl.sendMessage(msg)
#-----------SEARCH IG----------------
            elif "Ig:" in msg.text:
                cari = msg.text.replace("Ig:","")
                try:
                    response = requests.get("https://www.instagram.com/"+cari+"?__a=1")
                    data = response.json()
                    namaIG = str(data['user']['full_name'])
                    bioIG = str(data['user']['biography'])
                    mediaIG = str(data['user']['media']['count'])
                    verifIG = str(data['user']['is_verified'])
                    usernameIG = str(data['user']['username'])
                    followerIG = str(data['user']['followed_by']['count'])
                    profileIG = data['user']['profile_pic_url_hd']
                    privateIG = str(data['user']['is_private'])
                    followIG = str(data['user']['follows']['count'])
                    Url = str(data['user']['external_url'])
                    text = "==============================\n[Name] : "+namaIG+"\n[Biography] :\n"+bioIG+"\n[Follower] : "+followerIG +"\n[Following] : "+followIG+"\n[Media] : "+mediaIG+"\n[Verified] :"+verifIG+"\n[Private] : "+privateIG+"\nLinkID: instagram.com/"+usernameIG+"\nURL: "+Url+"\n=============================="
                    cl.sendImageWithURL(msg.to, profileIG)
                    cl.sendText(msg.to, str(text))
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#------------------------------------
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3name:" in msg.text:
                string = msg.text.replace("3name:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4name:" in msg.text:
                string = msg.text.replace("4name:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
#--------------------------------------------------------
            elif "5name:" in msg.text:
                string = msg.text.replace("5name:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6name:" in msg.text:
                string = msg.text.replace("6name:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OFF")
                    else:
                        cl.sendText(msg.to,"It is already OFF")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OFF")
                    else:
                        cl.sendText(msg.to,"It is already OFF")
#================All Deff ON========================
            elif msg.text in ['Deff on']:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable")
                    else:
                        cl.sendText(msg.to,"Already ON")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
#================Deff one by one=================
            elif msg.text in ['Protect on']:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable")
                    else:
                        cl.sendText(msg.to,"Already ON")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text in ['Qr on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text in ['Invite on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text in ['Cancel on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable")
                    else:
                        cl.sendText(msg.to,"Already ON")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text in ['Qr on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text in ['Invite on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text in ['Cancel on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Enable")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
#==================All Deff OFF===================
            elif msg.text in ["Deff off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
#==================Deff one by one off=============
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text in ["Qr off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text in ["Invite off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text in ["Cancel off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Disable")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value")
            elif msg.text in ["Auto leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ON")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Is already open")
            elif msg.text in ["Auto leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ON")
                    else:
                        cl.sendText(msg.to,"Sudah off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Is already close")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ON")
                    else:
                        cl.sendText(msg.to,"ON")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OFF")
                    else:
                        cl.sendText(msg.to,"OFF")
            elif msg.text in ["Auto reply on"]:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ON")
                    else:
                        cl.sendText(msg.to,"It is already ON")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Is already ON")
            elif msg.text in ["Auto reply off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"OFF")
                    else:
                        cl.sendText(msg.to,"Is OFF")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Is already OFF")
            elif "Kam on" in msg.text:
                wait["Welcome"] = True
                cl.sendText(msg.to,"Welcome has been set to On")

            elif "Kam off" in msg.text:
                wait["Welcome"] = False
                cl.sendText(msg.to,"Welcome has been set to off")
#-------------------------------------------
            elif "Out on" in msg.text:
                wait["Out"] = True
                cl.sendText(msg.to,"Get Out Has Been Set To On")

            elif "Out off" in msg.text:
                wait["Out"] = False
                cl.sendText(msg.to,"Get Out Has Been Set To Off")

            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+=" Contact:on✅ \n"
                else: md+=" Contact:off❌\n"
                if wait["autoJoin"] == True: md+=" Auto Join:on✅ \n"
                else: md +=" Auto Join:off❌\n"
                if wait["autoCancel"]["on"] == True:md+=" Auto cancel:" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel:off❌ \n"
                if wait["leaveRoom"] == True: md+=" Auto leave:on✅ \n"
                else: md+=" Auto leave:off❌ \n"
                if wait["timeline"] == True: md+=" Share:on✅ \n"
                else:md+=" Share:off❌ \n"
                if wait["autoAdd"] == True: md+=" Auto add:on✅ \n"
                else:md+=" Auto add:off❌ \n"
                if wait["commentOn"] == True: md+=" Auto komentar:on✅ \n"
                else:md+=" Auto komentar:off❌ \n"
                if wait["protect"] == True: md+=" Protect:on✅ \n"
                else:md+=" Protect:off❌ \n"
                if wait["linkprotect"] == True: md+="Link Protect:on✅ \n"
                else:md+=" Link Protect:off❌\n"
                if wait["inviteprotect"] == True: md+="Invitation Protect:on✅\n"
                else:md+=" Invitation Protect:off❌\n"
                if wait["cancelprotect"] == True: md+" CancelProtect:on✅ \n"
                else:md+=" Cancel Protect:off❌ \n"
                if wait["detectMention"] == True: md+=" Auto reply:on✅ \n"
                else:md+=" Auto reply:off❌ \n"
                if wait["Welcome"] == True: md+=" Kam:on✅ \n"
                else:md+=" Kam:off❌ \n"
                if wait["Out"] == True: md+=" Out:on✅ \n"
                else:md+=" Out:off❌ \n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            elif "@crash" in msg.text:
                msg.contentType = 13
                msg.contentMetadata={'mid': "ua839713afa40928bbac0f55df34b0825,'"}
                cl.sendMessage(msg)
            elif "OA DIBAWAH " in msg.text:
            	msg.contentType = 13
                msg.contentMetadata = {'mid': OA1}
                msg.contentMetadata = {'mid': OA2}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿")
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'bots out':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                #gid = ki6.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    #ki6.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All bots have been out of all the groups.")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Reject"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Reject all success")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Auto add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "1gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl+","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")
            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com unbl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("1kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb " in msg.text:
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass

            elif ("Ban " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["List group","Glist"]:
                 gid = cl.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⭐] %s \n" % (cl.getGroup(i).name + " | Members : " + str(len (cl.getGroup(i).members)))
                 cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))

#----------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")


            elif "Clearban" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Clear ban")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
#-----------------------------------------------------------
            elif msg.text == "Setview":
                    cl.sendText(msg.to, "Check Yang nyimak")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "Viewseen":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to,"======Tercyduck====== %s\n=====Tukang Ngintip======\n%s\nReading point creation date n time:\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                         cl.sendText(msg.to,"An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")


#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-------------------------[REBOOT]--------------------------
            elif msg.text in ["Reboot"]:
                cl.sendText(msg.to, "Bot Has Been Restart")
                restart_program()
                print ("Restart Success")
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            cl.sendText(msg.to, text)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

#-----------------------------------------------------------
            elif msg.text.lower() == 'respon':
                profile = ki.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki6.sendText(msg.to, text)

#-----------------------------------------------------------speed
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "�" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            #ki6.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

#---------------------------------------------------
            elif msg.text in ["Kembali","Default"]:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Back To Default")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif msg.text in ["Kembalii","Defaultall"]:
                    try:
                       ki.updateDisplayPicture(backup1.pictureStatus)
                       ki.updateProfile(backup1)
                       ki.sendText(msg.to, "Back To Default")
                       ki2.updateDisplayPicture(backup2.pictureStatus)
                       ki2.updateProfile(backup2)
                       ki2.sendText(msg.to, "Back To Default")
                       ki3.updateDisplayPicture(backup3.pictureStatus)
                       ki3.updateProfile(backup3)
                       ki3.sendText(msg.to, "Back To Default")
                       ki4.updateDisplayPicture(backup4.pictureStatus)
                       ki4.updateProfile(backup4)
                       ki4.sendText(msg.to, "Back To Default")
                       ki5.updateDisplayPicture(backup5.pictureStatus)
                       ki5.updateProfile(backup5)
                       ki5.sendText(msg.to, "Back To Default")
                    except Exception as e:
                       ki.sendText(msg.to, str(e))
                       ki2.sendText(msg.to, str(e))
                       ki3.sendText(msg.to, str(e))
                       ki4.sendText(msg.to, str(e))
                       ki5.sendText(msg.to, str(e))
#----------------[Copy Section]---------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                     for target in targets:
                         try:
                              cl.cloneContactProfile(target)
                         except Exception as e:
                             print e
#----------------------------------------------
            elif "Copy all @" in msg.text:
                if msg.toType == 2:
                    print "[COPY all] Ok"
                    _name = msg.text.replace("Copy all @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                     for target in targets:
                         try:
                              ki.cloneContactProfile(target)
                              ki2.cloneContactProfile(target)
                              ki3.cloneContactProfile(target)
                              ki4.cloneContactProfile(target)
                              ki5.cloneContactProfile(target)
                         except Exception as e:
                             print e
#-------------------------[Steal section------------------------------
            elif "Cov @" in msg.text:
                if msg.toType == 2:
                    print "[Command]cov executing"
                _name = msg.text.replace("Cov @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]cov executed"

            elif "Ava @" in msg.text:
                if msg.toType == 2:
                    print "[Command]dp executing"
                _name = msg.text.replace("Ava @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#---------------------------------Get all ava------------------------------------------------------
            elif "Getava" in msg.text:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                                  x=cl.getContact(target)
                                  tmid=x.mid
                                  msg.contentType = 0
                                  contact = cl.getContact(tmid)
                                  try:
                                          cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                  except Exception as pk:
                                          cl.sendText(msg.to,str(pk))

            elif "Stealgrup" in msg.text:
                    group = cl.getGroup(msg.to)
                    cl.sendMessage(msg.to,"Gambar Grup :\n=> http://dl.profile.line-cdn.net/" + group.pictureStatus)
#-------------------------------------------------------------
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass

#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Please Wait...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
               # ki6.sendText(msg.to, "%sseconds" % (elapsed_time))

#-----------------------------------------------
            elif msg.text.lower() == 'slave':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                       # ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                       # time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == 'backup':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == 'rk come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                       # ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "1in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "2in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "3in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "4in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "5in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "6in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == 'allbye':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                       # ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------[bye me]--------------
            elif "Dadah" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "1bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "2bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "3bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "4bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "5bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "6bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rk key" in msg.text:
                ki.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿SEXS BOT [Rk]􀜁􀇔􏿿􀜁􀇔􏿿
     􀜁􀇔􏿿ᶜᴼᴹᴹᴬᴺᴰ ᴬˢˢᴵˢᵀᴬᴺᵀ􀜁􀇔􏿿 

􀜁􀇔􏿿[1in]
􀜁􀇔􏿿[1name:]
􀜁􀇔􏿿[Cancelall]
􀜁􀇔􏿿[kick @]
􀜁􀇔􏿿[Ban @]
􀜁􀇔􏿿[kill]
􀜁􀇔􏿿[Sb say Text]
􀜁􀇔􏿿[Respon]
􀜁􀇔􏿿[1gift]
􀜁􀇔􏿿[Sb1 mid]
􀜁􀇔􏿿[1bye]

☆『S̳͇̭͖̥͊͌͟͠E̷̦͔͍̙͕̎̾͆̕X̯͓͓͈̽ͯ̌̋̃͑͐ͤ͠S̙̬̦͎͍̳ͥ͞ ̩͖̖͒͐B̧͍͙͈̱̫ͮ̇ͧ̈ͤ͗͒͊̀ͅO̶̭͙̹̞͙̗͚̿͑ͪ̿̎̇ͭ͂͜ͅT̴̺̼̜̮̝̠̱̐̊̂̓S̼̯͈͕ͫ̉ͅ ̪̯̳̯͕̰̫̓̽ͪ̇̄ͥͯA̸̙ͨ͆͌͜Sͥ͊҉̮͘S͙̬ͪ̏̔̅̂̈́ͯ̎I̳͕̺̞̰̭̬̫̔͑̒͌ͬͧ͘S̝̬̍ͤ̉T̫̝͙͔̖̯͔́̊ͦ͗́͜A̧̳̼ͦͦ̆ͮͨ̅̚͠N̶̛̯̯͕̺̠͓̹̓̈̈́ͧ̑͋̉T̞̙̙̽̄ͬ͢͝』☆
""")
                ki2.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿SEXS BOT [SB]􀜁􀇔􏿿􀜁􀇔􏿿
     􀜁􀇔􏿿ᶜᴼᴹᴹᴬᴺᴰ ᴬˢˢᴵˢᵀᴬᴺᵀ􀜁􀇔􏿿 

􀜁􀇔􏿿[2in]
􀜁􀇔􏿿[2name:]
􀜁􀇔􏿿[Cancelall]
􀜁􀇔􏿿[kick @]
􀜁􀇔􏿿[Ban @]
􀜁􀇔􏿿[kill]
􀜁􀇔􏿿[Sb say Text]
􀜁􀇔􏿿[Respon]
􀜁􀇔􏿿[2gift]
􀜁􀇔􏿿[Sb2 mid]
􀜁􀇔􏿿[2bye]

☆『S̳͇̭͖̥͊͌͟͠E̷̦͔͍̙͕̎̾͆̕X̯͓͓͈̽ͯ̌̋̃͑͐ͤ͠S̙̬̦͎͍̳ͥ͞ ̩͖̖͒͐B̧͍͙͈̱̫ͮ̇ͧ̈ͤ͗͒͊̀ͅO̶̭͙̹̞͙̗͚̿͑ͪ̿̎̇ͭ͂͜ͅT̴̺̼̜̮̝̠̱̐̊̂̓S̼̯͈͕ͫ̉ͅ ̪̯̳̯͕̰̫̓̽ͪ̇̄ͥͯA̸̙ͨ͆͌͜Sͥ͊҉̮͘S͙̬ͪ̏̔̅̂̈́ͯ̎I̳͕̺̞̰̭̬̫̔͑̒͌ͬͧ͘S̝̬̍ͤ̉T̫̝͙͔̖̯͔́̊ͦ͗́͜A̧̳̼ͦͦ̆ͮͨ̅̚͠N̶̛̯̯͕̺̠͓̹̓̈̈́ͧ̑͋̉T̞̙̙̽̄ͬ͢͝』☆
""")
                ki3.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿SEXS BOT [SB]􀜁􀇔􏿿􀜁􀇔􏿿
     􀜁􀇔􏿿ᶜᴼᴹᴹᴬᴺᴰ ᴬˢˢᴵˢᵀᴬᴺᵀ􀜁􀇔􏿿 

􀜁􀇔􏿿[3in]
􀜁􀇔􏿿[3name:]
􀜁􀇔􏿿[Cancelall]
􀜁􀇔􏿿[kick @]
􀜁􀇔􏿿[Ban @]
􀜁􀇔􏿿[kill]
􀜁􀇔􏿿[Sb say Text]
􀜁􀇔􏿿[Respon]
􀜁􀇔􏿿[3gift]
􀜁􀇔􏿿[Sb3 mid]
􀜁􀇔􏿿[3bye]

☆『S̳͇̭͖̥͊͌͟͠E̷̦͔͍̙͕̎̾͆̕X̯͓͓͈̽ͯ̌̋̃͑͐ͤ͠S̙̬̦͎͍̳ͥ͞ ̩͖̖͒͐B̧͍͙͈̱̫ͮ̇ͧ̈ͤ͗͒͊̀ͅO̶̭͙̹̞͙̗͚̿͑ͪ̿̎̇ͭ͂͜ͅT̴̺̼̜̮̝̠̱̐̊̂̓S̼̯͈͕ͫ̉ͅ ̪̯̳̯͕̰̫̓̽ͪ̇̄ͥͯA̸̙ͨ͆͌͜Sͥ͊҉̮͘S͙̬ͪ̏̔̅̂̈́ͯ̎I̳͕̺̞̰̭̬̫̔͑̒͌ͬͧ͘S̝̬̍ͤ̉T̫̝͙͔̖̯͔́̊ͦ͗́͜A̧̳̼ͦͦ̆ͮͨ̅̚͠N̶̛̯̯͕̺̠͓̹̓̈̈́ͧ̑͋̉T̞̙̙̽̄ͬ͢͝』☆
""")
                ki4.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿SEXS BOT [SB]􀜁􀇔􏿿􀜁􀇔􏿿
     􀜁􀇔􏿿ᶜᴼᴹᴹᴬᴺᴰ ᴬˢˢᴵˢᵀᴬᴺᵀ􀜁􀇔􏿿 

􀜁􀇔􏿿[4in]
􀜁􀇔􏿿[4name:]
􀜁􀇔􏿿[Cancelall]
􀜁􀇔􏿿[kick @]
􀜁􀇔􏿿[Ban @]
􀜁􀇔􏿿[kill]
􀜁􀇔􏿿[Sb say Text]
􀜁􀇔􏿿[Respon]
􀜁􀇔􏿿[4gift]
􀜁􀇔􏿿[Sb4 mid]
􀜁􀇔􏿿[4bye]

☆『S̳͇̭͖̥͊͌͟͠E̷̦͔͍̙͕̎̾͆̕X̯͓͓͈̽ͯ̌̋̃͑͐ͤ͠S̙̬̦͎͍̳ͥ͞ ̩͖̖͒͐B̧͍͙͈̱̫ͮ̇ͧ̈ͤ͗͒͊̀ͅO̶̭͙̹̞͙̗͚̿͑ͪ̿̎̇ͭ͂͜ͅT̴̺̼̜̮̝̠̱̐̊̂̓S̼̯͈͕ͫ̉ͅ ̪̯̳̯͕̰̫̓̽ͪ̇̄ͥͯA̸̙ͨ͆͌͜Sͥ͊҉̮͘S͙̬ͪ̏̔̅̂̈́ͯ̎I̳͕̺̞̰̭̬̫̔͑̒͌ͬͧ͘S̝̬̍ͤ̉T̫̝͙͔̖̯͔́̊ͦ͗́͜A̧̳̼ͦͦ̆ͮͨ̅̚͠N̶̛̯̯͕̺̠͓̹̓̈̈́ͧ̑͋̉T̞̙̙̽̄ͬ͢͝』☆
""")
                ki5.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿SEXS BOT [SB]􀜁􀇔􏿿􀜁􀇔􏿿
     􀜁􀇔􏿿ᶜᴼᴹᴹᴬᴺᴰ ᴬˢˢᴵˢᵀᴬᴺᵀ􀜁􀇔􏿿 

􀜁􀇔􏿿[5in]
􀜁􀇔􏿿[5name:]
􀜁􀇔􏿿[Cancelall]
􀜁􀇔􏿿[kick @]
􀜁􀇔􏿿[Ban @]
􀜁􀇔􏿿[kill]
􀜁􀇔􏿿[Sb say Text]
􀜁􀇔􏿿[Respon]
􀜁􀇔􏿿[5gift]
􀜁􀇔􏿿[Sb5 mid]
􀜁􀇔􏿿[5bye]

☆『S̳͇̭͖̥͊͌͟͠E̷̦͔͍̙͕̎̾͆̕X̯͓͓͈̽ͯ̌̋̃͑͐ͤ͠S̙̬̦͎͍̳ͥ͞ ̩͖̖͒͐B̧͍͙͈̱̫ͮ̇ͧ̈ͤ͗͒͊̀ͅO̶̭͙̹̞͙̗͚̿͑ͪ̿̎̇ͭ͂͜ͅT̴̺̼̜̮̝̠̱̐̊̂̓S̼̯͈͕ͫ̉ͅ ̪̯̳̯͕̰̫̓̽ͪ̇̄ͥͯA̸̙ͨ͆͌͜Sͥ͊҉̮͘S͙̬ͪ̏̔̅̂̈́ͯ̎I̳͕̺̞̰̭̬̫̔͑̒͌ͬͧ͘S̝̬̍ͤ̉T̫̝͙͔̖̯͔́̊ͦ͗́͜A̧̳̼ͦͦ̆ͮͨ̅̚͠N̶̛̯̯͕̺̠͓̹̓̈̈́ͧ̑͋̉T̞̙̙̽̄ͬ͢͝』☆
""")
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc","Kam"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Nan say " in msg.text:
				bctxt = msg.text.replace("Nan say ","")
                                ki.sendText(msg.to,(bctxt))
                                ki2.sendText(msg.to,(bctxt))
                                ki3.sendText(msg.to,(bctxt))
                                ki4.sendText(msg.to,(bctxt))
                                ki5.sendText(msg.to,(bctxt))
            elif "#:" in msg.text:
				bctxt = msg.text.replace("#:","")
                                cl.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				#ki6.sendText(msg.to,(bctxt))
#-------------------------------------PUISI SPAM-------------------------------------------
            elif "Hola @" in msg.text:
                            _name = msg.text.replace("Hola @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                   cl.sendText(msg.to,"Aku punya puisi buat kamu\n\n"+ datetime.today().strftime('%H:%M:%S'))
                                   cl.sendText(g.mid,"Ku mengejar bus yang mulai berjalan")
                                   cl.sendText(g.mid,"Ku ingin ungkapkan kepada dirimu")
                                   cl.sendText(g.mid,"Kabut dalam hatiku telah menghilang")
                                   cl.sendText(g.mid,"Dan hal yang penting bagiku pun terlihat")
                                   cl.sendText(g.mid,"Walaupun jawaban itu sebenarnya begitu mudah")
                                   cl.sendText(g.mid,"Tetapi entah mengapa diriku melewatkannya")
                                   cl.sendText(g.mid,"Untukku menjadi diri sendiri")
                                   cl.sendText(g.mid,"Ku harus jujur, pada perasaanku")
                                   cl.sendText(g.mid,"Ku suka dirimu ku suka")
                                   cl.sendText(g.mid,"Ku berlari sekuat tenaga")
                                   cl.sendText(g.mid,"Ku suka selalu ku suka")
                                   cl.sendText(g.mid,"Ku teriak sebisa suaraku")
                                   cl.sendText(g.mid,"Ku suka dirimu ku suka")
                                   cl.sendText(g.mid,"Walau susah untukku bernapas")
                                   cl.sendText(g.mid,"Tak akan ku sembunyikan")
                                   cl.sendText(g.mid,"Saat ku sadari sesuatu menghilang")
                                   cl.sendText(g.mid,"Hati ini pun resah tidak tertahankan")
                                   cl.sendText(g.mid,"Sekarang juga yang bisa ku lakukan")
                                   cl.sendText(g.mid,"Merubah perasaan ke dalam kata kata")
                                   cl.sendText(g.mid,"Mengapa sedari tadi")
                                   cl.sendText(g.mid,"Aku hanya menatap langit")
                                   cl.sendText(g.mid,"Mataku berkaca kaca")
                                   cl.sendText(g.mid,"Berlinang tak bisa berhenti")
                                   cl.sendText(g.mid,"Di tempat kita tinggal, didunia ini")
                                   cl.sendText(g.mid,"Dipenuhi cinta, kepada seseorang")
                                   cl.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   cl.sendText(g.mid,"Janji tak lepas dirimu lagi")
                                   cl.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   cl.sendText(g.mid,"Akhirnya kita bisa bertemu")
                                   cl.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   cl.sendText(g.mid,"Ku akan bahagiakan dirimu")
                                   cl.sendText(g.mid,"Ku ingin kau mendengarkan")
                                   cl.sendText(g.mid,"Jika jika kamu ragu")
                                   cl.sendText(g.mid,"Takkan bisa memulai apapun")
                                   cl.sendText(g.mid,"Ungkapkan perasaanmu")
                                   cl.sendText(g.mid,"Jujurlah dari sekarang juga")
                                   cl.sendText(g.mid,"Jika kau bersuara")
                                   cl.sendText(g.mid,"Cahaya kan bersinar")
                                   cl.sendText(g.mid,"Ku suka dirimu ku suka")
                                   cl.sendText(g.mid,"Ku berlari sekuat tenaga")
                                   cl.sendText(g.mid,"Ku suka selalu ku suka")
                                   cl.sendText(g.mid,"Ku teriak sebisa suaraku")
                                   cl.sendText(g.mid,"Ku suka dirimu ku suka")
                                   cl.sendText(g.mid,"Sampaikan rasa sayangku ini")
                                   cl.sendText(g.mid,"Ku suka selalu ku suka")
                                   cl.sendText(g.mid,"Ku teriakkan ditengah angin")
                                   cl.sendText(g.mid,"Ku suka dirimu ku suka")
                                   cl.sendText(g.mid,"Walau susah untuk ku bernapas")
                                   cl.sendText(g.mid,"Tak akan ku sembunyikan")
                                   cl.sendText(g.mid,"Oogoe daiyamondo~")
                                   cl.sendText(g.mid,"Katakan dengan berani")
                                   cl.sendText(g.mid,"Jika kau diam kan tetap sama")
                                   cl.sendText(g.mid,"Janganlah kau merasa malu")
                                   cl.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   cl.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   cl.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   cl.sendText(g.mid,"Ungkapkan perasaanmu")
                                   cl.sendText(g.mid,"Jujurlah dari sekarang juga..")
                                   cl.sendText(g.mid,"#Puisi by Unknown􀠁􀄅Bad Ass􏿿􀌂􀆿rose stalk􏿿")
                                   cl.sendText(g.mid,"Thanks For You\n􀄃􀄷heart􏿿 My Inspiration 􀄃􀄷heart􏿿 ")
                                   cl.sendText(msg.to, "Puisi dari aku untuk yg tercinta\nsudah terkirim :)\n\n"+ datetime.today().strftime('%H:%M:%S'))
                                   print "Done spam"
#-------------------------------------[PUISI SPAM2]----------------------------------------------								   
            elif "Cuy @" in msg.text:
                            _name = msg.text.replace("Cuy @","")
                            _nametarget = _name.rstrip(' ')
                            gs = cl.getGroup(msg.to)
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                   cl.sendText(msg.to,"Aku punya puisi buat kamu\n\n"+ datetime.today().strftime('%H:%M:%S'))
                                   ki.sendText(g.mid,"Ku mengejar bus yang mulai berjalan")
                                   ki.sendText(g.mid,"Ku ingin ungkapkan kepada dirimu")
                                   ki.sendText(g.mid,"Kabut dalam hatiku telah menghilang")
                                   ki.sendText(g.mid,"Dan hal yang penting bagiku pun terlihat")
                                   ki.sendText(g.mid,"Walaupun jawaban itu sebenarnya begitu mudah")
                                   ki.sendText(g.mid,"Tetapi entah mengapa diriku melewatkannya")
                                   ki.sendText(g.mid,"Untukku menjadi diri sendiri")
                                   ki.sendText(g.mid,"Ku harus jujur, pada perasaanku")
                                   ki.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki.sendText(g.mid,"Ku berlari sekuat tenaga")
                                   ki.sendText(g.mid,"Ku suka selalu ku suka")
                                   ki.sendText(g.mid,"Ku teriak sebisa suaraku")
                                   ki.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki.sendText(g.mid,"Walau susah untukku bernapas")
                                   ki.sendText(g.mid,"Tak akan ku sembunyikan")
                                   ki.sendText(g.mid,"Saat ku sadari sesuatu menghilang")
                                   ki.sendText(g.mid,"Hati ini pun resah tidak tertahankan")
                                   ki.sendText(g.mid,"Sekarang juga yang bisa ku lakukan")
                                   ki.sendText(g.mid,"Merubah perasaan ke dalam kata kata")
                                   ki.sendText(g.mid,"Mengapa sedari tadi")
                                   ki.sendText(g.mid,"Aku hanya menatap langit")
                                   ki.sendText(g.mid,"Mataku berkaca kaca")
                                   ki.sendText(g.mid,"Berlinang tak bisa berhenti")
                                   ki.sendText(g.mid,"Di tempat kita tinggal, didunia ini")
                                   ki.sendText(g.mid,"Dipenuhi cinta, kepada seseorang")
                                   ki.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   ki.sendText(g.mid,"Janji tak lepas dirimu lagi")
                                   ki.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   ki.sendText(g.mid,"Akhirnya kita bisa bertemu")
                                   ki.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   ki.sendText(g.mid,"Ku akan bahagiakan dirimu")
                                   ki.sendText(g.mid,"Ku ingin kau mendengarkan")
                                   ki.sendText(g.mid,"Jika jika kamu ragu")
                                   ki.sendText(g.mid,"Takkan bisa memulai apapun")
                                   ki.sendText(g.mid,"Ungkapkan perasaanmu")
                                   ki.sendText(g.mid,"Jujurlah dari sekarang juga")
                                   ki.sendText(g.mid,"Jika kau bersuara")
                                   ki.sendText(g.mid,"Cahaya kan bersinar")
                                   ki.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki.sendText(g.mid,"Ku berlari sekuat tenaga")
                                   ki.sendText(g.mid,"Ku suka selalu ku suka")
                                   ki.sendText(g.mid,"Ku teriak sebisa suaraku")
                                   ki.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki.sendText(g.mid,"Sampaikan rasa sayangku ini")
                                   ki.sendText(g.mid,"Ku suka selalu ku suka")
                                   ki.sendText(g.mid,"Ku teriakkan ditengah angin")
                                   ki.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki.sendText(g.mid,"Walau susah untuk ku bernapas")
                                   ki.sendText(g.mid,"Tak akan ku sembunyikan")
                                   ki.sendText(g.mid,"Oogoe daiyamondo~")
                                   ki.sendText(g.mid,"Katakan dengan berani")
                                   ki.sendText(g.mid,"Jika kau diam kan tetap sama")
                                   ki.sendText(g.mid,"Janganlah kau merasa malu")
                                   ki.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   ki.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   ki.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   ki.sendText(g.mid,"Ungkapkan perasaanmu")
                                   ki.sendText(g.mid,"Jujurlah dari sekarang juga..")
                                   ki.sendText(g.mid,"#Puisi by Unknown􀠁􀄅Bad Ass􏿿􀌂􀆿rose stalk􏿿")
                                   ki.sendText(g.mid,"Thanks For You\n􀄃􀄷heart􏿿 My Inspiration 􀄃􀄷heart􏿿 ")
                                   ki2.sendText(g.mid,"Ku mengejar bus yang mulai berjalan")
                                   ki2.sendText(g.mid,"Ku ingin ungkapkan kepada dirimu")
                                   ki2.sendText(g.mid,"Kabut dalam hatiku telah menghilang")
                                   ki2.sendText(g.mid,"Dan hal yang penting bagiku pun terlihat")
                                   ki2.sendText(g.mid,"Walaupun jawaban itu sebenarnya begitu mudah")
                                   ki2.sendText(g.mid,"Tetapi entah mengapa diriku melewatkannya")
                                   ki2.sendText(g.mid,"Untukku menjadi diri sendiri")
                                   ki2.sendText(g.mid,"Ku harus jujur, pada perasaanku")
                                   ki2.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki2.sendText(g.mid,"Ku berlari sekuat tenaga")
                                   ki2.sendText(g.mid,"Ku suka selalu ku suka")
                                   ki2.sendText(g.mid,"Ku teriak sebisa suaraku")
                                   ki2.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki2.sendText(g.mid,"Walau susah untukku bernapas")
                                   ki2.sendText(g.mid,"Tak akan ku sembunyikan")
                                   ki2.sendText(g.mid,"Saat ku sadari sesuatu menghilang")
                                   ki2.sendText(g.mid,"Hati ini pun resah tidak tertahankan")
                                   ki2.sendText(g.mid,"Sekarang juga yang bisa ku lakukan")
                                   ki2.sendText(g.mid,"Merubah perasaan ke dalam kata kata")
                                   ki2.sendText(g.mid,"Mengapa sedari tadi")
                                   ki2.sendText(g.mid,"Aku hanya menatap langit")
                                   ki2.sendText(g.mid,"Mataku berkaca kaca")
                                   ki2.sendText(g.mid,"Berlinang tak bisa berhenti")
                                   ki2.sendText(g.mid,"Di tempat kita tinggal, didunia ini")
                                   ki2.sendText(g.mid,"Dipenuhi cinta, kepada seseorang")
                                   ki2.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   ki2.sendText(g.mid,"Janji tak lepas dirimu lagi")
                                   ki2.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   ki2.sendText(g.mid,"Akhirnya kita bisa bertemu")
                                   ki2.sendText(g.mid,"Ku yakin ooo ku yakin")
                                   ki2.sendText(g.mid,"Ku akan bahagiakan dirimu")
                                   ki2.sendText(g.mid,"Ku ingin kau mendengarkan")
                                   ki2.sendText(g.mid,"Jika jika kamu ragu")
                                   ki2.sendText(g.mid,"Takkan bisa memulai apapun")
                                   ki2.sendText(g.mid,"Ungkapkan perasaanmu")
                                   ki2.sendText(g.mid,"Jujurlah dari sekarang juga")
                                   ki2.sendText(g.mid,"Jika kau bersuara")
                                   ki2.sendText(g.mid,"Cahaya kan bersinar")
                                   ki2.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki2.sendText(g.mid,"Ku berlari sekuat tenaga")
                                   ki2.sendText(g.mid,"Ku suka selalu ku suka")
                                   ki2.sendText(g.mid,"Ku teriak sebisa suaraku")
                                   ki2.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki2.sendText(g.mid,"Sampaikan rasa sayangku ini")
                                   ki2.sendText(g.mid,"Ku suka selalu ku suka")
                                   ki2.sendText(g.mid,"Ku teriakkan ditengah angin")
                                   ki2.sendText(g.mid,"Ku suka dirimu ku suka")
                                   ki2.sendText(g.mid,"Walau susah untuk ku bernapas")
                                   ki2.sendText(g.mid,"Tak akan ku sembunyikan")
                                   ki2.sendText(g.mid,"Oogoe daiyamondo~")
                                   ki2.sendText(g.mid,"Katakan dengan berani")
                                   ki2.sendText(g.mid,"Jika kau diam kan tetap sama")
                                   ki2.sendText(g.mid,"Janganlah kau merasa malu")
                                   ki2.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   ki2.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   ki2.sendText(g.mid,"“Suka” itu kata paling hebat!")
                                   ki2.sendText(g.mid,"Ungkapkan perasaanmu")
                                   ki2.sendText(g.mid,"Jujurlah dari sekarang juga..")
                                   ki2.sendText(g.mid,"#Puisi by Unknown􀠁􀄅Bad Ass􏿿􀌂􀆿rose stalk􏿿")
                                   ki2.sendText(g.mid,"Thanks For You\n􀄃􀄷heart􏿿 My Inspiration 􀄃􀄷heart􏿿 ")
                                   cl.sendText(msg.to, "Puisi dari aku untuk yg tercinta\nsudah terkirim :)\n\n"+ datetime.today().strftime('%H:%M:%S'))
                                   print "Done spam"
#=================SPAM GIFT=================================

            elif msg.text.lower() == 'pongg':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
#---------[Group Bc & Contact Bc Section]-----------------------------
            elif "Group bc " in msg.text:
                 bctxt = msg.text.replace("Group bc ", "")
                 n = cl.getGroupIdsJoined()
                 for manusia in n:
                      cl.sendText(manusia, (bctxt))

            elif "Contact bc " in msg.text:
                 bctxt = msg.text.replace("Contact bc ", "")
                 t = cl.getAllContactIds()
                 for manusia in t:
                      cl.sendText(manusia, (bctxt))
            elif "Allgbc " in msg.text:
                 bctxt = msg.text.replace("Allgbc ", "")
                 n = ki.getGroupIdsJoined()
                 n = ki2.getGroupIdsJoined()
                 n = ki3.getGroupIdsJoined()
                 n = ki4.getGroupIdsJoined()
                 n = ki5.getGroupIdsJoined()
                 for manusia in n:
                      ki.sendText(manusia, (bctxt))
                      ki2.sendText(manusia, (bctxt))
                      ki3.sendText(manusia, (bctxt))
                      ki4.sendText(manusia, (bctxt))
                      ki5.sendText(manusia, (bctxt))
            elif "Allcbc " in msg.text:
                 bctxt = msg.text.replace("Allcbc ", "")
                 t = ki.getAllContactIds()
                 t = ki2.getAllContactIds()
                 t = ki3.getAllContactIds()
                 t = ki4.getAllContactIds()
                 t = ki5.getAllContactIds()
                 for manusia in t:
                      ki.sendText(manusia, (bctxt))
                      ki2.sendText(manusia, (bctxt))
                      ki3.sendText(manusia, (bctxt))
                      ki4.sendText(manusia, (bctxt))
                      ki5.sendText(manusia, (bctxt))
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)

                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki3mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ks.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                cl.sendText

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,50):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rakaa\n\n😅😅😅")
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rakaa\n\n😅😅😅")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rakaa\n\n😅😅😅")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rakaa\n\n😅😅😅")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rakaa\n\n😅😅😅")
           # ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
           # ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rakaa\n\n😅😅😅")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
