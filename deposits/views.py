from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView, DetailView
from deposits.forms import DepositForm
from deposits.models import Deposit

class DepositListView(ListView):

    model = Deposit
    template_name = 'deposit_list.html'

class DepositDetailView(DetailView):

    model = Deposit
    template_name = 'visit_detail.html'

class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'add_deposit.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.interest = countInterest(self.object.deposit, self.object.term, self.object.rate)
        print(self.object.interest)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def countInterest(deposit, term, rate):
    sum = deposi
    for i in range(0, term):
        sum = sum * (1+rate)
    return sum - deposit
