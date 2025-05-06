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
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view._txt_result.controls.append(ft.Text(f"il numero di vertici del grafo : {self._model.getNumNodi()}"))
        self._view._txt_result.controls.append(ft.Text(f"il numero di archi del grafo : {self._model.getNumArchi()}"))
        self._view._txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumConnessa()} componenti connesse"))

        for nodo in lista_risultati:
            self._view._txt_result.controls.append(ft.Text(f"{nodo[0]} {nodo[1]}"))
        self._view.update_page()

