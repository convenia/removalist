
from removalist.main import RemovalistTest

def test_removalist(tmp):
    with RemovalistTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with RemovalistTest(argv=argv) as app:
        app.run()
