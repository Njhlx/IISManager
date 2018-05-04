#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import Common.Const
CONST = Common.Const


def create_app_pool(app_pool_name, runtime_version="v4.0",mode="Integrated"):
    print("增加应用程序池 %s \"%s\"" % (app_pool_name, runtime_version))
    cmd_str = "%s add apppool /name:\"%s\" /managedRuntimeVersion:\"%s\" /managedPipelineMode:\"%s\"" \
              % (CONST.IIS_CMD_DIR, app_pool_name, runtime_version, mode)
    print(cmd_str)
    print(os.popen(cmd_str).read())


def set_app_pool_recycling_periodic_restart_schedule(app_pool_name, time_span="02:00:00"):
    print("修改应用程序池 %s 回收（特定时间） \"%s\"" % (app_pool_name, time_span))
    cmd_str = "%s set apppool /apppool.name:\"%s\" /+recycling.periodicRestart.schedule.[value='%s']" \
              % (CONST.IIS_CMD_DIR, app_pool_name, time_span)
    print(cmd_str)
    print(os.popen(cmd_str).read())


def create_site(site_name,port,physical_path):
    # 创建IIS网站命令
    # appcmd add site /name:"site name" /bindings:http://*:1234 /physicalPath:"c:\TestSite"
    # 删除IIS网站命令
    # appcmd delete site "site name"
    print("增加网站 %s" % site_name)
    cmd_str = "%s add site /name:\"%s\" /bindings:http://*:%d /physicalPath:\"%s\""\
              % (CONST.IIS_CMD_DIR, site_name, port, physical_path)
    print(cmd_str)
    print(os.popen(cmd_str).read())


def set_site_app_pool(site_name, app_pool_name):
    print("修改网站 %s 的应用程序池为 %s" % (site_name, app_pool_name))
    cmd_str = "%s set site \"%s\" /[path='/'].applicationPool:\"%s\" " \
              % (CONST.IIS_CMD_DIR, site_name, app_pool_name)
    print(cmd_str)
    print(os.popen(cmd_str).read())


def set_site_auto_start(site_name, command=True):
    print("设置网站 %s 自动启动 %s" % (site_name, command))
    cmd_str = "%s set site /site.name:\"%s\" /serverAutoStart:%s" \
              % (CONST.IIS_CMD_DIR, site_name, command)
    print(cmd_str)
    print(os.popen(cmd_str).read())


if __name__ == "__main__":
    import ConstSettings
    ConstSettings.define()
    create_site("yxs test site", 1234, "C:\TestSite")
    print(os.popen("dir").read())
