# https://www.youtube.com/watch?v=rtLZBKNExLQ
import yt_dlp

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
    'referer': 'https://erikcoldperson.com/e/pqsochrgqah2'  # Add the referer if needed
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://delivery-node-9z0j4gdotobfhm0j.voe-network.net/engine/hls2-c/01/05872/pqsochrgqah2_,n,.urlset/master.m3u8?t=sy8-O9n2KkMYhV0b8zwKcrPJ2okBMuJFpr8SbKo9S9Q&s=1720297423&e=14400&f=29360923&node=delivery-node-wi114x2bre4yltgi.voe-network.net&i=88.23&sp=2500&asn=3352'])

