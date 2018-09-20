import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import NewTopicForm, PostForm, QueryForm
from .models import Board, Post, Topic


def home(request):
    boards = Board.objects.all()
    # pk = 7
    # return redirect('board_topics', pk=pk)
    return render(request, 'home.html', {'boards': boards})


def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


def helper(list, days):
    t1 = '09:00:00'
    t1 = datetime.datetime.strptime(t1, '%H:%M:%S').time()
    t2 = '18:00:00'
    t2 = datetime.datetime.strptime(t2, '%H:%M:%S').time()

    i = 0

    while not t1 == t2 and len(days) > i:
        if days[i].start_time == t1:
            ts = days[i].start_time
            tf = days[i].end_time
            while not ts == tf:
                list.append(days[i])
                ts = addSecs(ts, 1800)
            t1 = days[i].end_time
            i = i + 1
        else:
            list.append(t1)
            t1 = addSecs(t1, 1800)
    if not t1 == t2:
        while not t1 == t2:
            list.append(t1)
            t1 = addSecs(t1, 1800)

    return list


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    room = board.name
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(6)
    topics = board.topics.filter(day__range=[start_week, end_week], room=room).order_by('day')

    mons = topics.filter(day__week_day=2).order_by('start_time')
    tues = topics.filter(day__week_day=3).order_by('start_time')
    weds = topics.filter(day__week_day=4).order_by('start_time')
    thus = topics.filter(day__week_day=5).order_by('start_time')
    fris = topics.filter(day__week_day=6).order_by('start_time')

    sw2 = start_week + datetime.timedelta(1)
    sw3 = start_week + datetime.timedelta(2)
    sw4 = start_week + datetime.timedelta(3)
    sw5 = start_week + datetime.timedelta(4)

    mons1 = []
    helper(mons1, mons)
    tues1 = []
    helper(tues1, tues)
    weds1 = []
    helper(weds1, weds)
    thus1 = []
    helper(thus1, thus)
    fris1 = []
    helper(fris1, fris)

    if request.method == 'POST':
        form = QueryForm(request.POST)
        value = form['day'].value()
        topics = board.topics.filter(day=value)
        return render(request, 'topics2.html', {'board': board, 'topics': topics, 'value': value})
    else:
        form = QueryForm()
    return render(request, 'topics.html',
                  {'board': board, 'topics': topics, 'form': form, 'mons': mons1, 'tues': tues1, 'weds': weds1,
                   'thus': thus1, 'fris': fris1, 'list': list, 'start_week': start_week, 'sw2': sw2, 'sw3': sw3,
                   'sw4': sw4, 'sw5': sw5})


def board_topics2(request, pk):
    board = get_object_or_404(Board, pk=pk)

    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday()) + datetime.timedelta(7)
    end_week = start_week + datetime.timedelta(6)
    topics = board.topics.filter(day__range=[start_week, end_week]).order_by('day')

    mons = topics.filter(day__week_day=2).order_by('start_time')
    tues = topics.filter(day__week_day=3).order_by('start_time')
    weds = topics.filter(day__week_day=4).order_by('start_time')
    thus = topics.filter(day__week_day=5).order_by('start_time')
    fris = topics.filter(day__week_day=6).order_by('start_time')

    sw2 = start_week + datetime.timedelta(1)
    sw3 = start_week + datetime.timedelta(2)
    sw4 = start_week + datetime.timedelta(3)
    sw5 = start_week + datetime.timedelta(4)

    mons1 = []
    helper(mons1, mons)
    tues1 = []
    helper(tues1, tues)
    weds1 = []
    helper(weds1, weds)
    thus1 = []
    helper(thus1, thus)
    fris1 = []
    helper(fris1, fris)

    if request.method == 'POST':
        form = QueryForm(request.POST)
        value = form['day'].value()
        topics = board.topics.filter(day=value)
        return render(request, 'topics2.html', {'board': board, 'topics': topics, 'value': value})
    else:
        form = QueryForm()
    return render(request, 'topics.html',
                  {'board': board, 'topics': topics, 'form': form, 'mons': mons1, 'tues': tues1, 'weds': weds1,
                   'thus': thus1, 'fris': fris1, 'list': list, 'start_week': start_week, 'sw2': sw2, 'sw3': sw3,
                   'sw4': sw4, 'sw5': sw5})


def board_topics3(request, pk):
    board = get_object_or_404(Board, pk=pk)

    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday()) + datetime.timedelta(7) + datetime.timedelta(7)
    end_week = start_week + datetime.timedelta(6)
    topics = board.topics.filter(day__range=[start_week, end_week]).order_by('day')

    mons = topics.filter(day__week_day=2).order_by('start_time')
    tues = topics.filter(day__week_day=3).order_by('start_time')
    weds = topics.filter(day__week_day=4).order_by('start_time')
    thus = topics.filter(day__week_day=5).order_by('start_time')
    fris = topics.filter(day__week_day=6).order_by('start_time')

    sw2 = start_week + datetime.timedelta(1)
    sw3 = start_week + datetime.timedelta(2)
    sw4 = start_week + datetime.timedelta(3)
    sw5 = start_week + datetime.timedelta(4)

    mons1 = []
    helper(mons1, mons)
    tues1 = []
    helper(tues1, tues)
    weds1 = []
    helper(weds1, weds)
    thus1 = []
    helper(thus1, thus)
    fris1 = []
    helper(fris1, fris)

    if request.method == 'POST':
        form = QueryForm(request.POST)
        value = form['day'].value()
        topics = board.topics.filter(day=value)
        return render(request, 'topics2.html', {'board': board, 'topics': topics, 'value': value})
    else:
        form = QueryForm()
    return render(request, 'topics.html',
                  {'board': board, 'topics': topics, 'form': form, 'mons': mons1, 'tues': tues1, 'weds': weds1,
                   'thus': thus1, 'fris': fris1, 'list': list, 'start_week': start_week, 'sw2': sw2, 'sw3': sw3,
                   'sw4': sw4, 'sw5': sw5})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    room = board.name
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm(initial={'room': room})
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
    board = get_object_or_404(Board, pk=pk)
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(6)
    topics = board.topics.filter(day__range=[start_week, end_week]).order_by('day')

    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            topic.delete()
            return render(request, 'topics3.html', {'board': board, 'topics': topics})

    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
