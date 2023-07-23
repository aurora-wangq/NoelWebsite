####本项目是项目Noel的简化版本
####Project Leader：Noel
####Code Contributor：[AenStarAX](https://github.com/aurora-wangq) & [MoveToEx](https://github.com/MoveToEx)
---
#食用方法：
####开始前请确保您已安装python
##😊部署&起洞项目
###控制台进入Noel项目文件夹
###创建虚拟环境
```sh
python -m venv env
```
###激活虚拟环境
```sh
env\Scripts\activate
```
###安装需求包
```sh
pip install -r requirements.txt
```
###转移数据库文件
```sh
python manage.py migrate
```
###启动项目
```sh
python manage.py runserver
```
####至此，你已经成功启动项目🥳！
---
##😊文件结构/介绍
```text
Noel
|--fan
    |-migrations数据库迁移文件
    |-templates页面HTML模板文件
    |-__init__.py自带的初始化文件
    |-admin.py管理页面控制文件
    |-apps.py应用"fan"注册配置文件
    |-forms.pt表单控制文件(已弃用)
    |-models.py数据库字段关联文件
    |-url.py子路由配置文件
    |-views.py视图控制文件
|--media
    |-default默认图片
    |-post_images文章图片
    |-profile_images用户个人信息相关图片
    |-user_page_backimg个人页面背景图片
|--noel
    |-__init__.py自带的初始化文件
    |-settings.py项目配置文件
    |-urls.py主路由配置文件
    |-wsgi.py服务网关接口(仅支持HTTP(S))
|--staticHTML静态文件
|--thumbnail帖子预览图片文件
|--预览 项目预览图
|--collection.json网页上方文字json文件
|--db.sqlite3-默认数据库
|--manage.py项目管理文件
|--README.md说明文件
|--requirements.txt项目环境配置文件
```



---
##😊基本命令
###部署完成后的启动
```sh
env\Scripts\activate
python manage.py runserver
```
###创建一个管理员用户
```sh
python manage.py createsuperuser
```
###数据库相关
#####生成数据库迁移文件
```sh
python manage.py makemigrations
```
#####迁移数据库文件
```sh
python manage.py migrate
```
---
##😊管理页
####管理页使用Django自带的强大的后台管理系统
>注意！进入管理页前你必须先拥有一个管理员账户！
###管理页地址
```url
BASE_URL:PORT/admin/
例如：http://127.0.0.1:8000/admin/
```
###管理页面信息
####User
```text
用于修改用户用户名、昵称、个人资料、密码等
```
####Comments
```text
用于管理评论
```
####Likes
```text
用于管理点赞
```
####Notices
```text
用于发布公告
```
####Posts
```text
用于管理文章
```
---
###效果图
####登陆页
<image src="预览/Login.png">
####主页
<image src="预览/Home.png">
####个人主页
<image src="预览/MyPage.png">
####文章详情页面
<image src="预览/Post.png">

---

#注意事项
>**本项目默认使用WSGI启动且并未携带ASGI配置文件因此不支持直接使用WS/WSS协议,请自行查阅资料自行编写或直接使用HTTP/HTTPSX协议中长轮询的方式进行编写**
>**项目使用Django默认sqlite3数据库，不支持并发写入，可自行修改setting.py修改为其他数据库并自行接入**
>**禁止一切违法商业用途**



