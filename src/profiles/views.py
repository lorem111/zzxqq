from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


User = get_user_model()

@login_required
def profile_list_view(request):
    context = {
        "object_list": User.objects.filter(is_active=True)
       
    }
    return render(request, "profiles/list.html", context)

""" @login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    print('user.has_perm("auth.view_user")', user.has_perm("auth.view_user"))
    
    print('user.has_perm("visits.view_pagevisit")', user.has_perm("visits.view_pagevisit"))
    #profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = (profile_user_obj == user)
    if is_me:
        if user.has_perm("visits.pagevisit"):
            #qs = Pagevisits.Object.all()
            pass
    return HttpResponse(f"Hello there {username} - {profile_user_obj.id} - {user.id} - {is_me} - {user.has_perm('auth.view_user')}")
 """

@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user
    group = user.groups.get(name='Basic Plan')

    print(user.groups.all())
    print(group.user_set.all())

    print(group.permissions.all())

    subscription_content_type = ContentType.objects.get(app_label='subscriptions', model='subscription')
    print(subscription_content_type)

    #basic_perm = Permission.objects.get(codename='basic')
    #print("11111111", basic_perm.content_type)  # Ensure it matches the content type for your app

    print(
        user.has_perm("subscriptions.basic"), 
        user.has_perm("subscriptions.basic_ai"), 
        user.has_perm("subscriptions.pro"), 
        user.has_perm("subscriptions.advanced"), 
    )
    """ user_groups = user.groups.all()
    print("user_groups", user_groups)
    if user_groups.filter(name__icontains="basic").exists():
        return HttpResponse("Congratz!") """
   
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = (profile_user_obj == user)
    
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "is_me": is_me,
       
    }
    return render(request, "profiles/detail.html", context)
