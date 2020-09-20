import sys, traceback

from django.shortcuts import render
from django.http import HttpResponse

from .forms import CodeInput

def home(request):
    codearea = CodeInput(request.POST or None)
    ctx = {
        "frm" : codearea,
    }
    if request.method == "POST":
        print("inside if")
        if codearea.is_valid:
            # input(codearea)
            code = request.POST.get("codearea")
            execute_code(code)
            with open("test.txt", 'r') as f:
                output = f.read()
            ctx["output"] = output
        return render(request, 'code/home.html', ctx)
    print("outside if")
    return render(request, 'code/home.html', ctx)


def execute_code(code):

    out = sys.stdout
    sys.stdout = open("test.txt", 'w')
    # sys.stderr = f

    try:
        exec(code)
    except:
        print(traceback.format_exc())
    finally:
        sys.stdout.close()
        sys.stdout = out