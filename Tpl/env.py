# -*- coding: utf-8 -*-

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.conf import settings

from jinja2 import Environment
from . import filters
#from . import Extension

import json

SiteInfoPath=settings.BASE_DIR+"/data/SiteInfo.json"#站点信息数据相对路径
SiteInfoPath=SiteInfoPath.replace('\\', '/')

def environment(**options):

    variables = {
        "Title" : "Taoni",#站点标题
        "SubTitle": "Connect People",  # 站点副标题
        "WeiXinUrl" : "http://url.cn/45mrvIL",#微信关注地址
        "Statistics" : "",#统计代码
    }


    SiteInfo = json.loads(open(SiteInfoPath,"r").read())

    variables.update(SiteInfo)

    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'string':variables,
    })


    env.filters['getURLfromSource'] = filters.getURLfromSource
    env.filters['base64'] = filters.getbase64
    env.filters['getOrderStatus'] = filters.getOrderStatus
    env.filters['timesince'] = filters.timesince

    #env.add_extension(Extension.MoviebyCategoryExtension)
    #env.add_extension(Extension.GetCategoryListExtension)
    #env.add_extension(Extension.LinksExtension)


    return env
