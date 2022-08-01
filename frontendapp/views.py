from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,
                "frontendapp/show.html",{})
    
def index(request):
    return render(request,
                "frontendapp/01_index.html",{})
    
def blog(request):
    return render(request,
                "frontendapp/01_blog_list.html",{})
    
def about(request):
    return render(request,
                "frontendapp/01_about_me.html",{})
    
    
    
    
def index2(request):
    return render(request,
                "frontendapp/02_index_css.html",{})
def blog2(request):
    return render(request,
                "frontendapp/02_blog_list_css.html",{})
    
def about2(request):
    return render(request,
                "frontendapp/02_about_me_css.html",{})
    
    
    
def index3(request):
    return render(request,
                "frontendapp/03_index_css.html",{})
def blog3(request):
    return render(request,
                "frontendapp/03_blog_list_css.html",{})
    
def about3(request):
    return render(request,
                "frontendapp/03_about_me_css.html",{})
    
    
def index4(request):
    return render(request,
                "frontendapp/04_index_css.html",{})
def blog4(request):
    return render(request,
                "frontendapp/04_blog_list_css.html",{})
    
def about4(request):
    return render(request,
                "frontendapp/04_about_me_css.html",{})   
    
def index5(request):
    return render(request,
                "frontendapp/05_index_css_include.html",{})
def blog5(request):
    return render(request,
                "frontendapp/05_blog_list_css_include.html",{})
    
def about5(request):
    return render(request,
                "frontendapp/05_about_me_css_include.html",{})  
    
    
    
def index6(request):
    return render(request,
                  "frontendapp/06_index_javascript.html",{})

def blog6(request):
    return render(request,
                  "frontendapp/06_blog_list_javascript.html",{})

def about6(request):
    return render(request,
                "frontendapp/06_about_me_javascript.html",{})  
    
def index7(request):
    return render(request,
                  "frontendapp/07_index_javascript.html",{})
def blog7(request):
    return render(request,
                  "frontendapp/07_blog_list_javascript.html",{})

def about7(request):
    return render(request,
                "frontendapp/07_about_me_javascript.html",{})  
def index8(request):
    return render(request,
                  "frontendapp/08_index_bootstrap.html",{})
def index9(request):
    return render(request,
                  "frontendapp/09_index_bootstrap.html",{})
def blog9(request):
    return render(request,
                  "frontendapp/09_blog_list_bootstrap.html",{})

def about9(request):
    return render(request,
                "frontendapp/09_about_me_bootstrap.html",{}) 
    
    
    
