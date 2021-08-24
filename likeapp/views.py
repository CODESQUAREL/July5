from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView): #redirectview를 상속받음

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)

        if like_record.exists():
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk':kwargs['article_pk']}))

        else:
            LikeRecord(user=user, article=article).save()
        article.like += 1 #좋아요 개수를 1 추가하고
        article.save()    #DB에 반영
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']})