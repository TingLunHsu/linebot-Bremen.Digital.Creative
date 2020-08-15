from __future__ import unicode_literals
import os

from flask import Flask, request, abort, render_template

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import * # wMessageEvent, TextMessage, TextSendMessage, ImageSendMessage
#from linebot.models.send_messages import *
#from linebot.models.actions import *

import configparser

import urllib
import re
import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

image_path = ['https://upload.cc/i1/2020/08/18/wNEbuU.png',
              'https://upload.cc/i1/2020/08/18/7bOGPp.png',
              'https://upload.cc/i1/2020/08/18/1m8plA.png',
              'https://upload.cc/i1/2020/08/18/HBPVe7.png',
              'https://upload.cc/i1/2020/08/18/DxkvgL.png']

@app.route('/')
def home():
    return render_template("home.html")


# 接收 LINE 的資訊
@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def reply_1():
    message = [
        TextSendMessage(
            text='所謂的偏痛，即是「立場對立所造成的撕裂傷痛」\n而典型的偏痛青年，在與父母吵完架後⋯\n\n覺得不被理解，滿肚子委屈\n覺得跟父母之間隔著一道牆\n覺得回到家壓力就好大，總在餐桌缺席'
        ),
        TextSendMessage(
            text='這些感覺是否似曾相識⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='難道我也是偏痛青年？！',
                            text='難道我也是偏痛青年？！')
                    )
                ]
            )
        )
    ]

    return message

def reply_2():
    message = [
        TextSendMessage(
            text='先來測測你的偏痛指數\n若指數超過 60%\n你⋯就是我們在找的偏痛青年了！'
        ),
        ImageSendMessage(
            original_content_url='https://upload.cc/i1/2020/08/17/vG1icr.jpg',
            preview_image_url='https://upload.cc/i1/2020/08/17/vG1icr.jpg'
        ),
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='           結束了小小測驗⋯',
                actions=[
                    MessageAction(
                        label='【我完全是偏痛青年啊！】',
                        text='我完全是偏痛青年啊！'
                    ),
                    MessageAction(
                        label='【偏痛青年為了什麼而吵】',
                        text='偏痛青年為了什麼而吵'
                    )
                ]
            )
        )
    ]

    return message

def reply_3():
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.cc/i1/2020/08/13/LgvH0k.jpg',
            text='       偏痛青年為了什麼而吵',
            actions=[
                MessageAction(
                    label='【有一種偏痛叫藍綠政治】',
                    text='有一種偏痛叫藍綠政治'
                ),
                MessageAction(
                    label='【有一種偏痛叫挺同反同】',
                    text='有一種偏痛叫挺同反同'
                ),
                MessageAction(
                    label='【有一種偏痛叫生涯規劃】',
                    text='有一種偏痛叫生涯規劃'
                ),
                MessageAction(
                    label='【有一種偏痛叫伴侶條件】',
                    text='有一種偏痛叫伴侶條件'
                )
            ]
        )
    )

    return message


def reply_4(event):
    if event.message.text == '有一種偏痛叫藍綠政治':
        message = TextSendMessage(
            text='「你們這群年輕人都被洗腦去了」\n「這次你敢去投票就不要回來！」\n「都是蔡英文搞得世代對立，你看他多會操控」',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾聽過這幾句話😔',
                            text='我也曾聽過這幾句話😔')
                    )
                ]
            )
        )
    elif event.message.text == '有一種偏痛叫挺同反同':
        message = TextSendMessage(
            text='「你不准去跟人家搞同性戀聽到沒」\n「喜歡同性別是一種病你知道嗎」\n「我支持同婚阿，但不准是我們家小孩」',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾聽過這幾句話😟',
                            text='我也曾聽過這幾句話😟')
                    )
                ]
            )
        )
    elif event.message.text == '有一種偏痛叫生涯規劃':
        message = TextSendMessage(
            text='「叫你考公務員不聽，現在後悔了吧」\n「就跟你說念這個科系才好找工作」\n「你就繼續做你的夢，看以後怎麼養活自己」',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾聽過這幾句話😢',
                            text='我也曾聽過這幾句話😢')
                    )
                ]
            )
        )
    elif event.message.text == '有一種偏痛叫伴侶條件':
        message = TextSendMessage(
            text='「現在女朋友比父母重要就對了」\n「他的優點我是沒找到，但缺點倒是挺多的」\n「我敢肯定你們不會走到結婚啦」',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾聽過這幾句話☹️',
                            text='我也曾聽過這幾句話☹️')
                    )
                ]
            )
        )
    else:
        raise NameError('Invalid input for reply_4!')

    return message

def reply_5(event):
    if event.message.text == '我也曾聽過這幾句話😔':
        message = TextSendMessage(
            text='2020總統大選\n讓無數的家庭因為藍綠而產生對立\n「韓粉父母無助會」粉專湧入大量貼文\n處在社群網路同溫層中的我們\n似乎永遠無法理解光譜另一端的父母在想什麼',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='這樣的關係確實令人無奈阿⋯',
                            text='這樣的關係確實令人無奈阿⋯')
                    )
                ]
            )
        )
    elif event.message.text == '我也曾聽過這幾句話😟':
        message = [
            TextSendMessage(
                text='2018同婚公投\n許多人為了婚姻平權勇敢發聲\n有人為了社會能更加平等\n也有人為的是自己的幸福'
            ),
            TextSendMessage(
                text='當我們捍衛著愛的權益\n家裡的關係也因此畫上休止符\n彷彿跨出了櫃子\n同時也跨出了家門\n再也回不去⋯',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(
                                label='這樣的關係確實令人無奈呢⋯',
                                text='這樣的關係確實令人無奈呢⋯')
                        )
                    ]
                )
            )
        ]
    elif event.message.text == '我也曾聽過這幾句話😢':
        message = [
            TextSendMessage(
                text='人生有好幾個分叉路口\n其中一個是求學\n另外一個，是求職'
            ),
            TextSendMessage(
                text='每到一個路口\n我們膽戰心驚的拋出夢想藍圖\n而現實毫不留情的賞了一記又一記耳光\n來自父母的藍圖被強塞至我們面前',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(
                                label='這樣的關係確實令人無奈⋯',
                                text='這樣的關係確實令人無奈⋯')
                        )
                    ]
                )
            )
        ]
    elif event.message.text == '我也曾聽過這幾句話☹️':
        message = TextSendMessage(
            text='介紹伴侶給父母需要勇氣\n就像把珍藏已久的寶貝分享給他人一樣\n而同樣視我們為珍寶的父母\n卻永遠覺得對方條件永遠不夠好',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='這樣的關係確實令人無奈⋯⋯',
                            text='這樣的關係確實令人無奈⋯⋯')
                    )
                ]
            )
        )
    else:
        raise NameError('Invalid input for reply_5!')

    return message


def reply_6(event):
    if event.message.text == '這樣的關係確實令人無奈阿⋯':
        message = TextSendMessage(
            text='在政治面前親情變得脆弱\n隨著大選落幕\n家庭的撕裂傷依舊沒有復原\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾為藍綠政治而吵',
                            text='我也曾為藍綠政治而吵')
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label='我想了解更多偏痛議題',
                            text='我想了解更多偏痛議題')
                    )
                ]
            )
        )
    elif event.message.text == '這樣的關係確實令人無奈呢⋯':
        message = TextSendMessage(
            text='在同婚面前親情變得脆弱\n隨著公投的落幕\n家庭的撕裂傷依舊沒有復原\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾為挺同反同而吵',
                            text='我也曾為挺同反同而吵')
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label='我想了解更多偏痛議題',
                            text='我想了解更多偏痛議題')
                    )
                ]
            )
        )
    elif event.message.text == '這樣的關係確實令人無奈⋯':
        message = TextSendMessage(
            text='在理想面前親情變得脆弱\n人生旅途持續走著\n家庭的撕裂傷依舊沒有復原\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾為生涯規劃而吵',
                            text='我也曾為生涯規劃而吵')
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label='我想了解更多偏痛議題',
                            text='我想了解更多偏痛議題')
                    )
                ]
            )
        )
    elif event.message.text == '這樣的關係確實令人無奈⋯⋯':
        message = TextSendMessage(
            text='愛情與親情的比重該如何拿捏\n隱瞞、順從、抑或抵抗\n家庭的撕裂傷仍舊不會復原\t\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾為伴侶條件而吵',
                            text='我也曾為伴侶條件而吵')
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label='我想了解更多偏痛議題',
                            text='我想了解更多偏痛議題')
                    )
                ]
            )
        )
    else:
        raise NameError('Invalid input for reply_6!')

    return message

def reply_7(event):
    if event.message.text == '我也曾為藍綠政治而吵':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「前立委助理 孟孟」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/avjcbnzga6oja71/%E8%97%8D%E7%B6%A0%E6%94%BF%E6%B2%BB%EF%BC%BF%E5%AD%9F%E5%AD%9F.mp3',
                duration=231000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=Dtz0lvPlmpU'
            )
        ]
    elif event.message.text == '我也曾為挺同反同而吵':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「一言不合就出櫃的麵麵」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/z86dtocjyv1b32y/%E4%B8%80%E8%A8%80%E4%B8%8D%E5%90%88%E5%B0%B1%E5%87%BA%E8%BB%8C%E7%9A%84%E9%BA%B5%E9%BA%B5.mp3',
                duration=321000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=IkYgmPuF4o0'
            )
        ]
    elif event.message.text in ['我也曾為生涯規劃而吵', '我還想聽其他故事']:
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='關於生涯規劃的偏痛故事',
                text='你想先聽哪一則呢？',
                actions=[
                    MessageAction(
                        label='城市浪人創辦人 張希慈',
                        text='城市浪人創辦人 張希慈'
                    ),
                    MessageAction(
                        label='致信譚德賽的女孩 林薇',
                        text='致信譚德賽的女孩 林薇'
                    ),
                    MessageAction(
                        label='台大休學轉攻設計的 Wei',
                        text='台大休學轉攻設計的 Wei'
                    ),
                    MessageAction(
                        label='熱愛文學的商科少女 Jian',
                        text='熱愛文學的商科少女 Jian'
                    )
                ]
            )
        )
        return message
    elif event.message.text == '我也曾為伴侶條件而吵':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「愛家的犬系男孩 An」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/1sppra26241ovvi/%E7%8A%AC%E7%B3%BB%E7%94%B7%E5%AD%A9An.mp3',
                duration=229000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=DZTE7AZ1DQI'
            )
        ]
    else:
        raise NameError('Invalid input for reply_7!')

    button = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='          偏痛路上有你有我',
            actions=[
                MessageAction(
                    label='【原來不只我有這種煩惱】',
                    text='原來不只我有這種煩惱'
                )
            ]
        )
    )

    message.append(button)

    return message

def reply_8(event):
    if event.message.text == '城市浪人創辦人 張希慈':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「城市浪人創辦人 張希慈」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/0gv38y7t6stukz9/%E5%BC%B5%E5%B8%8C%E6%85%88-1.mp3',
                duration=300000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=DlngsyEjJWw'
            )
        ]
    elif event.message.text == '致信譚德賽的女孩 林薇':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「致信譚德賽的女孩 林薇」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/bau09ut1te28zwf/%E6%9E%97%E8%96%87.mp3',
                duration=266000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=3pr8UsDSv1s'
            )
        ]
    elif event.message.text == '台大休學轉攻設計的 Wei':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「台大休學轉攻設計的 Wei」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/x2w18daqd0ycbi8/%E8%B5%B0%E5%87%BA%E8%87%AA%E5%B7%B1%E8%A8%AD%E8%A8%88%E6%A8%82%E8%B7%AF%E7%9A%84Wei.mp3',
                duration=419000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=pS7IwRyDdjw'
            )
        ]
    elif event.message.text == '熱愛文學的商科少女 Jian':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年「熱愛文學的商科少女 Jian」想跟你分享他是如何修補這一段撕裂傷的\n\n一起來聽聽看吧！'
            ),
            AudioSendMessage(
                original_content_url='https://dl.getdropbox.com/s/mlcjp8nx1dj6g84/%E5%95%86%E7%A7%91%E5%A5%B3%E5%AD%A9Jian.mp3',
                duration=290000
            ),
            TextSendMessage(
                text='https://www.youtube.com/watch?v=JKPi7L__lzc'
            )
        ]
    else:
        raise NameError('Invalid input for reply_8!')

    button = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='          偏痛路上有你有我',
            actions=[
                MessageAction(
                    label='【原來不只我有這種煩惱】',
                    text='原來不只我有這種煩惱'
                ), 
                MessageAction(
                    label='【我還想聽其他故事】',
                    text='我還想聽其他故事'
                )
            ]
        )
    )

    message.append(button)

    return message

def reply_9():
    index = random.randint(0, 4)
    message = [
        TextSendMessage(
            text='即便彼此立場不同\n我們仍希望家庭能幸福和諧\n\n這次在愛面前\n試著先不談立場與對錯\n用用看我們送給你的偏痛良藥\n傳給還在冷戰中的爸媽吧！'
        ),
        ImageSendMessage(
            original_content_url=image_path[index],
            preview_image_url=image_path[index],
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我該怎麼使用它',
                            text='我該怎麼使用它')
                    )
                ]
            )
        )
    ]

    return message

def reply_10():
    message = TextSendMessage(
        text='分享「偏痛良藥」給你爸媽\t\n不只有防疫期間的注意事項\t\n你的小小心意也藏在圖片裡了！\t\n\t\n快趁機跟爸媽告白一波❤️\t',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='給我更多偏痛良藥',
                        text='給我更多偏痛良藥')
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='我想了解更多偏痛議題',
                        text='我想了解更多偏痛議題')
                )
            ]
        )
    )

    return message

def reply_11():
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://upload.cc/i1/2020/08/18/DJrUzC.png',
                    action=MessageAction(
                        label='我只想跟你零距離',
                        text='我只想跟你零距離',
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://upload.cc/i1/2020/08/18/62ngzc.png',
                    action=MessageAction(
                        label='逗陣坐下吃頓飯',
                        text='逗陣坐下吃頓飯',
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://upload.cc/i1/2020/08/18/9gmjeX.png',
                    action=MessageAction(
                        label='打開你的心門',
                        text='打開你的心門',
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://upload.cc/i1/2020/08/18/mEAesD.png',
                    action=MessageAction(
                        label='想家專線',
                        text='想家專線',
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://upload.cc/i1/2020/08/18/v92fmR.png',
                    action=MessageAction(
                        label='分享我的羅曼史',
                        text='分享我的羅曼史',
                    )
                )
            ]
        )
    )

    return message

def reply_12(event):
    if event.message.text == '分享我的羅曼史':
        index = 0
    elif event.message.text == '逗陣坐下吃頓飯':
        index = 1
    elif event.message.text == '我只想跟你零距離':
        index = 2
    elif event.message.text == '打開你的心門':
        index = 3
    elif event.message.text == '想家專線':
        index = 4
    else:
        raise NameError('Invalid input for reply_12!')

    message = ImageSendMessage(
        original_content_url=image_path[index],
        preview_image_url=image_path[index],
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='給我更多偏痛良藥',
                        text='給我更多偏痛良藥')
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='我想了解更多偏痛議題',
                        text='我想了解更多偏痛議題')
                )
            ]
        )
    )

    return message

def reply():
    message = TextSendMessage(
        text='既然我們有機會成為好友\n代表你也想知道自己是不是個偏痛青年吧\n\n就讓我們來替你解答！',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='偏痛青年是什麼',
                        text='偏痛青年是什麼')
                )
            ]
        )
    )

    return message

def error_reply():
    message = TextSendMessage(
        text='偏痛中心無法辨識此條訊息耶😣\n你想了解什麼資訊呢？',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='偏痛青年是什麼',
                        text='偏痛青年是什麼')
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='我是否也是偏痛青年呢？',
                        text='我是否也是偏痛青年呢？')
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='我想了解更多偏痛議題',
                        text='我想了解更多偏痛議題')
                )
            ]
        )
    )

    return message

@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):

    if event.source.user_id == 'Udeadbeefdeadbeefdeadbeefdeadbeef':
        return

    if event.message.text == '偏痛青年是什麼':
        message = reply_1()
    elif event.message.text in ['難道我也是偏痛青年？！', '我是否也是偏痛青年呢？']:
        message = reply_2()
    elif event.message.text in ['我完全是偏痛青年啊！', '偏痛青年為了什麼而吵', '我想了解更多偏痛議題']:
        message = reply_3()
    elif event.message.text in ['有一種偏痛叫藍綠政治', '有一種偏痛叫挺同反同', '有一種偏痛叫生涯規劃', '有一種偏痛叫伴侶條件']:
        message = reply_4(event)
    elif event.message.text in ['我也曾聽過這幾句話😔', '我也曾聽過這幾句話😟', '我也曾聽過這幾句話😢', '我也曾聽過這幾句話☹️']:
        message = reply_5(event)
    elif event.message.text in ['這樣的關係確實令人無奈阿⋯', '這樣的關係確實令人無奈呢⋯', '這樣的關係確實令人無奈⋯', '這樣的關係確實令人無奈⋯⋯']:
        message = reply_6(event)
    elif event.message.text in ['我也曾為藍綠政治而吵', '我也曾為挺同反同而吵', '我也曾為生涯規劃而吵', '我也曾為伴侶條件而吵', '我還想聽其他故事']:
        message = reply_7(event)
    elif event.message.text in ['城市浪人創辦人 張希慈', '致信譚德賽的女孩 林薇', '台大休學轉攻設計的 Wei', '熱愛文學的商科少女 Jian']:
        message = reply_8(event)
    elif event.message.text == '原來不只我有這種煩惱':
        message = reply_9()
    elif event.message.text == '我該怎麼使用它':
        message = reply_10()
    elif event.message.text == '給我更多偏痛良藥':
        message = reply_11()
    elif event.message.text in ['我只想跟你零距離', '逗陣坐下吃頓飯', '打開你的心門', '想家專線', '分享我的羅曼史']:
        message = reply_12(event)
    else:
        message = error_reply()

    line_bot_api.reply_message(event.reply_token, message)

@handler.add(FollowEvent)
def handle_follow(event):
    message = reply()
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()

