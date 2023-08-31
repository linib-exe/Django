from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BalanceTransferForm
from .models import Wallet, Transaction

def balance_transfer(request):
    if request.method == 'POST':
        form = BalanceTransferForm(request.POST)
        if form.is_valid():
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            
            sender_wallet = Wallet.objects.get(user=request.user)
            receiver_wallet = Wallet.objects.get(user=receiver)
            
            if sender_wallet.balance >= amount:
                sender_wallet.balance -= amount
                sender_wallet.save()
                
                receiver_wallet.balance += amount
                receiver_wallet.save()
                
                Transaction.objects.create(
                    sender=request.user,
                    receiver=receiver,
                    amount=amount
                )
                
                return redirect('wallet:balance_transfer')
    else:
        form = BalanceTransferForm()
    
    return render(request, 'balance_transfer.html', {'form': form})

def transaction_history(request):
    transactions = Transaction.objects.filter(sender=request.user) | Transaction.objects.filter(receiver=request.user)
    return render(request, 'transaction_history.html', {'transactions': transactions})