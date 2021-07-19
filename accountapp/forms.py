from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True  #크롬 개발자(F12)탭에서 아이디를 변경하더라도 장고에서는 변경되지 않는다. disabled = True 를 입력해놨기 때문