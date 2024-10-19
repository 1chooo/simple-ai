# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/08
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.1.1
'''

import flask
from flask import Flask, jsonify, request, render_template, g, make_response, redirect, url_for, json, send_from_directory
from flask_cors import CORS
import sys, os, random, bcrypt, time, re, pymysql, logging, datetime, requests, json, platform, shutil, traceback, pyhrv, gzip, base64, pytz
from urllib import parse
import app_config as ac
from werkzeug.exceptions import HTTPException
from markupsafe import escape
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

BASE_DIR = Path(__file__).resolve().parent
font_path = os.path.join(BASE_DIR, 'static', 'MicrosoftYaHeiMono-CP950.ttf')

# configuration
DEBUG = False

def send_email_from_gmail(email_title=None, email_from=None, email_to=None, email_body=None, gmail_id=None, gmail_password=None):
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = email_title  #郵件標題
    content["from"] = email_from  #寄件者
    content["to"] = email_to #收件者
    content.attach(MIMEText(email_body, 'html'))  #郵件內容
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(gmail_id, gmail_password)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            return("Complete!")
        except Exception as e:
            return("Error message: ", e)

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True

def sqlinjectionfilter(input_string=''):
    input_string=input_string.replace('"', '')
    input_string=input_string.replace("'", '')
    input_string=escape(input_string)
    return input_string

def getRootPath():
    try:
        return sys._MEIPASS
    except:
        return os.path.abspath(os.path.dirname(__file__))

def generateRandomString(length = 12):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    randomString=''
    for _ in range(length):
        randomString+=characters[random.randint(0,len(characters)-1)]
    return randomString

def login(email=None, password=None, userid=None, loginkey=None):
    if (loginkey and userid):
        sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `activate_code`, `fido2`, `fido2_challenge`, `fido2_registrations`, `forum_userid` FROM `user` WHERE `id`={userid} and `login_key`='{loginkey}'"
        return redirect(url_for('page_error', errorcode=999999))
    else:
        sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `activate_code`, `fido2`, `fido2_challenge`, `fido2_registrations`, `forum_userid` FROM `user` WHERE `email`='{email}'"
        with g.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
            if not data:
                return redirect(url_for('page_error', errorcode=460765))
            elif (data['activated'] == 0):
                new_user_activate_link = f"{g.parseResult.scheme}://{g.parseResult.netloc}/signup/{email}/{data['activate_code']}"
                try:
                    email_title="Please confirm your email for NCUEDU register"
                    email_from="ncuedutwmail@gmail.com"
                    email_to=data['email']
                    email_body=f'感謝您註冊NCUEDU會員，為了確認您的真實郵件，請點選以下連結：<br><a href={new_user_activate_link}>{new_user_activate_link}</a>'
                    gmail_id=ac.gmail.get('id')
                    gmail_password=ac.gmail.get('password')
                    send_email_from_gmail(email_title=email_title, email_from=email_from, email_to=email_to, email_body=email_body, gmail_id=gmail_id, gmail_password=gmail_password)
                    return redirect(url_for('page_success', successcode=674962))
                except:
                    # return redirect(url_for('page_success', successcode=674963))
                    return redirect(url_for('page_error', errorcode=460762))
            elif (data['salt']==None or len(data['salt'])==0):
                return redirect(url_for('page_error', errorcode=460801))
            try:
                passwordcrypt = bcrypt.hashpw(password.encode('utf-8'),data['salt'].encode('utf-8')).decode('utf-8')
            except:
                return redirect(url_for('page_error', errorcode=460801))
            if (passwordcrypt==data['password']):
                login_key = generateRandomString(24)
                sql_update = f"UPDATE user set login_key='{login_key}' where id={data['id']}"
                with g.conn.cursor() as cursor:
                    if not cursor.execute(sql_update):
                        return redirect(url_for('page_error', errorcode=470001))
                    else:
                        g.conn.commit()

                resp = make_response(redirect(url_for('page_success', successcode=674958)))
                resp.set_cookie("UserId", str(data['id']), expires=time.time()+60*60*24*7, domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
                resp.set_cookie("UserLoginKey", login_key, expires=time.time()+60*60*24*7, domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
                return resp
            else:
                return redirect(url_for('page_error', errorcode=460766))
    return None

def signup():
    email = str(sqlinjectionfilter(request.form.get('email')))
    username = str(sqlinjectionfilter(request.form.get('username')))
    password1 = str(sqlinjectionfilter(request.form.get('password1')))
    password2 = str(sqlinjectionfilter(request.form.get('password2')))
    name_last = str(sqlinjectionfilter(request.form.get('name_last')))
    name_first = str(sqlinjectionfilter(request.form.get('name_first')))
    if not email:
        return redirect(url_for('page_error', errorcode=460773))
    elif len(email)==0:
        return redirect(url_for('page_error', errorcode=460773))
    elif not username:
        return redirect(url_for('page_error', errorcode=460774))
    elif len(username)<3:
        return redirect(url_for('page_error', errorcode=460776))
    elif len(username)>20:
        return redirect(url_for('page_error', errorcode=460780))
    elif not re.findall('^\w{3,20}', username):
        return redirect(url_for('page_error', errorcode=460777))
    elif len(re.findall('^\w{3,20}', username)[0]) != len(username):
        return redirect(url_for('page_error', errorcode=460777))
    elif len(username.replace(' ', '')) != len(username):
        return redirect(url_for('page_error', errorcode=460777))
    elif not username.encode('UTF-8').isalnum():
        return redirect(url_for('page_error', errorcode=460777))
        
    elif len(password1)==0:
        return redirect(url_for('page_error', errorcode=460771))
    elif password1!=password2:
        return redirect(url_for('page_error', errorcode=460772))
    elif len(password1)<8:
        return redirect(url_for('page_error', errorcode=460775))
    
    username_blocklist = ('.git', '.htaccess', '.htpasswd', '.well-known', '400', '401', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '421', '422', '423', '424', '426', '428', '429', '431', '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '_domainkey', 'about', 'about-us', 'abuse', 'access', 'account', 'accounts', 'ad', 'add', 'admin', 'administration', 'administrator', 'ads', 'ads.txt', 'advertise', 'advertising', 'aes128-ctr', 'aes128-gcm', 'aes192-ctr', 'aes256-ctr', 'aes256-gcm', 'affiliate', 'affiliates', 'ajax', 'alert', 'alerts', 'alpha', 'amp', 'analytics', 'api', 'app', 'app-ads.txt', 'apps', 'asc', 'assets', 'atom', 'auth', 'authentication', 'authorize', 'autoconfig', 'autodiscover', 'avatar', 'backup', 'banner', 'banners', 'bbs', 'beta', 'billing', 'billings', 'blog', 'blogs', 'board', 'bookmark', 'bookmarks', 'broadcasthost', 'business', 'buy', 'cache', 'calendar', 'campaign', 'captcha', 'careers', 'cart', 'cas', 'categories', 'category', 'cdn', 'cgi', 'cgi-bin', 'chacha20-poly1305', 'change', 'channel', 'channels', 'chart', 'chat', 'checkout', 'clear', 'client', 'close', 'cloud', 'cms', 'com', 'comment', 'comments', 'community', 'compare', 'compose', 'config', 'connect', 'contact', 'contest', 'cookies', 'copy', 'copyright', 'count', 'cp', 'cpanel', 'create', 'crossdomain.xml', 'css', 'curve25519-sha256', 'customer', 'customers', 'customize', 'dashboard', 'db', 'deals', 'debug', 'delete', 'desc', 'destroy', 'dev', 'developer', 'developers', 'diffie-hellman-group-exchange-sha256', 'diffie-hellman-group14-sha1', 'disconnect', 'discuss', 'dns', 'dns0', 'dns1', 'dns2', 'dns3', 'dns4', 'docs', 'documentation', 'domain', 'download', 'downloads', 'downvote', 'draft', 'drop', 'ecdh-sha2-nistp256', 'ecdh-sha2-nistp384', 'ecdh-sha2-nistp521', 'edit', 'editor', 'email', 'enterprise', 'error', 'errors', 'event', 'events', 'example', 'exception', 'exit', 'explore', 'export', 'extensions', 'false', 'family', 'faq', 'faqs', 'favicon.ico', 'features', 'feed', 'feedback', 'feeds', 'file', 'files', 'filter', 'follow', 'follower', 'followers', 'following', 'fonts', 'forgot', 'forgot-password', 'forgotpassword', 'form', 'forms', 'forum', 'forums', 'friend', 'friends', 'ftp', 'get', 'git', 'go', 'graphql', 'group', 'groups', 'guest', 'guidelines', 'guides', 'head', 'header', 'help', 'hide', 'hmac-sha', 'hmac-sha1', 'hmac-sha1-etm', 'hmac-sha2-256', 'hmac-sha2-256-etm', 'hmac-sha2-512', 'hmac-sha2-512-etm', 'home', 'host', 'hosting', 'hostmaster', 'htpasswd', 'http', 'httpd', 'https', 'humans.txt', 'icons', 'images', 'imap', 'img', 'import', 'index', 'info', 'insert', 'investors', 'invitations', 'invite', 'invites', 'invoice', 'is', 'isatap', 'issues', 'it', 'jobs', 'join', 'js', 'json', 'keybase.txt', 'learn', 'legal', 'license', 'licensing', 'like', 'limit', 'live', 'load', 'local', 'localdomain', 'localhost', 'lock', 'login', 'logout', 'lost-password', 'm', 'mail', 'mail0', 'mail1', 'mail2', 'mail3', 'mail4', 'mail5', 'mail6', 'mail7', 'mail8', 'mail9', 'mailer-daemon', 'mailerdaemon', 'map', 'marketing', 'marketplace', 'master', 'me', 'media', 'member', 'members', 'message', 'messages', 'metrics', 'mis', 'mobile', 'moderator', 'modify', 'more', 'mx', 'mx1', 'my', 'net', 'network', 'new', 'news', 'newsletter', 'newsletters', 'next', 'nil', 'no-reply', 'nobody', 'noc', 'none', 'noreply', 'notification', 'notifications', 'ns', 'ns0', 'ns1', 'ns2', 'ns3', 'ns4', 'ns5', 'ns6', 'ns7', 'ns8', 'ns9', 'null', 'oauth', 'oauth2', 'offer', 'offers', 'online', 'openid', 'order', 'orders', 'overview', 'owa', 'owner', 'page', 'pages', 'partners', 'passwd', 'password', 'pay', 'payment', 'payments', 'paypal', 'photo', 'photos', 'pixel', 'plans', 'plugins', 'policies', 'policy', 'pop', 'pop3', 'popular', 'portal', 'portfolio', 'post', 'postfix', 'postmaster', 'poweruser', 'preferences', 'premium', 'press', 'previous', 'pricing', 'print', 'privacy', 'privacy-policy', 'private', 'prod', 'product', 'production', 'profile', 'profiles', 'project', 'projects', 'promo', 'public', 'purchase', 'put', 'quota', 'redirect', 'reduce', 'refund', 'refunds', 'register', 'registration', 'remove', 'replies', 'reply', 'report', 'request', 'request-password', 'reset', 'reset-password', 'response', 'return', 'returns', 'review', 'reviews', 'robots.txt', 'root', 'rootuser', 'rsa-sha2-2', 'rsa-sha2-512', 'rss', 'rules', 'sales', 'save', 'script', 'sdk', 'search', 'secure', 'security', 'select', 'services', 'session', 'sessions', 'settings', 'setup', 'share', 'shift', 'shop', 'signin', 'signup', 'site', 'sitemap', 'sites', 'smtp', 'sort', 'source', 'sql', 'ssh', 'ssh-rsa', 'ssl', 'ssladmin', 'ssladministrator', 'sslwebmaster', 'stage', 'staging', 'stat', 'static', 'statistics', 'stats', 'status', 'store', 'style', 'styles', 'stylesheet', 'stylesheets', 'subdomain', 'subscribe', 'sudo', 'super', 'superuser', 'support', 'survey', 'sync', 'sysadmin', 'sysadmin', 'system', 'tablet', 'tag', 'tags', 'team', 'telnet', 'terms', 'terms-of-use', 'test', 'testimonials', 'theme', 'themes', 'today', 'tools', 'topic', 'topics', 'tour', 'training', 'translate', 'translations', 'trending', 'trial', 'true', 'umac-128', 'umac-128-etm', 'umac-64', 'umac-64-etm', 'undefined', 'unfollow', 'unlike', 'unsubscribe', 'update', 'upgrade', 'usenet', 'user', 'username', 'users', 'uucp', 'var', 'verify', 'video', 'view', 'void', 'vote', 'vpn', 'webmail', 'webmaster', 'website', 'widget', 'widgets', 'wiki', 'wpad', 'write', 'www', 'www-data', 'www1', 'www2', 'www3', 'www4', 'you', 'yourname', 'yourusername', 'zlib')
    
    for _ in ('admin', 'moderator', 'administrator', 'mod', 'sys', 'system', 'community', 'info', 'you', 
    'name', 'username', 'user', 'nickname', 'discourse', 'discourseorg', 'discourseforum', 
    'ncuedu', 'ncuedutw', 'ncueduforum', 'macs', 'macsai', 'support', 'hp', 'account-created', 
    'password-reset', 'admin-login', 'confirm-admin', 'account-created', 'activate-account', 
    'confirm-email-token', 'authorize-email', 'thencuedu', 'theanswer', 'thencuedutw', 
    'theanswerorg', 'root', 'sudo')+username_blocklist:
        if username.lower() in _.lower():
            return redirect(url_for('page_error', errorcode=460781))
    sql = f"SELECT `id`, `email`, `username`, `password`, `salt` FROM user WHERE email='{email}'"
    with g.conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchone()
        if data:
            return redirect(url_for('page_error', errorcode=460764))
    
    sql = f"SELECT `id`, `email`, `username`, `password`, `salt` FROM user WHERE username='{username}'"
    with g.conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchone()
        if data:
            return redirect(url_for('page_error', errorcode=460763))
    
    salt = bcrypt.gensalt()
    passwordcrypt = bcrypt.hashpw(password1.encode('utf-8'), salt).decode('utf-8')    
    activate_code = generateRandomString(24)
    sql_insert = f"INSERT INTO user (`email`, `username`, `password`, `salt`, `activate_code`, `name_first`, `name_last`, `reset_pw_code`, `login_key`) VALUES ('{email}', '{username}', '{passwordcrypt}', '{salt.decode('utf-8')}', '{activate_code}', '{name_first}', '{name_last}', '', '')"
    with g.conn.cursor() as cursor:
        if not cursor.execute(sql_insert):
            return redirect(url_for('page_error', errorcode=470001))
        else:
            g.conn.commit()
            new_user_activate_link = g.parseResult.scheme+'://'+g.parseResult.netloc+'/signup/'+email+'/'+activate_code
            try:
                email_title="Please confirm your email for NCUEDU register"
                email_from="ncuedutwmail@gmail.com"
                email_to=f'{email}'
                email_body=f'感謝您註冊NCUEDU會員，為了確認您的真實郵件，請點選以下連結：<br><a href={new_user_activate_link}>{new_user_activate_link}</a>'
                gmail_id=ac.gmail.get('id')
                gmail_password=ac.gmail.get('password')
                send_email_from_gmail(email_title=email_title, email_from=email_from, email_to=email_to, email_body=email_body, gmail_id=gmail_id, gmail_password=gmail_password)
                return redirect(url_for('page_success', successcode=674963))
            except:
                return redirect(url_for('page_success', successcode=674963))

def activat_check_code(email=None, activatecode=None):
    sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `fido2`, `fido2_challenge`, `fido2_registrations` FROM user WHERE email='{email}' and activate_code='{activatecode}'"
    with g.conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchone()
        if not data:
            return redirect(url_for('page_error', errorcode=460768))
        elif data['activated']==1:
            return redirect(url_for('page_error', errorcode=460767))
    sql_update = f"UPDATE user SET `activated`=1 WHERE email='{email}' and activate_code='{activatecode}'"
    with g.conn.cursor() as cursor:
        if not cursor.execute(sql_update):
            return redirect(url_for('page_error', errorcode=470001))
        else:
            g.conn.commit()
            return redirect(url_for('page_success', successcode=674964))
    return redirect(url_for('page_index'))

def resetpw_check_code(email=None, resetpwcode=None):
    sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `fido2`, `fido2_challenge`, `fido2_registrations` FROM user WHERE email='{email}' and reset_pw_code='{resetpwcode}'"
    with g.conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchone()
        if not data:
            return redirect(url_for('page_error', errorcode=460770))
    return render_template('resetpw.html', email=email, resetpwcode=resetpwcode)

def resetpw_action(email=None, resetpwcode=None, password1=None, password2=None):
    if email != None and resetpwcode != None and password1 != None and password2 != None:
        if password1!=password2:
            return redirect(url_for('page_error', errorcode=460772))
        elif len(password1)==0:
            return redirect(url_for('page_error', errorcode=460771))
        elif len(password1)<8:
            return redirect(url_for('page_error', errorcode=460775))
        salt = bcrypt.gensalt()
        sql_update = f"UPDATE user SET salt='{salt.decode('utf-8')}', password='{bcrypt.hashpw(password1.encode('utf-8'), salt).decode('utf-8')}', reset_pw_code='{generateRandomString(24)}' WHERE email='{email}' and reset_pw_code='{resetpwcode}'"
        with g.conn.cursor() as cursor:
            if not cursor.execute(sql_update):
                return redirect(url_for('page_error', errorcode=470001))
            else:
                g.conn.commit()
            return redirect(url_for('page_success', successcode=674960))
    else:
        sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `fido2`, `fido2_challenge`, `fido2_registrations` FROM user WHERE email='{email}'"
        with g.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
            if not data:
                return redirect(url_for('page_error', errorcode=460765))
        reset_pw_code = generateRandomString(24)
        print(reset_pw_code)
        reset_pw_link = g.parseResult.scheme+'://'+g.parseResult.netloc+'/resetpw/'+email+'/'+reset_pw_code
        sql_update = f"UPDATE user SET reset_pw_code='{reset_pw_code}' WHERE email='{email}'"
        print(sql_update)
        with g.conn.cursor() as cursor:
            if not cursor.execute(sql_update):
                return redirect(url_for('page_error', errorcode=470001))
            else:
                g.conn.commit()
            
            email_title="Reset password"
            email_from="ncuedutwmail@gmail.com"
            email_to=f'{email}'
            email_body=f'<a href={reset_pw_link}>{reset_pw_link}</a>'
            gmail_id=ac.gmail.get('id')
            gmail_password=ac.gmail.get('password')
            send_email_from_gmail(email_title=email_title, email_from=email_from, email_to=email_to, email_body=email_body, gmail_id=gmail_id, gmail_password=gmail_password)
        return redirect(url_for('page_success', successcode=674959))

def user_data_update_action(user_github_id=None, user_pypal_id=None):
    if g.userdata:
        sql = f"SELECT `id`, `email`, `salt`, `password`, `github_id`, `pypal_id` FROM `user` WHERE `id`={g.userdata['id']}"
        with g.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
            if not data:
                return redirect(url_for('page_error', errorcode=460765))
            elif data['github_id']==user_github_id and str(data['pypal_id'])==user_pypal_id:
                return redirect(url_for('page_error', errorcode=460901))
        if not user_pypal_id: user_pypal_id=0
        sql_update = f"UPDATE `user` SET `github_id`='{user_github_id}', `pypal_id`={user_pypal_id} WHERE `id`={g.userdata['id']}"
        with g.conn.cursor() as cursor:
            if not cursor.execute(sql_update):
                return redirect(url_for('page_error', errorcode=470001))
            else:
                g.conn.commit()
                if user_pypal_id:
                    # bot.sendPhoto(chat_id=user_pypal_id, photo=open("./static/telegram_bot_materials/images/datalink.jpg", 'rb'))
                    bot.sendPhoto(chat_id=user_pypal_id, photo=request.url_root.rstrip('/')+url_for('static', filename='telegram_bot_materials/images/datalink.jpg'))
                    bot.sendMessage(chat_id=user_pypal_id, text='恭喜，您剛剛在[NCUEDU](https://ncuedu.tw/)做了PyPal教學型聊天機器人的資料綁定，如果不是你本人操作，請到[NCUEDU](https://ncuedu.tw/)修改您的密碼，以確保資料安全。', disable_web_page_preview=True, parse_mode='Markdown')
                return redirect(url_for('page_success', successcode=674968))
    else:
        return redirect(url_for('page_error', errorcode=460600))

def change_email_activate(email=None, change_email_code=None):
    sql = f"SELECT `id`, `email`, `new_email` FROM user WHERE `email`='{email}' and `change_email_code`='{change_email_code}'"
    print(sql)
    with g.conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchone()
        if not data:
            return redirect(url_for('page_error', errorcode=460770))
    sql_recheck_new_email = f"SELECT `id`, `email` FROM user WHERE email='{data['new_email']}'"
    with g.conn.cursor() as cursor:
        cursor.execute(sql_recheck_new_email)
        data_recheck = cursor.fetchone()
        if data_recheck:
            return redirect(url_for('page_error', errorcode=460764))
    sql_update_new_email = f"UPDATE `user` SET `email`='{data['new_email']}', `new_email`='', `change_email_code`='' WHERE id={data['id']}"
    with g.conn.cursor() as cursor:
        if not cursor.execute(sql_update_new_email):
            return redirect(url_for('page_error', errorcode=470001))
        else:
            g.conn.commit()
            g.userdata['email']=data['new_email']
            g.internalUserDataFromDbEmail=data['new_email']
            return redirect(url_for('page_success', successcode=674966))

def change_password_action(password=None, new_password=None, new_password2=None):
    if g.userdata:
        sql = f"SELECT `id`, `email`, `salt`, `password` FROM `user` WHERE id={g.userdata['id']}"
        with g.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
            if not data:
                return redirect(url_for('page_error', errorcode=460765))
            elif data['password'] != bcrypt.hashpw(password.encode('utf-8'), data['salt'].encode('utf-8')).decode('utf-8'):
                return redirect(url_for('page_error', errorcode=460766))
            elif new_password != new_password2:
                return redirect(url_for('page_error', errorcode=460772))
            elif new_password.__len__()<8:
                return redirect(url_for('page_error', errorcode=460775))
            elif new_password.__len__()==0:
                return redirect(url_for('page_error', errorcode=460771))
        salt = bcrypt.gensalt()
        strPassword = bcrypt.hashpw(new_password.encode('utf-8'), salt).decode('utf-8')
        strSalt = salt.decode('utf-8')
        sql_update = f"UPDATE `user` SET `password`='{strPassword}', `salt`='{strSalt}' WHERE `id`={g.userdata['id']}"
        with g.conn.cursor() as cursor:
            if not cursor.execute(sql_update):
                return redirect(url_for('page_error', errorcode=470001))
            else:
                g.conn.commit()
                return redirect(url_for('page_success', successcode=674967))
    else:
        return redirect(url_for('page_error', errorcode=460600))

def change_email_action(new_email=None, password=None):
    if g.userdata:
        sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `fido2`, `fido2_challenge`, `fido2_registrations`, `change_email_code` FROM user WHERE id={g.userdata['id']}"
        with g.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
            if not data:
                return redirect(url_for('page_error', errorcode=460765))
        sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `fido2`, `fido2_challenge`, `fido2_registrations`, `change_email_code` FROM user WHERE email='{new_email}'"
        with g.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
            if data:
                return redirect(url_for('page_error', errorcode=460764))
        str_change_email_code = generateRandomString(24)
        sql = f"UPDATE `user` SET `new_email`='{new_email}', `change_email_code`='{str_change_email_code}' WHERE `id`={g.userdata['id']}"
        with g.conn.cursor() as cursor:
            if not cursor.execute(sql):
                return redirect(url_for('page_error', errorcode=470001))
            else:
                g.conn.commit()
                change_email_activate_link = g.parseResult.scheme+'://'+g.parseResult.netloc+'/change_email/'+g.userdata['email']+'/'+str_change_email_code
                try:
                    email_title="Please confirm your new email address"
                    email_from="ncuedutwmail@gmail.com"
                    email_to=f'{new_email}'
                    email_body=f'您好，<br><br>由於您申請更換email地址，為了確認您的心email地址填寫正確，並可正常收到郵件，請點選連結確認：<br><a href={change_email_activate_link}>{change_email_activate_link}</a><br><br>若您沒有申請更換Email地址，請勿理會本郵件'
                    gmail_id=ac.gmail.get('id')
                    gmail_password=ac.gmail.get('password')
                    send_email_from_gmail(email_title=email_title, email_from=email_from, email_to=email_to, email_body=email_body, gmail_id=gmail_id, gmail_password=gmail_password)
                    return redirect(url_for('page_success', successcode=674965))
                except:
                    return redirect(url_for('page_error', errorcode=460769))
    else:
        return redirect(url_for('page_error', errorcode=460600))

app = Flask(__name__, 
            static_folder=getRootPath()+'/static', 
            static_url_path="/static", 
            template_folder=getRootPath()+'/templates', )
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.template_filter('formatdatetime')
def format_datetime(value, format="%Y/%m/%d %H:%M:%S"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
    if value is None:
        return ""       
    return datetime.datetime.fromtimestamp(datetime.datetime.fromisoformat(value[:-1]).timestamp()-offset).strftime(format)

@app.before_request
def before():
    g.internalUserDataFromDbId = 0
    g.internalUserDataFromDbEmail = ''
    g.internalUserDataFromDbUserName = ''
    g.internalstrUserDataFromDbNameFirst = ''
    g.internalstrUserDataFromDbNameLast = ''
    g.internalUserDataFromDbGithubID = ''
    g.internalUserDataFromDbPyPalID = ''
    g.parseResult = parse.urlparse(request.url)
    UserId = request.cookies.get('UserId')
    UserLoginKey = request.cookies.get('UserLoginKey')
    # 連接資料庫
    conn = pymysql.connect(host=ac.dbConfig['strServer'], 
                            port=ac.dbConfig['intPort'], 
                            user=ac.dbConfig['strDbUserID'], 
                            password=ac.dbConfig['strPassword'], 
                            database=ac.dbConfig['strDatabase'],
                            cursorclass=pymysql.cursors.DictCursor)
    g.conn = conn
    try:
        UserId = int(UserId)
        if UserId:
            try:
                with g.conn.cursor() as cursor:
                    sql = f"SELECT `id`, `email`, `username`, `password`, `salt`, `activated`, `login_key`, `name_first`, `name_last`, `forum_userid`, `github_id`, `pypal_id`, `garmin_oauth_token`, `garmin_oauth_token_secret` \
                            FROM user \
                            WHERE id='{UserId}'"
                    cursor.execute(sql)
                    g.userdata = cursor.fetchone()
                    if (g.userdata["login_key"]==UserLoginKey):
                        g.internalUserDataFromDbId = g.userdata["id"]
                        g.internalUserDataFromDbEmail = g.userdata["email"]
                        g.internalUserDataFromDbUserName = g.userdata["username"]
                        g.internalstrUserDataFromDbNameFirst = g.userdata["name_first"]
                        g.internalstrUserDataFromDbNameLast = g.userdata["name_last"]
                        g.internalUserDataFromDbGithubID = g.userdata["github_id"] if g.userdata["github_id"] else ''
                        g.internalUserDataFromDbPyPalID = g.userdata["pypal_id"] if g.userdata["pypal_id"] else ''
                        g.internalUserDataFromDbGarminOauthToken = g.userdata["garmin_oauth_token"] if g.userdata["garmin_oauth_token"] else ''
                        g.internalUserDataFromDbGarminOauthTokenSecret = g.userdata["garmin_oauth_token_secret"] if g.userdata["garmin_oauth_token_secret"] else ''
                    else:
                        resp = make_response(redirect(request.url))
                        resp.delete_cookie("UserId", domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
                        resp.delete_cookie("UserLoginKey", domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
                        return resp
            except:
                resp = make_response(redirect(request.url))
                resp.delete_cookie("UserId", domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
                resp.delete_cookie("UserLoginKey", domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
                return resp
            finally:
                pass
    except:
        pass

@app.after_request
def after_request(response):
    g.conn.close()
    global callback_data_previsus_list
    if 'callback_data' in g and 'chat_id' in g:
        if g.callback_data!='/help-call_submit':
            callback_data_previsus_list.setdefault(str(g.chat_id), []).insert(0, g.callback_data)
            callback_data_previsus_list[str(g.chat_id)]=callback_data_previsus_list.get(str(g.chat_id), [])[:5]
    return response

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return render_template("500.html", e=e), 500

@app.route('/')
def page_index():
    web_content = {}
    return render_template('index.html', web_content = web_content)

@app.route('/document')
@app.route('/course')
def page_course_index():
    return render_template('course.html')

@app.route('/resource/<int:cid>/<int:tid>')
@app.route('/resource')
@app.route('/resource/')
def page_resource(cid=None, tid=None):
    return render_template('resource.html', cid=cid, tid=tid)

@app.route('/about')
def page_about():
    return render_template('about.html')
    
@app.route('/profile', methods=['GET', 'POST'])
def page_profile():
    try:
        g.userdata
        if request.method=='POST':
            pass
        else:
            return render_template('profile.html')
    except:
        return redirect(url_for('page_index'))

@app.route('/user_data', methods=['GET', 'POST'])
def page_user_data():
    try:
        g.userdata
        if request.method=='POST':
            return user_data_update_action(user_github_id=sqlinjectionfilter(request.form.get('user_github_id')), user_pypal_id=sqlinjectionfilter(request.form.get('user_pypal_id')))
        else:
            print(g.userdata)
            return render_template('user_data.html', user_data=g.userdata)
    except:
        return redirect(url_for('page_error', errorcode=999999))

@app.route('/change_email/<string:email>/<string:change_email_code>')
def activate_change_email(email, change_email_code):
    return change_email_activate(email=email, change_email_code=change_email_code)

@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    try:
        g.userdata
        if request.method=='POST':
            return change_email_action(new_email=sqlinjectionfilter(request.form.get('new_email')), password=sqlinjectionfilter(request.form.get('password')))
        else:
            return render_template('change_email.html')
    except:
        return redirect(url_for('page_index'))


@app.route('/change_password', methods=['GET', 'POST'])
def page_change_password():
    if request.method == 'POST':
        return change_password_action(password=sqlinjectionfilter(request.form.get('password')), new_password=sqlinjectionfilter(request.form.get('new_password')), new_password2=sqlinjectionfilter(request.form.get('new_password2')))
    else:
        return render_template('change_password.html')

@app.route('/signout')
def page_signout():
    resp = make_response(render_template('success.html', successcode=674957))
    resp.delete_cookie("UserId", domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
    resp.delete_cookie("UserLoginKey", domain='.ncuedu.tw' if 'ncuedu.tw' in request.url_root.lower() else None)
    return resp

@app.route('/signin', methods=['GET', 'POST'])
def page_signin():
    if request.method=='POST':
        return login(email=sqlinjectionfilter(request.form.get('email')), password=sqlinjectionfilter(request.form.get('password')), userid=None, loginkey=None)
    else:
        return render_template('signin.html')

@app.route('/signup/<string:email>/<string:activatecode>', methods=['GET'])
def page_signup2(email, activatecode):
    return activat_check_code(email=email, activatecode=activatecode)

@app.route('/signup', methods=['GET', 'POST'])
def page_signup():
    if request.method=='POST':
        return signup()
    else:
        return render_template('signup.html')

@app.route('/resetpw/<string:email>/<string:resetpwcode>', methods=['GET', 'POST'])
def page_resetpw2(email, resetpwcode):
    if request.method=='POST':
        return resetpw_action(email=email, resetpwcode=resetpwcode, password1=sqlinjectionfilter(request.form.get('password1')), password2=sqlinjectionfilter(request.form.get('password2')))
    elif len(email)>0 and len(resetpwcode)>0:
        return resetpw_check_code(email=email, resetpwcode=resetpwcode)
        
@app.route('/resetpw', methods=['GET', 'POST'])
def page_resetpw():
    if request.method=='POST':
        return resetpw_action(email=sqlinjectionfilter(request.form.get('email')))
    else:
        return render_template('resetpw.html')

@app.route('/error/<int:errorcode>')
@app.route('/error/<int:errorcode>/cid/<int:course_id>/qid/<int:quiz_id>')
@app.route('/error/<int:errorcode>/<path:return_back_url>')
def page_error(errorcode=0, course_id=0, quiz_id=0, return_back_url=''):
    return render_template('error.html', errorcode=errorcode, course_id=course_id, quiz_id=quiz_id, return_back_url=return_back_url)

@app.route('/success/<int:successcode>')
@app.route('/success/<int:successcode>/cid/<int:course_id>/qid/<int:quiz_id>')
@app.route('/success/<int:successcode>/<path:return_back_url>')
def page_success(successcode=0, course_id=0, quiz_id=0, return_back_url=''):
    return render_template('success.html', successcode=successcode, course_id=course_id, quiz_id=quiz_id, return_back_url=return_back_url)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# run app
if __name__ == "__main__":
    app.debug=False
    if not app.debug:
        if not os.path.exists('./errorlog'): os.makedirs('./errorlog')
        handler = logging.FileHandler(f'{datetime.datetime.now():./errorlog/%Y%m%d_%H%M_ncuedu_flask.log}')
        app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port=5006, debug=app.debug, use_reloader=True)
