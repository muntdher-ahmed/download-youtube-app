from flet import *
from yt_dlp import YoutubeDL

class Migho:
    def __init__(self, page: Page):
        self.page = page
        page.title = "YouTube Downloader"
        page.window.width = 400
        page.window.height = 740
        page.window.top = 1
        page.window.left = 960
        page.bgcolor = colors.WHITE  # Light background
        page.scroll = "auto"
        page.window.resizable = False
        page.window_maximizable = False

        # Define the input field
        self.url_input = TextField(
            label="YouTube",
            hint_text="Enter YouTube URL:",
            width=350,
            border_radius=8,
            filled=True,
            bgcolor=colors.LIGHT_BLUE_50,  # Light input background
            color=colors.BLACK,
        )

        # Define the result message
        self.result_text = Text("", size=14, color=colors.BLUE_GREY_700)

        # Add components to the page
        page.add(
            Column(
                [
                    Text(''),
                    Text(''),
                    Text(''),
                    Text(''),
                    Text(''),
                    
                    Text(
                        "YouTube Downloader",
                        size=24,
                        color=colors.BLUE_GREY_800,
                        weight="bold",
                    ),
                    Markdown(
                        "### By [@69mw2](https://instagram.com/69mw2)",on_tap_link=lambda e:self.page.launch_url(e.data)
                    ),
                    Divider(height=1, color=colors.BLUE_GREY_200),
                    self.url_input,
                    ElevatedButton(
                        text="Download",
                        on_click=self.get_url,
                        bgcolor=colors.BLUE_ACCENT,
                        color=colors.WHITE,
                        width=200,
                    ),
                    Divider(height=1, color=colors.BLUE_GREY_200),
                    Markdown('#  كيفية التحميل من يوتيوب'),
                    Text('  Download  قم بوضع الرابط في حقل الكتابة ثم اضغط  وبعدها سيتم تحويلك الى متصفح كوكل سيظهر لك الفيديوا وبعدها اضغط 3 نقاط واضغط نحميل وشكرا',text_align=TextAlign.RIGHT),
                    Divider(height=1, color=colors.BLUE_GREY_200),
                    
                ],
                alignment=MainAxisAlignment.CENTER,  # Centers the content vertically
                horizontal_alignment=CrossAxisAlignment.CENTER,  # Centers the content horizontally
            
                
            )
        )

    def get_url(self, e):
        # Fetch the URL from the input field
        uryl = self.url_input.value.strip()

        if uryl:
            try:
                ydl_opts = {
                    'quiet': True,  # تعطيل الإخراج غير الضروري
                    'skip_download': True,  # لا تقم بتحميل الفيديو
                    'format': 'best',  # أفضل جودة
                }

                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(uryl, download=False)  # استخراج معلومات الفيديو
                    video_download_url = info['url']  # الحصول على رابط الفيديو
                    self.page.launch_url(video_download_url)
            except:
                self.result_text.value = "Please enter a valid YouTube URL."
                self.result_text.color = colors.RED

        #self.url_input.value = ''
        self.page.update()

app(target=Migho)
