from django.contrib.auth.forms import UserCreationForm



class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled =True # 이걸 이용해서 id를 변경하지 못하게 함