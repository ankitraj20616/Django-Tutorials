from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

posts = [
    {
        "id": 1,
        "title": "Let's explore python",
        "content": "Python is very powerful programming language."
    },
    {
        "id": 2,
        "title": "Let's explore java",
        "content": "Java is enterprise level programming language."
    },
    {
        "id": 3,
        "title": "Let's explore javascript",
        "content": "JavaScript is for frontend devlopment."
    }
]

# Create your views here.

def home(request: HttpRequest)-> HttpResponse:
    html = ""
    for post in posts:
        html += f"""
            <h1>{post.get("id")} - {post.get("title")}</h1>
            <p>{post.get("content")}</p>
            <br/>
        """
    return HttpResponse(html)

def post(request: HttpRequest, id: int)-> HttpResponse:
    resp_dict = None
    for post in posts:
        if post["id"] == id:
            resp_dict = post
            break
    if resp_dict is None:
        return HttpResponseNotFound("<h1>Item with this id doesn't exist.</h1>")
    html = f"""
        <h1>{resp_dict["id"]} - {resp_dict["title"]}</h1>
        <p>{resp_dict["content"]}</p>
    """
    return HttpResponse(html)

def visitGoogle(request: HttpRequest)-> HttpResponseRedirect:
    return HttpResponseRedirect("https://www.google.com")

def redirectPost(request: HttpRequest, id: int)-> HttpResponseRedirect:
    return HttpResponseRedirect(reverse('specific_post', args=[id]))