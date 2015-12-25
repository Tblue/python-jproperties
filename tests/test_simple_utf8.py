# vim: fileencoding=utf8

from jproperties import Properties

def test_load_write_file(datadir, tmpdir):
    p = Properties()

    with datadir["simple.utf8.prop"].open("rb") as fh:
        p.load(fh, "utf-8")

    with tmpdir.join("dump.prop").open("w+b") as out:
        p.store(out, encoding="utf-8", timestamp=False)

        out.seek(0)
        assert out.read() == b"tästkey=This is the value\nanotherkey=Not mäny välues in this file\n"
