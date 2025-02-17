from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Examapp.models import Admin, Question, Result, Users
from Examapp.serializers import QuestionSerilizer, ResultSerilizers, UsersSerilizers

from array import *

# Create your views here.

def hello(request):
    #return HttpResponse("Hello World")
    return render(request,"input.html")

@api_view(['GET'])
def getAllQuestions(request,subject):
    allquestions=Question.objects.filter(subject=subject)
    serilizer=QuestionSerilizer(allquestions,many=True)
    return Response(serilizer.data)

@api_view(['GET'])
def getAllSubjects(request):

    allquestions=Question.objects.all()

    mapresult=map(lambda question:question.subject,allquestions)

    return Response(set(mapresult))

#  {"username":"prakash","password":"prakash123","mobno":12340,"emailid":"prakash@jj"}

@api_view(['post'])
def saveUser(request):
    
    serilizer=UsersSerilizers(data=request.data)

    if serilizer.is_valid():
        serilizer.save()
        
    return Response(request.data) 

# username=x password=op   # data coming from browser while log in

@api_view(['post'])
def validate(request):

    userfromclient=request.data   # data coming from browser while log in

    userfromdb=Users.objects.get(username=userfromclient["username"])

    # username	password	mobno	emailid
    #   x	     y	        123	   x@hjhjjk     data from database

    if userfromclient["username"]==userfromdb.username and userfromclient["password"]==userfromdb.password:
        return Response(True) # response will be given to angular and then angular will show question page
    else:
        return Response(False) # response will be given to angular and then angular will show login page with error message



@api_view(['post'])
def validate2(request):

    userfromclient=request.data   # data coming from browser while log in

    userfromdb=Admin.objects.get(username=userfromclient["username"])

    # username	password	mobno	emailid
    #   x	     y	        123	   x@hjhjjk     data from database

    if userfromclient["username"]==userfromdb.username and userfromclient["password"]==userfromdb.password:
        return Response(True) # response will be given to angular and then angular will show question page
    else:
        return Response(False) # response will be given to angular and then angular will show login page with error message



@api_view(['post'])
def saveResult(request):

    serilizer=ResultSerilizers(data=request.data)

    if serilizer.is_valid():
        serilizer.save()
        
    return Response(request.data) 


@api_view(["GET"])
def getResults(request,subject):
    allresults=Result.objects.filter(subject=subject)
    serilizer=ResultSerilizers(allresults,many=True)
    return Response(serilizer.data)


@api_view(["GET"])
def getRecordsCounts(request,subject):

    count=Result.objects.filter(subject=subject).__len__()
    return Response(count)


@api_view(["GET"])
def getResults2(request,subject,pageno):

    print("given subject is  " + str(len(subject)))

    myresult=Result.objects.filter(subject=subject)

    print(myresult.query)

    noofrecords=myresult.__len__()
    
    print("no of records are " + str(noofrecords))
    
    # how many pages are required to show results

    pagenumber = 1#3
    while (3 * pagenumber) < noofrecords:
                        pagenumber += 1

    
    indexlist = list() #[0,3,6]

    count=0

    print("pagenumber is " , str(pagenumber))

    for i in range(0,pagenumber):
                indexlist.append(count)
                i=i+1
                count = count + 3
    
    print(indexlist)
    
    startindex=indexlist[int(pageno)-1]

    allrecords=list(Result.objects.filter(subject=subject))

    if pageno==pagenumber:
           totalrecordsshown = 3 * (pagenumber - 1)
           recordstoshow = noofrecords - totalrecordsshown
           endindex=startindex+recordstoshow
           allresults=allrecords[startindex:endindex]
           serilizer=ResultSerilizers(allresults,many=True)
           return Response(serilizer.data)
           
    else:
          endindex=startindex+3
          allresults=allrecords[startindex:endindex]
          serilizer=ResultSerilizers(allresults,many=True)
          return Response(serilizer.data)
          
          

@api_view(['GET'])
def viewQuestion(request,qno,subject):

    questionfromdb=Question.objects.get(qno=qno,subject=subject)

    serilizer=QuestionSerilizer(questionfromdb) 
    
    return Response(serilizer.data) # Response converts dictionary to json


@api_view(['post'])
def addQuestion(request):
    
    serilizer=QuestionSerilizer(data=request.data)

    if serilizer.is_valid():
        serilizer.save()
        
    return Response(True)


@api_view(['PUT'])
def updateQuestion(request):
    questionFromClient=request.data
    questionfromdb=Question.objects.get(qno=questionFromClient["qno"] ,subject=questionFromClient["subject"])
    serilizer=QuestionSerilizer(questionfromdb,data=questionFromClient,partial=False)
    if serilizer.is_valid():
        serilizer.save()
    return Response(True)    


@api_view(['DELETE'])
def deleteQuestion(request,qno,subject):
    
    Question.objects.filter(qno=qno,subject=subject).delete()

    return Response(True) 



    
				
	
    
    