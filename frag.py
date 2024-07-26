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
SMP_NAME = "11-コブシヲニギレ"
SMP_JACKET = Path("noctl/BMCR-7046.png")
SMP_NAME = "01 ロビンソン"
SMP_JACKET = Path("noctl/POCH-1983.jpg")
BITRATE = "320k"
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


# {{{ def wav2mp3():
def wav2mp3():
    mp3_metadata = {
        "tags": {"album": "ロビンソン", "artist": "SPITZ"},
        "cover": str(SMP_JACKET),
    }
    src = SRC_DIR / f"{SMP_NAME}.wav"
    dst = DST_DIR / f"{SMP_NAME}.mp3"
    enc(src, dst, metadata=mp3_metadata)
# }}}


# {{{ def view_info(src):
def view_info(src):
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
# }}}


# {{{ def main():
def main():
    # wav2mp3()
    src = DST_DIR / f"{SMP_NAME}.mp3"
    view_info(src)
    return None
# }}}


# {{{ if __name__ == "__main__":
if __name__ == "__main__":
    result = main()
# }}}

