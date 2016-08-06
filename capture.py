import re
import requests
from subprocess import call

f = open("index.html","w")
f.write('''<style>
    .img-wrap{
        width: 512; /*just here for the preview */
        position: relative;
        float: left;
        margin: 10;        
    }
        .img-wrap img{
            max-width: 100%;
            z-index: 1
        }
        .img-wrap .caption{
            display: block;
            width: 512;
            position: absolute;
            bottom: 5px; /*if using padding in the caption, match here */
            left: 0;
            z-index: 2;
            margin: 0;
            padding: 5px 0;
            text-indent: 5px;
            color: #fff;
            font-weight: bold;
            background: rgba(0, 0, 0, 0.4);
        }
</style>''')
for channelname in [
    'sport_stream_01',
    'sport_stream_02',
    'sport_stream_03',
    'sport_stream_04',
    'sport_stream_05',
    'sport_stream_06',
    'sport_stream_07',
    'sport_stream_08',
    'sport_stream_09',
    'sport_stream_10',
    'sport_stream_11',
    'sport_stream_12',
    'sport_stream_13',
    'sport_stream_14',
    'sport_stream_15',
    'sport_stream_16',
    'sport_stream_17',
    'sport_stream_18',
    'sport_stream_19',
    'sport_stream_20',
    'sport_stream_21',
    'sport_stream_22',
    'sport_stream_23',
    'sport_stream_24',
    ]:
    url = 'http://a.files.bbci.co.uk/media/live/manifesto/audio_video/%s/hls/uk/%s/%s/%s.m3u8' \
      % ('webcast', 'abr_hdtv', 'ak', channelname)
    r = requests.get(url)
    html = r.content
    for m in re.finditer(r'#EXT-X-STREAM-INF:PROGRAM-ID=(.+?),BANDWIDTH=(.+?),CODECS="(.*?)",RESOLUTION=(.+?)\s*(.+?.m3u8)',html):
        url = m.group(5)
        resolution = m.group(4)
        bitrate = m.group(2)
        #call(["ffmpeg", "-y", "-i", url, "-vframes", "1", "%s.png" % (channelname)])
        f.write('''<div class="img-wrap">
                    <img src="%s.png" alt= "">
                    <span class="caption">%s</span>
                    </div>
        ''' % (channelname,channelname))
        break
f.close()
     