from typing import Any
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import UpdateView , DeleteView , CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .forms import CommentForm , ArticleForm
from django.urls import reverse
# Create your views here.


""" class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html" """

def arttile_list(request):
    articles = Article.objects.all()
    context = {
        'article':articles,
    }
    return render(request,'articles/article_list.html',context)


""" class ArticleDetailView(FormMixin,DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("article_detail",kwargs={"pk":self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={"article":self.object,"writer":self.request.user})
        return context
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView,self).form_valid(form) """
    
""" article = Article.objects.get(id=pk) """
def article_detail(request,pk):
    article = get_object_or_404(Article,id=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.writer = request.user
            obj.article = article
            obj.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    
    return render(request,'articles/article_detail.html',{"article":article,"form":form})

""" class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ('title',"body")
    template_name = "articles/article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user """

def article_update(request,pk):
    article = get_object_or_404(Article,id=pk)
    form = ArticleForm(request.POST or None , instance = article)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+"articles/"+str(pk))
    form = ArticleForm()
    return render(request,"articles/article_edit.html",{"form":form})
    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "articles/article_create.html"
    fields = ('title',"body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    