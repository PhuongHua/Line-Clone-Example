from django.http.response import HttpResponse
from django.shortcuts import render
import os
import json
import random
import doco.client
import requests
from django.http import JsonResponse
from django.views.generic import View
import urllib
import editdistance
from bot import mecab_test

#Messaging API版エンドポイント
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

DOCOMO_API_KEY = '6255615075614d4a3455552f57546d583366686d3332314746456e6e49714a49464d43325a667561685a33'
EVENT_REGISTER = '138311609100106403'
EVENT_TALK = '138311609000106303'
DOCOMO_ENDPOINT = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'
MIZU_ENDPOINT = 'http://myconcierlb-708356017.us-west-2.elb.amazonaws.com:9000/api/ask'

# Messaging API版
def post_text(reply_token, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU="
    }
    output = mecab_test.make_output(text)
    payload_text = ''.join(output)
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": payload_text
                }
            ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

def post_carousel(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU="
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
              {
                "type": "template",
                "altText": "this is a carousel template",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
                          "thumbnailImageUrl": "https://www.google.co.jp/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=&url=http%3A%2F%2Fwww.hpfrance.com%2FBlog%2FMasami%2Fimages%2F%25E9%259B%25AA%25E7%258C%25AB__.JPG&psig=AFQjCNH4YD8jFu_MDALKV38JEYivKrA07Q&ust=1475299168321402",
                          "title": "this is menu",
                          "text": "description",
                          "actions": [
                              {
                                  "type": "postback",
                                  "label": "Buy",
                                  "data": "action=buy&itemid=111"
                              },
                              {
                                  "type": "postback",
                                  "label": "Add to cart",
                                  "data": "action=add&itemid=111"
                              },
                              {
                                  "type": "uri",
                                  "label": "View detail",
                                  "uri": "http://example.com/page/111"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://nekogazou.com/wp-content/uploads/2015/10/4ab5442a6d977922bcbe8850ff4b40bc.jpg",
                          "title": "this is menu",
                          "text": "description",
                          "actions": [
                              {
                                  "type": "postback",
                                  "label": "Buy",
                                  "data": "action=buy&itemid=222"
                              },
                              {
                                  "type": "postback",
                                  "label": "Add to cart",
                                  "data": "action=add&itemid=222"
                              },
                              {
                                  "type": "uri",
                                  "label": "View detail",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        }
                    ]
                }
              }
            ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

def post_confirm(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU="
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
            {
              "type": "template",
              "altText": "this is a confirm template",
              "template": {
                  "type": "confirm",
                  "text": "男性ですか？女性ですか？",
                  "actions": [
                      {
                        "type": "message",
                        "label": "Man",
                        "text": "男性"
                      },
                      {
                        "type": "message",
                        "label": "Woman",
                        "text": "女性"
                      }
                  ]
              }
            }
          ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

def post_image(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU="
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
              {
                  "type": "image",
                  "originalContentUrl": "http://d2dcan0armyq93.cloudfront.net/photo/odai/400/b72db8c019e3e2ee8e7da084da2c3dfb_400.jpg",
                  "previewImageUrl": "https://example.com/preview.jpg"
              }
        ]
    }
    print('This is post image')
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

# def post_imagemap(reply_token):
#     header = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer CN7ARoWPO9AiF29T6YwXWZsZpF8Ykq5ZQmJlfAvPYAXfz87Bep8WQjrQyMWf7dkJLbTQVlP7Itb5sraJ4+gGI8S65ai9Hphr3m52AX6Jxbg5YQ0BzC9c6beuY0C7LBqJ/eW92kQWABOfe/r+12YwAgdB04t89/1O/w1cDnyilFU="
#     }
#     payload = {
#           "replyToken":reply_token,
#           "messages":[
#             {
#               "type": "imagemap",
#               "baseUrl": "http://blogimg.goo.ne.jp/user_image/03/1f/d4a55e24e0cd7993539025c25fe426b8.jpg/1040",
#               "altText": "this is an imagemap",
#               "baseSize": {
#                   "height": 1040,
#                   "width": 1040
#               },
#               "actions": [
#                   {
#                       "type": "uri",
#                       "linkUri": "https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%90",
#                       "area": {
#                           "x": 0,
#                           "y": 0,
#                           "width": 520,
#                           "height": 1040
#                       }
#                   },
#                   {
#                       "type": "message",
#                       "text": "焼きそばだよ！！！！！",
#                       "area": {
#                           "x": 520,
#                           "y": 0,
#                           "width": 520,
#                           "height": 1040
#                       }
#                   }
#               ]
#             }
#           ]
#     }
#     req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

#Messaging API版
def dispose(events):
  print('This is dispose request')
  for event in events:
    reply_token = event['replyToken']
    event_type = event['type']
    user_id = event['source']['userId']
    response_to_talk(reply_token, event)

#Messaging API
def response_to_talk(reply_token, event):
  print("enter response to talk")
  text = event['message']['text']
  if 'カルーセル' in text:
    post_carousel(reply_token)
  elif 'やきさば' in text:
    post_image(reply_token)
  else:
    post_text(reply_token, text)


def post_test(request):
  return render(request, 'post_test.html')

class HelloView(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        return JsonResponse({'suzuki':'kosuke'})

    def post(self, request, *args, **kwargs):
      print(request.body.decode("utf-8"))
      #Trial版
      dispose(json.loads(request.body.decode("utf-8"))['events'])
      return JsonResponse({'kosuke': 'suzuki'})