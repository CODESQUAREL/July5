FROM python:3.9.0

WORKDIR /home/

RUN echo "asdfasasadsdfsdff"

RUN git clone https://github.com/CODESQUAREL/July5.git

WORKDIR /home/July5/

#RUN echo "SECRET_KEY=django-insecure-6hb=)#ll+9f2n^ywug5l+%^wqiznrfgr(md!cys-i+4n$ognt%" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=July2_강의보고따라하기.settings.deploy && python manage.py migrate --settings=July2_강의보고따라하기.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=July2_강의보고따라하기.settings.deploy July2_강의보고따라하기.wsgi --bind 0.0.0.0:8000"]
