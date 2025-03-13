from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from . import util
import markdown2
import random

def index(request):
    """نمایش لیست مقالات"""
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    """نمایش یک مقاله مشخص"""
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(content)
    })

def search(request):
    """جستجوی مقاله"""
    query = request.GET.get('q', '').strip()
    if not query:
        return redirect("index")

    entries = util.list_entries()
    matches = [entry for entry in entries if query.lower() in entry.lower()]

    # اگر مقاله دقیقا با عنوان جستجو برابر بود، هدایت به صفحه مقاله
    if query.lower() in (entry.lower() for entry in entries):
        return redirect(reverse("entry", kwargs={"title": query}))

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": matches
    })


def new_page(request):
    """ایجاد یک مقاله جدید"""
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()

        # بررسی اینکه مقاله‌ای با این عنوان وجود دارد یا نه
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {
                "message": "An entry with this title already exists."
            })

        util.save_entry(title, content)
        return redirect(reverse("entry", kwargs={"title": title}))

    return render(request, "encyclopedia/new_page.html")



def random_page(request):
    """انتخاب یک مقاله تصادفی و نمایش آن"""
    entries = util.list_entries()
    if not entries:
        return redirect("index")  # اگر مقاله‌ای وجود ندارد، برگردد به صفحه اصلی
    
    random_entry = random.choice(entries)
    return redirect(reverse("entry", kwargs={"title": random_entry}))



def edit_page(request, title):
    """ویرایش یک مقاله"""
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found."
        })

    if request.method == "POST":
        updated_content = request.POST.get("content").strip()
        util.save_entry(title, updated_content)
        return redirect(reverse("entry", kwargs={"title": title}))

    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": content
    })





