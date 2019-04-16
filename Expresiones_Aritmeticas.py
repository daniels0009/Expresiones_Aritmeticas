def evaluar(arbolAnalisis):
    operadores = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    hijoIzquierdo = arbolAnalisis.obtenerHijoIzquierdo()
    hijoDerecho = arbolAnalisis.obtenerHijoDerecho()

    if hijoIzquierdo and hijoDerecho:
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        return fn(evaluar(hijoIzquierdo),evaluar(hijoDerecho))
    else:
        return arbolAnalisis.obtenerValorRaiz()
