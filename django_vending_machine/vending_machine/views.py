from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Inventory
import yaml


def get_change(balance: int):
    if type(balance) is not int:
        return {'Invalid Value'}
    if balance == 0:
        return {'No Change'}
    currencies = (100, 50, 20, 10, 5, 1)
    change = {}
    for currency in currencies:
        if balance >= currency:
            change[f'RM {currency}'], balance = divmod(balance, currency)
    return change


class VendingMachine:
    def __init__(self, category_name='coffee'):
        self.category = category_name
        self.item_model = Inventory.objects.select_related('category')
        self.items = self.item_model.filter(category__slug=category_name)

    def pay_item(self, item_id, user, amount_inserted):
        balance = int(amount_inserted) - self.item_model.get(id=1).price
        change = get_change(balance)
        print(yaml.dump(change, width=1,  sort_keys=False))

@require_http_methods(["GET", "POST"])
@login_required(redirect_field_name="my_redirect_field")
def vending_machine_view(request, category='coffee'):
    template = loader.get_template('template.html')
    post_check = request.method == 'POST'
    if post_check:
        data = request.POST
        user = request.user
        item_id = data['item_select']
        amount_inserted = data['amount_inserted']
        category = data['amount_inserted']
    vm = VendingMachine(category)
    if post_check:
        vm.pay_item(item_id, user, amount_inserted)
    context = {
        'vm': vm,
    }
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET", "POST"])
def vending_machine_actions(request):
    template = loader.get_template('template.html')
    post_check = request.method == 'POST'
    print(post_check)
    if post_check:
        data = request.POST
        print(data)
        item_id = data['item_select']
        
        print(item_id)
        print(request.user)
    context = {
        'vm': '',
    }
    return HttpResponse(template.render(context, request))