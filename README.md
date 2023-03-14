

[中文](README.md "中文") [English](eng-README.md "English") 



> ### 这是一个基于TTS+VITS的ChatGPT语音对话程序!


**更新功能：**
* [x] ChatGPT的不间断对话聊天
* [x] 更加便捷的操作
* [x] 维持对话同时可更改语音
* [x] 支持自定义编辑资源
<br>
开放资源模型链接:https://pan.baidu.com/s/121CO4acg6qCWZY9-PIKobA?pwd=hana&_at_=1678763047948#list/path=%2F&parentPath=%2F&login_type=qzone  <br>
开放资源UP主视频:https://www.bilibili.com/video/BV1Jj411P77b/?spm_id_from=333.788.recommend_more_video.6&vd_source=31b7ae374762015e760da95b804fe7bf  <br>
开放资源UP主视频2:https://www.bilibili.com/video/BV1TD4y1E7e8/?spm_id_from=333.880.my_history.page.click&vd_source=31b7ae374762015e760da95b804fe7bf  <br>
感谢下列B站up主共享资源: <br>
B站Up主@当个扫帚 @addone123 <br>

# 运行方法

-环境部署: <br>
conda create --name chatWaifu python=3.10 <br>
conda activate chatWaifu <br>
pip install -r requirements.txt <br>

-模型放置: <br>
在ChatWaifuService.py 同级目录下创建model文件夹 <br>
下载模型文件,并放到model里面,一个.pth文件,一个.json文件.<br>
在model里再创建一个名为CN的文件夹<br>
将中文模型放进去即可<br>
模型角色名子与游戏名不同的问题可以在ChatWaifuGameL2D\game的script.rpy中进行修改<br>

-运行: <br>
python ChatWaifuService.py <br>

运行ChatWaifuGameL2D中的ChatWaifuL2D.exe即可 <br>



## <span id="915">鸣谢：</span> 
- [MoeGoe_GUI]https://github.com/CjangCjengh/MoeGoe_GUI 
- [Pretrained models]https://github.com/CjangCjengh/TTSModels
- [PyChatGPT]https://github.com/terry3041/pyChatGPT <br>
- [ChatWaifuL2D][cjyaddone/ChatWaifuL2D: An Renpy enabled ver of ChatWaifu (github.com)](https://github.com/cjyaddone/ChatWaifuL2D)
