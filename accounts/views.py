from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, DeleteView

from accounts.decorators import user_login_required
from accounts.forms import DebtForm
from accounts.models import Debt

from django.db.models import Q


@user_login_required
class DebtsTotalListView(TemplateView):
    template_name = 'accounts/debts_list.html'

    def get_context_data(self, **kwargs):
        detail_debt_list = []
        total_dept = 0
        debtors_list = []

        for debt_record in Debt.objects.filter(Q(creditor=self.request.user) | Q(debtor=self.request.user)):

            if debt_record.creditor == self.request.user:
                normalize_debt = {'id': debt_record.pk,
                                  'creditor': debt_record.creditor,
                                  'debtor': debt_record.debtor,
                                  'item_name': debt_record.item_name,
                                  'category': debt_record.category,
                                  'amount': debt_record.amount,
                                  'status': debt_record.status,
                                  'create_date': debt_record.create_date}
            else:
                normalize_debt = {'id': debt_record.pk,
                                  'creditor': debt_record.debtor,
                                  'debtor': debt_record.creditor,
                                  'item_name': debt_record.item_name,
                                  'category': debt_record.category,
                                  'amount': -1 * debt_record.amount,
                                  'status': debt_record.status,
                                  'create_date': debt_record.create_date}
            detail_debt_list.append({'id': debt_record.pk,
                                     'creditor': debt_record.creditor,
                                     'debtor': debt_record.debtor,
                                     'item_name': debt_record.item_name,
                                     'category': debt_record.category,
                                     'amount': debt_record.amount,
                                     'status': debt_record.status,
                                     'create_date': debt_record.create_date})

            if debt_record.status == 'X':
                if not any(deptor['name'] == normalize_debt['debtor'] for deptor in debtors_list):
                    debtors_list.append({'name': normalize_debt['debtor'], 'amount': normalize_debt['amount']})
                else:
                    for debtor in debtors_list:
                        if debtor['name'] == normalize_debt['debtor']:
                            debtor['amount'] += normalize_debt['amount']
        context = super(DebtsTotalListView, self).get_context_data(**kwargs)
        context['detail_debt_list'] = sorted(detail_debt_list, key=lambda debt: debt['create_date'], reverse=True)
        context['total_dept'] = total_dept
        context['debtors_list'] = debtors_list
        return context


@user_login_required
class RepaidView(RedirectView):
    model = Debt
    url = reverse_lazy('show')

    def get(self, request, *args, **kwargs):
        debt = get_object_or_404(Debt, pk=self.kwargs['pk'])
        debt.status = 'A'
        debt.save()
        return super(RepaidView, self).get(request, *args, **kwargs)


@user_login_required
class CancelView(RedirectView):
    model = Debt
    url = reverse_lazy('show')

    def get(self, request, *args, **kwargs):
        debt = get_object_or_404(Debt, pk=self.kwargs['pk'])
        debt.status = 'C'
        debt.save()
        return super(CancelView, self).get(request, *args, **kwargs)


@user_login_required
class DebtorDeleteView(DeleteView):
    model = Debt
    success_url = reverse_lazy('show')


@user_login_required
class HomeView(TemplateView):
    template_name = 'accounts/home.html'


@user_login_required
class DebtFormView(FormView):
    template_name = 'accounts/debt_form.html'
    form_class = DebtForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super(DebtFormView, self).form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
