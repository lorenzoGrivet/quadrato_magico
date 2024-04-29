import copy


class Model:
    def __init__(self):
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzioni=[]
        pass

    def risolvi_quadrato(self,N):
        self._n_iterazioni=0
        self._n_soluzioni=0
        self._ricorsione([],set(range(1,N*N+1)),N)


    def _ricorsione(self,parziale,rimanenti,N):
        self._n_iterazioni+=1

        if len(parziale)==N*N:

            if self.is_soluzione(parziale,N)==True:
                print(parziale)
                self._n_soluzioni+=1
                self._soluzioni.append(copy.deepcopy(parziale))
        else:
            for i in rimanenti:
                parziale.append(i)
                nuovi_rimanenti=copy.deepcopy(rimanenti)
                nuovi_rimanenti.remove(i)
                self._ricorsione(parziale,nuovi_rimanenti,N)
                parziale.pop()

    def stampa_soluzione(self, soluzione, N):
        print("-----------------------")
        for row in range(N):
            print([v for v in soluzione[row*N:(row+1)*N]])

    def is_soluzione(self,parziale,N):
        numero_magico=N*(N*N+1)/2

        for row in range(N):
            somma=0
            sottolista=parziale[row*N:(row+1)*N]

            for elemento in sottolista:
                somma+=elemento

            if somma!= numero_magico:
                return False

        for col in range(N):
            somma=0
            sottolista=parziale[0*N+ col : (N-1)*N+col+1:N]

            for elemento in sottolista:
                somma += elemento

            if somma != numero_magico:
                return False

        somma=0
        for riga_col in range(N):
            somma+=parziale[riga_col*N+riga_col]
        if somma!= numero_magico:
                return False


        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col * N + (N-1-riga_col)]
        if somma != numero_magico:
            return False

        return True

if __name__=="__main__":
    N=3
    model=Model()
    model.risolvi_quadrato(N)
    print(f"Quadrato di lato {N} risolto con  {model._n_iterazioni}")
    print(f"Trovate {model._n_soluzioni}")

    for sol in range(len(model._soluzioni)):
        model.stampa_soluzione(model._soluzioni[sol],N)

