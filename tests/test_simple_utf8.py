# vim: fileencoding=utf8

from jproperties import Properties

def test_load_write_file(datadir, tmpdir):
    p = Properties()

    with datadir["simple.utf8.prop"].open("rb") as fh:
        p.load(fh, "utf-8")

    with tmpdir.join("dump.prop").open("w+b") as out:
        p.store(out, encoding="utf-8", timestamp=False)

        out.seek(0)
        # assert out.read() == b"tÃ¤stkey=This is the value\nanotherkey=Not mÃ¤ny vÃ¤lues in this file\n"

        text = (b't\xc3\xa4stkey=This is the value\nanotherkey=Not m\xc3\xa4ny'
                b' v\xc3\xa4lues in this file\nBl\xc3\xa5b\xc3\xa6rsyltet\xc3'
                b'\xb8y=Blueberry jam\ngreek=\xce\x93\xce\xb1\xce\xb6\xce\xad'
                b'\xce\xb5\xcf\x82 \xce\xba\xce\xb1\xe1\xbd\xb6 \xce\xbc\xcf'
                b'\x85\xcf\x81\xcf\x84\xce\xb9\xe1\xbd\xb2\xcf\x82 \xce\xb4'
                b'\xe1\xbd\xb2\xce\xbd \xce\xb8\xe1\xbd\xb0 \xce\xb2\xcf\x81'
                b'\xe1\xbf\xb6 \xcf\x80\xce\xb9\xe1\xbd\xb0 \xcf\x83\xcf\x84'
                b'\xe1\xbd\xb8 \xcf\x87\xcf\x81\xcf\x85\xcf\x83\xce\xb1\xcf'
                b'\x86\xe1\xbd\xb6 \xce\xbe\xce\xad\xcf\x86\xcf\x89\xcf\x84'
                b'\xce\xbf\n')

        assert out.read() == text
