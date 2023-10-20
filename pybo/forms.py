from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 플라스크에서 폼을 사용하려면 Flask-WTF 라이브러리를 설치
# Flask-WTF를 사용하려면 플라스크의 환경변수 SECRET_KEY가 필요하다.
# SECRET_KEY는 CSRF(cross-site request forgery):사용자의 요청을 위조하는 웹 사이트 공격 기법을 막기위해 SECRET_KEY를 기반으로 해서 생성되는 CSRF 토큰으로-> 폼으로 전송된 데이터가 실제 웹 페이지에서 작성된 데이터인지를 판단
# 플라스크의 폼은 FlaskForm 클래스를 상속하여 만들어야 한다.
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다. ')])

#  validators는 검증을 위해 사용되는 도구

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])