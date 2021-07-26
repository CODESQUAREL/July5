from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        #이미지라는 데이터는 RGB로 이루어진 픽셀데이터가 있고
        #메타데이터 : 이미지 외적인 요소(언제,어떤카메라,어디)를 말한다.
        model = Profile
        fields = ['image', 'nickname', 'massege'] #이 세가지의 입력을 받을 것이다
        #models.py에 만든 것은 4개인데 왜 입력은 3개만 받느냐?
        #
