from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk']) #DB에서 찾는 과정
        if target_comment.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated