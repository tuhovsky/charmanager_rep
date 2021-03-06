from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import UserCharacter, Skill
from .forms import UserCharacterForm, UserCharacterChangeForm, \
    UserCharacterCreationForm, FilterForm
from . import settings


def register(request):
    if request.method == 'POST':
        form = UserCharacterCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(
                reverse(
                    'charmanager_app:usercharacters-list'
                )
            )
    else:
        form = UserCharacterCreationForm()
    return render(
        request,
        "registration/register.html",
        {
            'form': form
        }
    )


def usercharacters_list(request):

    queryset = UserCharacter.objects.all()

    # filter by spec and gender, search by username and nickname

    query_params = {}
    if request.GET.get('specialization'):
        query_params['specialization'] = request.GET['specialization']
    if request.GET.get('gender'):
        query_params['gender'] = request.GET['gender']

    search_field = request.GET[
        'search_field'
    ] if request.GET.get('search_field') else ""

    queryset = queryset.filter(
        Q(username__icontains=search_field) |
        Q(nickname__icontains=search_field),
        **query_params
    )

    # separate by 4 objects on page

    paginator = Paginator(queryset, settings.PAGINATE_COUNT)
    page = request.GET.get('page')
    try:
        usercharacters = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        usercharacters = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of
        # results.
        usercharacters = paginator.page(paginator.num_pages)

    return render(
        request,
        'charmanager_app/usercharacters_list.html',
        {
            'usercharacters': usercharacters,
            'filter_form': FilterForm,
            'paginator': paginator,
        }
    )


def usercharacter_detail(request, usercharacter_id):
    usercharacter = get_object_or_404(UserCharacter, pk=usercharacter_id)
    return render(
        request,
        'charmanager_app/usercharacter_detail.html',
        {'usercharacter': usercharacter, }
    )


@login_required()
def usercharacter_update(request):
    usercharacter = request.user
    if request.method == 'POST':
        form = UserCharacterChangeForm(
            request.POST, instance=usercharacter
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'charmanager_app:usercharacter-detail',
                    args=(usercharacter.id,)
                )
            )
    else:
        form = UserCharacterChangeForm(instance=usercharacter)
    return render(
        request,
        'charmanager_app/usercharacter_update.html',
        {
            'form': form,
            'usercharacter': usercharacter,
        }
    )

    # Create your views here.
