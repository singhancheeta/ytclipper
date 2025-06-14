import os
import subprocess
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ClippedVideo 

@csrf_exempt
def index(request):
    history = []
    
    if request.method == "POST":
        video_url = request.POST.get("url")
        start_time = request.POST.get("start")
        end_time = request.POST.get("end")

        try:
            output_path = "media/clips"
            os.makedirs(output_path, exist_ok=True)
            full_video_path = os.path.join(output_path, "downloaded.mp4")
            clipped_video_path = os.path.join(output_path, "clipped.mp4")

            cmd_download = [
                "yt-dlp",
                "-f", "mp4",
                "-o", full_video_path,
                video_url
            ]
            subprocess.run(cmd_download, check=True)

            cmd_clip = [
                "ffmpeg",
                "-ss", start_time,
                "-to", end_time,
                "-i", full_video_path,
                "-c:v", "libx264",
                "-c:a", "aac",
                "-strict", "experimental",
                clipped_video_path,
                "-y"
            ]
            subprocess.run(cmd_clip, check=True)

            if request.user.is_authenticated:
                ClippedVideo.objects.create(user=request.user, file_name="clipped.mp4")

                history = ClippedVideo.objects.filter(user=request.user).order_by('-created_at')

            return render(request, "clips/index.html", {
                "success": True,
                "video": "clipped.mp4",
                "history": history
            })

        except Exception as e:
            return render(request, "clips/index.html", {
                "error": str(e)
            })

    if request.user.is_authenticated:
        history = ClippedVideo.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "clips/index.html", {
        "history": history
    })
