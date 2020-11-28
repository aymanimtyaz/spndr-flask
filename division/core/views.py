from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
from src.forms.transaction_form import TransactionForm
from src import db
from spndr_tg.db_engine import db_operations as dbo

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('core.dashboard'))

    return render_template('index.html')

@core_bp.route('/about')
def about():

    return render_template('about.html')

@core_bp.route('/dashboard')
@login_required
def dashboard():
    
    spending_data = dbo.get_last_ten_transactions_ws(current_user.id)
    dash_array = []
    for row in spending_data:
        article = 'An' if row[0].lower()[0] in ['a', 'e', 'i', 'o', 'u'] else 'A'
        if row[0].lower().endswith('s'):
            article = ''
        dash_array.append(f'{article} {row[0]} for {row[1]} dollar(s) from {row[2]} on {row[3]}')

    return render_template('dashboard.html', dash_array = dash_array)

@core_bp.route('/newtransaction', methods = ['GET', 'POST'])
@login_required
def newtransaction():
    form = TransactionForm()

    if form.validate_on_submit():

        dbo.add_new_transaction_ws(current_user.id, form.item.data, float(form.price.data), form.vendor.data, form.category.data)
        return redirect(url_for('core.dashboard'))
    
    return render_template('newtransaction.html', form=form)




    
