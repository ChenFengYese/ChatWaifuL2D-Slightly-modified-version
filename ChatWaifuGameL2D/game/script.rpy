# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("Hiyori")
define y = Character("你")
define config.gl2 = True

image hiyori = Live2D("Resources/hiyori", base=.6, loop = True, fade=True)

init python:
    import socket
    import time
    thinking = 0
    total_data = bytes()
    renpy.block_rollback()
    ip_port = ('127.0.0.1', 9000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(ip_port)


# 游戏在此开始。

label start:
    $ renpy.block_rollback()
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    #scene bg library

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。
    show hiyori m01

    #show eileen happy
    jump OutPutLanguageDisplay
    return

label OutPutLanguageDisplay:
    $ renpy.block_rollback()
    menu OutPutLanguageDisplayChoice: #input 2
        e "Please select the interface display language"

        "中文":
            #block of code to run
            jump OutPutChineseDisplay
        "English":
            jump OutPutEnglishDisplay

label OutPutChineseDisplay:
    $ renpy.block_rollback()
    # 此处显示各行对话。
    e "让我们开始吧,可以在ChatWaifuServer中修改为你本人的api,可以在ChatWaifuGameL2D的Game的script.rpy中修改为自己想要的音色,音色对照表在源目录的character.txt中,建议修改前进行备份"
    e "日文对话时,为了看懂会让chatgpt同时返回中文,但有时可能会失效,需要经常借助翻译软件噢"
    e "尽量不要多次返回标题界面重新开始,可能会有未知bug,要经常看控制台要求"
    e "一般来说即使返回标题页面重新进入也是之前的chatgpt,即可以持续对话,但控制台如果程序error报错且说 等待UI连接,那就会中断"
    e "由于网络和缓存问题,有时可能会出现答非所问的现象,这时不要输入话语,不断点击让他把之前没说完的话说完就行,一般出现在返回标题页面重进之后的情况下"
    e "不想对话后记得关闭控制台"
    jump connectIf
label OutPutEnglishDisplay:
    $ renpy.block_rollback()
    e  "Let's get started. You can modify your api in ChatWaifuServer. You can modify it in script.rpy of Game ChatWaifuGameL2D to the sound you want. The sound map is in the source directory character.txt."
    e "When conversing in Japanese, chatgpt will also be sent back to Chinese in order to understand it, but sometimes it will not work. You need to use translation software frequently."
    e "Try not to return to the title interface many times to restart, there may be unknown bugs, always look at the console requirements"
    e "In general, even if you return to the title page and re-enter the same chatgpt as before, that is, you can continue the conversation, but the console will interrupt if the program makes an error and waits for the UI to connect."
    e "Due to network and caching issues, sometimes there may be a problem of not answering the question, then do not type the words, just keep clicking to let him finish what he didn't say before, usually after returning to the title page and reentering"
    e "Remember to turn off the console after you don't want to talk"
    jump connectIfEnglish
label connectIf:
    $ renpy.block_rollback()
    show hiyori m01
    python:
        token = "1"
        client.send(token.encode())
    menu inputMethod1: #input 1
        e "是否正常连接?请务必看控制台提示操作,若未连接则选否,选错了就重新打开"

        "是":
            jump checkToken
        "否":
            e "正在尝试重新连接"
            python:
                ip_port = ('127.0.0.1', 9000)
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(ip_port)
                token = "1"
                client.send(token.encode())


    jump checkToken

label connectIfEnglish:
    $ renpy.block_rollback()
    show hiyori m01
    python:
        token = "1"
        client.send(token.encode())
    menu inputMethod1: #input 1
        e "Is the connection normal? Please be sure to watch the console prompt operation, if not connected to select no, select the wrong to open again"

        "Connected":
            jump checkToken
        "disconnected":
            e "Trying to reconnect"
            python:
                ip_port = ('127.0.0.1', 9000)
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(ip_port)
                token = "1"
                client.send(token.encode())


    jump checkToken

    

label checkToken:
    $ renpy.block_rollback()
    e "正在等待程序加载...(Loading)"
    if (thinking == 0):
        show hiyori m03

    python:
        client.setblocking(0)
        try:
                data = client.recv(1024)
        except:
                data = bytes()
                client.setblocking(1)
    
    if(len(data) > 0):
        e "程序加载完成，我们进入下一步吧(Finish)"
        $ thinking = 0
        jump inputMethod
    else:
        e "正在等待程序加载......(Loading)"
        $ thinking == 1
        jump inputMethod


label inputMethod:
    $ renpy.block_rollback()
    show hiyori m01
    menu inputMethod1: #input 1
        e "请选择输入方式(input mode)"

        "键盘输入(Keyboard input)":
            python:
                client.send(("0").encode())
                keyboard = True
            jump outputMethod
        "语音输入(Voice input)":
            python:
                client.send(("1").encode())
                keyboard = False
            jump voiceInputMethod
    


label voiceInputMethod:
    $ renpy.block_rollback()
    menu inputLanguageChoice: #input 2
        e "请选择输入语言(InputLanguage)"

        "中文":
            #block of code to run
            python:
                client.send(("0").encode())
            jump outputMethod
        "日本語":
            #block of code to run
            python:
                client.send(("1").encode())
            jump outputMethod
        "English":
            python:
                client.send(("2").encode())
            jump outputMethod


label outputMethod:
    $ renpy.block_rollback()
    menu languageChoice: #input 3
        e "请选择输出语言(OutputLanguage)"

        "中文":
            #block of code to run
            python:
                client.send(("0").encode())
            jump modelChoiceCN
        "日本語":
            #block of code to run
            python:
                client.send(("1").encode())
            jump modelChoiceJP
        "英语(English)":
            #block of code to run
            python:
                client.send(("2").encode())
            jump modelChoiceJP


label modelChoiceCN:
    $ renpy.block_rollback()
    menu CNmodelChoice: #input 4
        e "我们来选择一个角色作为语音输出(choose a role as voice output)"

        "綾地寧々":
            python:
                client.send(("0").encode())
        "在原七海":
            python:
                client.send(("1").encode())
        "小茸":
            python:
                client.send(("2").encode())
        "唐乐吟":
            python:
                client.send(("3").encode())
    
    if keyboard:
        jump talk_keyboard
    else:
        jump talk_voice


label modelChoiceJP:
    $ renpy.block_rollback()
    menu JPmodelChoice: #input 4
        e "我们来选择一个角色作为语音输出"

        "伊雷娜":
            python:
                client.send(("0").encode())
                nextAgain = False
        "神里凌华":
            python:
                client.send(("87").encode())
                nextAgain = False
        "丽莎":
            python:
                client.send(("90").encode())
                nextAgain = False
        "荧":
            python:
                client.send(("91").encode())
                nextAgain = False
        "芭芭拉":
            python:
                client.send(("92").encode())
                nextAgain = False
        "温迪":
            python:
                client.send(("97").encode())
                nextAgain = False
        "下一页":
            python:
                nextAgain = True

    if nextAgain:
        jump modelChoiceJP2
    else:
        if keyboard:
            jump talk_keyboard
        else:
            jump talk_voice


label modelChoiceJP2:
    $ renpy.block_rollback()
    menu JPmodelChoice: #input 4
        e "我们来选择一个角色作为语音输出"

        "可莉":
            python:
                client.send(("103").encode())
                nextAgainA = False
        "七七":
            python:
                client.send(("109").encode())
                nextAgainA = False
        "刻晴":
            python:
                client.send(("115").encode())
                nextAgainA = False
        "宵宫":
            python:
                client.send(("122").encode())
                nextAgainA = False
        "优菈":
            python:
                client.send(("124").encode())
                nextAgainA = False
        "早柚":
            python:
                client.send(("126").encode())
                nextAgainA = False
        "下一页":
            python:
                nextAgainA = True

    if nextAgainA:
        jump modelChoiceJP3
    else:
        if keyboard:
            jump talk_keyboard
        else:
            jump talk_voice

label modelChoiceJP3:
    $ renpy.block_rollback()
    menu JPmodelChoice: #input 4
        e "我们来选择一个角色作为语音输出"

        "珊瑚宫心海":
            python:
                client.send(("127").encode())
                nextAgainAA = False
        "纳西妲":
            python:
                client.send(("142").encode())
                nextAgainAA = False
        "萝莎莉娅(崩坏)":
            python:
                client.send(("182").encode())
                nextAgainAA = False
        "布洛妮娅":
            python:
                client.send(("190").encode())
                nextAgainAA = False
        "迷城骇兔":
            python:
                client.send(("194").encode())
                nextAgainAA = False
        "朔夜观星":
            python:
                client.send(("207").encode())
                nextAgainAA = False
        "下一页":
            python:
                nextAgainAA = True

    if nextAgainAA:
        jump modelChoiceJP4
    else:
        if keyboard:
            jump talk_keyboard
        else:
            jump talk_voice


label modelChoiceJP4:
    $ renpy.block_rollback()
    menu JPmodelChoice: #input 4
        e "我们来选择一个角色作为语音输出"

        "爱莉希雅":
            python:
                client.send(("226").encode())
                nextAgainAAA = False
        "琪亚娜":
            python:
                client.send(("228").encode())
                nextAgainAAA = False
        "芽衣":
            python:
                client.send(("236").encode())
                nextAgainAAA = False
        "希儿":
            python:
                client.send(("195").encode())
                nextAgainAAA = False
        "回到第一页":
            python:
                nextAgainAAA = True
                nextAgain = False
                nextAgainA = False
                nextAgainAA = False


    if nextAgainAAA:
        jump modelChoiceJP
    else:
        if keyboard:
            jump talk_keyboard
        else:
            jump talk_voice
    
label talk_keyboard:
    $ renpy.block_rollback()
    show hiyori m02
    python:
        message = renpy.input("你：")
        client.send(message.encode())
        data = bytes()
    jump checkRes


label talk_voice:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hiyori m02
    y "你："
    python:
        client.setblocking(0)
        try:
                finishInput = client.recv(1024)
        except:
                finishInput = bytes()
                client.setblocking(1)

    if(len(finishInput) > 0):
        $ finishInput = finishInput.decode()
        $ renpy.block_rollback()
        y "[finishInput]"
        $ thinking = 0
        jump checkRes
    $ thinking = 1
    jump talk_voice


label checkRes:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hiyori m03
    e "..."

    python:
        client.setblocking(0)
        try:
                data = client.recv(1024)
                total_data += data
        except:
                data = bytes()
                client.setblocking(1)
    
    if(len(data) > 0 and len(data) < 1024):
        python:
            response = total_data.decode()
            total_data = bytes()
            thinking = 0
        jump answer
    else:
        $ renpy.block_rollback()
        e "......"
        $ thinking = 1
        jump checkRes

        


label answer:
    show hiyori talking
    voice "/audio/test.ogg"
    $ renpy.block_rollback()
    e "[response]"
    voice sustain
    
    if keyboard:
        $ client.send("语音播放完毕".encode())
        jump talk_keyboard
    else:
        $ client.send("语音播放完毕".encode())
        jump talk_voice
