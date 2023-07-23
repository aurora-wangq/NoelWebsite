from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


# Create your models here.

class UserProfile(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    nike_name = models.CharField('昵称', max_length=23, blank=True, default='')
    desc = models.TextField('个人简介', max_length=100, blank=True, default='', null=True)
    sign = models.CharField('个性签名', max_length=25, blank=True, default='', null=True)
    birthday = models.DateField('生日', null=True, blank=True)
    address = models.CharField('地址', max_length=100, blank=True, default='')
    title = models.CharField('头衔', max_length=100, default='善良的网友',blank=True)
    img = models.ImageField('头像', upload_to='profile_images',  default='/default/txdefault.jpg',blank=True)
    back_img = models.ImageField('个人主页背景', upload_to='user_page_backimg',  default='/default/backimg.jpg', blank=True, null=True)
    title_level = models.IntegerField('头衔类别,1站主,2管理员,3特殊,4普通', default=4)
    notice = models.TextField('发布公告', max_length=1000, null=True, blank=True, default='')
    def __str__(self):
        return self.nike_name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="文章作者")
    owner_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_content = models.CharField('帖子内容', max_length=10000, blank=True)
    post_img1 = models.ImageField('帖子图片1', upload_to='post_images', blank=True, null=True)
    show_view = models.BooleanField('预览图是否模糊', default=False)
    pinned = models.BooleanField('是否顶置',default = False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField('评论内容', max_length=500, blank=True, null=True)
    #like = models.IntegerField('点赞')

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='赞所属文章', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='点赞者', blank=True, null=True)

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="公告拥有者")#这一条仅用于admin界面能够集成Notice便于管理
    creater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="公告发布者")
    notice = models.TextField('公告内容', max_length=300, blank=True)

