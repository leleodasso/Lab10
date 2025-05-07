import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno is None or anno == "" or not anno.isdigit():
            self._view.create_alert("Inserire l'anno")
            return
        if int(anno) < 1816 or int(anno) > 2016:
            self._view.create_alert("Anno fuori portata")
            return

        self._model.buildGraph(anno)
        lista_risultati = self._model.getWeightNodes(anno)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumConnessa()} componenti connesse."))
        self._view._txt_result.controls.append(     ft.Text(f"il grafo ha {self._model.getNumNodi()} NODI."))
        self._view._txt_result.controls.append(     ft.Text(f"il grafo ha {self._model.getNumArchi()} ARCHI."))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito il dettaglio sui nodi:"))
        for nodo in lista_risultati:
            self._view._txt_result.controls.append(ft.Text(f"{nodo[0]} -- {nodo[1]} vicini"))
        self._view.update_page()

    def fillddStato(self):
        lista_paesi = self._model.getAllCountry()
        for stato in lista_paesi:
            self._view._ddStato.options.append(ft.dropdown.Option(text=stato.StateNme, key=stato.CCode))



    def handleStatiRaggiungibili(self, e):
        stato = self._view._ddStato.value
        anno = self._view._txtAnno.value
        if stato is None or stato == "":
            self._view.create_alert("Selezionare lo stato")
            return
        if anno is None or anno == "" or not anno.isdigit():
            self._view.create_alert("Inserire l'anno")
            return
        if int(anno) < 1816 or int(anno) > 2016:
            self._view.create_alert("Anno fuori portata")
            return
        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()
        listaRaggiungibili = self._model.getComponenteConnessa(stato)
        self._view._txt_result.controls.append(ft.Text(f"Ho calcolato la componente connessa:"))
        for el in listaRaggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{el.StateNme} è un vicino"))
        self._view.update_page()



