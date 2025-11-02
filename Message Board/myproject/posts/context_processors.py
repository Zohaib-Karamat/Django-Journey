from django.contrib import admin
from datetime import datetime, timedelta
from posts.models import Post

def admin_statistics(request):
    """
    Context processor to provide statistics for admin dashboard
    """
    if not request.path.startswith('/admin/'):
        return {}
    
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    
    try:
        total_posts = Post.objects.count()
        today_posts = Post.objects.filter(created_at__date=today).count()
        week_posts = Post.objects.filter(created_at__date__gte=week_ago).count()
    except:
        total_posts = today_posts = week_posts = 0
    
    return {
        'total_posts': total_posts,
        'today_posts': today_posts,
        'week_posts': week_posts,
    }