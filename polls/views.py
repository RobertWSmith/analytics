#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpResponseRedirect #, RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Poll, pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        # Alwyas return an HttpResponseRedirect after successfully deailing
        # with POST data. This prevents data from being posted twice if a user
        # hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(p.id, )))
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })


#def index(request):
#    latest_question_list = Poll.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request, {
#        'latest_question_list': latest_question_list,
#    })
#    return HttpResponse(template.render(context))

#def detail(request, question_id):
#    try:
#        poll = get_object_or_404(Poll, pk=question_id)
#    except Poll.DoesNotExist:
#        raise Http404
#    return render(request, 'polls/detail.html', {'poll': poll})
#
#def results(request, question_id):
#    return HttpResponse("You're looking at the results of question {0}".format(question_id))




