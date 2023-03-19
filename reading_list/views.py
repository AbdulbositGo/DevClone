from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ReadingListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'reading_list/reading-list.html')
