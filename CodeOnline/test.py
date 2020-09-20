
import sys,traceback
    f = open("test.txt", 'w')

    out = sys.stdout
    err = sys.stderr
    sys.stdout = f
    sys.stderr = f

    try:
        f"{code}"
    except Exception as ex:
        print(traceback.format_exc())
    finally:
        f.close()
        sys.stdout = out
        sys.stderr = err