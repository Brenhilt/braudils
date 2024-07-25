#!/usr/bin/env python3
# vim: set fileencoding=utf-8:
# author: Brenhilt <register+git@brenhilt.com>
# created: 2024/07/25


# {{{ modules loading
from pathlib import Path

from pydub import AudioSegment
from mutagen.mp3 import MP3
# }}}


# {{{ const settings
SRC_DIR = Path("noctl/src")
DST_DIR = Path("noctl/dst")
SMP_NAME = "11-コブシヲニギレ.mp3"
# }}}


# wav2mp3 with tag info
# {{{ def enc(src, dst, bitrate=BITRATE, metadata=None):
def enc(src, dst, bitrate=BITRATE, metadata=None):
    sound = AudioSegment.from_file(src, format="wav")
    options = {
        "format": "mp3",
        "bitrate": bitrate,
    }
    if metadata is not None:
        options.update(metadata)
    file_handle = sound.export(dst, **options)
# }}}






# {{{ def main():
def main():
    mp3_metadata = {
        "tags": {"album": "ELEVEN", "artist": "B'z"},
        "cover": str(JACKET),
    }
    src = SRC_DIR / SMP_NAME
    dst = DST_DIR / SMP_NAME
    enc(SRC, DST, metadata=mp3_metadata)

    audio = MP3(src)
    print("bitrate"         ,audio.info.bitrate)
    print("bitrate_mode"    ,audio.info.bitrate_mode)
    print("channels"        ,audio.info.channels)
    print("encoder_info"    ,audio.info.encoder_info)
    print("encoder_settings",audio.info.encoder_settings)
    print("frame_offset"    ,audio.info.frame_offset)
    print("layer"           ,audio.info.layer)
    print("length"          ,audio.info.length)
    print("mode"            ,audio.info.mode)
    print("padding"         ,audio.info.padding)
    print("protected"       ,audio.info.protected)
    print("sample_rate"     ,audio.info.sample_rate)
    print("sketchy"         ,audio.info.sketchy)
    print("track_gain"      ,audio.info.track_gain)
    print("track_peak"      ,audio.info.track_peak)
    print("version"         ,audio.info.version)
    return None
# }}}


# {{{ if __name__ == "__main__":
if __name__ == "__main__":
    result = main()
# }}}

