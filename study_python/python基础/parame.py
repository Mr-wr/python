#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
itg_conn_info = {
             'host': 'shr9-vrt-itg-003.inc.hpicorp.net',#'shr9-vrt-dev-003.inc.hpicorp.net',
             'port': 5433,
             'user': 'qi-you.xie@hp.com',#'SRVC_GSSBS_DEV',
             'password': '206032410.Xqy',#'SRVCGSSBSDEV#123',
             'database': 'shr9_vrt_itg_003',#'shr9_vrt_dev_003',
             'log_level': logging.DEBUG,
             # 默认情况下会自动生成会话标签，
             'session_label': 'some_label',
             # 无效的UTF-8结果默认抛出错误
             'unicode_error': 'strict',
             # 默认情况下禁用SSL
             'ssl': False,
             # 默认情况下，禁用使用服务器端预处理语句
             'use_prepared_statements': False,
             # 默认情况下未启用连接超时
             # 套接字操作5秒超时（建立TCP连接或读/写操作）
             'connection_timeout': 5}

dev_conn_info = {
            'host': 'shr9-vrt-dev-003.inc.hpicorp.net',
             'port': 5433,
             'user': 'SRVC_GSSBS_DEV',
             'password': 'SRVCGSSBSDEV#123',
             'database': 'shr9_vrt_dev_003',
             'log_level': logging.DEBUG,
             # 默认情况下会自动生成会话标签，
             'session_label': 'some_label',
             # 无效的UTF-8结果默认抛出错误
             'unicode_error': 'strict',
             # 默认情况下禁用SSL
             'ssl': False,
             # 默认情况下，禁用使用服务器端预处理语句
             'use_prepared_statements': False,
             # 默认情况下未启用连接超时
             # 套接字操作5秒超时（建立TCP连接或读/写操作）
             'connection_timeout': 5}
