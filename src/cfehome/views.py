import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent



def home_page_view(request, *args, **kwargs):
    # objects.all() means everything 
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": (page_qs.count()*100)/qs.count(),
        
    }
    path = request.path
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)



def my_old_home_page_view(request, *args, **kwargs):
    print(this_dir)
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>is this {page_title}? Really..?</h1>
</body>
</html>
""".format(**my_context)
    # html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()
    # way to return back the HTML
    return HttpResponse(html_)