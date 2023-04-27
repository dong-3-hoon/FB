문제 1: 처음 생성한 migrations파일이 꼬여서 db.sqlite3, migrations파일을 삭제 후 재설치

문제 2: model 클래스의 다양한 데이터 유형을 선정하는데 어려움을 겪음

문제 3: 그 중 float가 0.5씩 증가하지 않는 문제가 발생했고, 위젯을 활용해 해결함
widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.5"})

문제 4: base.html이미지만 띄워지고 상속이후 내용이 출력되지 않는 문제가 있었고, 블록 콘텐츠 를 넣음 상속 blockcontent 상속 형식으로 내용을 출력시킨 다는 사실을 배울 수 있었음
{% block content %}{% endblock content %}

문제 5: 달력 widjets를 어떻게 적용할 지 몰랐지만 docs참조 결과
release_data = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
코드로 해결함

문제 6: 서버를 켜놓은채로 작업을 하다 쿠키가 꼬였고, 전체 새로고침을 하자 해결됨

문제 7: 6 과정에서 바뀐 코드 때문에 그림 크기가 작게 고정되는 현상이 발생
base=style=100% 코드로 인해 발생했고 이후 base=style:100%로 변경