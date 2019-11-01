from django.http import HttpResponse

def index(zjm):
    return HttpResponse('hello django')

def demo(request,id):
    return HttpResponse('hello')
def getDay(request,year,month,day):
    return HttpResponse("%s/%s/%s是K%s的第63天"%(year,month,day,year))