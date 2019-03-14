from django import forms

from .models import *


# 为topic控件初始化数据
TOPIC_CHOICE=(
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)


# 表示评论内容的表单控件们
# 控件1 - 评论标题 - 文本框
# 控件2 - Email - Email框
# 控件3 - 评论内容 - Textarea
# 控件4 - 评论级别 - Select
# 控件5 - 是否保存 - Checkbox
class RemarkForm(forms.Form):
    # subject - input type='text'
    # label 表示的就是控件前的文本 -<label></label>
    subject=forms.CharField(max_length=30,label="标题")
    # email - input type='email'
    email=forms.EmailField(label="邮箱")
    # message - Textarea
    # widget=forms.Textarea 将当前的文本框变成多行的文本域
    message=forms.CharField(label="内容",widget=forms.Textarea)
    # 评论级别 - topic - select
    topic=forms.ChoiceField(label="级别",choices=TOPIC_CHOICE)
    # isSaved - checkbox
    isSaved=forms.BooleanField(label="是否保存")


# RegisterForm:结合models.py 中的 User 类来生成控件
class RegisterForm(forms.ModelForm):
    class Meta:
        # 1.指定关联的Model
        model = User
        # 2.指定要生成控件的属性们
        fields = "__all__"
        # 3.指定每个控件所对应的label文本
        labels = {
            'uname':"用户名称",
            'upwd':"用户密码",
            'uemail':"电子邮件",
        }
