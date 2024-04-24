from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from django.db.models import Max

def view_base(request):
    return render(request, 'base.html')


def view1(request):
    comments_data = [
        {"text": "Start of the comment.", "user": "User1", "comment_type": Comments.UPDATED_START},
        {"text": "This is a comment with Middle word.", "user": "User2", "comment_type": Comments.MIDDLE},
        {"text": "This comment should Finish here.", "user": "User3", "comment_type": Comments.FINISH},
        {"text": "Another comment.", "user": "User4", "comment_type": Comments.START},
        {"text": "Last comment.", "user": "User5", "comment_type": Comments.FINISH},
    ]

    for comment in comments_data:
        Comments.objects.create(text=comment["text"], user=comment["user"], comment_type=comment["comment_type"])

    return render(request, 'create_comments.html', {'message': 'Comments created successfully!'})


def view2(request):
    latest_comments = Comments.objects.order_by('created_at')[:5]
    return render(request, 'latest_comments.html', {'latest_comments': latest_comments})

def view3(request):
    latest_comments = Comments.objects.order_by('-created_at')[:5]
    latest_text = [comment.text for comment in latest_comments]
    print(latest_text)
    return render(request, 'latest_text.html', {'latest_text': latest_text})

def view4(request):
    special_comments = Comments.objects.all()
    
    for comment in special_comments:
        if comment.comment_type == Comments.START:
            comment.text = "Updated " + comment.text
            comment.comment_type = Comments.UPDATED_START 
            comment.save()

    updated_comments = Comments.objects.filter(comment_type=Comments.UPDATED_START)
     
    
    return render(request, 'special_comments.html', {'updated_comments': updated_comments, 'message': 'Comments updated successfully!'})


def view5(request):
    comments_to_delete = Comments.objects.filter(text__icontains='k').exclude(text__icontains='c')
    
    print("Comments to delete:", comments_to_delete)

    comments_to_delete.delete()

    message = f"Deleted {len(comments_to_delete)} comments successfully!"

    return render(request, 'delete_comments.html', {'message': message})

def view6(request):
    latest_author = Comments.objects.all().aggregate(Max('user'))['user__max']

    latest_comments = Comments.objects.filter(user=latest_author).order_by('-created_at')[:2]

    return render(request, 'latest_article_comments.html', {'latest_comments': latest_comments, 'latest_author': latest_author})
