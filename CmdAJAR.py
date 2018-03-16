import subprocess


def ejecutar_comando():
    my_process = subprocess.Popen(["node", "./AppNode/appResemble.js"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    out, error = my_process.communicate()

    return {'salida': out, 'error': error}
