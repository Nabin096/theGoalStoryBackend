from django.shortcuts import render
from SharedExperiences.forms import BlogsForm,BlogsTitleForm,GenreForm
from SharedExperiences.models import Elements,BlogsMetaData
import datetime
import urllib.parse
import json
"""
    Purpose:Method for creating blogs from admin.
    Author:Tonmoy Sagar
    Created On :23-07-2018
    Url=admin/blogsCreate
"""

def blogsCreate(request):
   blogId=1
   if(request.session.has_key('blogId')):
      blogId=request.session['blogId']

   else:

      if Elements.objects.filter().order_by('-blogId')[0]:
         blogId = Elements.objects.filter().order_by('-blogId')[0].blogId + 1
      request.session['blogId']=blogId
   error=''
   if request.method == 'POST':
      myform=BlogsForm(request.POST,request.FILES)
      if myform.is_valid():
         element=Elements()
         element.blogId=blogId
         elements=list(Elements.objects.filter(blogId=blogId))
         count=len(elements)+1
         if count<3:
            count=4
         element.sequenceNo=count
         element.tag=myform.cleaned_data['tag']

         if myform.cleaned_data['innerHTML1']:
            element.innerHTML = myform.cleaned_data['innerHTML1']
         elif myform.cleaned_data['innerHTML2']:
            element.innerHTML = myform.cleaned_data['innerHTML2']
         element.img=myform.cleaned_data['img']
         elements.append(element)

         element.save()


      else:
         error=myform.errors()

   blogPreview = Elements.objects.filter(blogId=blogId).order_by('sequenceNo')
   content = {
      'blogPreview': blogPreview,
      'errors':error
   }
   return render(request,'SharedExperiences/adminBlogCreate.html',content)




"""
    Purpose:Method for creating blogs title from admin.
    Author:Tonmoy Sagar
    Created On :09-08-2018
    Url=admin/blogsTitleCreate, Post only method no get available
"""


def blogsTitleCreate(request):
   blogId = 1
   if (request.session.has_key('blogId')):
      blogId = request.session['blogId']
   else:
      if Elements.objects.filter().order_by('-blogId')[0]:
         blogId = Elements.objects.filter().order_by('-blogId')[0].blogId + 1
      request.session['blogId'] = blogId
   if request.method == 'POST':
      myform=BlogsTitleForm(request.POST)
      if myform.is_valid():
         if not Elements.objects.filter(blogId=blogId,sequenceNo=1):
            elementDate = Elements()
            elementDate.blogId = blogId
            elementDate.sequenceNo = 1
            elementDate.innerHTML = str(datetime.datetime.now())
            elementDate.tag = "date"

            elementTitle = Elements()
            elementTitle.blogId = blogId
            elementTitle.sequenceNo = 2
            elementTitle.innerHTML = myform.cleaned_data['title']
            elementTitle.tag = "title"

            elementAuthor = Elements()
            elementAuthor.blogId = blogId
            elementAuthor.sequenceNo = 3
            elementAuthor.innerHTML = 'The Goal Story'
            elementAuthor.tag = "author"

            elementTitle.save()
            elementAuthor.save()
            elementDate.save()

         else:
            element=Elements.objects.filter(blogId=blogId, sequenceNo=2)
            element.update(innerHTML=myform.cleaned_data['title'])

   blogPreview = Elements.objects.filter(blogId=blogId).order_by('sequenceNo')
   content = {
      'blogPreview': blogPreview
   }
   return render(request, 'SharedExperiences/adminBlogCreate.html',content)



def blogsSubmit(request):
   blogId = 1
   if (request.session.has_key('blogId')):
      blogId = request.session['blogId']
   else:
      if Elements.objects.filter().order_by('-blogId')[0]:
         blogId = Elements.objects.filter().order_by('-blogId')[0].blogId + 1
      request.session['blogId'] = blogId
   if request.method == 'POST':
      myform = GenreForm(request.POST)
      genre=""
      if myform.is_valid():
         genre=myform.cleaned_data['genre']
         if genre=="NA":
            error="Please Enter valid Genre"
            content = {
               "error": error
            }
            return render(request, 'SharedExperiences/adminBlogCreate.html', content)
      if Elements.objects.filter(blogId=blogId, sequenceNo=2)[0].innerHTML and Elements.objects.filter(blogId=blogId,tag="Textarea").order_by("sequenceNo")[0].innerHTML:
         blogMeta=BlogsMetaData()
         blogMeta.blogId=blogId
         blogMeta.genre=genre
         blogMeta.date=datetime.datetime.now()
         if Elements.objects.filter(blogId=blogId,tag="Image").order_by("sequenceNo")[0].img:
            print(request.get_host())
            previewImage="http://"+request.get_host()+"/media/"+str(Elements.objects.filter(blogId=blogId,tag="Image").order_by("sequenceNo")[0].img)
            blogMeta.previewImage=previewImage

         blogMeta.previewText= Elements.objects.filter(blogId=blogId, sequenceNo=2)[0].innerHTML
         blogMeta.title=Elements.objects.filter(blogId=blogId,tag="Textarea").order_by("sequenceNo")[0].innerHTML
         blogMeta.author="The Goal Story"
         blogMeta.save()
         del (request.session['blogId'])
         return render(request, 'SharedExperiences/blogPreview.html')
      else:
         if (request.session.has_key('blogId')):
            Elements.objects.filter(blogId=blogId).delete()
         error="That small a blog ! You are either titleless or contentless buddy. I am deleting the blog cause you are the admin . So don't blame me "
         content={
            "error":error
         }
         del (request.session['blogId'])
         return render(request, 'SharedExperiences/adminBlogCreate.html',content)

   blogPreview=Elements.objects.filter(blogId=blogId).order_by('sequenceNo')
   content={
      'blogPreview':blogPreview
   }

   return render(request, 'SharedExperiences/adminBlogCreate.html',content)



def discardBlog(request):
   if request.method == 'POST':
      if (request.session.has_key('blogId')):
         blogId = request.session['blogId']
         Elements.objects.filter(blogId=blogId).delete()
         #del(request.session['img'])
         del(request.session['blogId'])
   return render(request, 'SharedExperiences/adminBlogCreate.html')




