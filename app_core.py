from __future__ import unicode_literals
import os

# 增加了 render_template
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


@app.route('/')
def home():
    return render_template("home_pixijs.html")


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
            text='所謂的偏痛，即是「立場對立所造成的撕裂傷痛」\n而典型的偏痛青年，在與父母吵完架後⋯\n\n覺得自己不被理解，滿肚子委屈\n覺得跟父母之間永遠隔著一道牆\n覺得回到家壓力就好大，總在餐桌缺席\n'
        ),
        TextSendMessage(
            text='這些感覺是否似曾相識⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='難道我也是偏痛青年？',
                            text='難道我也是偏痛青年？')
                    )
                ]
            )
        )
    ]

    return message

def reply_2():
    message = [
        TextSendMessage(
            text='先來測測你的偏痛指數，若指數超過 60%\n你⋯就是我們在找的偏痛青年了！'
        ),
        ImageSendMessage(
            original_content_url='https://upload.cc/i1/2020/08/14/7aFERT.jpg',
            preview_image_url='https://upload.cc/i1/2020/08/14/7aFERT.jpg'
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
                    label='【有一種偏痛叫職涯規劃】',
                    text='有一種偏痛叫職涯規劃'
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
    elif event.message.text == '有一種偏痛叫職涯規劃':
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
            text='2020總統大選\n讓無數的家庭因為藍綠而產生世代對立\n「韓粉父母無助會」粉專湧入大量貼文\n處在社群網路同溫層中的我們\n似乎永遠無法理解光譜另一端的父母在想什麼',
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
                text='2018同婚公投\n許多人為了婚姻平權勇敢站出來\n為了社會能更加平等，也有人為的是自己的幸福'
            ),
            TextSendMessage(
                text='在捍衛著自己愛的權益同時\n家裡的關係也因此畫上休止符\n彷彿跨出了櫃子，同時也跨出了家門，再也回不去',
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
                text='人生有好幾個分叉路口\n其中一個是求學\n另外一個，是求職\n'
            ),
            TextSendMessage(
                text='每到一個路口\n我們就膽戰心驚的拋出夢想藍圖\n而現實毫不留情的賞了一記又一記耳光\n來自父母的藍圖被強塞至我們面前',
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
            text='在政治面前，親情變得脆弱\n隨著大選的落幕，家庭的撕裂傷依舊沒有復原\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
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
            text='在同婚面前，親情變得脆弱\n隨著公投的落幕，家庭的撕裂傷依舊沒有復原\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
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
            text='在理想面前，親情變得脆弱\n人生旅途持續走著，家庭的撕裂傷依舊沒有復原\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(
                            label='我也曾為職涯規劃而吵',
                            text='我也曾為職涯規劃而吵')
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
            text='愛情與親情的比重該如何拿捏\n隱瞞、順從、抑或抵抗，家庭的撕裂傷仍舊不會復原\t\n難道擁有一個和樂的家庭真的這麼難嗎⋯？',
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
                text='這裡有一位偏痛青年 1號受訪人\n想跟你分享他是如何修補這一段撕裂傷的\n一起來聽聽看吧！'
            ),
            TextSendMessage(
                text='圖文語音1'
            )
        ]
    elif event.message.text == '我也曾為挺同反同而吵':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年 2號受訪人\n想跟你分享他是如何修補這一段撕裂傷的\n一起來聽聽看吧！'
            ),
            TextSendMessage(
                text='圖文語音2'
            )
        ]
    elif event.message.text == '我也曾為職涯規劃而吵':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年 3號受訪人\n想跟你分享他是如何修補這一段撕裂傷的\n一起來聽聽看吧！'
            ),
            TextSendMessage(
                text='圖文語音3'
            )
        ]
    elif event.message.text == '我也曾為伴侶條件而吵':
        message = [
            TextSendMessage(
                text='這裡有一位偏痛青年 4號受訪人\n想跟你分享他是如何修補這一段撕裂傷的\n一起來聽聽看吧！'
            ),
            TextSendMessage(
                text='圖文語音4'
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

def reply_8():
    message = [
        TextSendMessage(
            text='即便彼此立場不同\n我們都是希望家庭能幸福和諧的\n\n這次在愛面前，試著先不談立場與對錯\n用用看我們送給你的偏痛良藥\n傳給還在冷戰中的爸媽吧！'
        ),
        ImageSendMessage(
            original_content_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/86633713_2723861777704114_6490979843902013440_o.jpg?_nc_cat=103&_nc_sid=09cbfe&_nc_ohc=Qy413EqevkcAX_s8smu&_nc_ht=scontent-tpe1-1.xx&oh=12577ee857fbab892b7aff4c7f27bcdb&oe=5F5CFA0E',
            preview_image_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/86633713_2723861777704114_6490979843902013440_o.jpg?_nc_cat=103&_nc_sid=09cbfe&_nc_ohc=Qy413EqevkcAX_s8smu&_nc_ht=scontent-tpe1-1.xx&oh=12577ee857fbab892b7aff4c7f27bcdb&oe=5F5CFA0E',
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

def reply_9():
    message = [
        TextSendMessage(
            text='分享這個「偏痛良藥」給你爸媽\n不只有防疫期間應須注意的事項\n你的小小心意也藏在圖片裡了！\n（快去趁亂跟爸媽告白一波❤️）',
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
    ]

    return message

def reply(event):
    message = TextSendMessage(
        text='既然我們有機會成為好友\n代表你也想知道自己是不是個偏痛青年吧\n就讓我們來替你解答！',
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


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):

    if event.source.user_id == 'Udeadbeefdeadbeefdeadbeefdeadbeef':
        return

    if event.message.text == '偏痛青年是什麼':
        message = reply_1()
    elif event.message.text == '難道我也是偏痛青年？':
        message = reply_2()
    elif event.message.text in ['我完全是偏痛青年啊！', '偏痛青年為了什麼而吵', '我想了解更多偏痛議題']:
        message = reply_3()
    elif event.message.text in ['有一種偏痛叫藍綠政治', '有一種偏痛叫挺同反同', '有一種偏痛叫職涯規劃', '有一種偏痛叫伴侶條件']:
        message = reply_4(event)
    elif event.message.text in ['我也曾聽過這幾句話😔', '我也曾聽過這幾句話😟', '我也曾聽過這幾句話😢', '我也曾聽過這幾句話☹️']:
        message = reply_5(event)
    elif event.message.text in ['這樣的關係確實令人無奈阿⋯', '這樣的關係確實令人無奈呢⋯', '這樣的關係確實令人無奈⋯', '這樣的關係確實令人無奈⋯⋯']:
        message = reply_6(event)
    elif event.message.text in ['我也曾為藍綠政治而吵', '我也曾為挺同反同而吵', '我也曾為職涯規劃而吵', '我也曾為伴侶條件而吵']:
        message = reply_7(event)
    elif event.message.text == '原來不只我有這種煩惱':
        message = reply_8()
    elif event.message.text == '我該怎麼使用它':
        message = reply_9()
    elif event.message.text == '給我更多偏痛良藥':
        return
    else:
        message = reply(event)

    line_bot_api.reply_message(event.reply_token, message)

@handler.add(FollowEvent)
def handle_follow(event):
    message = reply(event)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
