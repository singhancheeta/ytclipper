# 🎬 YouTube Video Clipper

**Clip. Customize. Download.**  
A full-stack Django application that lets users clip YouTube videos by specifying custom start and end times. Built with a sleek UI, dark mode support, and user authentication – it's like scissors for YouTube!

![yt-clipper-banner](https://img.shields.io/badge/YouTube--Clipper-Django-blueviolet?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Features

✨ **Clip YouTube Videos**  
Paste a YouTube URL, select the time range, and download your favorite part.

🔐 **User Authentication**  
Register and login to manage your clip history privately.

🎨 **Responsive Dark Mode UI**  
Modern and mobile-friendly UI with sidebar navigation and Bootstrap 5.

🧾 **Download History**  
Authenticated users can access a list of previously clipped videos with download links.

🎉 **Success Confetti**  
Celebrate a successful clip with a burst of animation.

📁 **Media Management**  
Clipped videos are stored securely in `/media/clips/` and easily downloadable.

---

## 🖼️ Screenshots

### 🔒 Login Page  
<img src="https://i.imgur.com/your-login-screenshot.png" width="600"/>

### 🎞️ Clip Video Page  
<img src="https://i.imgur.com/your-clip-video-screenshot.png" width="600"/>

### 📂 Clip History  
<img src="https://i.imgur.com/your-clip-history-screenshot.png" width="600"/>

---

## 🛠️ Tech Stack

| Layer       | Tools Used                        |
|-------------|-----------------------------------|
| Frontend    | HTML, CSS, Bootstrap 5            |
| Backend     | Django, Python                    |
| Media Utils | moviepy, ffmpeg                   |
| Auth        | Django Authentication             |
| Storage     | Local FileSystem (Media Folder)   |

---

## 📦 Setup Instructions

### 🔧 Prerequisites
- Python 3.8+
- pip
- ffmpeg

---

### ⬇️ Clone the Repo
- git clone https://github.com/singhancheeta/ytbclipper.git
- cd ytbclipper
