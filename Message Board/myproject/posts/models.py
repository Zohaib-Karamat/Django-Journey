from django.db import models

class Post(models.Model):
    text = models.TextField(
        help_text="Write your message here. It will be displayed on the homepage for everyone to see.",
        verbose_name="Message Content"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """String representation that shows a preview of each message."""
        return self.text[:50] + '...' if len(self.text) > 50 else self.text
    
    class Meta:
        ordering = ['-created_at']  # Show newest posts first
        verbose_name = "Message"
        verbose_name_plural = "Messages"
