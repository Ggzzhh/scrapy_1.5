# -*- coding: utf-8 -*-
import requests
import json
from pprint import pprint

from urllib import parse
from bs4 import BeautifulSoup


def test():
    followers = 'https://www.zhihu.com/api/v4/members/excited-vczh/followers'
    followees = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees'
    include = 'https://www.zhihu.com/api/v4/members/guo-sheng-97-95'

    include_follow = 'data[*].answer_count, articles_count, gender, ' \
                     'follower_count, is_followed, is_following, ' \
                     'badge[?(type = best_answerer)].topics'
    include_userinfo = 'locations,employments,gender,educations,business' \
                       ',voteup_count,thanked_Count,follower_count' \
                       ',following_count,cover_url,following_topic_count' \
                       ',following_question_count,following_favlists_count' \
                       ',following_columns_count,avatar_hue,answer_count' \
                       ',articles_count,pins_count,question_count' \
                       ',commercial_question_count,favorite_count' \
                       ',favorited_count,logs_count,marked_answers_count' \
                       ',marked_answers_text,message_thread_token' \
                       ',account_status,is_active,is_force_renamed' \
                       ',is_bind_sina,sina_weibo_url,sina_weibo_name' \
                       ',show_sina_weibo,is_blocking,is_blocked,is_following' \
                       ',is_followed,mutual_followees_count,vote_to_count' \
                       ',vote_from_count,thank_to_count,thank_from_count' \
                       ',thanked_count,description,hosted_live_count' \
                       ',participated_live_count,allow_message' \
                       ',industry_category,org_name,org_homepage' \
                       ',badge[?(type=best_answerer)].topics'
    params = {
        'include': include_follow,
        'limit': 20,
        'offset': 0
    }
    params2 = {
        'include': include_userinfo
    }


    ajax_url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees' \
               '?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender' \
               '%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F' \
               '%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=2720'
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.146 Safari/537.36',
        'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
    }
    # t = session.get(followees, headers=headers, params=params)
    # print(t.cookies)
    x = session.get(include, headers=headers, params=params2)
    text = json.loads(x.text)
    pprint(text)
    print(len(text))
    L = include_userinfo.split(',')
    print(len(L))
    # print(len(text['data']))


if __name__ == '__main__':
    test()