# vim: fileencoding=utf-8

from jproperties import Properties

def test_simple_utf8_load_write_file(datadir, tmpdir):
    p = Properties()

    with datadir["simple.utf8.prop"].open("rb") as fh:
        p.load(fh, "utf-8")

    with tmpdir.join("dump.prop").open("w+") as out:
        p.store(out, encoding="utf-8", timestamp=False)

        out.seek(0)
        assert out.read() == (u't\\u00e4stkey=This is the value\nanotherkey='
                              u'Not m\\u00e4ny v\\u00e4lues in this file\n')
